from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def create_article(self, request):

    try:
        print(0)
    except print(0):
        pass
    
    return Response({})

@api_view(['GET'])
def fetch_articles(self, request):
    try:
        print(0)
    except print(0):
        pass

    return Response({})

@api_view(['DELETE'])
def delete_article(self, request, id):
    try:
        print(0)
    except print(0):
        pass
    return Response({})

@api_view(['GET'])
def fetch_article(self, request, id):
    try:
        print(0)
    except print(0):
        pass
    return Response({})

@api_view(['PUT'])
def update_article(self, request, id):
    try:
        print(0)
    except print(0):
        pass
    
    return Response({})
