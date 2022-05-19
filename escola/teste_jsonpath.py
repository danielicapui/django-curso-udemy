import requests
import jsonpath

avaliacoes=requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

#resultados=jsonpath.jsonpath(avaliacoes.json(),'results')
#print(resultados)

#primeiro=jsonpath.jsonpath(avaliacoes.json(),'results[0]')
#print(primeiro)

#nome=jsonpath.jsonpath(avaliacoes.json(),'results[0].nome')
#print(nome)

#nomes das pessoas que avaliaram um curso
nomes=jsonpath.jsonpath(avaliacoes.json(),'results[*].nome')
print(nomes)
