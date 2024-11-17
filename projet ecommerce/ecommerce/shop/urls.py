

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import connexion, produit_quantite,register, createproduits, deconnexion, deleteproduits, detail, index, table, updateproduits

urlpatterns = [
    
    path('', index, name='index'),
    path('create/', createproduits, name='create'),
    path('<int:myid>/', detail, name='detail'),
    path('table/update/<int:id>/', updateproduits, name='update'),
    path('table/', table, name='table'),
    path('table/delete/<int:id>/', deleteproduits, name='delete'),
    path('login/', connexion, name='login'),
    path('logout/', deconnexion, name='logout'),
    path('register/', register, name='register'),
    path('produit_quantit/', produit_quantite, name='produit_quantite'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

