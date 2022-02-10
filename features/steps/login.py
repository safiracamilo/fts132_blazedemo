import time

from behave import given, when, then
from selenium.webdriver.common.by import By


@when(u'clico em home')
def step_impl(context):
    context.driver.find_elemento(By.LINK_TEXT, 'home').click()


@when(u'preencho "<email>" "<senha>" e clico no botao Login')
def step_impl(context):
    time.sleep(10)
    context.driver.find_elemento(By.ID, 'email').send_keys('safiracamilo@gmail.com')
    context.driver.find_elemento(By.ID, 'passaword').send_keys('xpto1234')
    time.sleep(5)
    context.drive.find_elemento(By.CSS_SELECTOR, 'button.btn.btn-primary').click()


@then(u'vejo a mesagem de confirmacao')
def step_impl(context):
    time.sleep(10)
    assert context.drive.find_elemento(By.CSS_SELECTOR, 'div.code').text == '419'
    assert context.drive.find_elemento(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'


