import logging

from aiohttp import web

from build_system.build_system_service import BuildSystemService

if __name__ == '__main__':
    app = BuildSystemService()
    try:
        web.run_app(app.init_app())
        logging.info('Сервис остановлен')
    except RuntimeError as err:
        logging.error('Сервис остановлен из-за ошибки: {}'.format(err))
