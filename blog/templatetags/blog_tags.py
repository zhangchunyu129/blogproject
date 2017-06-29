from django import template
from django.db.models.aggregates import Count

from ..models import Post
from ..models import Category

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # category_list = 
    return Category.objects.annotate(num_posts=Count('post'))
