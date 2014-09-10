#!/usr/bin/env python
import pika
import logging

logging.basicConfig(level=logging.INFO)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()
try:
	channel.queue_declare(queue='test')
	logging.info("Publishing message.")
	channel.basic_publish(
		'',
		'test',
		'Hello World!',
		pika.BasicProperties(content_type='text/plain', delivery_mode=1))
except:
	logging.exception("Unable to communicate with RabbitMQ")
finally:
	channel.close()
	connection.close()
