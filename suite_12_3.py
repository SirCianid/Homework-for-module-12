import unittest
import test_12_3


runTS = unittest.TestSuite()
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTS)