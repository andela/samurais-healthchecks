from hc.api.models import Check
from hc.test import BaseTestCase


class AddCheckTestCase(BaseTestCase):

    def test_it_works(self):
        url = "/checks/add/"
        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url)
        self.assertRedirects(r, "/checks/")
        assert Check.objects.count() == 1

    ### Test that team access works
    def test_team_access_works(self):
         #creating a check "Alice Was Here" as Alice
        self.check = Check(user=self.alice, name="Alice Was Here")
        self.check.save()
        #Check accessible by Bob since he is in Alice's team
        self.client.login(username="bob@example.org", password="password")
        r = self.client.get("/checks/")
        self.assertContains(r, "Alice Was Here", status_code=200)
