from rest_framework import serializers
from cbvapi.models import Movie

def first_letter(value):
    if value[0].islower():
        raise serializers.ValidationError('first letter should be uppercase')

class MovieSerial(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    movie=serializers.CharField(validators=[first_letter])
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




#----------validations----------------------
    def validate(self, data):
        if data['movie']==data['desc']:
            raise serializers.ValidationError('movie name and desc not be same')
        else:
            return data

    def validate_movie(self, value):
        if  len(value)< 2:
            raise serializers.ValidationError('name is too short')
        else:
            return value
        