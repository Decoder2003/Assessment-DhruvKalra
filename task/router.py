from billing.viewset import *
from rest_framework import routers
router = routers.DefaultRouter()

router.register('invoice', invoiceViewset, 'invoice')
router.register('invoicedetail', invoiceDetailViewset, 'invoicedetail')