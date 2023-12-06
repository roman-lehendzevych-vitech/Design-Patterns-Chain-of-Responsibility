class Request:
    def __init__(self, data):
        self.data = data
        self.valid = True


class RequestHandler:
    def __init__(self, handler=None):
        self.handler = handler

    def handle_request(self, request):
        if self.handler:
            self.handler.handle_request(request)


class AuthenticationHandler(RequestHandler):
    def handle_request(self, request):
        if "token" not in request.data:
            request.valid = False
            print("Authentication failed")
        super().handle_request(request)


class DataValidationHandler(RequestHandler):
    def handle_request(self, request):
        if not request.valid:
            return
        if "data" not in request.data:
            request.valid = False
            print("Data validation failed")
        super().handle_request(request)


class LoggingHandler(RequestHandler):
    def handle_request(self, request):
        if not request.valid:
            return
        print("Logging request")
        super().handle_request(request)


if __name__ == "__main__":
    new_request = Request({"token": "some_token", "data": "some_data"})

    authentication_handler = AuthenticationHandler()
    validation_handler = DataValidationHandler(authentication_handler)
    logging_handler = LoggingHandler(validation_handler)

    logging_handler.handle_request(new_request)

    if new_request.valid:
        print("Success")
    else:
        print("Failed")
