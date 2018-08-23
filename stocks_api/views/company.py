from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class Company_api(APIViewSet):
    def retrieve(self, request, id=None):
        # http :6543/api/v1/company/{id}/
        return Response(json={'message': 'Provided a single resource for company'}, status=200)
