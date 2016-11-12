from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from ..models import *
import random


# class ViewsTestCase(TestCase):
	# press_material   =   PressMaterial.objects.create(media_type = "test-material")
	# user = User.objects.create(username = random.choice([1,2,3,4,5,6,7,8,9,0,99,88,43,56,76,12,89]), first_name = "test", email = "test@email.com")
	# fixtures = ['publication_test_data.json'] # set a prepopulated database to use for the test
	# ''' contains test for all views declared in easypr_ng.views'''
	
	# def test_index(self) :
	# 	# new_post = Publication.objects.create(title_slug = "test-post", status = "published", posted_by = User.objects.create(username = "tester"))
	# 	resp = self.client.get('/')
	# 	self.assertEqual(resp.status_code, 200)
	# 	self.assertTrue('recent_posts' in resp.context)
	# 	self.assertEqual([post.pk for post in resp.context['recent_posts']], []) # check if return type is a list


	# def create_post(self):
	# 	user = self.user
	# 	press_material = self.press_material
	# 	new_post = Publication.objects.create(posted_by = user, transaction_id = 12345, post_title = "test post", post_body = "test post content", 
	# 	person_to_quote = "person",persons_position = "position",press_material = press_material)
	# 	return new_post


	# def test_create_post(self):
	# 	post = self.create_post()
 #        self.assertTrue(isinstance(post, Publication))
		


