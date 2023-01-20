from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("<str:username>", views.profile, name='profile'),

    # path("<str:username>", views.profile, name='profile'),
]
urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)