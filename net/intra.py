
"""
" HTTP/SSL/...
"""
from http.client import HTTPSConnection
from base64 import b64encode

class IntraRetriever():

    __INTRA_URL = "intra.epitech.eu"
    __REQUEST_GET = "GET"
    # https_handler
    # https_manager
    # auth_handler


    def __init__(self):
        self.connection = HTTPSConnection(self.__INTRA_URL)
        self.login = None
        self.passwd = None


    def auth(self, login, passwd):
        self.login = login
        self.passwd = passwd
        auth = bytes(login + ':' + passwd, 'utf-8')
        connect_infos = b64encode(auth).decode('ascii')
        self.connect_headers = { 'Authorization': 'Basic ' + connect_infos }


    def retrieve(self, route, login=None, passwd=None):
        if login is not None and passwd is not None:
            self.auth(login, passwd)
        data = self.__get_at_route(route)
        return (data)


    def ping(self, route, login=None, passwd=None):
        ret = False

        if login is not None and passwd is not None:
            self.auth(login, passwd)
        data = self.__get_at_route(route)
        if data is not None and bytes('Password', 'utf-8') not in data:
            ret = True
        return (ret)


    def __get_at_route(self, route):
        ret = None
        self.connection.request(self.__REQUEST_GET, '/', headers=self.connect_headers)
        response = self.connection.getresponse()
        if response is not None:
            ret = response.read()
        return (ret)
