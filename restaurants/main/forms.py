from django.contrib.auth.forms import UserCreationForm
from .models import AdminUser
from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


def validate_excel(value):
	if value.name.split('.')[-1] not in ['xls', 'xlsx']:
		raise ValidationError(_('Invalid File Type: %(value)s'), params={'value': value},)


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
	table = forms.FileField(validators=[validate_excel])
	
