from django.shortcuts import render, redirect
from .models import Tweet
from .form import TweetForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

# Create your views here.
@login_required
def myfeed(request):
    now = timezone.localtime(timezone.now())  # Obtiene la fecha y hora actual con la zona horaria correcta
    yesterday = now - timedelta(days=1)
    if request.method == 'POST':
        form = TweetForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, ('¡Tweet Publicado!'))
        else:
            messages.error(request, "El tweet no puede superar los 300 caracteres.")
        return redirect('myfeed')
    else:
        all_tweets = Tweet.objects.all()
        paginator = Paginator(all_tweets, 8)
        page = request.GET.get('pg')
        all_tweets = paginator.get_page(page)
    return render(request, 'myfeed.html', {'all_tweets': all_tweets, 'now': now, 'yesterday': yesterday})

@login_required
def like_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = Tweet.objects.get(id=tweet_id)
        user = request.user

        if user in tweet.likes.all():
            tweet.likes.remove(user)  # Si ya dio like, lo quita
        else:
            tweet.likes.add(user)  # Si no, lo agrega
            tweet.dislikes.remove(user)  # Si tenía dislike, lo elimina

    return redirect('myfeed')

@login_required
def dislike_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = Tweet.objects.get(id=tweet_id)
        user = request.user

        if user in tweet.dislikes.all():
            tweet.dislikes.remove(user)  # Si ya dio dislike, lo quita
        else:
            tweet.dislikes.add(user)  # Si no, lo agrega
            tweet.likes.remove(user)  # Si tenía like, lo elimina

    return redirect('myfeed')

@login_required
def delete_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.delete()
        messages.warning(request, "El tweet ha sido eliminado.")

    return redirect('mytweets')

@login_required
def mytweets(request):
    now = timezone.localtime(timezone.now())  # Obtiene la fecha y hora actual con la zona horaria correcta
    yesterday = now - timedelta(days=1)
    my_tweets = Tweet.objects.filter(user=request.user)
    paginator = Paginator(my_tweets, 8)
    page = request.GET.get('pg')
    my_tweets = paginator.get_page(page)
    return render(request, 'mytweets.html', {'my_tweets': my_tweets, 'now': now, 'yesterday': yesterday,})

def index(request):
    return render(request, 'index.html')