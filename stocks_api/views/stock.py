from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class Stock_api(APIViewSet):
    """ Base CRUD class for stock
    """
    def list(self, request):
        """ Get all stocks
        """
        return Response(json={'message': 'List of all your stocks'}, status=200)

    def retrieve(self, request, id=None):
        """ Get a selected stock
        """
        return Response(json={'message': 'Here is a stock'}, status=200)

    def create(self, request):
        """ Post a new stock
        """
        return Response(json={'message': 'Created a new stock'}, status=201)

    def destroy(self, request, id=None):
        """ Remove a selected stcok
        """
        return Response(json={'message': 'Removed a stock'}, status=204)
