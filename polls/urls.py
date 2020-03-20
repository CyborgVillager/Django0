from django.urls import path
from . import views
# Try to import views.py info for polls
try:
    from .import views
    app_name = 'polls'

    urlpatterns = [
        # e.g URL: url/polls
        # -> Hello this is the poll index

        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
    print('.import views success @ polls/urls.py')
except:
    print('Unable to import views. Please check polls/urls.py for more information.' + '\n'
          +'Thank You')

