"""
" HTTP/SSL/...
"""
from http.client import HTTPSConnection
from base64 import b64encode
import http.cookiejar
import urllib

class IntraRetriever():

    __INTRA_URL = "https://intra.epitech.eu"
    # https_handler
    # https_manager
    # auth_handler


    def __init__(self):
        self.login = None
        self.passwd = None
        self.opener = None


    def auth(self, login, passwd):
        self.login = login
        self.passwd = passwd
        self.cookie_jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
                    urllib.request.HTTPRedirectHandler(),
                    urllib.request.HTTPHandler(),
                    urllib.request.HTTPSHandler(),
                    urllib.request.HTTPCookieProcessor(self.cookie_jar)
                )
        print(login)
        print(passwd)
        self.auth_data = urllib.parse.urlencode({
                'login': self.login,
                'pass': self.passwd
            })


    def retrieve(self, route, login=None, passwd=None):
        if login is not None and passwd is not None:
            self.auth(login, passwd)
        data = self.__get_at_route(route)
        return (data)


    def ping(self, route, login=None, passwd=None):
        ret = False

        try:
            if login is not None and passwd is not None:
                self.auth(login, passwd)
            data = self.__get_at_route(route)
            print(data)
            if data is not None and bytes('Password', 'utf-8') not in data:
                ret = True
        except Exception as err:
            try:
                ret = err.strerror
            except AttributeError:
                # print(err.with_traceback(err))
                ret = str(err)
        return (ret)


    def __get_at_route(self, route):
        ret = None
        print(self.auth_data)

        response = self.opener.open(self.__INTRA_URL + route, self.auth_data)
        if response is not None:
            ret = response.read()
        return (ret)
