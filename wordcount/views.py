from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def homepage(request):
    return render(request,"home.html")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    dictionary = {}
    for word in wordlist:
        if word in dictionary:
            dictionary[word] +=1
        else:
            dictionary[word] = 1

    newlist = sorted(dictionary.items(),key=itemgetter(1), reverse=True)
    return render(request,"count.html",{'text':fulltext,'wordlist' : len(wordlist),"dictwords":newlist})

def about(request):
    return render(request,"about.html")
