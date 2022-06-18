from core.celery import app
from orders.services import GoogleSheetService


@app.task
def set_orders():
    """

    Запускаю set_values() метод внутри класса GoogleSheetService
    подробнее об set_values() можете прочитать внутри класса GoogleSheetService.set_values()

    """
    GoogleSheetService().set_values()
