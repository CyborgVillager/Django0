from django.urls import path

# Try to import views.py info for polls
try:
    from .import views
    app_name = 'polls'
    urlpatterns = [
        # e.g URL: url/polls
        # -> Hello this is the poll index
        path('', views.index, name='index'),
        # e.g URL: /polls/#/
        # -> You are currently looking at question #
        path('<int:question_id>/', views.detail, name='detail'),
        # e.g URL: /polls/#/results/
        # -> Result for question #
        path('<int:question_id>/results/', views.results, name='results'),
        # e.g URL: /polls/#/vote/
        # -> You've voted for question #
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
    print('.import views success @ polls/urls.py')
except:
    print('Unable to import views. Please check polls/urls.py for more information.' + '\n'
          +'Thank You')

