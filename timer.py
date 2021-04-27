import producer
from sp_datetime import get_datetime_sp


def start_timer(instance_kafka):
    print("Timer will be initialize")
    start_time = get_datetime_sp()
    producer.publish_message(instance_kafka, "timer_started", "this is a key: {}".format(
        start_time), "this is a value: {}".format(start_time))
    print("Timer initialized successfully")
    return start_time


def timer_now(instance_kafka, time_lapsed_in_sec):
    msg = time_lapsed_in_sec
    producer.publish_message(instance_kafka, "timer_now", msg, msg)


def stop_timer(instance_kafka, start_time):
    print("Timer will be stop")
    end_time = get_datetime_sp()
    time_lapsed = end_time - start_time
    producer.publish_message(instance_kafka, "timer_stopped", "this is a key: {}".format(
        end_time), "this is a value: {}".format(end_time))
    print("Timer stopped successfully")
    return time_lapsed


def print_open_msg():
    print("*********************************")
    print("******Controle de Cronômetro*****")
    print("*********************************")
    print("What should I do")
    print("1-start timer / 2-stop timer / 3-get time")


if __name__ == "__main__":

    opc = 0
    broker = producer.connect_kafka_producer()
    print_open_msg()
    initial_time = 0
    end_time = 0
    while opc != 9:
        opc = int(input("choose... "))

        if opc == 1:
            if initial_time == 0:
                initial_time = start_timer(broker)
            else:
                print("timer already started")

        if opc == 2:
            print(end_time)
            if initial_time != 0 and (not bool(end_time) or end_time == 0):
                end_time = stop_timer(broker, initial_time)
                initial_time = 0
                end_time = 0
            else:
                print("timer already stopped")

        if opc == 3:
            if initial_time != 0:
                now = timer_now(broker, get_datetime_sp() - initial_time)
            else:
                print("timer not yet started")
