from Length_conv import app
import unittest

class FlaskTest(unittest.TestCase):

    #check if the response is correct
    def test_index(self):
        tester=app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content(self):
        tester=app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type,"text/html; charset=utf-8")

if __name__=="__main__":
    unittest.main()        
