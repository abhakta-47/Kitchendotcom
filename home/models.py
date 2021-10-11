from django.db import models
from django.db.models.deletion import CASCADE
from uuid import uuid4
from datetime import datetime
# Create your models here.


class c_details(models.Model):
    name = models.CharField(max_length=122, default="NA")
    phone = models.CharField(max_length=12, default="NA")
    email = models.CharField(max_length=122, default="NA")
    location = models.CharField(max_length=12, default="NA")
    message = models.TextField(default="NA")

    def __str__(self):
        return self.name


class kitchen_details(models.Model):
    Name = models.CharField(max_length=122, default="NA")
    Phone = models.CharField(max_length=12, default="NA")
    Email = models.CharField(max_length=122, default="NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=132, default="NA")
    Appliances = models.TextField(max_length=132, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(auto_created=True)
    # Summary_Pdf = models.FileField(upload_to = 'pdf/',  default="/Summary.pdf")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Kitchen Details'
        verbose_name_plural = 'Kitchen Details'

    def __str__(self):
        return self.Name

# Model after adding sessions


class Constant(models.Model):
    Essentials = models.CharField(max_length=12, default="NA")
    Premium = models.CharField(max_length=12, default="NA")
    Luxe = models.CharField(max_length=12, default="NA")
    countertop = models.CharField(max_length=12, default="NA")
    HDHMR = models.CharField(max_length=12, default="NA")
    MR_Plywood = models.CharField(max_length=12, default="NA")
    BWR_Plywood = models.CharField(max_length=12, default="NA")
    BWP_Plywood = models.CharField(max_length=12, default="NA")
    Laminate = models.CharField(max_length=12, default="NA")
    PVC_Laminate = models.CharField(max_length=12, default="NA")
    Anti_scratch_Acrylic = models.CharField(max_length=12, default="NA")
    Glossy_PU = models.CharField(max_length=12, default="NA")
    Basic_Acc = models.CharField(max_length=12, default="NA")
    Intermediate_Acc = models.CharField(max_length=12, default="NA")
    Prem_Acc = models.CharField(max_length=12, default="NA")

    def __str__(self):
        return "Rates"


class City(models.Model):
    kitchen = models.OneToOneField(
        kitchen_details, on_delete=models.CASCADE, blank=True, null=True)
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(auto_created=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.kitchen:
            self.kitchen = kitchen_details.objects.create()
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if self.kitchen:
            self.kitchen.delete()

    def __str__(self):
        return self.kitchen.Name


class City1(City):
    class Meta:
        proxy = True
        verbose_name = 'Varanasi kitchen'


class City2(City):
    class Meta:
        proxy = True
        verbose_name = 'Chandauli kitchen'


class City3(City):
    class Meta:
        proxy = True
        verbose_name = 'Mirzapur kitchen'


class City4(City):
    class Meta:
        proxy = True
        verbose_name = 'Sonbhadra kitchen'


class City5(City):
    class Meta:
        proxy = True
        verbose_name = 'Ayodhya kitchen'


class City6(City):
    class Meta:
        proxy = True
        verbose_name = 'Prayagraj kitchen'


class City7(City):
    class Meta:
        proxy = True
        verbose_name = 'Lucknow kitchen'


class City8(City):
    class Meta:
        proxy = True
        verbose_name = 'Bhadohi kitchen'


class City9(City):
    class Meta:
        proxy = True
        verbose_name = 'Gorakhpur kitchen'


class City10(City):
    class Meta:
        proxy = True
        verbose_name = 'Sonbhadra kitchen'


class City11(City):
    class Meta:
        proxy = True
        verbose_name = 'Mirzapur kitchen'


class TempLink(models.Model):
    kitchen_details = models.OneToOneField(kitchen_details, on_delete=CASCADE)
    link = models.UUIDField(default=uuid4, unique=True,)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.kitchen_details.Name
