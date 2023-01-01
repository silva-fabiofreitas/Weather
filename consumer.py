import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='climate')

def callback(ch, method, properties, body):
        print("[x] received %r" %body)

channel.basic_consume(queue='climate', on_message_callback=callback, auto_ack=True)

print(" [*] waiting for the messages. To exit press Ctrl-C")

channel.start_consuming()

channel.close()

