# coding=utf-8
"""Calculator SOAP API Interactions feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
import zeep


class ThingFixture:  # pylint: disable=too-few-public-methods
    """Test Fixture Class.
    Here we're just using this to transfer values around because I was having
    issues with Python modifying global values and passing them on.
    So, we're using this as a transport method for values.
    """

    def __init__(self):
        """Initialization Method.
        """
        self.x: int = 0  # pylint: disable=invalid-name
        self.y: int = 0  # pylint: disable=invalid-name
        self.result: int = 0


# This object is used to transport values for assignment and testing.
tf = ThingFixture  # pylint: disable=invalid-name


@scenario('features/calculator.feature', 'Subtraction works')
def test_subtraction_works():
    """Subtraction works."""


@given('two numbers 10 and 5')
def two_numbers_10_and_5():
    """two numbers 10 and 5."""
    tf.x = 10
    tf.y = 5


@when('subtracting 5 from 10')
def subtracting_5_from_10():
    """subtracting 5 from 10."""
    wsdl_url = "http://www.dneonline.com/calculator.asmx?WSDL"
    soap = zeep.Client(wsdl=wsdl_url,
                       service_name="Calculator",
                       port_name="CalculatorSoap12")
    tf.result = soap.service.Subtract(intA=tf.x, intB=tf.y)


@then('result equals 5')
def result_equals_5():
    """result equals 5."""
    assert tf.result == 5
