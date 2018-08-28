from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
from ..models.schemas import PortfolioSchema, StockSchema
from ..models.portfolio import Portfolio
from ..models.stock import Stock
from sqlalchemy.exc import DataError, IntegrityError
import requests
import json


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    url = 'https://api.iextrading.com/1.0/stock/{}/company/'.format(
        request.matchdict['symbol'],
    )
    response = requests.get(url)
    return Response(json=response.json(), status=200)


class PortfolioAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        if not id:
            return Response(json='ID not found', status=404)

        try:
            portfolio = Portfolio.one(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        schema = PortfolioSchema
        data = schema.dump(portfolio).data
        return Response(json=data, status=200)

    def create(self, request):
        try:
            kwarg = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'id' not in kwarg:
            return Response(json='Expected value: id', status=400)

        try:
            portfolio = Portfolio.new(request, **kwarg)
        except IntegrityError:
            return Response(json='Duplicate Key Error, Zip code already exists', status=400)

        schema = PortfolioSchema
        data = schema.dump(portfolio).data
        return Response(json=data, status=201)

    # def destroy(self, request, id=None):
    #     if not id:
    #         return Response(json='ID not found', status=404)

    #     try:
    #         Portfolio.remove(request=request, pk=id)
    #     except (DataError, AttributeError):
    #         return Response(json='Not Found', status=404)

    #     return Response(status=204)


class StockAPIView(APIViewSet):
    # def list(self, request):
    #     return Response(json={'message': 'List of all your stock'}, status=200)

    def retrieve(self, request, id=None):
        if not id:
            return Response(json='ID not found', status=404)

        try:
            stock = Stock.one(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        schema = StockSchema
        data = schema.dump(stock).data
        return Response(json=data, status=200)

    def create(self, request):
        try:
            kwarg = json.load(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'id' not in kwarg:
            return Response(json='Expected value: id', status=400)

        try:
            stock = Stock(request, **kwarg)
        except IntegrityError:
            return Response(json='Duplicate Key Error, Zip code already exist', status=400)

        schema = StockSchema
        data = schema.dump(stock).data
        return Response(json=data, status=201)

    def destroy(self, request, id=None):
        if not id:
            return Response(json='ID not found', status=404)

        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)


class CompanyAPIView(APIViewSet):
    def retrieve(self, request, id=None):
        return Response(json='you got one', status=200)
    # @view_config(route_name='lookup', renderer='json', request_method='GET')
    #     def (request):
    #     if not id:
    #         return Response(json='ID not found', status=404)
    #     url = 'https://api.iextrading.com/1.0/stock/{}/company/'.format(
    #         request.matchdict['symbol'],
    #     )
    #     response = requests.get(url)
    #     return Response(json=response.json(), status=200)
