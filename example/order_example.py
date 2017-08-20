import sys

from accurate_bg_check.order import Order
from .client_example import client

payload = {
    'candidateId': '',  # use id which is return by candidate resource
    'packageType': 'PKG_STANDARD',
    'workflow': 'EXPRESS',
    'jobLocation': {
        'city': 'Burbank',
        "region": "CA",
        "country": "US"
    }
}

order = Order(client)

if __name__ == '__main__':
    len_sys_args = len(sys.argv)
    if len_sys_args < 2:
        raise Exception('Parameter missing')

    file, opr = sys.argv
    opr = int(opr)
    if opr == 1:
        order.create(payload)

    if opr == 2:
        order_list = order.list()
        print(order_list)
        print("total orders ", len(order_list))

    if opr == 3:
        order_id = ''  # use order id user that is return by order resource
        order_data = order.get(order_id)
        print('Order result ', order_data['result'])
