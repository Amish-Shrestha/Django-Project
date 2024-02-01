from functools import wraps
from django.http import HttpResponseForbidden

def user_group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is in the specified group
            if request.user.groups.filter(name=group_name).exists():
                # User is in the group, proceed with the original view function
                return view_func(request, *args, **kwargs)
            else:
                # User is not in the group, return a forbidden response
                return HttpResponseForbidden("Permission Denied: You don't have the required group.")

        return _wrapped_view

    return decorator

def group_permission_required(group_name, permissions):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is in the specified group
            if request.user.groups.filter(name=group_name).exists():
                # Check if the user has any of the specified permissions within the group
                if any(request.user.has_perm(permission) for permission in permissions):
                    # User has the required permission, proceed with the original view function
                    return view_func(request, *args, **kwargs)
                else:
                    # User doesn't have the required permission, return a forbidden response
                    return HttpResponseForbidden("Permission Denied: You don't have the required permission.")
            else:
                # User is not in the group, return a forbidden response
                return HttpResponseForbidden("Permission Denied: You don't have the required group.")

        return _wrapped_view

    return decorator
