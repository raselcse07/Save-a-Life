from django.db import models



BLOOD_GROUP_LIST = [

    ("a+","A+"),
    ("a-","A-"),
    ("b+","B+"),
    ("b-","B-"),
    ("o+","O+"),
    ("o-","O-"),
    ("ab+","AB+"),
    ("ab-","AB-"),
]

class Distict(models.Model):
    name        = models.CharField(max_length=220)

    class Meta:
        ordering = ["name"]


    def __str__(self):
        return str(self.name)


class PoliceStation(models.Model):
    distict     = models.ForeignKey(Distict,on_delete = models.CASCADE) 
    name        = models.CharField(max_length=220)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return str(self.name)


class Donar(models.Model):
    name                = models.CharField(max_length=220)
    mobile_number_1     = models.CharField(max_length=220)
    mobile_number_2     = models.CharField(max_length=220,null=True,blank=True)
    blood_group         = models.CharField(max_length=220,choices=BLOOD_GROUP_LIST)
    address             = models.CharField(max_length=220)
    distict             = models.ForeignKey(Distict, on_delete=models.SET_NULL, null=True)
    police_station      = models.ForeignKey(PoliceStation, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ["blood_group"]
    
    def __str__(self):
        return self.name
