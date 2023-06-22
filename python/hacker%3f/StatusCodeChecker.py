#a code to check different connections with different URL prefixes.


from fcts2 import tspac, endCode
import requests as rq
#https://
mainAd = 'https://brasilescola.uol.com.br/'
#https://m.vestibular.brasilescola.uol.com.br/enem
sufix = ['disciplinas', 'images', 'admin', 'm.vestibular', 'enem' ]

for i in sufix:
    try:
        r = rq.get(mainAd + i)
        print(r.status_code)
        print("#####")
    except:
        print("no response")
        print("#####")
        
endCode()
