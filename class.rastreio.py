#rastreador.py
#Criado por Vicente Victor Sombo
#Data 15-11-2022

import requests

class Rastreador:

    def __init__(self,ip):
       self.ip = ip
       data = requests.get("http://ipwho.is/"+self.ip)
       json = data.json()
       self.ipret = json["ip"]
       self.continente = json["continent"]
       self.pais = json["country"]
       self.regiao = json["region"]
       self.cidade = json["city"]
       self.latitude = json["latitude"]
       self.longitude = json["longitude"]
       self.capital = json["capital"]
       self.bandeira = json["flag"]["emoji"]
       self.organizacao = json["connection"]["org"]
       self.dominio = json["connection"]["domain"]
            
            
    def get_ip(self):
       return self.ipret

    def get_continente(self):
       return self.continente

    def get_pais(self):
       return self.pais

    def get_regiao(self):
       return self.regiao

    def get_cidade(self):
       return self.cidade
       
    def get_latitude(self):
       return self.latitude

    def get_longitude(self):
       return self.longitude

    def get_capital(self):
       return self.capital

    def get_organizacao(self):
       return self.organizacao

    def get_dominio(self):
       return self.dominio

    def get_emoji(self):
       return self.bandeira
