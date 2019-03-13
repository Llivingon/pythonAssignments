#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    Created By - Lingesh Aradhya
    License: GNU GPL
    Source Control: https://github.com/Llivingon/
    Creation Date: 12 Mar 2019
  Overview -
    Platform - Unix/Windows
    Use Open source scripting language - Python
  Summary  
    Returns True if 2 x-axes lines intersects else returns False 
  Background
    Install Python 2.7
    Install below modules
'''

import unittest

class Assignment1(object):
    """Determines if two x axis lines overlap
    """

    def doesLinesIntersect(self, line1, line2):
        """Arguments:
        Line 1 Co-Ordinates: List with 2 integer co ordinate integers for 1st Line
        Line 2 Co-Ordinates: List with 2 integer co ordinate integers for 2nd Line"""
        """Returns True if intersects else returns false"""

        #Sorting Co-ordinates to make them left aligned
        line1.sort()
        line2.sort()
        #Logic to determine if lines overlap
        if max(line1[1], line2[1]) - min(line1[0], line2[0]) < \
            (line1[1] - line1[0]) + (line2[1] - line2[0]):
            return True
        else:
            return False



class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.obj = Assignment1()

    def tearDown(self):
        """Call after every test case."""
        pass

    def test1(self):
        """Positive Co-Ordinates that do not overlap"""
        assert self.obj.doesLinesIntersect([1,2], [6,10]) == False, "Positive Co-Ordinates that do not overlap"

    def test2(self):
        """Positive Co-Ordinates that overlap"""
        assert self.obj.doesLinesIntersect([1,10], [12,2]) == True, "Positive Co-Ordinates that overlap"

    def test3(self):
        """Positive Co-Ordinates that have a common co-ordinate but do not overlap"""
        assert self.obj.doesLinesIntersect([1,10], [10,12]) == False, "Positive Co-Ordinates that overlap"

    def test4(self):
        """Negative Co-Ordinates that do not overlap"""
        assert self.obj.doesLinesIntersect([-6,2], [-6,-10]) == False, "Negative Co-Ordinates that do not overlap"

    def test5(self):
        """Negative Co-Ordinates that overlap"""
        assert self.obj.doesLinesIntersect([-6,10], [2,10]) == True, "Negative Co-Ordinates that overlap"

    def test6(self):
        """Co-Ordinates with dot is not a line"""
        assert self.obj.doesLinesIntersect([1,1], [1,1]) == False, "Co-Ordinates with dot is not a line"

    def test7(self):
        """Co-Ordinates with both lines overlap 100%"""
        assert self.obj.doesLinesIntersect([1,10], [10,1]) == True, "Co-Ordinates that overlap 100%"

    def test8(self):
        """Co-Ordinates with one line overlaps 100%"""
        assert self.obj.doesLinesIntersect([1,5], [-5,+15]) == True, "Co-Ordinates that overlap 100%"

    def test9(self):
        """Co-Ordinates with Zero co-ordinates"""
        assert self.obj.doesLinesIntersect([0,0], [0,0]) == False, "Empty Co-Ordinates"


if __name__ == '__main__':
    unittest.main()
