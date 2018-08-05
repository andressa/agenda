from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()

    class Meta:
        model = Meeting
        fields = ('id', 'name', 'date')
