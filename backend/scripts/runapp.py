from orders.tasks import set_orders


def run():
    set_orders.delay()


