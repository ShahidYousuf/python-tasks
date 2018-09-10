from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }


    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question,
                                                     'error_message': "You didn't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            r_pass = form.cleaned_data.get('password')
            user = authenticate(username=username, password=r_pass)
            login(request, user)
            return redirect('polls:index')
        else:
            return redirect('polls:signup')
    else:
        form = UserCreationForm()
        return render(request,'polls/signup.html', {'form':form} )
@login_required(login_url='/accounts/login/')
def testpage(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'polls/testpage.html', {'username':username})

