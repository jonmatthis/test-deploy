from fastapi import FastAPI

from . import enabled_routers


def create_app():
    app = FastAPI()
    for router in enabled_routers:
        app.include_router(router)
    return app


if __name__ == "__main__":
    app = create_app()
