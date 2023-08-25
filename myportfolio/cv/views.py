from rest_framework import generics
from .models import UserCV, WorkHistory, Education
from .serializers import UserCVSerializer, WorkHistorySerializer, EducationSerializer
from rest_framework import permissions


class UserCVListCreateView(generics.ListCreateAPIView):
    queryset = UserCV.objects.all()
    serializer_class = UserCVSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the CVs
        for the currently authenticated user.
        """
        user = self.request.user
        return UserCV.objects.filter(user=user)



