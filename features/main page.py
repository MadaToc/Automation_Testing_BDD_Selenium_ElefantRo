from behave import *

@given ('Main Page: I am on the ask.com main page')
def step_impl(context):
    context.main_page_object.navigate_to_main_page()

@when ('Main Page: I click on "{element}"')
def step_impl(context, element):
    context.main_page_object.click_on_main_page_elements(element)

@then ('I am on the "{page}" and I write "panda"')
def step_impl(context, page, success_text, text_element):
     context.main_page_object.check_page_url(page)
     context.main_page_object.check_success_text(success_text, text_element)
