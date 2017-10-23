from . import models, serializers
from rest_framework import viewsets, views, status, filters, pagination, permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication


# class PersonView(views.APIView):
    # '''Regresa una lista de personas. Metodos permitidos: GET'''
    # def get(self, request, format = None):
    #     serial = serializers.PersonSerializer(models.Person.objects.all(), many=True)
    #     return Response(serial.data)

    # def post(self, request, format=None):
    #     serial = serializers.PersonSerializer(data=request.data)
    #     if serial.is_valid():
    #         serial.save()
    #         return Response(serial.data, status=status.HTTP_201_CREATED)
    #     return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
    # permission_classes = [TokenHasScope]
    # required_scopes = ['read']
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name',)
    ordering_fields=('name',)

# class PersonView(generics.ListAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.PersonSerializer

# class PersonView(generics.ListAPIView):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.PersonSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('name','program__name')

#class PersonView(views.APIView):

    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    # def get(self, request, format=None):
    #     user = request.user
    #     print(request.user)

    #     return Response({"hola":{"mundo"}})


# class PersonViewset(viewsets.ModelViewSet):
#     queryset = models.Person.objects.all()
#     serializer_class = serializers.PersonSerializer

class PersonViewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

# class FileUploadView(views.APIView):
    
#     parser_classes = (FileUploadParser,)

#     def put(self, request, filename, format=None):
#         file_obj = request.FILES['file']
#         f = open('/tmp/test_upload', 'w')
#         f.write('test123\n')
#         f.close()
#         f = open('/tmp/test_upload', 'rb')
#         return Response(status=204)
