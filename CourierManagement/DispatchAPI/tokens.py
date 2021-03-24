from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six,bcrypt
from secrets import token_hex
from django.conf import settings


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.id) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
childmail_activation_token = TokenGenerator()


class VerifyTokenUtil():
    def __init__(self):
        pass
    
    def Hash(password:str):
        return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")

    def Match(password:str,hashed:str):
        return bcrypt.checkpw(password.encode("UTF-8"),hashed.encode("UTF-8")) 

    def GeneratePassword():
        return str(token_hex(settings.PASS_LENGTH))