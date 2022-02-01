from django.test import TestCase
from django.urls import reverse

from .models import Favorite

class FavoriteModelTests(TestCase):
    
    def test_should_correctly_run_fake_test(self):
        a = 1
        b = 2
        poorlyDesigned = Favorite(ticker="abc", name="abc")
        message = "Fake function failed"
        self.assertEqual(3, poorlyDesigned.fake_function(a,b), message)

# class FavoriteIndexViewTests(TestCase):
#     def test_should_not_contain_ETH_in_query_set(self):
#         response = self.client.get(reverse('cryptos:index'))
#           response.status_code
#           response.contents
#              response.context 
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No polls are available.")
#         self.assertQuerysetEqual(response.context['cryptos'], [])
