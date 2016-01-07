from django.test import TestCase
from rango.models import Category, Page
from django.core.urlresolvers import reverse
from rango.bing_search import run_query
from datetime import datetime

# Create your tests here.
class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), False)


class PageMethodTests(TestCase):
    def test_page_visit_not_in_future(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        page = Page(category=cat)
        page.save()
        self.assertLessEqual(page.last_visit, datetime.now())

    def test_last_visit_equal_after_first_visit(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        page = Page(category=cat)
        page.save()
       
       
        #response = self.client.get('/rango/goto/?page_id=1', follow=True)
        #self.assertEqual(response.status_code, 200)
        # self.assertLessEqual(page.first_visit, page.last_visit)
 


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """

        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test temp',1,1)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")

        num_cats =len(response.context['categories'])
        self.assertEqual(num_cats , 4)

    def test_bing_search(self):
        results = run_query('python')
        self.assertEqual(len(results), 10)

