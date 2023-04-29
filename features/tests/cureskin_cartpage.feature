Feature: Cureskin shop page update cart functionality test

  Scenario: User can remove the product from the cart page by pressing the - button
    Given Open Cureskin shop page
    When Click on search
    And Enter the product name face foam
    And Click on product search button
    And Click the first item
    And Click add to cart button
    And Click on cart icon
    And Click on - button to reduce product quantity
    Then Verify that Your cart is currently empty message is displayed