from falcon import testing
import sample

class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = sample.api

class TestSample(MyTestCase):
    def test_get_message(self):
        result = self.simulate_get('/faithful')
        doc = "try({duration.freq})\nduration.cut\n[1.5,2) [2,2.5) [2.5,3) [3,3.5) [3.5,4) [4,4.5) [4.5,5) [5,5.5) \n     51      41       5       7      30      73      61       4 \n"
        self.assertEqual(result.text, doc)
