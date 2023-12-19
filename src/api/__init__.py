from .controllers.health_controller import health_check_router

enabled_routers = [
    health_check_router
]
