from django.contrib import admin



# Question Imports
try :
    from .models import Question,Choice
    # Question choices , can modify # of questions from -> extra
    class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3

    class QuestionAdmin(admin.ModelAdmin):
        # fields of question
        fieldsets = [
            (None, {'fields': ['question_text']}),
            ('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline]

        # Shows Date published info / check if it was published recently on the questions txt list
        list_display = ('question_text', 'published_date', 'was_published_recently')
        # symbol / connects to models.py
        list_filter = ['published_date']
        # search for questions bar
        search_fields = ['question_text']
    admin.site.register(Question, QuestionAdmin)



    print('Polls Admin Module - Question Import Success')
except ImportError:
    print('Unable to import .models import Question.' + '\n' +
          'Please check polls/models.py or polls/admin.py for more information' + '\n'
          + 'Thank you.')



