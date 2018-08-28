# from pyramid_restful.viewsets import APIViewSet
# from pyramid.response import Response
# from pyramid.view import view_config
# # from ..models import stock, portfolio
# import requests
# import json


# # @view_config(route_name='lookup', renderer='json', request_method='GET')
# # def lookup(request):
# #     url = 'https://api.iextrading.com/1.0/stock/{}/company/'.format(
# #         request.matchdict['symbol'],
# #     )
# #     response = requests.get(url)
# #     return Response(json=response.json(), status=200)


# class CompanyAPIView(APIViewSet):
#     def retrieve(self, request, id=None):
#         # http :6543/api/v1/company/{id}/
#         return Response(json={'message': 'Provided a single resource for company'}, status=200)
