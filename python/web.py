import urllib.request,  urllib.parse, urllib.error
import my_exceptions
import json
import logger
import sys, os

class WebService:
    '''Es la clase para pedir solicitudes

    Attributes:
    url -- Necesita una url para funcionar
    '''

    __log = logger.Log()
    __data = {}
    __headers = {}
    __file = os.path.basename(__file__)
    def __init__(self, url):
        self.url = url

    def __request(self):
        try:
            response = urllib.request.urlopen(self.url)
            self.__log.info(self.__file, 'request', 'url request successfull')
            self.__log.debug(self.url)
            return response
        except Exception as err:
            raise my_exceptions.CustomError("Error en la url", sys.exc_info())

    def __get_read_from_request(self, request):
        try:
            return request.read()
        except:
            raise my_exceptions.CustomError("No se puede leer el request", sys.exc_info())

    def __parse_values_for_post(self, values):
        data = urllib.parse.urlencode(values)
        self.__data = data.encode('utf-8')

    def __set_headers(self, values):
        self.__headers = values

    def __post_request(self):
        return urllib.request.Request(self.url, self.__data, self.__headers)

    def get(self):
        '''get request'''
        request  = self.__request()
        response = self.__get_read_from_request(request)
        return response
        
    def post(self, headers, values):
        '''make post request'''
        self.__set_headers(headers)
        self.__parse_values_for_post(values)
        request = self.__post_request()
        response = self.get()
        return response

    def return_json(self, func):
        '''return json response'''
        try:
            response = json.loads(func)
            return response
        except json.decoder.JSONDecodeError as err:
            raise my_exceptions.CustomError("Error en el json format", sys.exc_info())
        except Exception as excepti:
            raise my_exceptions.CustomError(excepti, sys.exc_info())

        
        

    
