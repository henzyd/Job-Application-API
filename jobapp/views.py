from django.shortcuts import render, redirect
from .forms import JobAdvertForm
from django.contrib import messages

# Create your views here.

def drop_down_view(request):
    if request.method == "POST":
        form = JobAdvertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job created")
            return redirect("test")
    else:
        form = JobAdvertForm()
    return render(request, 'index.html', {'form': form})