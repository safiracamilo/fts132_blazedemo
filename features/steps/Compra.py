import time

from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# precisa sempre importar a classe environment (onde estão o Antes e o Depois do Teste)
from features import environment

# método executado antes da feature e serve para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            # pode ser incluidas outras ações
        )

@given(u'que acesso o site Blazedemo')
@given(u'que acesso o portal Blazedemo')
def step_impl(context):
    context.driver.get('https://www.blazedemo.com')
    print('Passo 1 - Acessou o site Blazedemo')
    # time.sleep(5) # Espera bruta - Sempre remover - alfinete

@when(u'seleciono a cidade de origem como "{origem}"')
def step_impl(context, origem):

    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)

    print('Passo 2 - Selecionou a cidade de origem')

@when(u'seleciono a cidade de destino como "{destino}"')
def step_impl(context, destino):
    # Mapeia o combo com as cidades de origem
    combo_destino = context.driver.find_element(By.NAME, 'toPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_destino = Select(combo_destino)

    # Seleciona o elemento no combo
    objeto_destino.select_by_visible_text(destino)
    print('Passo 3 - Selecionou a cidade de destino')
    # time.sleep(3)

@when(u'clico no botao Find Flights')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 4 - Clicou no botão Find Flights')

@then(u'sou direcionado para a pagina de selecao de voos de "{origem}" para "{destino}"')
def step_impl(context, origem, destino):
    print()
    # 3 Principais motivos para um script de automação não funcionar:
    # - Seletores ou Identificadores
    # - Sincronismo
    # - "Programação Exótica"

    # assert context.driver.find_element(By.TAG_NAME, 'h3').text() == 'Flights from São Paolo to Rome: '

    time.sleep(5)
    assert context.driver.find_element(By.XPATH,
    '/html[1]/body[1]/div[2]/h3[1]').text ==f'Flights from {origem} to {destino}: '
    print('Passo 5 - Direcionou para a página de seleção de vôos')


@when(u'seleciono o primeiro voo')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small').click()
    print('Passo 6 - Selecionou o primeiro vôo')



@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,
     "//p[contains(text,'Please submit the form below to purchase the flight.')]").text == \
     'Please submit the form below to purchase the flight.'
    print('Passo 7 - Direcionou para a página de pagamento')

@when(u'preencho os dados para o pagamento')
def step_impl(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('James Bond')
    print('Passo 8 - Preencheu os dados para o pagamento')


@when(u'clico no botao Purchase Flight')
def step_impl(context):

    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 9 - Clicou no botão Purchase Flight')


@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
    print()

    assert context.driver.find_element(By.TAG_NAME, 'h1').text == 'Thank you for your purchase today!'
    print('Passo 10 - Direcionou para a página de confirmação')


@when(u'seleciono de "{origem}" para "{destino}"')
def step_impl(context, origem, destino):
    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)

    # Mapeia o combo com as cidades de origem
    combo_destino = context.driver.find_element(By.NAME, 'toPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_destino = Select(combo_destino)

    # Seleciona o elemento no combo
    objeto_destino.select_by_visible_text(destino)

    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

    print('Passo 2c - Selecionou a cidade de origem e destino')