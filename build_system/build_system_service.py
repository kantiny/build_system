
from aiohttp import web


class BuildSystemService:
    """
    Класс для работы с сервисом
    """

    def __init__(self):
        """
        Инициализация класса сервиса
        """
        self._app = None
        self.router = None

    async def _init_route(self):
        self.router = web.RouteTableDef()

    def init_app(self):
        """
        Инициализация расширений приложения
        @return: приложение
        """
        # logging.info('сервис %s (v.%s) запущен', config.NAME, config.VERSION)
        self._app = web.Application()

        self._app.on_startup.extend([
            self._init_route,
        ])
        return self._app
