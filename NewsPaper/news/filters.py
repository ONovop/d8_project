import django_filters
from django_filters import FilterSet
from .models import Post
from django import forms

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category__name = django_filters.CharFilter(lookup_expr='icontains')
    time_creating = django_filters.DateFilter(lookup_expr='gt')
    time_creating.field.widget = forms.DateInput(attrs={'type': 'date'})
    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = [
           # поиск по названию
           'title',
           # количество товаров должно быть больше или равно
           'category__name',
           'time_creating',
       ]
