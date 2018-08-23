from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='text', request_method='GET')
def home_view(request):
    message = "GET / - The base API route\nPOST /api/v1/auth/ - for registering a new account and signing up\nGET /api/v1/portfolio/{id}/ - for retrieving a user's portfolio\nPOST /api/v1/stock/ - for creating a new company record\nGET /api/v1/stock/{id}/ - for retrieving a companies information\nDELETE /api/v1/stock/{id} - for deleting a company record\nGET /api/v1/company/{symbol} - for retrieving company detail from 3rd party API, where `{symbol}` is variable"
        
    return Response(body=message, content_type='text/plain', status=200)
