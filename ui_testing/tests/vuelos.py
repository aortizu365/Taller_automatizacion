import time
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class VuelosTest(unittest.TestCase):
    def init_driver(self):
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/alex-/PycharmProjects/taller/ui_testing/drivers/chromedriver.exe')
        self.driver.maximize_window()

    # Este método recibe como parámetro la URL del sitio
    def test_go_url(self, url):
        self.driver.get(url)

    def test_login(self, user, password):
        self.driver.find_element_by_name("userName").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("login").click()

    def test_seleccionar_one_way(self):
        self.driver.find_element_by_css_selector("font:nth-child(1) > input:nth-child(2)").click()

    def test_numero_pasajeros(self, numero):
        self.select("passCount", numero)

    def test_seleccionar_partida(self, partida):
        self.select("fromPort", partida)

    def test_seleccionar_fecha_partida(self, mes, dia):
        self.select("fromMonth", mes)
        self.select("fromDay", dia)

    def test_seleccionar_llegada(self, llegada):
        self.select("toPort", llegada)

    def test_seleccionar_fecha_retorno(self, mes, dia):
        self.select("toMonth", mes)
        self.select("toDay", dia)

    def test_seleccionar_clase(self):
        self.driver.find_element_by_css_selector("font:nth-child(2) > input:nth-child(2)").click()

    def test_seleccionar_aerolinea(self, aerolinea):
        self.select("airline", aerolinea)

    def test_enviar_formulario(self):
        self.driver.find_element_by_name("findFlights").click()
        time.sleep(2)

    def test_ida_costoso(self):
        self.driver.find_element_by_css_selector("table:nth-child(9) tr:nth-child(9) input").click()

    def test_retorno_costoso(self):
        self.driver.find_element_by_css_selector("table:nth-child(10) tr:nth-child(9) input").click()

    def test_enviar_seleccion(self):
        self.driver.find_element_by_name("reserveFlights").click()
        time.sleep(2)

    def test_pasajero_numero(self, numero, nombre, apellido, comida):
        num = int(numero) - 1
        self.driver.find_element_by_name("passFirst" + str(num)).send_keys(nombre)
        self.driver.find_element_by_name("passLast" + str(num)).send_keys(apellido)
        self.select("pass." + str(num) + ".meal", comida)

    def test_tarjeta_tipo(self, tipo):
        self.select("creditCard", tipo)

    def test_tarjeta_numero(self, numero):
        self.driver.find_element_by_name("creditnumber").send_keys(numero)

    def test_tarjeta_fecha(self, mes, year):
        self.select("cc_exp_dt_mn", mes)
        self.select("cc_exp_dt_yr", year)

    def test_tarjeta_nombre(self, nombre, apellido):
        self.driver.find_element_by_name("cc_frst_name").send_keys(nombre)
        self.driver.find_element_by_name("cc_last_name").send_keys(apellido)

    def test_direccion_facturacion(self, direccion):
        self.driver.find_element_by_name("billAddress1").send_keys(direccion)

    def test_ciudad_facturacion(self, ciudad):
        self.driver.find_element_by_name("billCity").send_keys(ciudad)

    def test_estado_facturacion(self, estado):
        self.driver.find_element_by_name("billState").send_keys(estado)

    def test_codigo_postal_facturacion(self, codigo):
        self.driver.find_element_by_name("billZip").send_keys(codigo)

    def test_pais_facturacion(self, pais):
        self.select("delCountry", pais)

    def test_entrega(self):
        self.driver.find_element_by_css_selector("tr:nth-child(14) input").click()

    def test_enviar_datos(self):
        self.driver.find_element_by_name("buyFlights").click()

    def test_validar_reserva(self):
        elem = self.driver.find_element_by_css_selector("td:nth-child(1) tr:nth-child(1) > td:nth-child(1) > img:nth-child(1)")
        self.assertTrue(elem)

    def test_pagina_resultados_busqueda_vuelos(self):
        elem = self.driver.find_element_by_name("reserveFlights")
        self.assertTrue(elem)

    def test_pagina_ida_vuelta(self):
        elem = self.driver.find_element_by_name("buyFlights")
        self.assertTrue(elem)

    def close(self):
        self.driver.quit()
        print("prueba completada con éxito")

    def select(self, id, valor):
        elem = self.driver.find_element_by_name(id)
        dropdown = Select(elem)
        dropdown.select_by_visible_text(valor)

if __name__ == '__main__':
    unittest.main()
