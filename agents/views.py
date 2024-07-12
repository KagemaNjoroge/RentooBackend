from rest_framework import viewsets
from .serializers import AgentSerializer, Agent


class AgentsViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
