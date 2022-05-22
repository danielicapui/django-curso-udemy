import requests
headers={'Authorization':'Token 0d89b122b7981575f6c9179aded018d27b1f7985'}

url_base_cursos='http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes='http://127.0.0.1:8000/api/v2/avaliacoes/'


curso_atualizado={
    "titulo":"Curso de Yuri 1",
    "url":"http://www.yuri.com",
}
#curso=requests.get(url=f'{url_base_cursos}6/',headers=headers)
#print(curso.json())

resultado=requests.put(url=f'{url_base_cursos}6/',headers=headers,data=curso_atualizado)
#print(resultado.json())
#teste de resposta
assert resultado.status_code==200
#teste de atualização
assert resultado.json()['titulo']==curso_atualizado['titulo']

print("Nenhum problema encontrado!")
