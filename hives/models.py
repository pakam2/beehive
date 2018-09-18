from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class HiveModel(models.Model):

    numberOfHive = models.IntegerField(null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    additional_info = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class FirstHiveDataModel(models.Model):

    first_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    first_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    first_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    first_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    second_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    second_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    second_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    second_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    third_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    third_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    third_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    third_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    fourth_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fourth_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fourth_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fourth_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    fifth_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fifth_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fifth_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fifth_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    sixth_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    sixth_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    sixth_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    sixth_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    seventh_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    seventh_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    seventh_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    seventh_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    eight_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    eight_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    eight_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    eight_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    ninth_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ninth_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ninth_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ninth_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    tenth_frame_honey = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    tenth_frame_speck = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    tenth_frame_beebread = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    tenth_frame_worm = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    addDate = models.DateField(auto_now_add=True)
    motherBee = models.BooleanField(default=False)
    hive = models.ForeignKey(HiveModel, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
