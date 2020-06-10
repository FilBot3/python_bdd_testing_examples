Feature: Calculator SOAP API Interactions

  The Calculator SOAP API provides basic functions of a calculator to learn more
  about how SOAP API's work and how to read the WSDL they provide. Using Zeep
  we'll go through and see how to use Python's Behave suite to perform BDD tests
  against the results of the SOAP API.

  Scenario: Addition works
    Given we have two numbers 5 and 5
    When added together
    Then equal 10

  Scenario: Subtraction works
    Given two numbers 10 and 5
    When subtracting 5 from 10
    Then result equals 5
