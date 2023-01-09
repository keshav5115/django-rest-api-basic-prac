from rest_framework import serializers
from restapp.models import Movie

class movieserial(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    movie=serializers.CharField()
    desc=serializers.CharField()
    active=serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.movie=validated_data.get('movie',instance.movie)
        instance.desc=validated_data.get('desc',instance.desc)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance