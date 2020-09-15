from django import forms


class Contact(forms.Form):
    Name=forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'placeholder':' Name'}))
    Email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':' Email'}))
    Message=forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder': ' Message'}))