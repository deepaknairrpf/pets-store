from rest_framework.viewsets import ModelViewSet

from .models import Pet, PetViewCounter
from .serializers import PetSerializer
from rest_framework.response import Response
import math


class PetModelViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        view_count = PetViewCounter.incr(instance)
        instance.view_count = view_count

        for _ in range(1000000):
            math.sqrt(_)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
