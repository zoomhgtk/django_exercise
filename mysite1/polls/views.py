from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views import generic

from .models import Choice, Question

from django.utils import timezone
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    '''
    Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset containing Questions whose
    pub_date is less than or equal to -that is, earlier than or equal to -timezone.now()
    '''
    #    """Return the last five published questions."""
    #    return Question.objects.order_by('-pub_date')[:5]
    # comment out on Jan 21st

    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
    #        'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
# we are changing to Generic views. A sense of Object Oriented.


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/detail.html', {'question': question}) 

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST['choice'] returns the ID of the selected choice.
    except (KeyError, Choice.DoesNotExist):
        # Will raise KeyError if choice was not provided in pOST Data
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
            })
    else:
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
        #always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from
        #being posted twice if a user hits the Back button. hmm......
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

