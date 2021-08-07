from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Articl, Comment


def index(request):
    latest_article_list = Articl.objects.order_by('-pub_date')[:5]
    return render(request, 'articls/list.html', {'latest_article_list': latest_article_list})

def detail(request, article_id):
    try:
        a = Articl.objects.get( id = article_id)
    
    except:
        raise Http404("Article not found")
        
    latest_commet_list = a.comment_set.order_by('-id')[:10]
    
    return render(request, 'articls/detail.html', {'article': a, 'latest_commet_list': latest_commet_list })
    
    
    
def leave_comment(request, article_id):
    try:
        a = Articl.objects.get( id = article_id)
    
    except:
        raise Http404("Article not found")
        
    a.comment_set.create(autor_name = request.POST['name'], comment_text = request.POST['text'])
    
    return HttpResponseRedirect( reverse('articls:detail', args = (a.id,)))
    
