import unittest
import re

def test_alpha(s):
    pattern ='[a-zA-Z]+'
    result = re.findall(pattern,s)
    print(result)
    return None