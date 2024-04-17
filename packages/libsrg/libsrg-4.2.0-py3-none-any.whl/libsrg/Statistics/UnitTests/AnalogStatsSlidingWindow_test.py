import math
import random
import unittest
from time import time, ctime

from libsrg.Statistics.AnalogStatsBase import AStatsRecord
from libsrg.Statistics.AnalogStatsSlidingWindow import AnalogStatsSlidingWindow

# force reproducible random data
my_random = random.Random()
my_random.seed(42)

gdata_mu = 100.
gdata_sigma = 10.
gdata = [my_random.gauss(mu=gdata_mu, sigma=gdata_sigma) for _ in range(10000)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # with alpha and beta set to 1, weighted and non-weighted stats should match
        r = AnalogStatsSlidingWindow("varname")
        self.assertEqual(0, r._sample_count)
        self.assertEqual("varname", r.name())

        r.sample(4)
        self.assertEqual(1, r._sample_count)
        self.assertAlmostEqual(4., r._sum_samples)

        r.sample(5)
        r.sample(6)

        self.assertEqual(3, r._sample_count)

        self.assertAlmostEqual(15., r._sum_samples)

        self.assertAlmostEqual(5., r.mean())

        ex: float = sum([4. * 4., 5. * 5., 6. * 6.])
        self.assertAlmostEqual(ex, r._sum_samples_sq)

        ex: float = sum([4 * 4, 5 * 5, 6 * 6]) / 3.
        print(f"{ex=}")
        self.assertAlmostEqual(ex, r.mean_squared())
        print(r)

    def test_random_0_9(self):
        self.random_inner(alpha=0.9)

    # noinspection PyUnusedLocal
    def random_inner(self, alpha=0.99):
        print("---------------------")
        t0 = time()
        r = AnalogStatsSlidingWindow("random1")
        for i, s in enumerate(gdata):
            r.sample(s, sample_time=(t0 + i))
        self.assertAlmostEqual(gdata_mu, r.mean(), delta=0.2)
        self.assertAlmostEqual(gdata_sigma, r.sd(), delta=0.2)
        print(f"{r._time_last_sample=}")
        print(
            f"{ctime(r._time_first_sample)}  {ctime(r._time_last_sample)}")
        print(r)
        print("---------------------")

    def callback(self, record):
        self.record = record

    def test_callback(self):
        t0 = time()
        r = AnalogStatsSlidingWindow("callback", callbacks=[self.callback])
        self.record: AStatsRecord | None = None
        r.sample(1000, sample_time=t0)
        print(self.record)
        self.assertIsNotNone(self.record)
        self.assertAlmostEqual(1000., self.record.value)
        print(r)

    def test_window(self):
        r = AnalogStatsSlidingWindow("window", window=3)
        r.sample(9)
        r.sample(10)
        r.sample(11)
        sd = math.sqrt(2 / 3)
        self.assertAlmostEqual(3, r.count())
        self.assertAlmostEqual(10., r.mean(), delta=0.1)
        self.assertAlmostEqual(sd, r.sd(), delta=0.1)

        r.sample(90)
        r.sample(100)
        r.sample(110)
        self.assertAlmostEqual(3, r.count())
        self.assertAlmostEqual(100., r.mean(), delta=0.1)
        self.assertAlmostEqual(10 * sd, r.sd(), delta=0.1)


if __name__ == '__main__':
    unittest.main()
