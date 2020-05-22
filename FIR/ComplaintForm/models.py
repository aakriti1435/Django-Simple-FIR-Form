from django.db import models

# Create your models here.
class InputForm(models.Model):
    complainant_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=500, null=True, blank=True, default="")
    last_name = models.CharField(max_length=500, null=True, blank=True, default="")
    father_husband_name = models.CharField(max_length=500, null=True, blank=True, default="")
    email = models.CharField(max_length=100, null=True, blank=True, default="")
    mobile = models.CharField(max_length=100, default=0, null=True, blank=True)
    address1 = models.CharField(max_length=500, null=True, blank=True, default="")
    address2 = models.CharField(max_length=500, null=True, blank=True, default="")
    city = models.CharField(max_length=100, null=True, blank=True, default="")
    state = models.CharField(max_length=100, null=True, blank=True, default="")
    zip_code = models.CharField(max_length=100, null=True, blank=True, default="")
    distance = models.CharField(max_length=100, default=0, null=True, blank=True)
    direction = models.CharField(max_length=500, null=True, blank=True, default="")
    date = models.DateField()
    time = models.TimeField()
    nature_offence = models.CharField(max_length=500, null=True, blank=True, default="")
    particulars_property = models.CharField(max_length=1000, null=True, blank=True, default="")
    description_accused = models.CharField(max_length=1000, null=True, blank=True, default="")
    witness_details = models.CharField(max_length=1000, null=True, blank=True, default="")
    brief_facts = models.CharField(max_length=1000, null=True, blank=True, default="")

    def __str__(self):
        return self.first_name