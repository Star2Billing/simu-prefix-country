from django import forms
from django.forms import ModelForm
from django.contrib import *
from django.contrib.admin.widgets import *
from django.utils.translation import ugettext_lazy as _
from prefix_country.models import *
from datetime import *
# place form definition here


def country_list():
    """
    Return Country List
    """
    list = Country.objects.all()
    return ((l.countrycode, l.countryname) for l in list)