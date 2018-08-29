from pyramid_restful.views import APIView
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models import Account
import json


class AuthAPIView(APIView):
    def create(self, request, auth=None):
        data = json.loads(request.body)
        if auth == 'register':
            try:
                user = Account.new(
                    request,
                    data['email'],
                    data['password'],
                )
            except (IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)

            return Response(json='Created', status-201)

        if auth == 'login':
            pass
        return Response(json='Not Found', status=404)
