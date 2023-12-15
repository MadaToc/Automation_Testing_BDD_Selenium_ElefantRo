from behave import *

@given ("Login Page: I am on the elefant.ro login page")
def step_impl(context):
    context.login_page_object.navigate_to_login_page()

@when ('Login Page: I insert the email "{email}" and password "{password}"')
def steps_impl(context, email, password):
    context.login_page_object.insert_email(email)
    context.login_page_object.insert_password(password)

@when ('Login Page: I click the login button')
def step_impl(context):
    context.login_page_object.login_button_click()

@when ('Login Page: I insert the correct email "JohnyNebunu@mail.com" and the correct password "DacaMaiBeauUnPahar"')
def step_impl(context):
    context.login_page_object.insert_specific_email()
    context.login_page_object.insert_specific_password()


@then ('Main Page: I successfully login into the application')
def step_impl(context):
    context.login_page_object.verify_url_and_title()


@then ('Login Page: I can not login into the application and I receive an error "{error_message}"')
def step_impl(context, error_message):
    context.login_page_object.check_login_error(error_message)