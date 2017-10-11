from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models
from django.views.generic.base import TemplateView
# Create your views here.

#Function Views
@login_required
def index(request):
    print(dir(request))
    #metodo feo
    # if not request.user.is_authenticated():
        # return redirect('login')
    if request.method == 'GET':    
        greet = "hi"
        person = get_object_or_404(models.Person, pk=675)
        name = person.name
        lista = [1,2,3,4,5]
        diccio = {"elemento":"ninguno", "elemento2":"uno solo"}
        return render(request, 'index.html', 
                    {'object':greet, 
                    'name': name, 
                    'collection':lista, 
                    "diccionario":diccio}
                    )
    else:
        raise Http404("Uoops esto es embarazoso")

#baseview
from django.views import View

class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {
                        "greet":"hola base view"
                        })

    
    def post(self, request):
        return render(request, 'index.html', {
                        "greet":"recibi el post"
                        })

    def update(self, request):
        return render(request, 'index.html', {
                        "greet":"update"
                        })

#Templateview
from django.views.generic.base import TemplateView

class HomeTemplateView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context["greet"] = "hello desde template view"
        return context

#generic views
#detail view
from django.views.generic.detail import DetailView

class PersonDetailView(DetailView):
    model = models.Person
    template_name = 'detail.html'

#listview

from django.views.generic.list import ListView
class PersonList(ListView):
    model = models.Person
    template_name= 'list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(PersonList, self).get_context_data(**kwargs)
    #     context["object_list"] = models.Person.objects.older()
    #     return context

#createview
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class PersonCreate(CreateView):
    model = models.Person
    fields = '__all__'  #['name', 'email']
    template_name = 'create.html'
    success_url = reverse_lazy('list')


#updateview
from django.views.generic.edit import UpdateView

class PersonUpdate(UpdateView):
    model = models.Person
    fields =  ['name', 'email']
    template_name = 'create.html'
    success_url = reverse_lazy('list')

#deleteview
from django.views.generic.edit import DeleteView

class PersonDelete(DeleteView):
    model = models.Person
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('list')