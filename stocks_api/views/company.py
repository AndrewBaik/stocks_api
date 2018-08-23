from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class Company_api(APIViewSet):
    def retrieve(self, request, id=None):
        # http :6543/api/v1/company/{id}/
        return Response(json={'message': f'Provided a single resource for {id}'}, status=200)
