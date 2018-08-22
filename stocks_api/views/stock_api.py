from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class Stock_api(APIViewSet):
    def list(self, request):
        return Response(json={'message': 'All the list of your stock'}, status=200)

    def retreive(self, request):
        return Response(json={'message': 'Here is a stock'}, status=200)
    
    def create(self, request):
        return Response(json={'message': 'Created a new stock'}, status=201)

    def destroy(self, request):
        return Response(json={'message': 'Removed a stock'}, status=204)