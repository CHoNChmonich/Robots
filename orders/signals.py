from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from robots.models import Robot
from orders.models import Order

@receiver(post_save, sender=Robot)
def notify_customers_on_robot_availability(sender, instance, **kwargs):
    # Получаем все заказы, связанные с роботами той же модели и версии, которые еще не уведомлены
    pending_orders = Order.objects.filter(
        robot_serial=instance.serial,
    )

    for order in pending_orders:
        # Получаем email клиента
        customer_email = order.customer.email

        # Отправка письма клиенту
        send_mail(
            subject="Ваш робот теперь в наличии!",
            message=(
                f"Добрый день!\n"
                f"Недавно вы интересовались нашим роботом с серийным номером {order.robot_serial}.\n"
                f"Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
            ),
            from_email="noreply@yourcompany.com",  # Замените на вашу почту
            recipient_list=[customer_email],
        )
        order.save()
