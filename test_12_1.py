from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj1 = Runner('Толик')
        for _ in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    def test_run(self):
        obj2 = Runner('Санёк')
        for _ in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    def test_challenge(self):
        obj3 = Runner('Олег')
        obj4 = Runner('Игорь')
        for _ in range(10):
            obj3.walk()
            obj4.run()
        self.assertNotEqual(obj3.distance, obj4.distance)


if __name__ == '__main__':
    unittest.main()
