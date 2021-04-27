from kafka import KafkaConsumer
from sp_datetime import get_datetime_sp

consumer = KafkaConsumer('timer_started', auto_offset_reset='latest',
                         bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)

def start_timer():
    print("Timer will be initialize")
    start_time = get_datetime_sp()
    print("Timer initialized successfully")
    print("faz de conta que escrevi no banco a hora que começou")
    arquivo = open('tabela_start.txt','w')
    arquivo.write(str(start_time))
    arquivo.close()
    return start_time

while 1 == 1:
    for msg in consumer:
        initial_time = start_timer()





