from rest_framework.serializers import ModelSerializer
from app.models import Post
from rest_framework import serializers

class PostSerializer(ModelSerializer):
    
    class Meta:
        model =  Post
        fields = ('id','UserName')


class PostDetailSerializer(ModelSerializer):
    
    class Meta:
        model =  Post
        fields = '__all__'

class PostDeleteSerializer(ModelSerializer):
    
    class Meta:
        model =  Post
        fields = '__all__'        

class PostUpdateSerializer(ModelSerializer):
    
    class Meta:
        model =  Post
        fields = '__all__'                