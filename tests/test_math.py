'''
Testing MolSSI math module
'''

import redesigned_guacamole as rdg
import pytest

def test_add():
	assert rdg.add(5, 6) == 11
	assert rdg.add(2, 6) == 8	
	
testdata = [
	(2, 5, 10),
	(6, 5, 30),	
	(0, 5, 0),
]	

@pytest.mark.parametrize("a,b,expected", testdata)	
def test_mult(a, b, expected):
	assert rdg.mult(a, b) == expected