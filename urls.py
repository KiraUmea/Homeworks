"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about/', include('myapp.urls')),
    # path('/', name='/'),
    # path('<slug>/', include('/<slug>/')),
    # path('<slug>/comment/', include('/<slug>/comment/')),
    # path('create/', include('/create/')),
    # path('<slug>/update/', include('/<slug>/update/')),
    # path('<slug>/delete/', include('/<slug>/delete/')),
    # path('profile/<username>/', include('/profile/<username>/')),
    # path('change_password/', include('/change_password/')),
    # path('register/', include('/register/')),
    # path('login/', include('/login/')),
    # path('logout/', include('/logout/'))
]

