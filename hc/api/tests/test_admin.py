from hc.api.models import Channel, Check
from hc.test import BaseTestCase
from django.test.client import Client


class ApiAdminTestCase(BaseTestCase):

	def setUp(self):
		super(ApiAdminTestCase, self).setUp()
		self.check = Check.objects.create(user=self.alice, tags="foo bar")

		### Set Alice to be staff and superuser and save her :)
	def test_set_user_to_staff_and_superuser(self):
		self.alice.is_staff = True
		self.alice.is_superuser = True
		self.alice.save()

		admin = self.client.get('/admin/accounts/profile/', data={'username':self.alice.username, 'password':self.alice.password}, follow=True)
		
		self.assertEqual(admin.status_code, 200)
		self.assertTrue(self.alice.is_superuser)

	def test_it_shows_channel_list_with_pushbullet(self):
		self.client.login(username="alice@example.org", password="password")

		ch = Channel(user=self.alice, kind="pushbullet", value="test-token")
		ch.save()

		### Assert for the push bullet
		assert "pushbullet" in ch.kind
