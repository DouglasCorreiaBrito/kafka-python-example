from datetime import datetime
from kafka import KafkaConsumer
from sp_datetime import get_datetime_sp

consumer = KafkaConsumer('timer_now', auto_offset_reset='latest',
                         bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)

def timer_now():
    now_time = get_datetime_sp()
    initial_time = 0
    arquivo = open('tabela_start.txt','r')

    with open('tabela_start.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        print(last_line)
        initial_time = datetime.fromisoformat(last_line)
    arquivo.close()

    arquivo2 = open('tabela_now.txt','w')
    arquivo2.write(str(now_time() - initial_time))
    arquivo2.close()
    print("faz de conta que escrevi no banco o quanto tempo passou")

while 1 == 1:
    for msg in consumer:
        initial_time = timer_now()





