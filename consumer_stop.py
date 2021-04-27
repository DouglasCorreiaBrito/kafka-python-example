from kafka import KafkaConsumer
from sp_datetime import get_datetime_sp

consumer = KafkaConsumer('timer_stopped', auto_offset_reset='latest',
                         bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)

def stop_timer():
    print("Timer will be stop")
    end_time = get_datetime_sp()
    print("Timer stopped successfully")
    print("faz de conta que escrevi no banco a hora que parou")
    arquivo = open('tabela_stop.txt','w')
    arquivo.write(str(end_time))
    arquivo.close()
    return end_time

while 1 == 1:
    for msg in consumer:
        initial_time = stop_timer()





