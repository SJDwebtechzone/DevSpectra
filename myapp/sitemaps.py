from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        # only include URLs that actually exist in urls.py
        return ['index']

    def location(self, item):
        return reverse(item)
