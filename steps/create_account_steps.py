from behave import *

@given ("Create Account Page: I am on the account creation page")
def step_impl(context):
    context.create_account_page_object.navigate_to_create_account_page()

@when ('Create Account Page: I insert the surname "{surname}" , name "{name}", email "{email}" , password "{password}"')
def step_impl(context, surname, name, email, password):
    context.create_account_page_object.insert_new_surname(surname)
    context.create_account_page_object.insert_new_name(name)
    context.create_account_page_object.insert_new_email(email)
    context.create_account_page_object.insert_password(password)

@when ('Create Account Page: I click on status')
def step_impl(context):
    context.create_account_page_object.choose_status()

@when ('Create Account Page: I click on "all preferences"')
def step_impl(context):
    context.create_account_page_object.click_on_all_preferences()

@when ('Create Account Page: I click on "agree with terms and conditions"')
def step_impl(context):
    context.create_account_page_object.click_on_agreement()

@when ("Create Account Page: I click the create account button")
def step_impl(context):
    context.create_account_page_object.click_create_account()

@then ('Create Account Page: I cannot create an account and I receive an error "{error_message}"')
def step_impl(context, error_message):
    context.create_account_page_object.check_mail_error(error_message)
    context.create_account_page_object.password_error(error_message)
    context.create_account_page_object.check_create_account_error(error_message)

@when ('Create Account Page: I insert the surname with special characters "{surname}" , name with special characters "{name}", email "{email}" , password "{password}"')
def step_impl(context, surname, name, email, password):
    context.create_account_page_object.insert_new_surname(surname)
    context.create_account_page_object.insert_new_name(name)
    context.create_account_page_object.insert_new_email(email)
    context.create_account_page_object.insert_password(password)

@when('New Create Account Page: I will be sent to another page where an error alert/box will appear but with no actual error inside it')
def step_impl(context):
    context.new_create_account_page_object.check_url()
    context.new_create_account_page_object.assert_element_has_text()

@then('New Create Account Page: we insert special characters to the name "{name}" and to the surname "{surname}" again and we finally receive the error "{error_message}"')
def step_impl(context, error_message):
    context.new_create_account_page_object.add_special_characters_to_surname_and_name()
    context.new_create_account_page_object.verify_special_char_error(error_message)