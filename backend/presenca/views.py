from rest_framework import viewsets

from .models import CadastraPresenca
from .serializers import CadastraPresencaSerializer


class CadastraPresencaViewSet(viewsets.ModelViewSet):

    serializer_class = CadastraPresencaSerializer
    queryset = CadastraPresenca.objects.all()
# Create your views here.
