from behave import *

@when ('Main Page: In search bar I search for "{product}"')
def step_impl(context, product):
    context.main_page_object.search_for_product(product)

@then ('Products Page: I see the results "{search_results}" that contains "{product}"')
def  step_impl(context, product, search_results):
    context.products_page_object.verify_results_contain_product_text(search_results, product)

@when ('Products Page: I click on the product "{search_results}"')
def step_impl(context, search_results):
    context.products_page_object.click_on_the_product(search_results)

@when ('Cart Page: I am on the cart page and I click add to basket')
def step_impl(context):
    context.cart_page_object.check_url_on_cart_page()
    context.cart_page_object.click_on_add_to_basket()

@when ('Cart Page: I see message "{added_to_cart_message}" and then I click on see basket')
def step_impl(context,added_to_cart_message):
    context.cart_page_object.verify_message_of_added(added_to_cart_message)
    context.cart_page_object.view_basket()

@when ('Checkout Page: I am on the checkout page and I click to remove the product')
def step_impl(context):
    context.checkout_page_object.remove_from_basket()

@when ('Checkout Page: I see message "{removed_from_cart_message}" and I click on continue shopping')
def step_impl(context,removed_from_cart_message):
    context.checkout_page_object.verify_no_product_message(removed_from_cart_message)
    context.checkout_page_object.click_on_continue_shopping()

@then ('Main Page: I am on the main page')
def step_impl(context):
    context.main_page_object.verify_that_we_are_on_main_page()