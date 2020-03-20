from django.contrib import admin

# Question Imports
try :
    from .models import Question
    admin.site.register(Question)
    print('Polls Admin Module - Question Import Success')
except ImportError:
    print('Unable to import .models import Question.' + '\n' +
          'Please check polls/models.py or polls/admin.py for more information' + '\n'
          + 'Thank you.')



