from django import forms


class ClientId(forms.Form):
    client_id = forms.IntegerField(initial=1)
