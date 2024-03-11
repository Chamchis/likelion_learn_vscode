from unittest.mock import MagicMock
from calculator import *
import unittest

class TestWithMock(unittest.TestCase):
    def test_external_service(self):
        service = ChatGPTAPI()
        service.service_method = MagicMock(return_value=True)
        self.assertTrue(service.service_method())

# 이메일 서비스
class TestEmailService(unittest.TestCase):
    def test_send_email(self):
        email_send_service = EmailService()
        email_send_service.send_email = MagicMock(return_value=True)
        self.assertTrue(email_send_service.send_email('user@nasa.com','Hello'))

# API 요청 테스트
class TestAPIClient(unittest.TestCase):
    def test_fetch_data(self):
        client = APIClient()
        client.fetch_data = MagicMock(return_value = {'key':'value'})
        self.assertEqual(client.fetch_data('http://'), {'key':'value'})

# database 연결
class TestDatabaseClient(unittest.TestCase):
    def test_database_connection(self):
        db_client = DatabaseClient()
        db_client.connect = MagicMock(return_value=True)
        self.assertTrue(db_client.connect())

class TestFileOperations(unittest.TestCase):
    # test.txt 파일을 열어서 읽고 그 내용을 확인한다
    # 파일 열기
    def setUp(self):
        self.file = open('test.txt','w')
    # 닫기
    def tearDown(self) -> None:
        self.file.close()
    # test
    def test_write_to_file(self):
        self.file.write('Hello world')
        self.file.close()
        with open('test.txt','r') as f:
            self.assertEqual(f.read(),'Hello world')

# 임시 데이터베이스 테스트
class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.db = TemporaryDatabase()
        self.db.connect()
    def tearDown(self) -> None:
        self.db.disconnect()
    def test_database_insert(self):
        self.db.insert('data')
        self.assertTrue(self.db.contains('data'))

# 숙제
class TestNetworkConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = NetworkConnection()
        self.connection.open()
    def tearDown(self) -> None:
        self.connection.close()
    def test_send_data(self):
        self.assertTrue(self.connection.send('data)'))

# python 버전에 따른 테스트
import sys
@unittest.skipIf(sys.version_info > (3,9), 'Test required Python 3.9')
class TestPython3_10Feature(unittest.TestCase):
    def test_new_feature(self):
        pass

@unittest.skipUnless(sys.platform.startswith('linux'),'Linux')
class TestLinuxSpecific(unittest.TestCase):
    def test_linux_behavior(self):
        pass

import os
@unittest.skipIf(os.environ.get("NO_NETWORK_TESTS"),"")
class TestNetworkFeature(unittest.TestCase):
    def test_network_call(self):
        pass


if __name__ == '__main__':
    unittest.main()