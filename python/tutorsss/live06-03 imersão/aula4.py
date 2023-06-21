#usa yfinance pra conseguir uma base(e trata ela) e cria uma previsão de dados com um modelo de dados
#rodar no jupyter amr, pfv, nn tem espaço aqui
from fcts2 import endCode 
import yfinance as yf 
from prophet import Prophet 
from prophet.plot import plot_plotly #conexão entre packages
ticker = "PETR4.SA"
acoes = yf.Ticker(ticker).history("1mo") #historico de ticker de 1mo

dados = acoes.reset_index()
treinamento = dados[['Date', 'Close']] #extrair 2 colunas
treinamento['Date'] = treinamento['Date'].dt.tz_localize(None) #.date and .timezone is substituted by (arg)
treinamento.columns = ['ds', 'y'] #especifico dc, y
print(treinamento)

#prophet:modelo de dado do face (import linha3)
modelo = Prophet()
modelo.fit(treinamento)
periodo = modelo.make_future_fataframe(180)
print(periodo)




endCode()