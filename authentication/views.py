from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from authentication.forms import UserRegistrationForm
from newsapi import NewsApiClient
import json
from pprint import pprint

newsapi = NewsApiClient(api_key='bc2049afb59a407c856653a48655d44c')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    data = {'success': 'Sucessfully logged out'}
    return redirect('home')

def home(request):
    if request.user.is_authenticated:

        all_articles = newsapi.get_everything(q='bitcoin',
                                            sources='bbc-news,the-verge',
                                            domains='bbc.co.uk,techcrunch.com',
                                            language='en',
                                            sort_by='relevancy',
                                            page=1)
        # pprint(all_articles)
        return render(request, 'home.html', {'user': request.user, 'data': all_articles['articles'][:5]})
    else:
        return redirect('login')

