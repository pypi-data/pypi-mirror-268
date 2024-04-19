# Copyright 2024 Agnostiq Inc.

import asyncio
import inspect
from functools import partial
from typing import Any

import covalent as ct
import uvicorn
from covalent._shared_files.context_managers import active_lattice_manager
from fastapi import FastAPI

from covalent_cloud.function_serve.common import (
    DEPLOY_ELECTRON_PREFIX,
    SupportedMethods,
    rename,
    wait_for_deployment_to_be_active,
)
from covalent_cloud.function_serve.models import Endpoint, FunctionServiceModel, ServeAsset
from covalent_cloud.shared.schemas.volume import Volume

__all__ = [
    "FunctionService",
]


TESTING_WARNING = "This is an unoptimized version of the app, useful only for local testing."
EXAMPLE_USAGE = "Sample usage to make a request to the endpoint: `requests.post('http://localhost:8000/your-route', params={'arg_name': 'arg_value'})`"
USE_JSON_WARNING = (
    "When using the deployed version, make sure to use `json=` instead of `params=` in the request"
)


class FunctionService:
    def __init__(
        self,
        func=None,
        executor=None,
        name=None,
        description=None,
        auth=None,
        tags=None,
        compute_share=None,
        volume=None,
        *,
        _main_func,
    ) -> None:
        self.init_func = func

        self.executor = executor

        self.func_name = None
        self.name = name
        self.func_source = None
        self.func_description = None

        if func is not None:
            self.func_name = func.__name__
            self.name = name or func.__name__
            self.func_source = inspect.getsource(func)
            self.func_description = (
                description
                or func.__doc__
                or "Add a docstring to your service function to populate this section."
            )

        self.auth = True if auth is None else auth
        self.tags = tags
        self.compute_share = compute_share

        self.all_endpoints = []

        # This will be the main function that is used to start adding endpoints to
        # this will NEVER BE NONE
        self._main_func = _main_func

        # Set the volume to None by default, it will be set by the `cc.deploy` function
        self.volume: Volume = volume

    def _get_method_filtered_endpoints(self, method: str):
        return [ep for ep in self.all_endpoints if ep.method == method]

    def _is_testable_endpoint(self, func):
        sig = inspect.signature(func)

        # Return False if the function has any parameters without default values
        for param in sig.parameters.values():
            if param.default == inspect.Parameter.empty:
                return False

        return True

    def _method_decorator_generator(self, method, route, name, description, streaming, /, func):
        method_endpoints = self._get_method_filtered_endpoints(method)

        if route in [ep.route for ep in method_endpoints]:
            raise ValueError(f"A {method} method function already exists for this route")

        # Register the route and the method function
        self.all_endpoints.append(
            Endpoint(
                route=route,
                name=name or func.__name__,
                endpoint_fn=ServeAsset(serialized_object=ct.TransportableObject(func).serialize()),
                endpoint_fn_source=inspect.getsource(func),
                streaming=streaming,
                description=description
                or func.__doc__
                or "Either add a docstring to your endpoint function or use the endpoint's 'description' parameter to populate this section.",
                test_endpoint_enabled=self._is_testable_endpoint(func),
                method=method,
            )
        )
        return self

    # Assigning and returning the decorator like this as it is slightly easier to understand

    def _get(self, route: str, name: str = None, description: str = None, streaming: bool = False):
        get_decorator = partial(
            self._method_decorator_generator,
            SupportedMethods.GET,
            route,
            name,
            description,
            streaming,
        )
        return get_decorator

    def _post(
        self, route: str, name: str = None, description: str = None, streaming: bool = False
    ):
        post_decorator = partial(
            self._method_decorator_generator,
            SupportedMethods.POST,
            route,
            name,
            description,
            streaming,
        )
        return post_decorator

    def _put(self, route: str, name: str = None, description: str = None, streaming: bool = False):
        put_decorator = partial(
            self._method_decorator_generator,
            SupportedMethods.PUT,
            route,
            name,
            description,
            streaming,
        )
        return put_decorator

    def _delete(
        self, route: str, name: str = None, description: str = None, streaming: bool = False
    ):
        delete_decorator = partial(
            self._method_decorator_generator,
            SupportedMethods.DELETE,
            route,
            name,
            description,
            streaming,
        )
        return delete_decorator

    def _patch(
        self, route: str, name: str = None, description: str = None, streaming: bool = False
    ):
        patch_decorator = partial(
            self._method_decorator_generator,
            SupportedMethods.PATCH,
            route,
            name,
            description,
            streaming,
        )
        return patch_decorator

    def endpoint(
        self, route: str, name: str = None, description: str = None, streaming: bool = False
    ):
        return self._post(route, name, description, streaming)

    def _create_app(self, args, kwargs):
        """
        Create a FastAPI app from the instance of this class.
        FOR TESTING PURPOSES ONLY.
        """

        # User warning to let them know that this is for testing purposes only
        print(TESTING_WARNING)
        print(EXAMPLE_USAGE)
        print(USE_JSON_WARNING)

        # Running the init function once before starting the app
        init_result = {}
        if self.init_func is not None:
            init_result = self.init_func(*args, **kwargs)

        print(f"Initial init result is: {init_result.keys()}")

        # Create a new FastAPI app from this instance
        app = FastAPI()

        # Add all the endpoints to the app
        for ep in self.all_endpoints:
            function_to = ct.TransportableObject.deserialize(ep.endpoint_fn.serialized_object)

            # Only attach those arguments which are also in the function signature of endpoint function
            func = function_to.get_deserialized()
            sig = inspect.signature(func)
            final_kwargs = {k: v for k, v in init_result.items() if k in sig.parameters}

            print(f"Final init result for endpoint {func.__name__} is: {final_kwargs.keys()}")

            attachable_fn = partial(function_to.get_deserialized(), **final_kwargs)

            if ep.method == SupportedMethods.GET:
                app.get(ep.route)(attachable_fn)
            elif ep.method == SupportedMethods.POST:
                app.post(ep.route)(attachable_fn)
            elif ep.method == SupportedMethods.PUT:
                app.put(ep.route)(attachable_fn)
            elif ep.method == SupportedMethods.DELETE:
                app.delete(ep.route)(attachable_fn)
            elif ep.method == SupportedMethods.PATCH:
                app.patch(ep.route)(attachable_fn)

        return app

    def test_run(self, port: int = 8000, *args, **kwargs):
        """
        Run the FastAPI app locally using uvicorn.
        This is useful for testing the FastAPI app before deploying it to a cloud service.
        """

        # Run the app using uvicorn
        app = self._create_app(args, kwargs)

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop is not None:
            raise RuntimeError(
                f"Use `await {self.func_name}.test_run_async()` instead if there's a running event loop such as in Jupyter Notebook."
            )

        uvicorn.run(app, port=port)

    async def test_run_async(self, port: int = 8000, *args, **kwargs):
        """
        In case running inside a Jupyter notebook, await this method.

        Run the FastAPI app using uvicorn.
        This is useful for deploying the FastAPI app to a cloud service.
        """
        app = self._create_app(args, kwargs)
        config = uvicorn.Config(app, port=port)
        server = uvicorn.Server(config)

        await server.serve()

    def get_model(self, *init_args, **init_kwargs):
        return FunctionServiceModel(
            title=self.name,
            description=self.func_description,
            executor=self.executor,
            compute_share=self.compute_share,
            tags=self.tags,
            auth=self.auth,
            init_fn=ServeAsset(
                serialized_object=ct.TransportableObject(self.init_func).serialize()
            ),
            init_fn_args=ServeAsset(
                serialized_object=ct.TransportableObject(list(init_args)).serialize()
            ),
            init_fn_kwargs=ServeAsset(
                serialized_object=ct.TransportableObject(init_kwargs).serialize()
            ),
            init_fn_source=self.func_source,
            endpoints=self.all_endpoints,
            volume=self.volume,
        )

    def get_model_no_S3(self, *init_args, **init_kwargs):

        model_without_s3 = self.get_model(*init_args, **init_kwargs)

        # Remove the S3 assets from the model
        model_without_s3.init_fn = model_without_s3.init_fn.serialized_object
        model_without_s3.init_fn_args = model_without_s3.init_fn_args.serialized_object
        model_without_s3.init_fn_kwargs = model_without_s3.init_fn_kwargs.serialized_object

        for ep in model_without_s3.endpoints:
            ep.endpoint_fn = ep.endpoint_fn.serialized_object

        return model_without_s3

    def __call__(self, *args: Any, **kwargs: Any) -> Any:

        import covalent_cloud as cc

        active_lattice = active_lattice_manager.get_active_lattice()
        if active_lattice is not None:

            dispatcher_uri = cc.settings.dispatcher_uri
            api_key = cc.get_api_key()

            @rename(DEPLOY_ELECTRON_PREFIX + self.func_name)
            def _electronic_deploy(
                function_service, dispatcher_uri, api_key, volume, *args, **kwargs
            ):

                import covalent_cloud as cc

                cc.settings.dispatcher_uri = dispatcher_uri
                cc.save_api_key(api_key)

                print("Current settings are: ")
                print(cc.settings.model_dump())

                new_executor: cc.CloudExecutor = function_service.executor
                new_executor.settings = cc.settings.model_dump()
                function_service.executor = new_executor

                deployment_info = cc.deploy(function_service, volume)(*args, **kwargs)

                return wait_for_deployment_to_be_active(deployment_info, verbose=True)

            # Rename the deploy function to the name of the calling function
            deploy_func = partial(_electronic_deploy, self, dispatcher_uri, api_key, self.volume)
            deploy_func.__name__ = _electronic_deploy.__name__
            deploy_func.__doc__ = _electronic_deploy.__doc__
            deploy_func.__qualname__ = _electronic_deploy.__qualname__

            # Create, run, and return the electron -> leveraging
            # the already built mechanisms in electrons
            return ct.electron(
                deploy_func,
                executor=self.executor,
            )(*args, **kwargs)
