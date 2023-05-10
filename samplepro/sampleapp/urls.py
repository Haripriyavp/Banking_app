from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('temporary/',views.temporary,name='temporary'),
    path('add_details/',views.add_details,name='add_details'),
    path('redirecting/',views.redirecting,name='redirecting'),
    path('logout/',views.logout,name='logout'),
]
