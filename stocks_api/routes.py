from pyramid_restful.routers import ViewSetRouter
from .views.stock_api import Stock_api


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    router = ViewSetRouter(config)
    router.register('api/v1/stock', Stock_api, 'stock')