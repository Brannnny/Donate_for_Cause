from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.app.api.routes.users import router


def get_application():
    """Get FastAPI application instance
    :return: FastAPI app"""

    app = FastAPI(title="brown", version="1.0.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api")

    return app


app = get_application()


