import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		numero = int(ui.dialog1())
		r = requests.get(url='https://consulta-numero.p.rapidapi.com/apis/astrahvhdeus/Consultas%20Privadas/HTML/numero.php', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36','x-rapidapi-key':'9353b1d886msh73e7a0771d6600dp14ec4cjsn883fd8b4cf13','x-rapidapi-host': 'consulta-numero.p.rapidapi.com'}, params={'consulta': numero}).text
		if 'A Consulta Esta Funcionando Normalmente' in r:
			msg='A consulta está funcionando normalmente, porém, o Telefone inserido não foi encontrado.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n').replace('DDD:', 'DDD: ').replace('NOME:', 'Nome completo: ').replace('FONE:', 'Telefone: ').replace('INST:', 'Data de Compra: ').replace('PESSOA:', 'Pessoa: ').replace('CPF:', 'CPF: ').replace('PESSOA:', 'Pessoa: ')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()
