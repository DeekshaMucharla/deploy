from django.shortcuts import render

from django.http import HttpResponse
# 'request' name is convention. It can be some other name too.
def index(request) :    
  return render(request, 'index.html')