import pika
import json
students_names = json.dumps({
    'student1': 'Qusai',
    'student2': 'Cando',
    'student3': 'Amer',
    'student4': 'Fadi',
    'student5': 'Zataar'
})

teachers_names = json.dumps({
    'teacher1': 'Selim',
    'teacher2': 'Serkan',
    'teacher3': 'Seda',
    'teacher4': 'Taha',
    'teacher5': 'Mustafa'
})

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.queue_declare('students_names')
channel.queue_declare('teachers_names')

channel.basic_publish(exchange='', routing_key='students_names', body=students_names)
channel.basic_publish(exchange='', routing_key='teachers_names', body=teachers_names)

print("Teachers names and students names have been sent!")
connection.close()