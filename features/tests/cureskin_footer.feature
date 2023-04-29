Feature: Cureskin shop page footer tests

  Scenario: Subscription successful message is displayed when user enters valid email
    Given Open Cureskin shop page
    When Enter valid email id aaravsairam@gmail.com
    And Click on arrow
    Then Verify Thanks for subscribing message is shown
