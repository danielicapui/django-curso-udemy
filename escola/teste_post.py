import requests
headers={'Authorization':'Token f5aec91588315d1fe902f726b77d0bc5ef9ea3eb'}

url_base_cursos='http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes='http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso={
    "titulo":"Criação de yuki",
    "url":"https://www.yuki.com.br"
}

resultado=requests.post(url=url_base_cursos,headers=headers,data=novo_curso)
#verificando se criou o curso
assert resultado.status_code==201
#print(resultado.json())

#verificando se os dados do curso enviado são o mesmo que o criado
assert resultado.json()['titulo']==novo_curso['titulo']
print("Nenhum problema encontrado!")