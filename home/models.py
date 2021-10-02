from django.db import models

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

    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=132, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.FileField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)
    pdf = models.FileField(upload_to='detaispdf', max_length=100)
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

class City1(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City2(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City3(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City4(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City5(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City6(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City7(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City8(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City9(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name


class City10(models.Model):
    Name = models.CharField(max_length=122, default = "NA")
    Shape = models.CharField(max_length=12, default="NA")
    Size = models.CharField(max_length=30, null=True, default="NA")
    Type = models.CharField(max_length=30, default="NA")
    Material = models.CharField(max_length=12, default="NA")
    Countertop = models.CharField(max_length=12, default="NA")
    Loft = models.CharField(max_length=12, default="NA")
    Finish = models.CharField(max_length=12, default="NA")
    Accessories = models.CharField(max_length=12, default="NA")
    Services = models.TextField(max_length=32, default="NA")
    Appliances = models.TextField(max_length=32, default="NA")
    # customer = models.ForeignKey(c_details, blank=True, null=True, on_delete=models.CASCADE )
    Price = models.CharField(max_length=12, default="NA")
    Location = models.CharField(max_length=12, default="NA")
    date = models.DateField(default=1111-11-11)

    def __str__(self):
        return self.Name