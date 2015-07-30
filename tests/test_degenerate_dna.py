"""test_degenerate_dna

Tests for `degenerate-dna` module.
"""
import unittest

from degenerate_dna import Degenera


class TestApi(unittest.TestCase):
    def setUp(self):
        self.dna = 'AGTTCTTTACTACGTAGA'
        self.res = Degenera(dna=self.dna)

    def test_standard_code_normal(self):
        self.res.table = 1
        self.res.type = 'normal'
        self.res.degenerate()

        result = self.res.degenerated
        expected = 'AGYTCNYTNYTNMGNMGN'
        self.assertEqual(expected, result)

    def test_standard_code_S(self):
        self.res.table = 1
        self.res.type = 'S'
        self.res.degenerate()

        result = self.res.degenerated
        expected = 'AGYAGYYTNYTNMGNMGN'
        self.assertEqual(expected, result)

    def test_standard_code_Z(self):
        self.res.table = 1
        self.res.type = 'Z'
        self.res.degenerate()

        result = self.res.degenerated
        expected = 'TCNTCNYTNYTNMGNMGN'
        self.assertEqual(expected, result)

    def test_standard_code_SZ(self):
        self.res.table = 1
        self.res.type = 'SZ'
        self.res.degenerate()

        result = self.res.degenerated
        expected = 'NNNNNNYTNYTNMGNMGN'
        self.assertEqual(expected, result)
