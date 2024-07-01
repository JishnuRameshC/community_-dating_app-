from django import forms
from .models import User, EmployeeEmployer, JobSeeker, Address
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.utils import timezone
from django.forms import (
    ModelForm,
    TextInput,
    PasswordInput,
    CharField,
    CheckboxInput,
    DateField,
    DateInput,
    Select,
    Form
)


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


class UserForm(UserCreationForm):
    first_name = CharField(
        label=("First Name"),
        max_length=30,
        required=False,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    last_name = CharField(
        label=("Last Name"),
        max_length=30,
        required=False,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    password1 = CharField(
        label=("Password"),
        strip=False,
        widget=PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )
    password2 = CharField(
        label=("Confirm Password"),
        strip=False,
        widget=PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}
        ),
    )

    username = CharField(
        label="username", widget=TextInput(attrs={"class": "form-control"})
    )
    email = CharField(
        min_length=5,
        max_length=50,
        label="Email",
        required=True,
        validators=[EmailValidator()],
        widget=TextInput(attrs={"class": "form-control"}),
    )
    dob = DateField(
        label="Date of Birth",
        required=False,
        widget=DateInput({"class": "form-control"}),
        initial=timezone.now,
    )
    gender = CharField(
        label="Gender",
        required=False,
        widget=Select(
            choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
            attrs={"class": "form-select"},
        ),
    )
    phone = CharField(
        label="Phone",
        required=False,
        widget=TextInput(attrs={"class": "form-control"}),
    )
    smoke = CharField(
        label="Smoke",
        required=False,
        widget=Select(
            choices=[("N", "No"), ("Y", "Yes"), ("P", "Plan to Quit")],
            attrs={"class": "form-select"},
        ),
    )
    drinking = CharField(
        label="Drinking",
        required=False,
        widget=Select(
            choices=[("T", "Yes"), ("F", "No"), ("P", "Plan to Quit")],
            attrs={"class": "form-select"},
        ),
    )
    rel_status = CharField(
        label="Relationship Status",
        required=False,
        widget=Select(
            choices=[
                ("S", "Single"),
                ("M", "Married"),
                ("W", "Widow"),
                ("D", "Divorced"),
            ],
            attrs={"class": "form-select"},
        ),
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "dob",
            "gender",
            "phone",
            "smoke",
            "drinking",
            "rel_status",
        ]


class EmployeeEmployerForm(ModelForm):
    class Meta:
        model = EmployeeEmployer
        fields = "__all__"


class JobSeekerForm(ModelForm):
    class Meta:
        model = JobSeeker
        fields = "__all__"


class AddressUpsertForm(ModelForm):
    class Meta:
        model = Address
        exclude = ["user"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "address_line_1": TextInput(attrs={"class": "form-control"}),
            "address_line_2": TextInput(attrs={"class": "form-control"}),
            "address_line_3": TextInput(attrs={"class": "form-control"}),
            "city": TextInput(attrs={"class": "form-control"}),
            "state": TextInput(attrs={"class": "form-control"}),
            "country": TextInput(attrs={"class": "form-control"}),
            "pincode": TextInput(attrs={"class": "form-control"}),
            "is_default": CheckboxInput(attrs={"class": "form-check-input"}),
        }
