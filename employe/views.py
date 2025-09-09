from django.shortcuts import get_object_or_404, redirect, render
from .models import Employe
from .forms import EmployeForm

def list_employes(request):
    employes = Employe.objects.all()
    return render(request, 'employe/list.html', {'employes': employes})

def ajouter_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_employes')
    return render(request, 'employe/formulaire.html', {'form': form})

def modifier_employe(request, id):
    employe=get_object_or_404(Employe, id=id)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('list_employes')
    return render(request, 'employe/formulaire.html', {'form': form})

def supprimer_employe(request, id):
    employe=get_object_or_404(Employe, id=id)
    if request.method == 'POST':
        employe.delete()
        return redirect('list_employes')
    return render(request, 'employe/confirmer_suppression.html', {'employe': employe})