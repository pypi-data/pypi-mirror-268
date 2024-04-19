from django.template import Library, loader
from ..models import Post
from _data.zenblogds import context, CATEGORY
from ..forms import SearchForm
from taggit.models import Tag

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.ERROR)

register = Library()

# https://localcoder.org/django-inclusion-tag-with-configurable-template


@register.filter
def category_display(post_obj):
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.get_FOO_display
    return post_obj.get_category_display()


@register.simple_tag(takes_context=True)
def header(context):
    t = loader.get_template("zenblogds/header.html")
    context.update({
        'form': SearchForm(),
        'category': CATEGORY,
        'latest_one': Post.objects.filter(status=1).latest('updated_on'),
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def footer(context):
    t = loader.get_template("zenblogds/footer.html")

    # about 모듈 사용여부에 따라 footer의 배치를 다르게 하기 위해
    is_about_used = False
    for module, is_used, _, _ in context['components']:
        if module == 'about' and is_used:
            is_about_used = True
            break

    context.update({
        'is_about_used': is_about_used,
        'category': CATEGORY,
        'recents4': Post.objects.filter(status=1).order_by('-updated_on')[:4],
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def hero(context):
    t = loader.get_template(f"zenblogds/_hero.html")
    context.update({
        'remarkables': Post.objects.filter(status=1).filter(remarkable=True).order_by('-updated_on')
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def post_grid(context):
    t = loader.get_template(f"zenblogds/_post-grid.html")
    context.update({
        'latest_one': Post.objects.filter(status=1).latest('updated_on'),
        'the_others': Post.objects.filter(status=1).order_by('-updated_on')[1:7],
        'trending': Post.objects.filter(status=1).order_by('hit_count_generic')[:5],
    })
    logger.info(context)
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def sidebar(context):
    t = loader.get_template(f"zenblogds/_sidebar.html")
    tags = Tag.objects.all()
    context.update({
        'category': CATEGORY,
        'all_tags': tags,
        'latest': Post.objects.filter(status=1).order_by('-updated_on')[:6],
        'trending': Post.objects.filter(status=1).order_by('hit_count_generic')[:6],
    })
    logger.info(context)
    return t.render(context.flatten())


@register.inclusion_tag('zenblogds/_grid-pattern1.html')
def grid_pattern1(category_int):
    objects = Post.objects.filter(status=1).filter(category=category_int).order_by('-updated_on')
    return {
        'top4': objects[:4],
        'the_others': objects[4:10]
    }


@register.inclusion_tag('zenblogds/_grid-pattern2.html')
def grid_pattern2(category_int):
    objects = Post.objects.filter(status=1).filter(category=category_int).order_by('-updated_on')
    return {
        'top4': objects[:4],
        'the_others': objects[4:10]
    }


@register.inclusion_tag('zenblogds/_grid-pattern3.html')
def grid_pattern3(category_int):
    objects = Post.objects.filter(status=1).filter(category=category_int).order_by('-updated_on')
    return {
        'top3': objects[:3],
        'the_others1': objects[3:6],
        'the_others2': objects[6:9],
        'the_others3': objects[9:15],
    }


