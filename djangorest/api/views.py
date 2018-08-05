from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MeetingSerializer
from .models import Meeting
from django.http import Http404

import pdb

class MeetingsList(APIView):
    """
    Class to render `meetings` get and post
    """

    def get(self, request, format=None):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingDetails(APIView):
    """
    Retrieve a single `meeting` instance.
    """

    def get_object(self, id):
        try:
            return Meeting.objects.get(pk=id)
        except Meeting.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        meeting = self.get_object(id)
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

