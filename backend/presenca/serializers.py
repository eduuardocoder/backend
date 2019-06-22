from rest_framework import serializers

from .models import CadastraPresenca


class CadastraPresencaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CadastraPresenca
        fields = '__all__'
