from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView, DeleteView

# Create your views here.
class PollCreate(CreateView):
    model = Poll
    fields = ["desc", 'subject']             #'__all__'
    success_url = '/poll/'

class PollEdit(UpdateView):
    model = Poll
    fields = ['subject', 'desc']
    success_url = '/poll/'

class PollList(ListView):
    model = Poll

class PollView(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['option_list'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return data

class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        opt = Option.objects.get(id=self.kwargs['oid'])
        # opt.count = opt.count + 1
        opt.count += 1
        opt.save()
        return '/poll/{}/'.format(opt.poll_id)
