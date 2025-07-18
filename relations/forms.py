from django import forms


class Invite_Forms(forms.Form):
    email = forms.EmailField(label="E-mail do Convidado")
