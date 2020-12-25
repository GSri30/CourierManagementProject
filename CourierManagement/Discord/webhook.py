from discord_webhooks import DiscordWebhooks
from .webhookURL import WEBHOOK_URL

class DiscordWebhook:
    def __init__(self,webhookURL):
        self.webhookURL=webhookURL
    
    def setWebhookURL(self,webhookURL):
        self.webhookURL=webhookURL
    
    # Static method
    def Notify(CourierId,FromName,StudentName,RollNumber,Email,Mobile,ReceivedDT,OtherInfo,edited):
        webhook=DiscordWebhooks(WEBHOOK_URL)
        webhook.title="New Courier! :smile:"
        webhook.description=f"Courier Id : {CourierId}"
        if(FromName):
            webhook.add_field(name='From', value=FromName)
        if(StudentName):
            webhook.add_field(name='Student Name', value=StudentName)
        if(RollNumber):
            webhook.add_field(name='Roll Number', value=RollNumber)
        if(Email):
            webhook.add_field(name='Email', value=Email)
        if(Mobile):
            webhook.add_field(name='Mobile', value=Mobile[:len(Mobile)-3]+"***")
        if(OtherInfo):
            webhook.add_field(name='Other Information', value=OtherInfo)
        if(ReceivedDT):
            if(edited):
                webhook.set_footer(text=f"Edited on {ReceivedDT}")
            else:    
                webhook.set_footer(text=f"Received on {ReceivedDT}")
        webhook.send()