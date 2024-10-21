from runner import Runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj1 = Runner('Толик')
        for _ in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj2 = Runner('Санёк')
        for _ in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj3 = Runner('Олег')
        obj4 = Runner('Игорь')
        for _ in range(10):
            obj3.walk()
            obj4.run()
        self.assertNotEqual(obj3.distance, obj4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', speed=10)
        self.runner2 = runner_and_tournament.Runner('Андрей', speed=9)
        self.runner3 = runner_and_tournament.Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        print({place: runner.name for place, runner in cls.all_results.items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_and_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_multiple_participants(self):
        runner4 = runner_and_tournament.Runner('Иван', speed=8)
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3, runner4)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_fastest_runner(self):
        runner5 = runner_and_tournament.Runner('Мария', speed=12)
        tournament = runner_and_tournament.Tournament(90, self.runner1, runner5, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')


if __name__ == '__main__':
    unittest.main()