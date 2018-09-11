from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.decorators import api_view
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.



class QuoteList(APIView):
    # adding authentication
    # authentication_classes = (SessionAuthentication, TokenAuthentication)
    # adding permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # get list of quotes
    # try to create token
    def get(self, request, format=None):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)
    # create a new quote
    def post(self, request, format=None):
       # token = Token.objects.create(user=request.user)
       # print("Token is {}".format(str(token)))
        serializer = QuoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteDetail(APIView):

    # add permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # Retrive, update or delete a quote

    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404
    # retrive an individual quote
    def get(self, request, pk, format=None):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    # update a quote
    def put(self, request, pk, format=None):
        quote = self.get_object(pk)
        serializer = QuoteSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a quote
    def delete(self, request, pk, format=None):
        quote = self.get_object(pk)
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data,
                                           context = {'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id': user.pk,
            'email':user.email
        })



