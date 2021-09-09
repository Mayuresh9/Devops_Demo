from Length_conv import conversion, check_valid_input
from Length_conv import app
import unittest



class FlaskTest(unittest.TestCase):

    #check if the response is correct
    def test_1_index(self):
        print("Verifying the statuscode is correct")
        tester=app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
        print("status code is",statuscode)
        print("statuscode verified successfully")
        

    def test_2_index_content(self):
        print("verifying the content type of the UI")
        tester=app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type,"text/html; charset=utf-8")
        print("The content type of UI is", response.content_type)
        print("Content type verified successfully")

    def test_3_check_output(self):
        print("Verifying Output for various Inputs")
        self.assertEqual(conversion("meters","meters", 50),50)
        self.assertEqual(round(conversion("kilometers","miles", 50),4),31.0686)
        self.assertEqual(round(conversion("miles","feet", 50),4),264000)
        self.assertEqual(round(conversion("feet","meters", 50),4),15.2400)
        print("Output verification Successful")

    def test_4_check_output(self):
        print("Verifying output for invalid inputs")
        self.assertEqual(check_valid_input(-300),True)
        self.assertEqual(check_valid_input(200),False)
        self.assertEqual(check_valid_input(-24.254),True)
        self.assertEqual(check_valid_input(12423),False)
        print("Output verified successfully")

if __name__=="__main__":
    unittest.main()        
