import unittest
import towers

class TestTowers(unittest.TestCase):

    def test_state_init(self):
        state = towers.State(6)
        self.assertEqual(state.left, [6, 5, 4, 3, 2, 1])

    def test_state_print(self):
        state = towers.State(6)
        # import pdb; pdb.set_trace()
        self.assertIsNotNone(state.__str__())


if __name__ == '__main__':
    unittest.main()
