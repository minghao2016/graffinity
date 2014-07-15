from unittest import TestCase

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

        #with open("atest.py",'r') as tf:
        #  data = eval(tf.read())

        gender_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        age_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        languages_func = lambda x: 5*(len(x) - len(set(x)))

        funcs = {
            "gender": gender_func,
            "age": age_func,
            "languages": languages_func,
        }

        affinityfunc = "gender_func(x) + 3.5*age_func(x) + 0.1*languages_func(x)"

        g = graffinity.Graffinity(data, funcs, affinityfunc)
        results = g.calculate()
        self.assertEqual(results["n1"]["n1"], 0.0)
        self.assertEqual(results["n1"]["n2"], 4.699007150707624)
        self.assertEqual(results["n2"]["n1"], 4.699007150707624)
        self.assertEqual(results["n2"]["n2"], 0.0)
        self.assertEqual(results["n2"]["n3"], 4.317276211268162)

    def test_group_calculation(self):
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

        #with open("atest.py",'r') as tf:
        #  data = eval(tf.read())

        gender_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        age_func = lambda x: abs(statistics.mean(x) - statistics.stdev(x))/statistics.mean(x)
        languages_func = lambda x: 5*(len(x) - len(set(x)))

        funcs = {
            "gender": gender_func,
            "age": age_func,
            "languages": languages_func,
        }

        affinityfunc = "gender_func(x) + 3.5*age_func(x) + 0.1*languages_func(x)"
        groupaffinityfunc = "gender_func(x) + 3.5*age_func(x) + 0.1*languages_func(x)"

        g = graffinity.Graffinity(data, funcs, affinityfunc, groupaffinityfunc)
        group = ['n1','n3','n4']
        result = g.calculategroup(group)
        self.assertEqual(result, 3.4631259739423936)
