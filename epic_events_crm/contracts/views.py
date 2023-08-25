from rest_framework import viewsets
from contracts.models import Contract
from contracts.serializers import ContractSerializer
from permissions import ContractAccess
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404



class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractAccess]
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.check_object_permissions(request, instance) 
        contract = get_object_or_404(Contract, id=self.kwargs["pk"])
        contract.delete()
        return Response({"detail": "Contrat supprimé."}, status=status.HTTP_202_ACCEPTED)
