from rest_framework import viewsets
from events.models import Event
from events.serializers import EventSerializers
from permissions import EventAccess
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated, EventAccess]
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.check_object_permissions(request, instance) 
        event = get_object_or_404(Event, id=self.kwargs["pk"])
        event.delete()
        return Response({"detail": "Evènement supprimé."}, status=status.HTTP_202_ACCEPTED)
