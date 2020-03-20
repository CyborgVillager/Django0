from django.urls import path

# Try to acquire views.py info
try:
    from .import views
except:
    print('Unable to import views. Please check polls/urls.py for more information.' + '\n'
          +'Thank You')

urlpatterns = [
    path('', views.index, name='index')
]