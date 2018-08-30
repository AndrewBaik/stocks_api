from pyramid.response import Response
from pyramid.view import forbidden_view_config, notfound_view_config


@forbidden_view_config()
def forbidden(request):
    """ error display for forbidden
    """
    return Response(json='Forbidden', status=403)


@notfound_view_config()
def not_found(request):
    """ error display for not found
    """
    return Response(json='Not found', status=404)
