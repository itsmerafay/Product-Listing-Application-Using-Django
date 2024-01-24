
from django.contrib import admin
from django.urls import path
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index , name = "index"),
    path('table/', table , name = "table"),
    path('delete-product/<id>/', deleteproduct , name = "deleteproduct"),
    path('update-product/<id>/', updateproduct , name = "updateproduct"),
    path('login/', login_page , name = "login_page"),
    path('register/', register_page , name = "register_page"),
    path('logout/', logout_page , name = "logout_page"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
