from rest_framework import serializers
from base.models import Word, Time, Mistake, BannerClick

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