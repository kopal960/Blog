from .models import Post
import django_filters

class PostFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr="kop")
    class Meta:
        model = Post
        fields = ['title','author'] 
