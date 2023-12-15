import the as the

Feature: check the functionality of the main page

  Background:
    Given Main Page: I am on the ask.com main page

  @main_page
    Scenario Outline:
      When Main Page: I click on "<element>"
      Then I am on the "<page>" and I see text "<success_text>" with text element "<text_element>"
      Examples:
        | element                                                 | page                                                        | success_text                    | text_element                                |
       https://www.ask.com/web?q=panda&ad=dirN&o=0&ueid=99ea687f-2407-4e50-94d9-0b06641f1b15
       www.reference.com/pets-animals/pandas-important-ef370616ba825b9f
       www.reference.com/pets-animals/many-types-pandas-eda790f3934f96b7
       www.reference.com/pets-animals/fun-pandas-8ce21dbdd0adb121
