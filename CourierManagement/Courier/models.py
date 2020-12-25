from django.db import models


class Post(models.Model):
    CourierId=models.AutoField(primary_key=True)
    MessageId=models.CharField(max_length=100)
    FromName=models.CharField(max_length=100)
    StudentName=models.CharField(max_length=50)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Mobile=models.CharField(max_length=15,null=True,blank=True)
    RollNumber=models.CharField(max_length=50,null=True,blank=True)
    PODnumber=models.CharField(max_length=50)
    Received_On=models.DateTimeField(auto_now_add=True)
    OtherInformation=models.CharField(max_length=100,null=True,blank=True)
    Collected=models.BooleanField(default=False,null=True,blank=True)
    Collected_On=models.DateTimeField(null=True,blank=True)

    class Meta:
        ordering=['-Received_On',]
    
    def __str__(self):
        return f"{self.CourierId} {self.StudentName}"
    
    def getCourierId(self):
        return f"{self.CourierId}"
    
    def getMessageId(self):
        return f"{self.MessageId}"
    
    def getFromName(self):
        return f"{self.FromName}"
    
    def getStudentName(self):
        return f"{self.StudentName}"

    def getEmail(self):
        return f"{self.Email}"
    
    def getMobile(self):
        return f"{self.Mobile}"
    
    def getRollNumber(self):
        return f"{self.RollNumber}"
    
    def getReceivedOn(self):
        return f"{self.Received_On}"
    
    def getOtherInfo(self):
        return f"{self.OtherInformation}"