"""Behave Calculator SOAP
"""
# pylint: disable=unused-wildcard-import, undefined-variable, unused-argument
# pylint: disable=wildcard-import


from behave import *
import zeep


class TestFixture:  # pylint: disable=too-few-public-methods
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
tf = TestFixture  # pylint: disable=invalid-name


@given(u'we have two numbers 5 and 5')
def the_setup(context):
    """Setup
    """
    tf.x = 5
    tf.y = 5


@when(u'added together')
def add_stuff(context):
    """Do the addition
    """
    wsdl_url = "http://www.dneonline.com/calculator.asmx?WSDL"
    soap = zeep.Client(wsdl=wsdl_url,
                       service_name="Calculator",
                       port_name="CalculatorSoap12")
    tf.result = soap.service.Add(intA=tf.x, intB=tf.y)


@then(u'equal 10')
def the_result(context):
    """Match results
    """
    assert tf.result == 10
