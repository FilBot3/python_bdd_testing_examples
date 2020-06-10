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


@scenario('features/calculator.feature', 'Addition works')
def test_addition_works():
    """Addition works."""


@given('we have two numbers 5 and 5')
def we_have_two_numbers_5_and_5():
    """we have two numbers 5 and 5."""
    tf.x = 5
    tf.y = 5


@when('added together')
def added_together():
    """added together."""
    wsdl_url = "http://www.dneonline.com/calculator.asmx?WSDL"
    soap = zeep.Client(wsdl=wsdl_url,
                       service_name="Calculator",
                       port_name="CalculatorSoap12")
    tf.result = soap.service.Add(intA=tf.x, intB=tf.y)


@then('equal 10')
def equal_10():
    """equal 10."""
    assert tf.result == 10
