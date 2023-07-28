import time
import pika

# def push_message(message):
#     time.sleep(2)
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#
#     channel.queue_declare(queue='task_finished_queue', durable=True)
#
#     channel.basic_publish(exchange='',
#                           routing_key='task_finished_queue',
#                           body=bytes(message),
#                           properties=pika.BasicProperties(
#                               delivery_mode=2,  # make message persistent
#                           ))
#     print(f" [x] Sent {message}")
#     connection.close()
#
#
# def consume_rabbitmq():
#     def callback(ch, method, properties, body):
#         task_id = body.decode()
#         print(f" [x] Received {task_id}")
#         time.sleep(body.count(b'.'))
#         print(" [x] Done")
#         ch.basic_ack(delivery_tag=method.delivery_tag)
#
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#
#     channel.queue_declare(queue='task_queue', durable=True)
#     print(' [*] Waiting for messages. To exit press CTRL+C')
#
#     channel.basic_qos(prefetch_count=1)
#     channel.basic_consume(queue='task_queue', on_message_callback=callback)
#
#     channel.start_consuming()
