
from tools.src._shared.controller.https.http_response import HttpResponse
from tools.src._shared.errors.bad_request import BadRequestError
from tools.src._shared.errors.forbidden import ForbiddenError
from tools.src._shared.errors.not_found import NotFoundError
from tools.src._shared.errors.unauthorized import UnauthorizedError


def handle_errors(error: Exception) -> HttpResponse:

    if(isinstance(BadRequestError)):
        return HttpResponse(
            status_code=400,
            body=error.message
        )
    
    if(isinstance(NotFoundError)):
        return HttpResponse(
            status_code=404,
            body=error.message
    )

    if(isinstance(UnauthorizedError)):
        return HttpResponse(
            status_code=401,
            body=error.message
    )

    if(isinstance(ForbiddenError)):
        return HttpResponse(
            status_code=403,
            body=error.message
        )


    return HttpResponse(
        status_code=500,
        body=error.message,
    )