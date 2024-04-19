from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all().filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return [
            'zenblogds:home',
        ]

    def location(self, item):
        return reverse(item)
