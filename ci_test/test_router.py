import unittest

from ci_test.util.test_util import get_content

base_url = "http://127.0.0.1:8002"


class TestRouter(unittest.TestCase):
    def test_router(self):
        x, y = 9, 4
        url = base_url + '?x=' + str(x) + '&y=' + str(y)
        self.assertEqual(get_content(url), "{\"error\": false, \"string\": \"9^4=6561\", \"answer\": 6561}")


if __name__ == '__main__':
    unittest.main()
