from rest_framework import viewsets
from clients.models import Client
from clients.serializers import ClientSerializer
from permissions import ClientAccess
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientAccess]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        client = get_object_or_404(Client, id=self.kwargs["pk"])
        client.delete()
        return Response({"detail": "Client supprimé."}, status=status.HTTP_202_ACCEPTED)
