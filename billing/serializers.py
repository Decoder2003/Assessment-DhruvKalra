from rest_framework import serializers
from .models import *

class invoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = invoice
        fields = "__all__"

class invoiceDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = invoiceDetail
        fields = "__all__"