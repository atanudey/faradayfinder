from emails.models import Email


def log_email(to, from_email, subject, message):
    email = Email(
        to=to, from_email=from_email, subject=subject, message=message
    )
    email.save()
