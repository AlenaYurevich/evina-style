from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Ваше имя"}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
        'class': "form-control", 'placeholder': "Ваш email"}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Ваш телефон"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control",
                                                           'placeholder': "Услуга, желаемая дата и время"}),
                              max_length=1000)
