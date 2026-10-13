import pytest
from triangle_classifier import triangle_type
from insurance_discount import insurance_discount

def test_equilateral_triangle():
    assert triangle_type(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert triangle_type(3, 3, 2) == "Isosceles"

def test_scalene_triangle():
    assert triangle_type(3, 4, 5) == "Scalene"

def test_degenerate_triangle_is_invalid():
    assert triangle_type(100, 100, 200) == "Invalid"
def test_under25_no_claims_standard():
    assert insurance_discount("<25", "none", "Standard") == 10

def test_under25_no_claims_premium():
    assert insurance_discount("<25", "none", "Premium") == 15

def test_age25to65_one_claim_standard():
    assert insurance_discount("25-65", "1", "Standard") == 10

def test_over65_two_or_more_claims_premium():
    assert insurance_discount(">65", "2+", "Premium") == 5