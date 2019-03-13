#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    Created By - Lingesh Aradhya
    License: GNU GPL
    Source Control: https://github.com/Llivingon/
    Creation Date: 12 Mar 2019
  Overview -
    Compare two version strings
       Logic: Split versions based on ".", then start comparing from left to right and determine which is a bigger version.
       Results are Lower Greater or Equal with regards to v1   
  Background
    Install Python 2.7

'''

import unittest

class Assignment2(object):
    """Compare two version strings
       Logic: Split versions based on ".", then start comparing from left to right and determine which is a bigger version.
       Results are Lower Greater or Equal with regards to v1
    """

    def versionCompare(self, v1, v2): 
          
        # This will split both the versions by '.' 
        arr1 = v1.split(".") 
        arr2 = v2.split(".")

        #Some version maybe longer, we need to keep comparing till the smaller
        #version exhausts
        smallerVersion =  list(min(arr1, arr2, key=len))

        while(smallerVersion):
            string1 = arr1.pop(0)
            string2 = arr2.pop(0)
 
            if string2 > string1: 
                return v1 + " is Lower than "+ v2
              
            if string1 > string2: 
                return v1 + " is Greater than " + v2
      
            # Can't conclude yet 
            smallerVersion.pop(0)
              
        # After comparisons, we are left with 3 options,
            # 1. They are equal if their version length matches.
            # 2. v1 is greater if length of v1 is greater and
            # 3. v2 is greater if length of v2 is greater
            
        if len(arr1) == len(arr2):
            return v1 + " is Equal to " + v2
        if len(arr1) > len(arr2):
            return v1 + " is Greater than " + v2
        return v1 + " is Lower than "+ v2



class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.obj = Assignment2()

    def tearDown(self):
        """Call after every test case."""
        pass

    def test1(self):
        """v1 is Lower"""
        assert self.obj.versionCompare("1.0.2.1", "1.0.4.1") == "1.0.2.1 is Lower than 1.0.4.1", "v1 should be Lower"

    def test2(self):
        """v1 is greater"""
        assert self.obj.versionCompare("1.0.7", "1.0.2") == "1.0.7 is Greater than 1.0.2", "v1 should be Greater"

    def test3(self):
        """v1 is greater with alphabet in version number"""
        assert self.obj.versionCompare("1.0.7a", "1.0.7") == "1.0.7a is Greater than 1.0.7", "v1 should be Greater"

    def test4(self):
        """v1 is lower with alphabet in version number"""
        assert self.obj.versionCompare("1.0.2", "1.0.26") == "1.0.2 is Lower than 1.0.26", "v1 should be Lower"

    def test5(self):
        """v1 is lower, looks like v2 is a patch of v1"""
        assert self.obj.versionCompare("1.0.7", "1.0.7.1") == "1.0.7 is Lower than 1.0.7.1", "v1 should be Lower"

    def test6(self):
        """v1 is greater, looks like v1 is a patch of v2 (with alphabet in version)"""
        assert self.obj.versionCompare("1.0.7.a", "1.0.7") == "1.0.7.a is Greater than 1.0.7", "v1 should be Greater"        

    def test7(self):
        """Both versions are the same"""
        assert self.obj.versionCompare("1.0.7", "1.0.7") == "1.0.7 is Equal to 1.0.7", "Both versions are Equal"

    def test8(self):
        """Both versions are empty"""
        assert self.obj.versionCompare("", "") == " is Equal to ", "Both versions are Equal"

    def test9(self):
        """v1 versions is empty"""
        assert self.obj.versionCompare("", "2.1") == "Equal", "Both versions are Equal"
        
    def test9(self):
        """Both versions are alphabets. v1 is Lower"""
        assert self.obj.versionCompare("a", "b") == "a is Lower than b", "v1 should be Lower"

    def test10(self):
        """Both versions are alphabets. v1 is Greater"""
        assert self.obj.versionCompare("b", "a") == "b is Greater than a", "v1 should be Greater"


if __name__ == '__main__':
    unittest.main()
