from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class Portfolio_api(APIViewSet):
    def retrieve(self, request, id=None):
        # http :6543/api/v1/company/{id}/
        return Response(json={'message': f'Here is your portfolio {id}'}, status=200)
