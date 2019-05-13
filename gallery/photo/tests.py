from django.test import TestCase
from .models import Image,Location,Category


class LocationTestClass(TestCase):

  def setUp(self):
    self.rehema = Location(name='Africa')

    def test_instance(self):
        self.assertTrue(isinstance(self.rehema,Location)) 