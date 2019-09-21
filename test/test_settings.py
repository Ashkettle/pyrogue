"""Simple example test to make sure pytest is up and running"""

from game import settings

def test_black_color():
    """Test BLACK constant"""
    assert settings.Colors.BLACK == (0, 0, 0)

def test_white_color():
    """Test WHITE constant"""
    assert settings.Colors.WHITE == (255, 255, 255)

def test_red_color():
    """Test RED constant"""
    assert settings.Colors.RED == (255, 0, 0)

def test_green_color():
    """Test GREEN Constant"""
    assert settings.Colors.GREEN == (0, 255, 0)

def test_blue_color():
    """Test BLUE constant"""
    assert settings.Colors.BLUE == (0, 0, 255)
