from django.contrib.auth.forms import UserCreationForm
from .models import AdminUser
from django import forms


# Create your forms here.

class NewUserForm(UserCreationForm):
	username = forms.CharField(max_length=255, required=True)

	class Meta:
		model = AdminUser
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		if commit:
			user.save()
		return user


class UploadDataForm(forms.Form):
	name = forms.CharField(max_length=255)
	table = forms.FileField()
	
