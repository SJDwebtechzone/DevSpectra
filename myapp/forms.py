from django import forms
import re

class ProjectRequestForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={'required': "Name is required"}
    )

    email = forms.EmailField(
        required=True,
        error_messages={
            'required': "Email is required",
            'invalid': "Enter a valid email"
        }
    )

    number = forms.CharField(
        required=True,
        max_length=10,
        error_messages={
            'required': "Phone number is required",
        }
    )

    budget = forms.CharField(
        required=True,
        error_messages={'required': "Please select a budget"}
    )

    brief = forms.CharField(
        required=True,
        min_length=20,
        error_messages={
            'required': "Project brief is required",
            'min_length': "Brief must be at least 20 characters"
        }
    )

    # --------------------------
    # VALIDATION SECTION
    # --------------------------

    # ✅ Validate name (letters + spaces only)
    def clean_name(self):
        name = self.cleaned_data["name"]

        if not re.match(r'^[A-Za-z ]+$', name):
            raise forms.ValidationError("Name can contain only letters and spaces.")

        return name

    # (Email validation is automatically handled by EmailField)

    # ✅ Validate phone number
    def clean_number(self):
        number = self.cleaned_data["number"]

        # Must be digits only
        if not number.isdigit():
            raise forms.ValidationError("Phone number must contain digits only.")

        # Must be exactly 10 digits
        if len(number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")

        return number

from django import forms
from .models import CareerApplication

class CareerForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = ['resume']
class CareerForm(forms.Form):
    resume = forms.FileField()

    def clean_resume(self):
        file = self.cleaned_data.get('resume')
        if file and not file.name.endswith('.pdf'):
            raise forms.ValidationError("Only PDF files are allowed.")
        return file