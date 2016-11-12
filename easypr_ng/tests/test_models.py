from django.test import TestCase
from easypr_ng.models import * 
from django.utils import timezone



class Easypr_ngTest(TestCase):
	# fixtures = ['easypr_ng_test_data.json']
	
	def create_media_platform(self, name="test platform", name_slug = "test-slug", active = True):
		return MediaPlatform.objects.create(name = name, name_slug = name_slug, active = active)

	def test_create_media_platform(self):
		mp = self.create_media_platform()
		self.assertTrue(isinstance(mp, MediaPlatform))
		self.assertEqual(mp.__unicode__(), mp.name)
		self.assertEqual(mp.save(), True)


	def create_sector(self, name="test platform", name_slug = "test-slug", active = True):
		return Sector.objects.create(name = name, name_slug = name_slug, active = active)

	def test_create_sector(self):
		ms = self.create_sector()
		self.assertTrue(isinstance(ms, Sector))
		self.assertEqual(ms.__unicode__(), ms.name)
		self.assertEqual(ms.save(), None)


	def create_media_contact(self):
		return  MediaContact.objects.create(media_house = self.create_media_house(), first_name = "test contact", last_name ="test contact lastname", email = "testcontact@mail.com", phone_number = "080testnumber")

	def test_create_media_contact(self):
		mc = self.create_media_contact()
		self.assertTrue(isinstance(mc, MediaContact))
		return_str = mc.media_house.name + "," + mc.first_name + mc.last_name + "," + mc.email
		self.assertEqual(mc.__unicode__(), return_str)
		self.assertEqual(mc.save(), None)


	def create_media_house(self):
		mh =  MediaHouse.objects.create(name="test media house")
		mh.platform.add(self.create_media_platform())
		mh.save()
		return mh

	def test_create_media_house(self):
		mh = self.create_media_house()

		self.assertTrue(isinstance(mh, MediaHouse))
		self.assertEqual(mh.__unicode__(), mh.name)
		self.assertEqual(mh.save(), None)
		# self.assertEqual(mh.get_contacts(), [])


	
	def create_press_material(self, name_slug = "test-press-material",media_type="test-media",caption ="test media caption"):
		return PressMaterial.objects.create(name_slug = name_slug, media_type = media_type, caption = caption)


	def test_create_pressmaterial(self):
		tm = self.create_press_material()
		self.assertTrue(isinstance(tm, PressMaterial))
		self.assertEqual(tm.__unicode__(), tm.media_type)















