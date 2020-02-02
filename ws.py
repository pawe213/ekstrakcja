import json
import requests


response = requests.get("https://api-v3.mojepanstwo.pl/dane/poslowie.json?conditions[poslowie.kadencja]=8")
politicy = response.json()['Links']

a = politicy[0]['data'].keys()  #['poslowie.liczba_glosowan_opuszczonych']

def printLazyPolitics(absent_voting_limit: int):
    response = requests.get("https://api-v3.mojepanstwo.pl/dane/poslowie.json?conditions[poslowie.kadencja]=8")
    next_page = response.json()['Links'].get('next', False)

    while next_page:
        politicy = response.json()['Dataobject']
        for polityk in politicy:
            dane_posla = polityk['data']
            if dane_posla['poslowie.liczba_glosowan_opuszczonych'] >= absent_voting_limit:
                print(dane_posla['ludzie.nazwa'] + '  ' +
                    str(dane_posla['poslowie.liczba_glosowan_opuszczonych']))



        response = requests.get(next_page)
        next_page = response.json()['Links'].get('next', False)

printLazyPolitics(30)