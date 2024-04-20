import unittest
import requestrepo
import requests
import socket

class TestRequest(unittest.TestCase):
    def test_add_dns(self):
      r = requestrepo.RequestRepo()

      r.add_dns("testcanary1", "A", "1.1.1.1")
      r.add_dns("testcanary2", "A", "1.1.1.1")

      ip = socket.gethostbyname(f"testcanary1.{r.domain}")

      self.assertEqual(ip, "1.1.1.1")

      r.remove_dns("testcanary2", "A")

      ip = socket.gethostbyname(f"testcanary2.{r.domain}")

      self.assertNotEqual(ip, "1.1.1.1")

if __name__ == '__main__':
  unittest.main()
