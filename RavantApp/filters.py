import django_filters
#import django_filters
from .models import *

class machineFilter(django_filters.FilterSet):
    class Meta:
        model =MachinevisionCamera
        fields ='__all__'
        