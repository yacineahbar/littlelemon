from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="test@789!")
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(title="Pasta", price=12.99, inventory=10)
        self.menu2 = MenuItem.objects.create(title="Pizza", price=15.99, inventory=20)
        self.menu3 = MenuItem.objects.create(title="Salad", price=9.99, inventory=30)

    def test_getall(self):
        self.client.login(username="testuser", password="test@789!")
        response = self.client.get(reverse('menu-items')) 
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)