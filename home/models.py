from django.db import models

CONTENT_TYPES = (
    ('Novinky'),
    ('Staticky_clanek'),
)

class Section(models.Model):
    name = models.CharField(max_length = 100, primary_key = True)

    def __str__(self):
        return self.name

class SubSection(models.Model):
    name = models.CharField(max_length = 100, primary_key = True)
    section = models.ForeignKey(Section)

    def __str__(self):
        return self.name

