from rest_framework import serializers
from userproject.models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'likes', 'start_date', 'end_date')