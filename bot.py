import tweepy
import time

#Tokens do seu bot
#Eles são disponibilizados ao criar o bot
consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

#Autenticação do nosso bot
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

#Arquivo .txt para salvar o ultimo id respondido
FILE_NAME = 'ultimo_id.txt'

#Metodo para ler o ultimo id respondido
def read_last_id(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

#Metodo para salvar um novo ultimo id respondido
def store_last_id_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


#conjunto de palavras que vão ser buscadas
hashtag = ("")   #ex: ("Ai dentu"), para várias palavras é só separar por virgula ("Ai dentu", "fuleragi")

#Esse parametro serve para informar qual vai ser o tamanho da sua busca
#A cada X segundos ele vai buscar os ultimos 10 registros
#Caso o seu bot responsa a um termo muito usado, sugiro que vc aumente esse range de busca
tweetNumber = 10

#O metodo de busca
def search():
    tweets = tweepy.Cursor(api.search, hashtag, since_id=read_last_id(FILE_NAME)).items(tweetNumber)
    for tweet in tweets:
        try:
            print("Find: " +  str(tweet.id))
            
            #Aqui definimos a resposta que o Bot enviara
            api.update_status("@" + tweet.user.screen_name + " ieeeeeeeeeeeeeeeeeeeeei", tweet.id)
            store_last_id_seen(FILE_NAME, tweet.id)
            print("retweet")
        except tweepy.TweepError as e:
            print(e.reason)

#Abaixo temos o laço que será executado a cada 5 segundos
#Caso deseje aumentar ou diminuir a periodicidade, é só mudar o parametro da função sleep abaixo
while True:
    try:
        search()
    except:
        print("Deu erro")

    print("Running...")
    time.sleep(5)
