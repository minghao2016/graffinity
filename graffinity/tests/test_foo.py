from unittest import TestCase
import unittest

import graffinity
import statistics


class TestFoo(TestCase):

    def test_basic_calculation(self):
        data = {
            "n1": {
                "gender": [0],
                "age": [36],
                "languages": [2,5,6],
            },
            "n2": {
                "gender": [1],
                "age": [33],
                "languages": [2,6],
            },
            "n3": {
                "gender": [1],
                "age": [25],
                "languages": [1,6,9,10],
            },
            "n4": {
                "gender": [1],
                "age": [28],
                "languages": [1],
            }

        }

        gender_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        age_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        languages_func = lambda x: 5*(len(x) - len(set(x)))
        affinity_func = lambda x: gender_func(x) + 3.5*age_func(x) + 0.1*languages_func(x)

        funcs = {
            "gender": gender_func,
            "age": age_func,
            "languages": languages_func,
            "affinity": affinity_func
        }
        g = graffinity.Graffinity(data, funcs)
        results = g.calculate()
        self.assertEqual(results["n1"]["n1"], 100)
        self.assertEqual(results["n1"]["n2"], 6.106775831422421)
        self.assertEqual(results["n2"]["n1"], 6.106775831422421)
        self.assertEqual(results["n2"]["n2"], 100)


if __name__=="__main__":
  unittest.main()
