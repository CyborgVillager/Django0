from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404
from django.template import loader


from .models import Question
# Index
def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# Detail 404 Error
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



# Result
def results(request, question_id):
    response = 'Result for question %s.'
    return HttpResponse(response % question_id)

# Voted
def vote(request, question_id):
    return HttpResponse('You\'ve voted for question %s.' % question_id)