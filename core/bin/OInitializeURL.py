import re
from urllib.parse import urlparse, parse_qs

class OInitializeURL:
    def __init__(self, Url):
        self._url = Url
        parsed_url = urlparse(self._url)

        self._scheme = parsed_url.scheme  # 协议部分
        self._netloc = parsed_url.netloc  # 域名部分
        self._path = parsed_url.path      # 地址部分
        self._query = parsed_url.query    # 查询部分

        self.query_dict = parse_qs(self._query)

    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, value):
        self._scheme = value

    @property
    def netloc(self):
        return self._netloc

    @netloc.setter
    def netloc(self, value):
        self._netloc = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
        self.query_dict = parse_qs(self._query)

    def print_all(self):
        print(f"Scheme: {self.scheme}")
        print(f"Netloc: {self.netloc}")
        print(f"Path: {self.path}")
        print(f"Query: {self.query}")

        if self.query_dict:
            print("Query Parameters:")
            for param, values in self.query_dict.items():
                print(f"  {param}: {', '.join(values)}")

if __name__ == "__main__":
    url = "https://www.example.com:8080/?param1=value1&param2=value2&param2=value3"
    oinitialize_url = OInitializeURL(url)
    oinitialize_url.print_all()

    # 测试 get 和 set 方法
    oinitialize_url.scheme = "http"
    oinitialize_url.netloc = "www.test.com"
    oinitialize_url.path = "/test"
    oinitialize_url.query = "paramA=valueA&paramB=valueB"
    oinitialize_url.print_all()
