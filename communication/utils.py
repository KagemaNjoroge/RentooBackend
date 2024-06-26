from django.core.mail import send_mail


def send_email_to_user(receiver, sender, message, subject, auth_user, auth_password):
    return send_mail(
        auth_password=auth_password,
        auth_user=auth_user,
        fail_silently=True,
        from_email=sender,
        recipient_list=[receiver],
        message=message,
        subject=subject,
    )
