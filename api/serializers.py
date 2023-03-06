from rest_framework import serializers
from base.models import Word, Time, Mistake

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