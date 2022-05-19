import requests 

#GET Avaliações
avalicoes=requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')
#ver código de status
#print(avalicoes.status_code)

#dados da requisição
#print(avalicoes.json())

#GET Avaliação
avaliacao=requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/2/')
print(avaliacao.json())

#GET Cursos
headers={'Authorization':'Token f5aec91588315d1fe902f726b77d0bc5ef9ea3eb'}
cursos=requests.get(url='http://127.0.0.1:8000/api/v2/cursos/',headers=headers)
print(cursos.status_code)
print(cursos.json())

#GET Cursos
curso=requests.get('http://127.0.0.1:8000/api/v2/cursos/2/')