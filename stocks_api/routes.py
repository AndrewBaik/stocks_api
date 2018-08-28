from pyramid_restful.routers import ViewSetRouter
from .views import StockAPIView, CompanyAPIView, PortfolioAPIView
# from .views.company import Company_api
# from .views.portfolio import Portfolio_api


def includeme(config):
    """ Defining route by url
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # config.add_route('lookup', '/api/v1/lookup/{symbol}')
    router = ViewSetRouter(config)
    router.register('api/v1/stock', StockAPIView, 'stock')
    router.register('api/v1/company/{symbol}', CompanyAPIView, 'company')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio')
