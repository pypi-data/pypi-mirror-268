"""
Test: Fun

Version: 1.0.2
Date updated: 06/04/2024 (dd/mm/yyyy)
"""

# Library
###########################################################################
import pytest

from absfuyu.fun import im_bored, zodiac_sign


# Test
###########################################################################
# zodiac
def test_zodiac():
    assert zodiac_sign(1, 1) == "Capricorn"


def test_zodiac_2():
    assert zodiac_sign(1, 1, zodiac13=True) == "Sagittarius"


# im_bored
@pytest.mark.skip
def test_im_bored():
    # Basically True but put it in anyway
    assert im_bored()
