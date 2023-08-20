from rest_framework import viewsets
from clients.models import Client
from clients.serializers import ClientSerializer
from permissions import IsCommercialEmployeeOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsCommercialEmployeeOrReadOnly]
