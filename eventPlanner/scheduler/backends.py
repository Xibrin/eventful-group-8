#from django.contrib.auth.backends import ModelBackend
#from .models import User

#class EmailBackendAuth(ModelBackend):
   # def authenticate(self, username = None, password = None, **kwargs):
        #if '@' in username:
           # kwargs = {'email': username}
       # else:
           # return None
       # if password is None:
          #  return None
        #try:
          #  user = User.objects.get(**kwargs)
        #except User.DoesNotExist:
           # User.set_password(password)

        #else:
            #if user.check_password(password) and self.user_can_authenticate(user):
                #return user





