from rest_framework import status
from rest_framework.exceptions import APIException


class PasswordMismatchException(APIException):
    """
    raise if password and password_confirm mismatch.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Password and Confirm Password fields must have the same value."
    default_code = "bad_request"


class InvalidStartTimeException(APIException):
    """
    raise if past time is chosen during booking.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Past time can not be chosen during booking."
    default_code = "bad_request"


class TimeValidationException(APIException):
    """
    raise if end_time is not greater than start_time.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "End time must be greater than start time."
    default_code = "bad_request"


class RoomNotAvailableException(APIException):
    """
    raise if Room is not available in provided range of time.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Room is not available in this range of time."
    default_code = "bad_request"
