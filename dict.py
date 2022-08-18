# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 19:58:55 2022

@author: Acer
"""

import re
import requests
from PyDictionary import PyDictionary


def text(input_text):
    dictionary = PyDictionary(input_text)
    res = (dictionary.getMeanings()) 
    return res
   



