from rest_framework import serializers
from base.models import Word, Time, Mistake, BannerClick, Game

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'

class MistakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mistake
        fields = '__all__'

class BannerClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerClick
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    website = serializers.CharField(allow_blank=True)
    app_store = serializers.CharField(allow_blank=True)
    google_play = serializers.CharField(allow_blank=True)
    video = serializers.CharField(allow_blank=True)
    class Meta:
        model = Game
        fields = ['pk', 'name', 'description', 'website', 'app_store', 'google_play', 'video', 'image', 'genre']

class FullGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'