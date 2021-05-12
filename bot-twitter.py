import tweepy
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

#Autenticação das chaves do Twitter
auth = tweepy.OAuthHandler('L1W4qofW067CnFs2fp4BCBbfB', 'BYyatvVoIPLtVvoPAQQQSmNiVDXUrlMy67wGvOsLnxFR613dqS')
auth.set_access_token('1391083748679200770-qDeQdjDcWcIDANPoBsJ3j7SIHYDH3N', 'iTMJZFy51jstHMV6zLXIa8EW46upIMJo5EzrLDUHhWeFv')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
nDeTweets = 30

#Requisição dos dados do governo
res = requests.get('https://vacinaja.sp.gov.br')

#Pegando os itens do HTML
soup = BeautifulSoup(res.text, 'html.parser')
doses_total = soup.findAll('div', {'class': 'pane'})
dose =  soup.findAll('p', {'class': 'vac-doses'})
total_doses = doses_total[0].text.strip()
dose1 = dose[0].text.strip()
dose2 = dose[1].text.strip()

#Formatação de data e hora
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

#Formatação do texto
sp = ('⚪⚫ Vacinação em São Paulo: \n' + \
      'Total de doses aplicadas: ' + total_doses + "\n"
      'Primeira dose: '+ dose1 + "\n"
      'Segunda dose: '+ dose2 + '\n' +  data_e_hora_em_texto )


#Validação da requisição
if res:
  print("Buscando dados")
  for tweet in tweepy.Cursor(api.user_timeline).items(nDeTweets):
    try:
      api.update_status(status = sp)
      print("Enviado")
      time.sleep(700)
      print("Dormindo") 
    except tweepy.TweepError as e:
      print(e.reason)
      print(res)
    except StopIteration:  
      break
else:
  print("Erro na requisição")
  print(res)                                                               