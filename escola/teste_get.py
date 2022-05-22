import requests
import sys

def teste_get(id=None):
    headers={'Authorization':'Token f5aec91588315d1fe902f726b77d0bc5ef9ea3eb'}

    url_base_cursos='http://127.0.0.1:8000/api/v2/cursos/'
    url_base_avaliacoes='http://127.0.0.1:8000/api/v2/avaliacoes/'
    resultado=requests.get(url=url_base_cursos,headers=headers)
    if id:
        curso=requests.get(url=f'{url_base_cursos}{id}/',headers=headers)
        print(curso.json())
    print("Resultados dos cursos----------------------")
    print(resultado.json())
    #testando se requisição está correta
    assert resultado.status_code==200

    #testando a quantidade de registros
    #assert resultado.json()['count']==4

    #testando o título do primeiro elemento
    assert resultado.json()['results'][0]['titulo']=='Crie APIs REST com Python e Django REST Framework: Essencial'

if __name__=='__main__':
    try:
        teste_get(sys.argv[1])
    except IndexError:
        teste_get()