# coding=utf-8
"""Calculator SOAP API Interactions feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/calculator.feature', 'Addition works')
def test_addition_works():
    """Addition works."""


@scenario('features/calculator.feature', 'Subtraction works')
def test_subtraction_works():
    """Subtraction works."""


@given('two numbers 10 and 5')
def two_numbers_10_and_5():
    """two numbers 10 and 5."""
    raise NotImplementedError


@given('we have two numbers 5 and 5')
def we_have_two_numbers_5_and_5():
    """we have two numbers 5 and 5."""
    raise NotImplementedError


@when('added together')
def added_together():
    """added together."""
    raise NotImplementedError


@when('subtracting 5 from 10')
def subtracting_5_from_10():
    """subtracting 5 from 10."""
    raise NotImplementedError


@then('equal 10')
def equal_10():
    """equal 10."""
    raise NotImplementedError


@then('result equals 5')
def result_equals_5():
    """result equals 5."""
    raise NotImplementedError
