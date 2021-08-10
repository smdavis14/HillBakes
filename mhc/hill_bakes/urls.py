from django.urls import path
from .views import home_page, cookies, cakes, cake_balls, about, login, signup

app_name = 'hill_bakes'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('cookies/', cookies, name='cookies'),
    path('cakes/', cakes, name='cakes'),
    path('cake_balls/', cake_balls, name='cake_balls'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
