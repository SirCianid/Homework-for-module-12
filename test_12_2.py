import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
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

    def test_tusain_and_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    def test_andrey_and_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    def test_usain_andrey_and_nik(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    def test_multiple_participants(self):
        runner4 = runner_and_tournament.Runner('Иван', speed=8)
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3, runner4)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    def test_fastest_runner(self):
        runner5 = runner_and_tournament.Runner('Мария', speed=12)
        tournament = runner_and_tournament.Tournament(90, self.runner1, runner5, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')


if __name__ == '__main__':
    unittest.main()


# Решение логической ошибки метода start класса Tournament:
# Исправленный метод start:
#    def start(self):
#        finishers = {}
#        while self.participants:
#            for participant in self.participants:
#                participant.run()
#                if participant.distance >= self.full_distance and participant not in finishers.values():
#                    finishers[len(finishers) + 1] = participant
#                    self.participants.remove(participant)
#        return finishers

# Для присваивания мест теперь использую finishers[len(finishers) + 1].Это позволяет автоматически присваивать места
# на основе текущего количества финишировавших участников.

# Также добавил дополнительную проверку - participant not in finishers.values(). Это гарантирует, что участник
# не будет добавлен в список финишировавших, если он уже был зарегистрирован.
# Это может помочь в те моменты, когда участники могут случайно обрабатываться несколько раз.

# Добавил два новых теста для исправленного метода start:
# test_multiple_participants - Проверяет, что Ник все еще финиширует последним, даже если добавляется еще один участник.
# test_fastest_runner - Проверяет, что Ник финиширует последним, даже если добавляется более быстрый бегун.
