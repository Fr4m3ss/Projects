"""movieproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from users import views as userviews
from django.contrib.auth import views as credviews
from movies.views import MovieListView,MovieDetailView
from reviews import views as reviewviews



								#placing all urls in entire application here-no other urls.py files in app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/',MovieListView.as_view(),name="movie-home"),
    path('movie/<int:pk>/',MovieDetailView.as_view(),name='movie-detail'),
    path('registration/',userviews.registration,name='registration'),			#calls fxn 'registration' in views.py
    path('',credviews.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',credviews.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('movie/leavereview/',reviewviews.LeaveReview,name='leave-review'),		#calls this fxn in views.py

]


