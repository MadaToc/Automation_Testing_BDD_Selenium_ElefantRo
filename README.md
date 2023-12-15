TESTED APPLICATION

https://elefant.ro/

I chose to check the Elefant.ro website. We have evolved adding a product to the basket, leaving the page, contacting the site representatives, creating an account, delivery points, logging in to the page, creating a new account, the product page and searching for a product. To ensure that all these functions work correctly, we have checked functionalities such as: incorrect account entry, out-of-stock products, etc.

LANGUAGE, IDE, BOOKSTORES

I chose to perform the testing using the Python programming language and the PyCharm IDE. I used the Selenium, webdriver-manager, behave and behave-html-formatter libraries to automate the interaction with the Elefant.ro website. The "Python Packages" section of PyCharm can be accessed to install these libraries. After adding the name of the desired library in the field, I pressed the "Install" button.

THE IMPORTANCE OF AUTOMATED TESTING

Efficiency in software development depends on automated testing. Speed, reproducibility, extended coverage, reusability, ease of integration with agile development practices and early detection of errors are the main benefits. This constantly helps to ensure the quality of the software.

THE CHOSEN METHODOLOGY

The software development methodology called BDD (Behavior-Driven Development) focuses on the collaboration of team members and on describing the behavior of the application in a simple language, such as Gherkin. We chose BDD to facilitate communication between developers, testers and other interested parties and to create automated tests that reflect the behavior clearly specified by stakeholders. Benefits include: clear communication, easy-to-understand and up-to-date tests, and alignment between requirements and implementation. BDD encourages teamwork and guarantees that development focuses on developing useful functionalities that meet user expectations.

DESIGN PATTERN

I chose to organize the code of the automated tests using the "Page Object Model" (POM). Reusability, encapsulation, ease of maintenance, readability and resistance to change are some of its benefits. POM improves the development and maintenance of automated tests and code structure.

USE OF THE PROJECT

Using the project starts by cloning it from GitHub. Access the project, press the green "Code" button, copy the link, navigate on the computer to the desired folder, open Git Bash, write the command "git clone" followed by the link and press "Enter". The cloned project can be opened in PyCharm. To run tests, use the command "behave -f html -o behave-report.html" in the terminal. To view the generated report, open the "behave-report.html" file in Chrome.

STRUCTURE OF THE PROJECT

The project has a structure consisting of a series of files and directories.  We have the structure of the pages tested in the "environment". "features", "pages" and "steps".The test scenarios are written in Gherkin syntax and can be found in the "features" category. 

My project contains 10 test scenarios, covering different aspects of the elefant.ro website. These scenarios include checking the cart page, checkout page, filling out and submitting a form, interacting with items, checking available delivery points, and more. Each scenario is implemented by defining corresponding classes and methods that extend the base classes and use the functionality and methods in Selenium.
Risks associated with these automation programs include changes to the user interface of the elefant.ro website, dependence on external factors (such as the Chrome browser and Chrome driver), timing and speed of page loading, dependence on test data and limitations of automation .
To minimize these risks, it is important to regularly update and maintain the automation code to reflect changes in the elefant.ro website. You can also apply best practices in automated testing and use appropriate techniques to address specific risks.

