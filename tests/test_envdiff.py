import os
import tempfile
import unittest

from envdiff import diff, load


class EnvDiffTest(unittest.TestCase):
    def test_parse(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = os.path.join(tmp, ".env")
            open(p, "w").write("# c\nexport A=1\nB='two'\nC=\"3\"\n")
            self.assertEqual(load(p), {"A": "1", "B": "two", "C": "3"})

    def test_diff(self):
        d = diff({"a": "1", "b": "2"}, {"b": "3", "c": "4"})
        self.assertEqual(d["added"], ["c"])
        self.assertEqual(d["removed"], ["a"])
        self.assertEqual(d["changed"], ["b"])


if __name__ == "__main__":
    unittest.main()
