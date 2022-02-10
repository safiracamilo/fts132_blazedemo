from selenium import webdriver
# Início
def before_all(context):    # Antes de Tudo
    # Declarar o Selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('C:/Users/SAFIRA/PycharmProjects/fts132_blazedemo/drivers/chrome96/chromedriver.exe')
    # Maximizar a janela do navegador
    context.driver.maximize_window()

    # Define uma espera máxima para todos os elementos do script
    context.driver.implicitly_wait(30)

    print('Passo A - Antes de Tudo')

# Fim
def after_all(context):     # Depois de Tudo
    # Desligar / Detruir o objeto do Selenium
    context.driver.quit()

    print('Passo Z - Depois de Tudo')
    print('Passo Z - Depois de Tudo')

# Bloco executado ao final de cada step
def after_step(context, step):
    print()

