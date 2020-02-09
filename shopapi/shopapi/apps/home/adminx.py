from .models import Banner, Nav
import xadmin
from xadmin import views


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobleSetting:
    site_title = 'shop'
    site_footer = 'my-shop'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView,GlobleSetting)


class BannerModelAdmin:
    list_display = ['name', 'order', 'is_show']


xadmin.site.register(Banner, BannerModelAdmin)


class NavModelAdmin:
    list_display = ['name', 'order', 'opt']


xadmin.site.register(Nav, NavModelAdmin)


