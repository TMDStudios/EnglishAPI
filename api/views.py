from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Word, Time
from .serializers import WordSerializer, TimeSerializer

@api_view(['GET'])
def getWords(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWordsByLevel(request, level):
    words = Word.objects.filter(level=level)
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addWord(request):
    serializer = WordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getLeaderboard(request):
    times = Time.objects.all()
    serializer = TimeSerializer(times, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLeaderboardLevel(request, level):
    times = Time.objects.filter(level=level)
    serializer = TimeSerializer(times, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTime(request):
    serializer = TimeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)