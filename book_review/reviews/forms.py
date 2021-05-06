from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Ticket, Review, UserFollows


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = None
            self.fields[field_name].label = ""
        self.fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de pass'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer mot de passe'

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class MyAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = None
            self.fields[field_name].label = ""

        self.base_fields['username'].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
        self.base_fields['password'].widget.attrs['placeholder'] = 'Mot de pass'


class TicketModelForm(forms.ModelForm):
    title = forms.CharField(
        label='Titre',
        required=False,
    )

    description = forms.CharField(
        label="Description",
        required=False,
        widget=forms.Textarea(
            attrs={
                # "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 5,
                'cols': 50
            }
        )
    )

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]


class ReviewModelForm(forms.ModelForm):
    RATING_RANGE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    rating = forms.ChoiceField(
        label='Note',
        required=False,
        choices=RATING_RANGE,
        widget=forms.RadioSelect
    )

    headline = forms.CharField(
        label='Titre',
        required=False,
    )

    body = forms.CharField(
        label="Commentaire",
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 5,
                'cols': 50,
            }
        )
    )

    class Meta():
        model = Review
        fields = ["headline", "rating", "body"]


class UserFollowsModelForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]

    def __init__(self, *args, **kwargs):
        super(UserFollowsModelForm, self).__init__(*args, **kwargs)
        self.base_fields["followed_user"].widget.attrs['placeholder'] = 'Nom d\'utilisateur'
