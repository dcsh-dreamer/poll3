from django.shortcuts import render
from .models import Poll

# Create your views here.
def poll_list(req):
    polls = Poll.objects.all()
    return render(req, 'poll_list.html', {'poll_list': polls})
