from reportlab.platypus import SimpleDocTemplate,Paragraph
import time
import datetime as dt
def gerar_pdf():
    doc=SimpleDocTemplate("declaracao.pdf")
    nome="Daniel Lucas dos Reis Silva"
    id="071.976.023-27"
    validade=dt.datetime.strptime("45","%d %m %y")
    print(validade)
    data_atual=time.strftime("%d-%m-%Y",time.localtime())
    print(data_atual)
    data_ingresso=data_atual
    data_vencimento=time.strftime("d-%m-%Y",time.localtime()+validade)
    p1=f"<font size='12'><strong>Por meio do presente documento, a Secretaria de Desenvolvimento Rural e da Agricultura Familiar-SEDRAF certifica que o usuário de nome {nome} , identificação {id} possuí cadastro no siraf ativo, ingressando na {str(data_ingresso)}.<br></br>Documento gerado por processo automatizado em {str(data_atual)}Valido até a {str(date_expiration)}</strong></font>"
    info=[]
    info.append(Paragraph(p1))
    doc.build(info)
    return doc
if __name__=='__main__':
    gerar_pdf()