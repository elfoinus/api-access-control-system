from django.db import models
from django.contrib.auth.models import User

class Profile( models.Model ):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.IntegerField(null=True)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=13)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['phoneNumber', 'address', 'country', 'region', 'city']

    def __str__(self):
        return self.address

    class Meta:
        db_table='profiles'