from django.db import models

class Member(models.Model):

    price = models.DecimalField(max_digits=20 , decimal_places=2)
    Name = models.CharField(max_length=50)
    Place = models.CharField(max_length=150)
    date_time = models.DateTimeField (auto_now_add = True)