from django.db import models
from django_mysql.models import JSONField


class Inventory(models.Model):
    serial_number = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

    class Meta:
        verbose_name_plural = "inventories"

    def __str__(self):
        return self.serial_number


class FileUpload(models.Model):
    filename = models.CharField(max_length=180)
    file_date = models.DateTimeField()
    field = models.FileField(upload_to='app/uploads/')
    calculate_field = JSONField(null=True)

    def __str__(self):
        return self.filename
