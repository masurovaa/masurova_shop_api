from celery import shared_task

@shared_task
def send_hello_email(email):
    print(f'Привет отправлен на {email}')