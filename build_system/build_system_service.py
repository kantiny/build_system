import logging

from aiohttp import web
from aiohttp_cors import (
    ResourceOptions,
    setup
)

from build_system import config


class BuildSystemService:
    """
    Класс для работы с сервисом
    """

    def __init__(self):
        """
        Инициализация класса сервиса
        """
        self._app = None

    def _setup_cors(self, resource):
        """
        Настройка CORS
        @param resource: сущность в таблице роута
        """
        cors = setup(
            self._app,
            defaults={
                '*': ResourceOptions(
                    allow_credentials=True,
                    expose_headers='*',
                    allow_headers='*',
                    allow_methods='POST'
                )
            })
        cors.add(resource)

    async def _init_views(self, _app):
        """
        Инициализация роутов, CORS-прав и доступных CRUD-методов
        @param _app: приложение
        """
        resource = self._app.router.add_resource('/get_tasks', name='get_tasks')
        self._setup_cors(resource)
        resource.add_route('*', view)

    def init_app(self):
        """
        Инициализация расширений приложения
        @return: приложение
        """
        logging.info('сервис %s (v.%s) запущен', config.NAME, config.VERSION)
        self._app = web.Application()

        self._app.on_startup.extend([
            self._init_views,
        ])
        return self._app
