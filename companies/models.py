from django.db import models

class Company( models.Model ):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    nit = models.CharField()
    name = models.CharField(max_length=255)
    commerceName = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    webSite = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['phoneNumber', 'address', 'country', 'region', 'city']

    def __str__(self):
        return self.address

    class Meta:
        db_table='profiles'
