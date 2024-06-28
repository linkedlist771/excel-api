from excel_api.api import v1


from fastapi import FastAPI


def register_router(app: FastAPI):
    """
    routers

    :param app: FastAPI
    :return:
    """

    # API
    app.include_router(v1)


def register_app():
    app = FastAPI(
        # title=settings.TITLE,
        # version=settings.VERSION,
        # description=settings.DESCRIPTION,
        # docs_url=settings.DOCS_URL,
        # redoc_url=settings.REDOCS_URL,
        # openapi_url=settings.OPENAPI_URL,
        # default_response_class=MsgSpecJSONResponse,
        # lifespan=register_init,
    )
    register_router(app)
    return app
