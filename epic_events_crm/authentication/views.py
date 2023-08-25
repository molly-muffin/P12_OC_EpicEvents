from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from permissions import UserAccess
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserAccess]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        user = get_object_or_404(User, id=self.kwargs["pk"])
        user.delete()
        return Response({"detail": "Utilisateur supprimé."}, status=status.HTTP_202_ACCEPTED)
