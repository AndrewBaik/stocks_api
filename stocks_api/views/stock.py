from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class Stock_api(APIViewSet):
    def list(self, request):
        return Response(json={'message': 'List of all your stocks'}, status=200)

    def retrieve(self, request, id=None):
        return Response(json={'message': f'Here is a stock {id}'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Created a new stock'}, status=201)

    def destroy(self, request, id=None):
        return Response(json={'message': f'Removed a {id}'}, status=204)
