from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    pw = models.CharField(max_length=20)
class Scrap(models.Model):
    store_name = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    locality = models.CharField(max_length=2000,default=None)
    phone = models.CharField(max_length=20)
    img_path = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.first