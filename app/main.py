class Request:
    def __init__(self, data):
        self.data = data
        self.valid = True


def auth_handler(func):
    def wrapper(request):
        if "token" not in request.data:
            request.valid = False
            print("Authentication failed")
        return func(request)
    return wrapper


def data_handler(func):
    def wrapper(request):
        if "data" not in request.data:
            request.valid = False
            print("Data validation failed")
        return func(request)
    return wrapper


def login_handler(func):
    def wrapper(request):
        if request.valid:
            print("Logging request")
        return func(request)
    return wrapper


@auth_handler
@data_handler
@login_handler
def request_handler(request):
    if not request.valid:
        return "Failed"
    return "Success"


if __name__ == "__main__":
    new_request = Request({"token": "some_token", "data": "some_data"})

    print(request_handler(new_request))
