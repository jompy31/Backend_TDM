from rest_framework import serializers
from files.models import File, NewsPost, Distributor

class FileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = File
        fields = ['id', 'file', 'user', 'created_at', 'name']

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = '__all__'

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'