from django.db import models
from .utils import create_shortcode


class ShortUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        main_qc = super(ShortUrlManager, self).all(*args, **kwargs)
        qc = main_qc.filter(active=True)
        return qc

    def refresh_shortcode(self):
        qc = ShortUrl.objects.filter(id__gte=1)
        count = 0
        for q in qc:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            count += 1
        return str(count)


class ShortUrl(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ShortUrlManager()
    # new = ShortUrlManager()

    def save(self, *args, **kwargs):  # override the save method with shortcode generator
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
