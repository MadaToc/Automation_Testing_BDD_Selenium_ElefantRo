from tabnanny import check

import on

Feature: check the functionality of the search function

  Background:
    Given Main Page: I am on the ask.com main page


    @search_products
    Scenario Outline: test search functionality
      When Main Page: In search bar I search for "<panda>"
      Then Products Page: I see the results "<search_results>" that contains "<panda>"
      Examples:
      images with panda bears
      images with panda toys
      images with books with panda


    @add_searched_panda
    Scenario Outline: test that products are showed to site
      When Main Page: In search bar I search for "<panda>"

      And I see images and I verify the link
      Then Main Page: I am on the main page
      Examples:
       images with panda
      # we have only this one search result, because in the results page there are multiple of these from which we choose

