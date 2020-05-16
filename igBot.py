from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password 
        self.driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha = driver.find_element_by_xpath("//button[@type='submit']")
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(3)
    
    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comenta_na_foto(self):
        driver = self.driver
        driver.get("https://www.instagram.com/p/B7zKs_wBMV-/?utm_source=ig_web_copy_link")
        try:
            comentarios = ["Quem viu", "essa mensagem", "me manda eu", "no direct"]
            driver.find_element_by_class_name("Ypffh").click()
            comment_input_box = driver.find_element_by_class_name("Ypffh")
            time.sleep(random.randint(2, 6))
            self.digite_como_uma_pessoa(random.choice(comentarios), comment_input_box)
            time.sleep(random.randint(3, 6))
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            time.sleep(random.randint(24,47))
        except Exception as e:
            print(e)
            time.sleep(5)

schilinBot = instagramBot("username", "password")
schilinBot.login()


i = 1
while 1 > 0:
    schilinBot.comenta_na_foto()
    print(i)
    i += 1
    