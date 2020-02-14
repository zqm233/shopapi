import xadmin
from xadmin import views
from .models import User

class UserModelAdmin:
    list_display = ['username', 'mobile', ]


# xadmin.site.register(User, UserModelAdmin)
