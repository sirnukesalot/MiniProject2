import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
logger = logging.getLogger('django')

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.info(f'User logged in: {user.email}')


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info(f'User logged out: {user.email}')