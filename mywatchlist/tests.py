from django.test import TestCase, Client

class TestUrls(TestCase):
    def test_html_test(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEquals(response.status_code, 200)

    def test_xml_test(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEquals(response.status_code, 200)

    def test_json_test(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEquals(response.status_code, 200)

# Create your tests here.
