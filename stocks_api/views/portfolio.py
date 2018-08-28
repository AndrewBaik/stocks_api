from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
from ..models.schemas import PortfolioSchema, StockSchema
from ..models.portfolio import Portfolio
from ..models.stock import Stock
from sqlalchemy.exc import DataError, IntegrityError
import requests
import json


# @view_config(route_name='lookup', renderer='json', request_method='GET')
# def lookup(request):
#     """ Looking up a json based on the third-party api
#     """
#     url = 'https://api.iextrading.com/1.0/stock/{}/company/'.format(
#         request.matchdict['symbol']
#     )
#     response = requests.get(url)
#     return Response(json=response.json(), status=200)


class PortfolioAPIView(APIViewSet):
    """ CRUD class for portfolio
    """
    def retrieve(self, request, id=None):
        """ Getting a single portfolio
        """
        if not id:
            return Response(json='ID not found', status=404)

        try:
            portfolio = Portfolio.one(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data
        return Response(json=data, status=200)

    def create(self, request):
        """ Posting a new portfolio
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'name' not in kwargs:
            return Response(json='Expected value: name', status=400)

        try:
            portfolio = Portfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error, portfolio exists', status=400)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data
        return Response(json=data, status=201)


class StockAPIView(APIViewSet):
    """ CRUD class for Stock
    """
    def list(self, request):
        """ Get all stocks method
        """
        return Response(json={'message': 'List of all your stock'}, status=200)

    def retrieve(self, request, symbol=None):
        """ Get a single stock method
        """
        if not symbol:
            return Response(json='symbol not found', status=404)

        try:
            stock = Stock.one(request=request, pk=symbol)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        schema = StockSchema()
        data = schema.dump(stock).data
        return Response(json=data, status=200)

    def create(self, request):
        """ post a new stock
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'symbol' not in kwargs:
            return Response(json='Expected value: symbol', status=400)

        try:
            stock = Stock.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error, Stock already exist', status=400)

        schema = StockSchema()
        data = schema.dump(stock).data
        return Response(json=data, status=201)

    def remove(self, request, id=None):
        """ Remove a selected portfolio
        """
        if not id:
            return Response(json='ID not found', status=404)

        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)


class CompanyAPIView(APIViewSet):
    """ CRUD class for Company
    """
    def list(self, request, symbol=None):
        if not symbol:
            return Response(json='Company not found', status=404)
        url = 'https://api.iextrading.com/1.0/stock/{}/company/'.format(symbol)
        response = requests.get(url)
        return Response(json=response.json(), status=200)
