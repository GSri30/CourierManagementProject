from django.db import models

class EmailMapping(models.Model):
    ParentMail=models.CharField(max_length=50,blank=False)
    ChildMail=models.CharField(max_length=50,blank=False)
    HashedPassword=models.CharField(max_length=70,blank=False)
    Verified=models.BooleanField(default=False)

    def __str__(self):
        return self.ParentMail

class MobileNumberMapping(models.Model):
    ParentMail=models.CharField(max_length=50,blank=False)
    ChildNumber=models.CharField(max_length=50,blank=False)
    HashedPassword=models.CharField(max_length=70,blank=False)
    Verified=models.BooleanField(default=False)

    def __str__(self):
        return self.ParentMail