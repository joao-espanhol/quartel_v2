from django.http import HttpResponseForbidden
from functools import wraps

def user_is_aprov(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.user_type == 'aprov':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Você não tem permissão para visualizar esta página.")
    return _wrapped_view
