import unittest

from enum import Enum
from libsrg.Statistics.DiscreteStatsSlidingWindow import DiscreteStatsSlidingWindow


class Status(Enum):
    NODATA = (-1, 'grey', 'lightgrey')
    OK = (0, 'lime', 'lightgreen')
    UNKNOWN = (1, 'magenta', '#f1a7fe')
    MAINT = (2, 'cyan', '#e0ffff')
    WARNING = (3, 'yellow', 'lightyellow')
    CRITICAL = (4, 'red', '#ffc0cb')


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ds = DiscreteStatsSlidingWindow("Colors")
        ds.sample("red")
        ds.sample("red")
        ds.sample("red")
        ds.sample("blue")
        ds.sample("blue")
        ds.sample("green")

        self.assertEqual(3, ds.count_for("red"))
        self.assertEqual(2, ds.count_for("blue"))
        self.assertEqual(1, ds.count_for("green"))
        self.assertEqual(0, ds.count_for("yellow"))

        print(ds.counts())
        act = ds.most_common(2)
        # print(ds.most_common())
        print(ds.most_common(1))
        print(ds.most_common(2))
        print(ds.most_common(3))
        print(ds.most_common(4))
        exp = [('red', 3), ('blue', 2)]
        self.assertEqual(exp, act)

    def test_status(self):
        ds = DiscreteStatsSlidingWindow("Status")
        ds.sample(Status.OK)
        ds.sample(Status.OK)
        ds.sample(Status.CRITICAL)
        self.assertEqual(2, ds.count_for(Status.OK))
        self.assertEqual(1, ds.count_for(Status.CRITICAL))
        self.assertEqual(0, ds.count_for(Status.WARNING))
        print(ds.counts())
        print(ds.most_common(3))
        print(ds.most_common_as_str(3))

    def test_window(self):
        ds = DiscreteStatsSlidingWindow("Status",window=3)
        ds.sample(Status.OK)
        ds.sample(Status.OK)
        ds.sample(Status.CRITICAL)
        self.assertEqual(2, ds.count_for(Status.OK))
        self.assertEqual(1, ds.count_for(Status.CRITICAL))
        self.assertEqual(0, ds.count_for(Status.WARNING))

        ds.sample(Status.WARNING)
        self.assertEqual(1, ds.count_for(Status.OK))
        self.assertEqual(1, ds.count_for(Status.CRITICAL))
        self.assertEqual(1, ds.count_for(Status.WARNING))

        ds.sample(Status.WARNING)
        self.assertEqual(0, ds.count_for(Status.OK))
        self.assertEqual(1, ds.count_for(Status.CRITICAL))
        self.assertEqual(2, ds.count_for(Status.WARNING))

        ds.sample(Status.WARNING)
        self.assertEqual(0, ds.count_for(Status.OK))
        self.assertEqual(0, ds.count_for(Status.CRITICAL))
        self.assertEqual(3, ds.count_for(Status.WARNING))



if __name__ == '__main__':
    unittest.main()
