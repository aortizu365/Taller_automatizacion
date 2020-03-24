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
        elem = self.driver.find_element_by_name("passCount")
        dropdown = Select(elem)
        dropdown.select_by_value(numero)


    def test_seleccionar_partida(self, partida):
        elem = self.driver.find_element_by_name("fromPort")
        dropdown = Select(elem)
        dropdown.select_by_value(partida)

    def test_seleccionar_fecha_partida(self, mes, dia):
        elem_mes = self.driver.find_element_by_name("fromMonth")
        dropdown = Select(elem_mes)
        dropdown.select_by_visible_text(mes)
        elem_dia = self.driver.find_element_by_name("fromDay")
        dropdown = Select(elem_dia)
        dropdown.select_by_value(dia)

    def test_seleccionar_llegada(self, llegada):
        elem = self.driver.find_element_by_name("toPort")
        dropdown = Select(elem)
        dropdown.select_by_value(llegada)

    def test_seleccionar_fecha_retorno(self, mes, dia):
        elem_mes = self.driver.find_element_by_name("toMonth")
        dropdown = Select(elem_mes)
        dropdown.select_by_visible_text(mes)
        elem_dia = self.driver.find_element_by_name("toDay")
        dropdown = Select(elem_dia)
        dropdown.select_by_value(dia)

    def test_seleccionar_clase(self):
        self.driver.find_element_by_css_selector("font:nth-child(2) > input:nth-child(2)").click()

    def test_seleccionar_aerolinea(self, aerolinea):
        elem = self.driver.find_element_by_name("airline")
        dropdown = Select(elem)
        dropdown.select_by_visible_text(aerolinea)

    def test_enviar_formulario(self):
        self.driver.find_element_by_name("findFlights").click()
        time.sleep(2)

    def test_validar_respuesta(self):
        elem = self.driver.find_element_by_name("results")
        self.assertTrue(elem)

    def close(self):
        self.driver.quit()
        print("prueba completada con éxito")


if __name__ == '__main__':
    unittest.main()
