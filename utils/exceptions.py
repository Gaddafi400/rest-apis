from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    handlers = {
        'ValidationError': _handle_validation_error,
        'Http404': _handle_not_found_error,
        'NotAuthenticated': _handle_authentication_error,
        'ObjectDoesNotExist': _handle_object_does_not_exist_error,
        'TooManyRequests': _handle_too_many_requests_error,
        'AuthenticationFailed': _handle_authentication_failed_error,
        'ParseError': _handle_parse_error,
        'PermissionDenied': _handle_permission_denied_error,
        'MethodNotAllowed': _handle_method_not_allowed_error,
        'NotAcceptable': _handle_not_acceptable_error,
        'Conflict': _handle_conflict_error,
        'UnsupportedMediaType': _handle_unsupported_media_type_error,
        'InternalServerError': _handle_internal_server_error,
        'NotImplemented': _handle_not_implemented_error,
        'BadGateway': _handle_bad_gateway_error,
        'ServiceUnavailable': _handle_service_unavailable_error,
        # Add more custom handlers here...
    }

    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        # import pdb
        # pdb.set_trace()
        return handlers[exception_class](exc, context)

    # If no custom handler is found, use the default DRF exception handler
    return exception_handler(exc, context)


# Define more custom handler functions here...

def _handle_validation_error(exc, context):
    return Response({'detail': 'Validation error', 'errors': exc.detail}, status=status.HTTP_400_BAD_REQUEST)


def _handle_not_found_error(exc, context):
    return Response({'detail': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)


def _handle_permission_denied_error(exc, context):
    return Response({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)


def _handle_authentication_error(exc, context):
    return Response({'detail': 'Authentication required 💥', 'status': status.HTTP_401_UNAUTHORIZED},
                    status=status.HTTP_401_UNAUTHORIZED)


def _handle_method_not_allowed_error(exc, context):
    return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def _handle_object_does_not_exist_error(exc, context):
    return Response({'detail': 'Resource does not exist'}, status=status.HTTP_404_NOT_FOUND)


def _handle_too_many_requests_error(exc, context):
    return Response({'detail': 'Too many requests'}, status=status.HTTP_429_TOO_MANY_REQUESTS)


def _handle_unsupported_media_type_error(exc, context):
    return Response({'detail': 'Unsupported media type'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)


def _handle_authentication_failed_error(exc, context):
    return Response({'detail': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)


def _handle_parse_error(exc, context):
    return Response({'detail': 'Malformed request'}, status=status.HTTP_400_BAD_REQUEST)


def _handle_not_acceptable_error(exc, context):
    return Response({'detail': 'Not acceptable'}, status=status.HTTP_406_NOT_ACCEPTABLE)


def _handle_conflict_error(exc, context):
    return Response({'detail': 'Conflict'}, status=status.HTTP_409_CONFLICT)


def _handle_internal_server_error(exc, context):
    return Response({'detail': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def _handle_not_implemented_error(exc, context):
    return Response({'detail': 'Not implemented'}, status=status.HTTP_501_NOT_IMPLEMENTED)


def _handle_bad_gateway_error(exc, context):
    return Response({'detail': 'Bad gateway'}, status=status.HTTP_502_BAD_GATEWAY)


def _handle_service_unavailable_error(exc, context):
    return Response({'detail': 'Service unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

# Add more custom handler functions as needed...
