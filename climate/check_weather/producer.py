import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))



channel = connection.channel()
# channel.exchange_declare(exchange='climate', exchange_type='fanout')

def publish(body):
    channel.basic_publish(exchange='',
                          routing_key='climate',
                          body=body)

    print("[x] Sent Hello World")
    connection.close()