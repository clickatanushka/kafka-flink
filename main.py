from faker import Faker
from confluent_kafka import SerializingProducer
from datetime import datetime
import random
import time
import json

faker = Faker()

def generate_sales_transactions():
    user = faker.simple_profile()

    return {
        "transactionID": faker.uuid4(),
        "productID": random.choice(['product1','product2','product3','product4', 'product5','product6']),
        "productName": random.choice(['laptop','mobile','tablets','watch','headphones','speaker']),
        "productCategory": random.choice(['electronic', 'fashion', 'grocery', 'home', 'beauty', 'sports']),
        "productPrice": round(random.uniform(  10,1000),2),
        "productQuantity": random.randint(1,10),
        "productBrand": random.choice(['apple','smasung','oneplus','mi','boat','sony']),
        "currency": random.choice (['USD', 'GBP']),
        "customerID": user['username'],
        "transactionDate":   datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%F%z'),
        "paymentmethod": random.choice(['creditCard','debitCard','online'])
    }


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failes: {err}')
    else:
        print(f'Message Delivered to {msg.topic} [{msg.partition()}]')


def main():
    topic = 'financial_transactions'
    producer = SerializingProducer({
        'bootstrap.servers': 'localhost:9092'
    })

    curr_time = datetime.now()

    while((datetime.now() - curr_time).seconds) < 120:
        try:
            transaction = generate_sales_transactions()
            transaction['totalAmount'] = transaction['productPrice'] * transaction["productQuantity"]
            print(transaction)


            producer.produce(topic,
                            key=transaction['transactionID'],
                            value=json.dumps(transaction),
                            on_delivery= delivery_report
                            )
            
            producer.poll(0)
            
            time.sleep(5)


        except BufferError:
            print("Buffer full... waiting")
            time.sleep(1)
        except Exception as e:
            print(e)
            time.sleep(5)


if __name__ == "__main__":
    main()