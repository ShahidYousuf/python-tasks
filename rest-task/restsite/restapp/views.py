from rest_framework import status
#from rest_framework.decorators import api_view
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
#@api_view(['GET', 'POST'])
#def quote_list(request):
#    # list all quotes
#    if request.method == 'GET':
#        quotes = Quote.objects.all()
#        serializer = QuoteSerializer(quotes, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = QuoteSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# using class based view

class QuoteList(APIView):
    # get list of quotes
    def get(self, request, format=None):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)
    # create a new quote
    def post(self, request, format=None):
        serializer = QuoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteDetail(APIView):
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

