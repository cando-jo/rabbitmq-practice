import pika
import json

def on_message_received(ch, method, properties, body):
    message_body = body.decode('utf-8')
    data = json.loads(message_body)
    print(f'Recieved this: {data}')
    
connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='students_names')
channel.queue_declare(queue='teachers_names')
channel.basic_consume(queue='students_names', auto_ack=True, on_message_callback=on_message_received)
channel.basic_consume(queue='teachers_names', auto_ack=True, on_message_callback=on_message_received)


print("Starting consuming, to exit click CTRL C")
channel.start_consuming()