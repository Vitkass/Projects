from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import TexturesFilter
from .models import Texture



def index(request):
    latest_textures = Texture.objects.all()
    form = TexturesFilter(request.GET)
    textures = Texture.objects.all()
    ident = True
    

    
    if form.is_valid():
        
        if form.cleaned_data['oder']:
            try:
                textures = textures.filter(oder_number=form.cleaned_data["oder"])
            except:
                Http404("Not found")
    
            
        if form.cleaned_data['sn']:
            try:
                textures = textures.filter(sn_number=form.cleaned_data["sn"])
            except:
                Http404("Not found")
           
                
        if form.cleaned_data['texture1']:
            try:
                textures = textures.filter(texture1=form.cleaned_data["texture1"])
            except:
                Http404("Not found")
            
            
        if form.cleaned_data['texture2']:
            try:
                textures = textures.filter(texture2=form.cleaned_data["texture2"])
            except:
                Http404("Not found")
            
            
        if form.cleaned_data['size']:
            try:
                textures = textures.filter(size=form.cleaned_data["size"])
            except:
                Http404("Not found")
        
        if ((form.cleaned_data['oder']=='')&(form.cleaned_data['sn']=='')&(form.cleaned_data['texture1']=='')&(form.cleaned_data['texture2']=='')&(form.cleaned_data['size']=='')):
            
            textures = None
            
        else:
            
            ident = False
        
        

      
    
    
    return render(request, 'textures/list.html', {'latest_textures' : latest_textures, 'form' : form, 'textures' : textures, 'ident' : ident})
    
        




def detail(request, texture_id):
    try:
        a = Texture.objects.get(id = texture_id)
    except:
        raise Http404("Not found")
        
    return render(request, 'textures/detail.html', {'texture': a})
    

    

