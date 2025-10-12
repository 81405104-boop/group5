from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=50)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="訊息", widget=forms.Textarea, min_length=10)
