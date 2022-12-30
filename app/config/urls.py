from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('awaken.urls')),
    path('auth/', include('userauth.urls'))
]
