from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


@login_required
def home(request):
    pets = Pet.objects.all()
    return render(request, 'market/home.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'market/pet_detail.html', {'pet': pet})

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'market/pet_list.html', {'pets': pets})


@login_required
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('home')
    else:
        form = PetForm()
    return render(request, 'market/pet_form.html', {'form': form, 'title': 'Add Pet'})

@login_required
def edit_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetForm(instance=pet)
    return render(request, 'market/pet_form.html', {'form': form, 'title': 'Edit Pet'})

@login_required
def delete_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == 'POST':
        pet.delete()
        return redirect('home')
    return render(request, 'market/pet_confirm_delete.html', {'pet': pet})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately
            return redirect('pet_list')  # or wherever you want to redirect
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})