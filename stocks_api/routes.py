from pyramid_restful.routers import ViewSetRouter
from .views.portfolio import StockAPIView, CompanyAPIView, PortfolioAPIView
from .views.auth import AuthAPIView
from .views.visual import VisualAPIView


def includeme(config):
    """ routes to APIView by request
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # config.add_route('lookup', '/api/v1/lookup/{symbol}')
    router = ViewSetRouter(config)
    router.register('api/v1/stock/{symbol}', StockAPIView, 'stock', permission='admin')
    router.register('api/v1/company/{symbol}', CompanyAPIView, 'company', permission='admin')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio', permission='admin')
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
    router.register('api/v1/visual/{symbol}', VisualAPIView, 'visual')
