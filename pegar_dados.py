
from rastreio import Rastreador
import sys

if(sys.argv[1] != "-ip"):
  print("Erro ")

elif sys.argv[2] == "":

  print ("Erro")

else:
 c = Rastreador(sys.argv[2])
 print("IP:",c.get_ip())
 print("CONTINENTE:",c.get_continente())
 print("PAIS ",c.get_pais())
 print("REGIÃO:",c.get_regiao())
 print("CIDADE:",c.get_cidade())
 print("LATITUDE:",c.get_latitude())
 print("LONGITUDE:",c.get_longitude())
 print("CAPITAL:",c.get_capital())
 print("EMOJI:",c.get_emoji())
 print("ORGANIZAÇÃO:",c.get_organizacao())
 print("DOMINIO:",c.get_dominio())
