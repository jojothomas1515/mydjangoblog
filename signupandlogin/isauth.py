from functools import wraps
from django.shortcuts import redirect


def is_authenticated(view_func):
    @wraps
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
