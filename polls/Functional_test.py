from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):
    def setUp(self):
       self.browser = webdriver.Chrome("D:/Universidad/Procesos Agiles/chromedriver.exe")

    def tearDown(self):
        self.browser.quit()
    ##test titulo
    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Busco Ayuda', self.browser.title)

        ##test registro independiente
    def test_registro(self):
        self.browser.get('http://127.0.0.1:8000/')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(10)
        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('D:/Universidad/Procesos Agiles/desarrollador.jpg')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    #test  ver el desalle
    def test_verDetalle(self):
        self.browser.get('http://127.0.0.1:8000/')
        span=self.browser.find_element(By.XPATH,'//span[text()="Juan Daniel Arevalo"]')
        span.click()
        h2=self.browser.find_element(By.XPATH,'//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo',h2.text)

    #test Login
    def test_login(self):
        self.browser.get('http://localhost:8000')
        #buscando el boton login
        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()
        self.browser.implicitly_wait(10)
        #esperando que la pagina abra
        self.browser.implicitly_wait(10)
        #llenando datos del usuario creado
        usuario = self.browser.find_element_by_id("id_username")
        usuario.send_keys('juan645')
        contrasena = self.browser.find_element_by_id("id_password")
        contrasena.send_keys('clave123')
        ingresar = self.browser.find_element_by_id('id_send')
        ingresar.click()
        #esperando que el inicio abra
        self.browser.implicitly_wait(10)
        respuesta= self.browser.find_element_by_class_name('float-message').text
        self.assertTrue(respuesta.index('SUCCESS: Bienvenido al sistema juan645'))

    #test editar
    def test_editar(self):
        self.browser.get('http://localhost:8000')
        # buscando el boton login
        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()
        self.browser.implicitly_wait(10)
        #se realiza login
        usuario = self.browser.find_element_by_id("id_username")
        usuario.send_keys('juan645')
        contrasena = self.browser.find_element_by_id("id_password")
        contrasena.send_keys('clave123')
        ingresar = self.browser.find_element_by_id('id_send')
        ingresar.click()

        self.browser.implicitly_wait(10)
        linkEditar = self.browser.find_element_by_id('id_editar')
        #Se hace click para editar
        linkEditar.click()

        #Edicion de datos
        self.browser.implicitly_wait(10)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.clear()
        nombre.send_keys('Chuck')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Norris')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(10)

        linkEditar = self.browser.find_element_by_id('id_editar')
        linkEditar.click()

        self.browser.implicitly_wait(10)

        nombre = self.browser.find_element_by_id('id_nombre')
        self.assertEqual(nombre.get_attribute("value"),'Chuck')
        apellidos = self.browser.find_element_by_id('id_apellidos')
        self.assertEqual(apellidos.get_attribute("value"), 'Norris')

    #test_comentar
    def test_comentario(self):
        self.browser.get('http://127.0.0.1:8000/')
        linkUsuario = self.browser.find_element(By.XPATH, '//span[text()="Chuck Norris"]')
        linkUsuario.click()

        self.browser.implicitly_wait(10)

        email = self.browser.find_element_by_id('correo')
        email.send_keys('chuck.norris@google.com')

        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('comentario de prueba')

        self.browser.implicitly_wait(20)

        linkUsuario = self.browser.find_element_by_id('id_agregarComentario')
        linkUsuario.click()

        self.browser.implicitly_wait(20)

        for option in self.browser.find_element_by_id('comentarios').find_elements_by_tag_name('h4'):
            if option.text.index('chuck.norris@google.com'):
                self.assertTrue(self.browser.find_element_by_id('comentarios').find_elements_by_tag_name('p')[option.text.index])



