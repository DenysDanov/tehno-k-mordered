from django.test import *
from colorama import *
from .custom import validate_phone_number, validate_request

init()

class ValidatorTest(SimpleTestCase):
    def test_phone_validation(self):
        print(Fore.CYAN + 'Phone validation')
        self.assertEqual(
            validate_phone_number('+1 (231) 231-23-33'),
            True,
            msg=Fore.GREEN + 'Test 1 failed!'
        )
        print(Fore.GREEN + 'Test 1 passed!')

        self.assertEqual(
            validate_phone_number('+1 (231)asfadf231-23-33'),
            False,
            msg=Fore.GREEN + 'Test 2 failed!'
        )
        print(Fore.GREEN + 'Test 2 passed!')
        
        self.assertEqual(
            validate_phone_number('+1 (231) a*/134231-23-33'),
            False,
            msg=Fore.GREEN + 'Test 3 failed!'
        )
        print(Fore.GREEN + 'Test 3 passed!')
    

    def test_req_validation(self):
        print(Fore.CYAN + 'Request validation')
        self.assertEqual(
            validate_request({'key': 'value'}, 'key'),
            True,
            msg=Fore.GREEN + 'Test 1 failed!'
        )
        print(Fore.GREEN + 'Test 1 passed!')

        self.assertEqual(
            validate_request({'key': 'value'}, 'value'),
            False,
            msg=Fore.GREEN + 'Test 2 failed!'
        )
        print(Fore.GREEN + 'Test 2 passed!')
        
        self.assertEqual(
            validate_request({'key': 'value'}, 'a'),
            False,
            msg=Fore.GREEN + 'Test 3 failed!'
        )
        print(Fore.GREEN + 'Test 3 passed!')
    
