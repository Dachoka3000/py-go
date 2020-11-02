import django_filters
from .models import Business

class BusinessFilter(django_filters.FilterSet):
    class Meta:
        model=Business
        fields = {'name':['icontains'],'description':['icontains'],'area__name':['icontains']}

