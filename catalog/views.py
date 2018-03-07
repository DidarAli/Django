from django.shortcuts import render

# Create your views here.
from .models import Kafedra, Predmet

def index(request):
    num_predmets=Predmet.objects.all().count()
    num_kafedras=Kafedra.objects.count()
    
   
    return render(
        request,
        'index.html',
        context={'num_predmets':num_predmets,'num_kafedras':num_kafedras},
    )
	
from django.views import generic

class PredmetListView(generic.ListView):
    model = Predmet
    paginate_by = 2
class PredmetDetailView(generic.DetailView):
    model = Predmet

class KafedraListView(generic.ListView):
    model = Kafedra
    paginate_by = 2
class KafedraDetailView(generic.DetailView):
    model = Kafedra
