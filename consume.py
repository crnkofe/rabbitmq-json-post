import pika
import logging

logging.basicConfig(level=logging.INFO)

connection = pika.BlockingConnection()
channel = connection.channel()

try:
	# Get ten messages and break out
	for method_frame, properties, body in channel.consume('test'):
		# Display the message parts
		logging.info(method_frame)
    	logging.info(properties)
    	logging.info(body)

    	# Acknowledge the message
    	channel.basic_ack(method_frame.delivery_tag)

	# Cancel the consumer and return any pending messages
	requeued_messages = channel.cancel()
except KeyboardInterrupt:
	logging.info("Stopping by user request.")
except:
	logging.exception("Failed to consume messages.")
finally:
	# Close the channel and the connection
	channel.close()
	connection.close()
