from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Word, Time, Mistake, BannerClick
from .serializers import WordSerializer, TimeSerializer, MistakeSerializer, BannerClickSerializer
from random import shuffle
from django.db.models import Q

@api_view(['GET'])
def getWords(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWordsByLevel(request, level, activity):
    if level == 0:
        words = Word.objects
    else:
        words = Word.objects.filter(level=level)
    if activity==2:
        if level == 0:
            words = Word.objects.filter(~Q(regular="null"))
        else:
            words = Word.objects.filter(level=level).filter(~Q(regular="null"))
    if activity==3:
        if level == 0:
            words = Word.objects.filter(~Q(conjugation="null"))
        else:
            words = Word.objects.filter(level=level).filter(~Q(conjugation="null"))
    serializer = WordSerializer(words, many=True)

    wordList = []
    for i in serializer.data:
        wordList.append(i)
    shuffle(wordList)

    return Response(wordList[:10])

@api_view(['POST'])
def addWord(request):
    serializer = WordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getLeaderboard(request):
    times = Time.objects.all().order_by('time').values()
    serializer = TimeSerializer(times, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLeaderboardLevel(request, level):
    times = Time.objects.filter(level=level).order_by('time').values()
    serializer = TimeSerializer(times, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTime(request):
    serializer = TimeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getMistakes(request):
    mistakes = Mistake.objects.all()
    serializer = MistakeSerializer(mistakes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addMistake(request):
    serializer = MistakeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getBannerClicks(request):
    bannerClicks = BannerClick.objects.all()
    serializer = BannerClickSerializer(bannerClicks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addBannerClick(request):
    serializer = BannerClickSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)