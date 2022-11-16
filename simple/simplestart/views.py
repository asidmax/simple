from django.shortcuts import render
from .models import Ss, Rubric
from django.views.generic.edit import CreateView
from .forms import SsForm
from django.urls import reverse_lazy


def index(request):
    sss = Ss.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'simplestart/index.html', {'sss': sss, 'rubrics': rubrics})


def by_rubric(request, rubric_id):
    sss = Ss.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'sss': sss,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'simplestart/by_rubric.html', context)


class SsCreateView(CreateView):
    template_name = 'simplestart/create.html'
    form_class = SsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context
