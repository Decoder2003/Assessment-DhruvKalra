from django.db import models
from datetime import datetime

class invoice(models.Model):

    date = models.DateField(default=datetime.now())
    invoiceNo = models.IntegerField()
    customerName = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("invoice")
        verbose_name_plural = ("invoices")
    def __str__(self):
        return f"{self.invoiceNo} {self.customerName}"

class invoiceDetail(models.Model):

    invoicee = models.ForeignKey(invoice,on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    quantity = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=11,decimal_places=4)
    price = models.DecimalField(max_digits=11,decimal_places=4)

    class Meta:
        verbose_name = ("invoiceDetail")
        verbose_name_plural = ("invoiceDetail")
    def __str__(self):
        return f"{self.invoicee}"