Feature: Cureskin face page tests

  Scenario: User can see the word "face" in the first product name
    Given Open Cureskin shop page
    When Click on shop by category
    And Click on face option
    Then Verify Face is present in first product name


  Scenario: User can see "face" header
    Given Open Cureskin shop page
    When Click on shop by category
    And Click on face option
    Then Verify face header is shown
