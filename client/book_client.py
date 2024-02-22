from requests import Response, get


class BookClient:
    def __init__(self):
        self.api_key = "123456"
        self.book_endpoint = "http://localhost:8081/api/books"

    def find_all(self) -> Response:
        return get(
            f"{self.book_endpoint}",
            headers={"ApiKey": self.api_key},
        )
