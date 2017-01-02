# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

from home.models import Article, Section

# class TestHomePage(TestCase):
    # def test_uses_index_template(self):
    #     response = self.client.get(reverse("home"))
    #     self.assertTemplateUsed(response, "index.html")

    # def test_uses_base_template(self):
    #     response = self.client.get(reverse("home"))
    #     self.assertTemplateUsed(response, "base.html")

class TestSaving(TestCase):
    def setUp(self):
        self.index = Section(name='index',
                             url='index')
        self.index.save()
    
    def test_url_doesnt_change_after_resave(self):
        ''' chyba ze po uprave clanku a ulozeni se vygeneruje
        nove unikatni url, i kdyz to stare je taky unikatni'''
        art = Article(name='test',
                      text='ahoj joko',
                      url = 'test')
        art.save()
        self.assertEqual(art.url, 'test')
        art.save()
        self.assertEqual(art.url, 'test')

    def test_url_uniqueness(self):
        art = Article(name='test',
                      text='ahoj joko',
                      url = 'test')
        art.save()
        sec = Section(name='test',
                      url='test',
                      parent_section=self.index)
        sec.save()
        self.assertNotEqual(art.url, sec.url)
        
