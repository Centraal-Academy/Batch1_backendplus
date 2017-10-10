from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from . import models
# Create your views here.

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
