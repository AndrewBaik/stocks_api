from pyramid_restful.routers import ViewSetRouter
from .views import Stock_api, Company_api, Portfolio_api
# from .views.company import Company_api
# from .views.portfolio import Portfolio_api


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    router = ViewSetRouter(config)
    router.register('api/v1/stock', Stock_api, 'stock')
    router.register('api/v1/company', Company_api, 'company')
    router.register('api/v1/portfolio', Portfolio_api, 'portfolio')