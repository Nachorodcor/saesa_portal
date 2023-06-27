import os
import time
import shutil
import rpa as r
import requests

from domain.chrome_node import ChromeNode

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

class Scraper():
    def __init__(self, url, email, password, driver_path):
        print(url, email, password, driver_path)
        self.url = url
        self.email = email
        self.password = password
        self.driver_path = driver_path

    def wait(self, seconds):
        return WebDriverWait(self.driver, seconds)
    
    def close(self):
        self.driver.close()
        self.driver = None

    def quit(self):
        self.driver.quit()
        self.driver = None
        
    def login(self):
        print('Entrando en la funcion login...')
        print('----------------------------------------------------------------------')
        
        options = webdriver.ChromeOptions()
        
        self.driver = webdriver.Chrome(self.driver_path, options=options)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        
        # Controlar evento alert() Notificacion
        try:
            alert = WebDriverWait(self.driver, 35).until(EC.alert_is_present())
            alert = Alert(self.driver)
            #texto_alerta = alert.text
            alert.accept()
            
            # if texto_alerta == 'Mostrar notificaciones':
            #     alert.accept()  # Clic en el botón "Aceptar" o "Permitir"
            # else:
            #     alert.dismiss()  # Clic en el botón "Cancelar" o "Bloquear"
                
        except:
            print("No se encontró ninguna alerta.")        
        
        # Seteo de las credenciales
        username = self.email
        password = self.password
        
        # Seteo de selectores login
        selector_username_input = '//*[@id="rutIndex"]'
        selector_password_input = '//*[@id="passwordIndex"]'
        selector_submit_button = '//*[@id="dataLoginIndexForm"]/button'

        # Seleccionar campo y setear usuario
        intentos = 0
        reintentar = True
        while (reintentar):
            try:
                print('Try en la funcion click_element_xpath para el campo username...', intentos)
                print('----------------------------------------------------------------------')
                intentos += 1
                self.wait(20).until(EC.presence_of_element_located((By.XPATH, selector_username_input)))
                self.wait(20).until(EC.element_to_be_clickable((By.XPATH, selector_username_input)))
                element_username = self.driver.find_element(By.XPATH, selector_username_input)
                element_username.click()
                element_username.send_keys(username)
                reintentar = False
            except Exception as e:    
                print('Exception en la funcion click_element_xpath', e)
                print('----------------------------------------------------------------------')
                reintentar = intentos <= 3

        # Seleccionar campo y setear password
        intentos = 0
        reintentar = True
        while (reintentar):
            try:
                print('Try en la funcion click_element_xpath para el campo password...', intentos)
                print('----------------------------------------------------------------------')
                intentos += 1
                self.wait(20).until(EC.presence_of_element_located((By.XPATH, selector_password_input)))
                self.wait(20).until(EC.element_to_be_clickable((By.XPATH, selector_password_input)))
                element_password = self.driver.find_element(By.XPATH, selector_password_input)
                element_password.click()
                element_password.send_keys(password)
                reintentar = False
            except Exception as e:    
                print('Exception en la funcion click_element_xpath', e)
                print('----------------------------------------------------------------------')
                reintentar = intentos <= 3

        # Seleccionar boton y hacer en boton ingresar
        intentos = 0
        reintentar = True
        while (reintentar):
            try:
                print('Try en la funcion click_element_xpath para el boton ingresar...', intentos)
                print('----------------------------------------------------------------------')
                intentos += 1
                self.wait(20).until(EC.presence_of_element_located((By.XPATH, selector_submit_button)))
                self.wait(20).until(EC.element_to_be_clickable((By.XPATH, selector_submit_button)))
                element_button_ingresar = self.driver.find_element(By.XPATH, selector_submit_button)
                element_button_ingresar.click()
                reintentar = False
            except Exception as e:    
                print('Exception en la funcion click_element_xpath', e)
                print('----------------------------------------------------------------------')
                reintentar = intentos <= 3

        time.sleep(20)
        
    def scraper(self):
        print('Entrando en la funcion scraper...')
        print('----------------------------------------------------------------------')
        
        # Seleccionar campo pagos y facturas
        intentos = 0
        reintentar = True
        selector_pagos_facturas = '//*[@id="pagos-tab"]'
        while (reintentar):
            try:
                print('Try en la funcion click_element_xpath para el campo pagos y facturas...', intentos)
                print('----------------------------------------------------------------------')
                intentos += 1
                self.wait(20).until(EC.presence_of_element_located((By.XPATH, selector_pagos_facturas)))
                self.wait(20).until(EC.element_to_be_clickable((By.XPATH, selector_pagos_facturas)))
                element_pagos_facturas = self.driver.find_element(By.XPATH, selector_pagos_facturas)
                element_pagos_facturas.click()
                reintentar = False
            except Exception as e:    
                print('Exception en la funcion click_element_xpath', e)
                print('----------------------------------------------------------------------')
                reintentar = intentos <= 3

        # Seleccionar campo facturacion historica
        intentos = 0
        reintentar = True
        selector_facturacion_historica = '//*[@id="facturacion-historica-collapsed"]'
        while (reintentar):
            try:
                print('Try en la funcion click_element_xpath para el campo facturacion historica...', intentos)
                print('----------------------------------------------------------------------')
                intentos += 1
                self.wait(20).until(EC.presence_of_element_located((By.XPATH, selector_facturacion_historica)))
                self.wait(20).until(EC.element_to_be_clickable((By.XPATH, selector_facturacion_historica)))
                element_facturacion_historica = self.driver.find_element(By.XPATH, selector_facturacion_historica)
                element_facturacion_historica.click()
                reintentar = False
            except Exception as e:    
                print('Exception en la funcion click_element_xpath', e)
                print('----------------------------------------------------------------------')
                reintentar = intentos <= 3

        # Seleccionar campo seleccione servicio
        intentos = 0
        reintentar = True
        selector_seleccione_servicio = '//*[@id="dataFacturacionHistorica"]/form/div/div/button/div/div/div'
        while (reintentar):
            try:
                print('Try en la funcion click_element_xpath para el campo seleccione_servicio...', intentos)
                print('----------------------------------------------------------------------')
                intentos += 1
                self.wait(20).until(EC.presence_of_element_located((By.XPATH, selector_seleccione_servicio)))
                self.wait(20).until(EC.element_to_be_clickable((By.XPATH, selector_seleccione_servicio)))
                element_seleccione_servicio = self.driver.find_element(By.XPATH, selector_seleccione_servicio)
                element_seleccione_servicio.click()
                reintentar = False
            except Exception as e:    
                print('Exception en la funcion click_element_xpath', e)
                print('----------------------------------------------------------------------')
                reintentar = intentos <= 3

        self.driver.implicitly_wait(25)
        
        # Encontrar todos los elementos <li> dentro del <ul> utilizando un selector XPath
        li_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.inner ul.dropdown-menu li')
        self.driver.implicitly_wait(25)
            
        # Borrar elemento vacios y no usable
        depured_list = li_elements[3:]
        texto_legible = [elemento.text for elemento in depured_list]
        print('Lista de Texto: ', texto_legible)
        print('----------------------------------------------------------------------')
        
        # Split de cada elemento para extraer Cliente
        list_client = []
        for elemento in texto_legible:
            primeros_7 = elemento[:7]
            list_client.append(primeros_7)        
                
        time.sleep(25)  # Esperar unos segundos para que se descargue el archivo
        print('Lista de Clientes: ', list_client)
        print('----------------------------------------------------------------------')
            
        # Extraer el valor de cada elemento <li>
        for x in range(0, len(texto_legible)):            

            # Obtener el texto del elemento <li>
            text = texto_legible[x]
            print('Detalle del texto :', text)
            print('----------------------------------------------------------------------')

            # Seleccionar el texto a buscar           
            self.wait(50).until(EC.presence_of_element_located(("link text", text)))
            self.wait(50).until(EC.element_to_be_clickable(("link text", text)))
            link_li_text = self.driver.find_element("link text", text)
            link_li_text.click()
            self.driver.implicitly_wait(50)                

            # Encontrar los elementos de descarga de boletas y Hacer clic en el icon
            # Leer y capturar web table  --------->>>>
            try:
                caption_table = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#grillaFacturacionHistorica_wrapper > div:nth-child(2) > div')))
                print('caption_table', caption_table)
                print('----------------------------------------------------------------------')
                body_table = caption_table.find_element("xpath", "//tbody")
                self.driver.implicitly_wait(50)
            except:
                self.driver.refresh()
                print('Web table...')
                pass
            
            # Leer y capturar TR web table
            try:
                body_rows = body_table.find_elements("xpath", "//tr")
                print('Body Lineas: ', len(body_rows))
                print('----------------------------------------------------------------------')
                self.driver.implicitly_wait(50)
            except:
                self.driver.refresh()
                print('TR web table...')
                pass
                
            self.driver.implicitly_wait(50)

            # Encontrar el elemento <select> por su nombre
            intentos = 0
            reintentar = True
            while (reintentar):
                try:
                    print('Try en la funcion Select para el campo cantidad de facturas...', intentos)
                    print('----------------------------------------------------------------------')
                    intentos += 1
                    self.wait(20).until(EC.presence_of_element_located((By.NAME, "grillaFacturacionHistorica_length")))
                    self.wait(20).until(EC.element_to_be_clickable((By.NAME, "grillaFacturacionHistorica_length")))
                    select_element = Select(self.driver.find_element(By.NAME, "grillaFacturacionHistorica_length"))
                    
                    # Selecciona la última opción de la lista
                    select_element.select_by_value("100")
                    self.driver.implicitly_wait(35)

                    reintentar = False
                except Exception as e:    
                    print('Exception en la funcion click_element_xpath', e)
                    print('----------------------------------------------------------------------')
                    reintentar = intentos <= 3

            # Encontrar los elementos de descarga de boletas
            intentos = 0
            reintentar = True
            while (reintentar):
                try:
                    print('Try en la funcion cargar Grilla de facturas...', intentos)
                    print('----------------------------------------------------------------------')
                    intentos += 1
                    #self.driver.implicitly_wait(50)
                    elementos_descarga = WebDriverWait(self.driver, 50).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#grillaFacturacionHistorica tbody tr")))
                    print('Elementos a descargar: ', elementos_descarga)
                    #elementos_descarga = self.driver.find_elements(By.CSS_SELECTOR, '#grillaFacturacionHistorica tbody tr')
                    self.driver.implicitly_wait(50)
                    if len(elementos_descarga) > 0:
                        reintentar = False
                        
                except Exception as e:    
                    print('Exception en la funcion cargar Grilla de facturas', e)
                    print('----------------------------------------------------------------------')
                    reintentar = intentos <= 3

            # Iterar sobre los elementos y descargar las boletas
            self.driver.implicitly_wait(50)
            file_row = []
            for elemento in elementos_descarga:
                print('Elemento...', elemento)
                print('----------------------------------------------------------------------')
                try:
                    WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[onclick^="ver_detalle"] a')))                
                    WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[onclick^="ver_detalle"] a')))
                    elemento.find_element(By.CSS_SELECTOR, 'span[onclick^="ver_detalle"] a')
                    self.driver.implicitly_wait(50)                
                    data_text = str(elemento.text.encode("utf8"), 'utf-8')
                    print('Agregar data_essbio_text: ', data_text)

                    split_data_text = [i for j in data_text.split() for i in (j, ' ')][:-1]
                    for data_split in split_data_text:
                        if data_split != " ":
                            file_row.append(data_split)
                    time.sleep(5)  # Esperar unos segundos para que se descargue el archivo
                    
                    number_bill = []
                    for i in range(3, len(file_row), 4):
                        elemento = file_row[i]
                        number_bill.append(elemento)
                
                except Exception as e:    
                    print('Exception en la funcion Iterar sobre los elementos y descargar las boletas', e)
                    print('----------------------------------------------------------------------')
                    reintentar = intentos <= 3

            print('Resultado: ', number_bill)
            print('----------------------------------------------------------------------')

            # Leer y capturar TD web table
            try:
                for row in body_rows:
                    
                    span_elements = row.find_elements("xpath", "//span[contains(@onclick, 'ver_detalle')]")
                    print('Contenido Linea Data: ', row)
                    print('----------------------------------------------------------------------')
                    print('Data: ', len(span_elements))
                    print('----------------------------------------------------------------------')
                    self.driver.implicitly_wait(35)
                    
                    file_row_download = []
                    for data_essbio in span_elements:
                        print('Agregar data_essbio_text: ', data_essbio)
                        file_row_download.append(data_essbio)
                    
                    time.sleep(5)            
                    break

                print('Resultado: ', file_row_download)
                print('----------------------------------------------------------------------')
                        
            except:
                self.driver.refresh()
                print('TD web table...')
                pass
            
            # Iterar sobre los elementos y hacer clic en el ícono de descarga
            count = 0
            for span in file_row_download:

                # Obtiene el identificador de la ventana actual
                current_window = self.driver.current_window_handle
                print('Ventana principal: ', current_window)
                print('----------------------------------------------------------------------')

                print('Click to Download: ', span)
                print('----------------------------------------------------------------------')
                span.click()
                time.sleep(60) #espera para que cargue ventana emergente

                # Esperar a que se abra la ventana emergente
                intentos = 0
                reintentar = True
                while (reintentar):
                    try:
                        print('Try en la funcion manejo de ventanas abiertas...', intentos)
                        print('----------------------------------------------------------------------')
                        intentos += 1
                        window_handles_all = self.driver.window_handles
                        self.wait(50).until(EC.number_of_windows_to_be(2))
                        self.driver.implicitly_wait(50)

                        reintentar = False
                    except Exception as e:    
                        print('Exception en la funcion manejo de ventanas abiertas', e)
                        print('----------------------------------------------------------------------')
                        print('Click to Download Againt: ', span)
                        print('----------------------------------------------------------------------')
                        span.click()
                        time.sleep(60) #espera para que cargue ventana emergente
                        
                        reintentar = intentos <= 3
                        
                # Obtiene los identificadores de las ventanas abiertas
                #window_handles_all = self.driver.window_handles
                self.driver.implicitly_wait(35)
                print('Ventanas abiertas: ', window_handles_all, len(window_handles_all))
                print('----------------------------------------------------------------------')            
                        
                # Cambiar al manejo de la ventana emergente
                for window_handle in window_handles_all:
                    if window_handle != current_window:
                        self.driver.switch_to.window(window_handle)
                        print('Ventana emergente: ', window_handle)
                        print('----------------------------------------------------------------------')
                        break

                # Esperar hasta que el elemento esté presente en la página
                self.driver.implicitly_wait(35)
                
                try:
                    # Obtener la URL de la ventana emergente
                    ventana_emergente_url = self.driver.current_url
                    print("URL de la ventana emergente:", ventana_emergente_url)
                    print('----------------------------------------------------------------------')

                    # Realizar una solicitud GET para obtener la data binaria del documento
                    response = requests.get(ventana_emergente_url, stream=True)

                    # Obtener el nombre del archivo a partir de los datos del proceso de descarga
                    folder_path = './input/'
                    file_name = folder_path + str(list_client[x])+"_"+str(number_bill[count])+".pdf" 

                    # Guardar la data binaria en un archivo PDF
                    with open(file_name, 'wb') as file:
                        response.raw.decode_content = True
                        shutil.copyfileobj(response.raw, file)
                        print("Guardando archivo:", file_name)
                        print('----------------------------------------------------------------------')
                        
                except Exception as e:    
                    print("No se encontró el elemento con el id especificado...", e)
                    print('----------------------------------------------------------------------')
                    
                count += 1
                print('Conteo de documentos: ', count)
                print('----------------------------------------------------------------------')                

                # Cerrar la ventana emergente
                self.driver.close()
                time.sleep(50)                            

                # Cambiar de nuevo al manejo de ventana principal
                self.driver.switch_to.window(current_window)
                print('Cual ventana es: ', current_window)
                print('----------------------------------------------------------------------')
            
            time.sleep(45)            
            
            # Seleccionar campo seleccione servicio
            self.wait(10).until(EC.presence_of_element_located((By.XPATH, selector_seleccione_servicio)))
            self.wait(10).until(EC.element_to_be_clickable((By.XPATH, selector_seleccione_servicio)))
            element_seleccione_servicio = self.driver.find_element(By.XPATH, selector_seleccione_servicio)
            element_seleccione_servicio.click()
            self.driver.implicitly_wait(20)

        time.sleep(20)
    
    def upload(self):
        print('Entrando en la funcion upload...')
        print('----------------------------------------------------------------------')
    
        # Obtener en una lista todos los archivos 
        folder_path = './input/'