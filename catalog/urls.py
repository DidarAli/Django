from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
	path('predmets/', views.PredmetListView.as_view(), name='predmets'),
    path('predmet/<int:pk>', views.PredmetDetailView.as_view(), name='predmet-detail'),
	path('kafedras/', views.KafedraListView.as_view(), name='kafedras'),
	path('kafedra/<int:pk>', views.KafedraDetailView.as_view(), name='kafedra-detail'),
]