from re import M
from wsgiref import headers
import requests


url_base_avaliacoes='http://127.0.0.1:8000/api/v2/avaliacoes/'

class TestCursos:
    headers={'Authorization':'Token 0d89b122b7981575f6c9179aded018d27b1f7985'}
    url_base_cursos='http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos=requests.get(url=self.url_base_cursos,headers=self.headers)
        print(cursos.json())
        assert cursos.status_code==200
    def test_get_curso(self):
        curso=requests.get(url=f'{self.url_base_cursos}3/',headers=self.headers)
        assert curso.status_code==200
    def test_post_curso(self):
        novo_curso={
            "titulo":"Criação de Lole",
            "url":"https://www.lole.com"
        }
        resultado=requests.post(url=self.url_base_cursos,headers=self.headers,data=novo_curso)
        assert resultado.status_code==201
    def test_put_curso(self):
        curso_atualizado={
            "titulo":"Programando em GDScript",
            "url":"https://www.godot.com"
        }
        resultado=requests.put(url=f'{self.url_base_cursos}3/',headers=self.headers,data=curso_atualizado)
        assert resultado.status_code==200
    def test_put_titulo(self):
        curso_atualizado={
            "titulo":"Programando em Godot",
            "url":"https://www.godot1.com"
        }
        resultado=requests.put(url=f'{self.url_base_cursos}3/',headers=self.headers,data=curso_atualizado)
        assert curso_atualizado["titulo"]==resultado.json()['titulo']
    def test_delete_curso(self):
        resultado=requests.delete(url=f'{self.url_base_cursos}3/',headers=self.headers)
        assert resultado.status_code==204 and len(resultado.text)==0