import os, sys
def restart():
	python=sys.executable;os.excl(python, python, *sys.argv)
try:
	import colorama, requests
except:
	os.system('pip install -r requirements.txt');restart()
try:
	from data import ui, numero, cpf, nome, rg, email, cpnj, cep1, cep2
except Exception as e:
	print('ARQUIVO CORROMPIDO! '+str(e));exit()
C= "\033[97;1m"
G = "\033[92;1m"
P = "\033[1;35m"
Sair=False
while(Sair==False):
	try:
		op=int(ui.menu(ms0=f'\n{C}[{G}1{C}] Numero\n{C}[{G}2{C}] CPF\n{C}[{G}3{C}] Nome\n{C}[{G}4{C}] CEP\n{C}[{G}5{C}] RG\n{C}[{G}6{C}] Email\n{C}[{G}7{C}] CNPJ\n\n{C}[{P}0{C}] Sair'))
		if op==1:
			numero.consultar()
		elif op==2:
			cpf.consultar()
		elif op==3:
			nome.consultar()
		elif op==4:
			op2=int(ui.menu(ms0=f'\n{C}[{G}1{C}] CEP 1\n{C}[{G}2{C}] CEP 2'))
			if op2==1:
				cep1.consultar()
			elif op2==2:
				cep2.consultar()
		elif op==5:
			rg.consultar()
		elif op==6:
			email.consultar()
		elif op==7:
			cnpj.consultar()
		elif op==0:
			ui.clear();Sair=True
	except:
		ui.error()
