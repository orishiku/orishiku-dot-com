import uvicorn

from settings import AppSettings

settings = AppSettings()


def run():
    config = uvicorn.Config(
        f"{settings.name}.app:service",
        port=settings.port,
        host="0.0.0.0",
        log_level="debug" if settings.debug else "info",
        reload=settings.debug)

    server = uvicorn.Server(config)
    server.run()
