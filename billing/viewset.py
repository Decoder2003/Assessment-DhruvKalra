from rest_framework import viewsets
from .models import *
from .serializers import *

class invoiceViewset(viewsets.ModelViewSet):
    queryset = invoice.objects.all()
    serializer_class = invoiceSerializer

class invoiceDetailViewset(viewsets.ModelViewSet):
    queryset = invoiceDetail.objects.all()
    serializer_class = invoiceDetailSerializer