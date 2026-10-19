import pytz
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Field, Layout, Submit
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class InitalAdminAccountForm(UserCreationForm):
    name = forms.CharField(label=_("Name"), max_length=500)
    timezone = forms.ChoiceField(
        label=_("Timezone"), choices=[(x, x) for x in pytz.common_timezones]
    )
    language = forms.ChoiceField(
        label=_("Language"),
        choices=settings.LANGUAGES,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].initial = settings.ORGANIZATION_NAME
        self.fields["name"].widget = forms.HiddenInput()
        self.fields["timezone"].initial = "Asia/Seoul"
        self.fields["timezone"].widget = forms.HiddenInput()
        self.fields["language"].initial = settings.ORGANIZATION_LANGUAGE
        self.fields["language"].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("name"),
            Field("timezone"),
            Field("language"),
            HTML(f"<h2>{_('Account')}</h2>"),
            Div(
                Div(Field("first_name"), css_class="col-6"),
                Div(Field("last_name"), css_class="col-6"),
                css_class="row",
            ),
            Div(
                Div(Field("email"), css_class="col-12"),
                Div(Field("password1"), css_class="col-12"),
                Div(Field("password2"), css_class="col-12"),
                css_class="row",
            ),
            Submit(name="submit", value=_("Submit")),
        )

    def clean_name(self):
        return settings.ORGANIZATION_NAME

    def clean_timezone(self):
        return "Asia/Seoul"

    def clean_language(self):
        return settings.ORGANIZATION_LANGUAGE

    class Meta:
        model = get_user_model()
        fields = (
            "name",
            "timezone",
            "language",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class FileForm(forms.Form):
    file = forms.FileField()
