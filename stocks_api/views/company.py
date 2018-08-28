from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class Company_api(APIViewSet):
    """ Base CRUD for Company
    """
    def retrieve(self, request, id=None):
        """ Get a selected Company
        """
        # http :6543/api/v1/company/{id}/
        return Response(json={'message': 'Provided a single resource for company'}, status=200)
