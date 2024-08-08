from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models  import User 
# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class AccountInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    reminder_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.account_name