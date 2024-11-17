
from django.shortcuts import get_object_or_404, redirect, render

from shop.form import CreateProduct, UserForm
from .models import Category, Product
from django.core.paginator import Paginator

# pour authentification
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# pour les messages
from django.contrib import messages


# Create your views here.

def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')  # Redirection vers la page de connexion

    produits = Product.objects.all()
    
    # pour rechercher un produit
    items_name = request.GET.get('item-name', '').strip()  # Nettoyage de la chaîne de recherche
    if items_name:  # Vérifie si la chaîne n'est pas vide après nettoyage
        produits = produits.filter(nom__icontains=items_name)
        if not produits.exists():  # Vérifie s'il y a des résultats
            return render(request, 'shop/index.html', {'message': 'Désolé, ce produit n\'existe pas'})

    # pour la pagination
    paginator = Paginator(produits, 8)
    page = request.GET.get('page')
    produits = paginator.get_page(page)

    context = {"produits": produits}
    return render(request, "shop/index.html", context)


def detail(request, myid):
    produits = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'produits':produits})
@login_required
def table(request):
    produits = Product.objects.all()
    return render(request, 'shop/table.html', {'produits':produits})

def createproduits(request):
    form = CreateProduct()
    categories = Category.objects.all()  # Récupérer toutes les catégories
    

    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CreateProduct()
            messages.success(request,'le produits a bien ete ajouté avec succes')
        else :
            messages.error(request,'le produits n\'a pas pu etre ajouté')

    return render(request, 'shop/createproduits.html', {
        "form": form,
        
        "categories": categories  # Passer les catégories au template
    })

def updateproduits(request, id):
    produits = get_object_or_404(Product, id=id)
    message=""
    form = CreateProduct(instance=produits)
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES, instance=produits)
        if form.is_valid():
            form.save()
            # vider le formulaire
            form = CreateProduct()
            message="le produits a bien ete modifié"
    return render(request, 'shop/updateproduit.html', {'form':form,'message':message})

def deleteproduits(request, id):
    message=""
    produits = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        produits.delete()
        message="le produits a bien ete supprimé"
        return redirect('table')
    
    return render(request, 'shop/delete.html', {'produits':produits,'message':message})


def register(request):
    form=UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'votre compte a bien été crée')
            return redirect('login')
        else:
            messages.error(request, 'votre compte n\'a pas été crée')

    return render(request, 'shop/register.html', {'form':form})


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion reussie')
            return redirect('table')
        else:
            messages.error(request, 'Votre identifiant ou mot de passe est incorrect')
    return render(request, 'shop/login.html')
@login_required
def deconnexion(request):
    logout(request)
    return redirect('login')

def produit_quantite(request):
    produits = Product.objects.all()
    for produit in produits:
        if produit.quantite_en_stock < 5:
            messages.warning(request, f"Le stock du produit {produit.nom} est faible ({produit.quantite_en_stock} restants).")
    return render(request, 'shop/produit_list.html', {'produits': produits})



    
            
            
            


