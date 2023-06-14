from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, CharFilter, ModelMultipleChoiceFilter
from .models import Post, PostCategory, Category


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    post_category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        conjoined=True,
    )


    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'postTitle': ['icontains'],
            #'postCategory': ['in'],
        }
