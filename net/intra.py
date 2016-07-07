
"""
" HTTP/SSL/...
"""
from http.client import HTTPSConnection
from base64 import b64encode

class IntraRetriever():

    __INTRA_URL = "intra.epitech.eu"
    # https_handler
    # https_manager
    # auth_handler


    def __init__(self):
        self.connection = HTTPSConnection(self.__INTRA_URL)


    def auth(self, login, passwd):
        auth = bytes(login + ':' + passwd, 'utf-8')
        connect_infos = b64encode(auth).decode('ascii')
        self.connect_headers = { 'Authorization': 'Basic ' + connect_infos }

        self.connection.request('GET', '/', headers=self.connect_headers)
        response = self.connection.getresponse()
        if response is not None:
            print(response.read())
            print("Auth SUCCESS")
        else:
            print("Auth FAIL")


    def connect(self, login, passwd, route):
        print(login)
        print(passwd)
        self.auth(login, passwd)
