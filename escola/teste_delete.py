import requests
import sys
def test_delete(id):
    headers={'Authorization':'Token 0d89b122b7981575f6c9179aded018d27b1f7985'}
    url_base_cursos='http://127.0.0.1:8000/api/v2/cursos/'
    url_base_avaliacoes='http://127.0.0.1:8000/api/v2/avaliacoes/'
    resultado=requests.delete(url=f'{url_base_cursos}{id}/',headers=headers)
    #teste de resposta de deletar
    print(resultado.json())
    assert resultado.status_code==204
    #teste de retorno de contéudo
    assert len(resultado.text)==0
    print("DELETE:Nenhum problema encontrado!")
if __name__=='__main__':
    try:
        test_delete(sys.argv[1])
    except IndexError:
        test_delete(7)