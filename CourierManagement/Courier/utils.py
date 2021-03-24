'''
Checks if the given mail id has iiitb domain
'''

def IIITBdomain(mailId:str):
    return mailId.split('@')[1] == 'iiitb.org' or mailId.split('@')[1] == 'iiitb.ac.in'