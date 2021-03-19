from django import forms

class TexturesFilter(forms.Form):
    oder = forms.CharField(max_length = 50, required=False)
    sn = forms.CharField(max_length = 50, required=False)
    texture1 = forms.CharField(max_length = 50, required=False)
    texture2 = forms.CharField(max_length = 50, required=False)
    size = forms.CharField(max_length = 50, required=False)
    
    

    

