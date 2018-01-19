from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import login, authenticate
from book_listing.models import Book_List


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/booklisting/search')
    else:
        form = Register()
        return render(request, 'sign_in/register.html', {'form': form})


def profile(request):
    user = Book_List.objects.filter(uploaded_by=request.user)
    name = request.user
    return render(request, 'sign_in/profile.html', {'user': user, 'name': name})
