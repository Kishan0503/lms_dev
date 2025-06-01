from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import BorrowRequest

@receiver(post_save, sender=BorrowRequest)
def update_book_copies_on_borrow_status_change(sender, instance, **kwargs):
    """
    Handles auto-decrement/increment of book's available_copies on borrow status changes.
    Send emails to students when borrow request is approved or rejected.
    """
    if not instance.pk:
        return

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    if old_instance.status != instance.status:
        subject = ''
        message = ''
        if instance.status == 'APPROVED':
            subject = 'Your Book Request is Approved'
            message = f"Your request for '{instance.book.title}' has been approved."
            
            if instance.book.available_copies > 0:
                instance.book.available_copies -= 1
                instance.book.save()
                
        elif instance.status == 'REJECTED':
            subject = 'Your Book Request is Rejected'
            message = f"Your request for '{instance.book.title}' has been rejected."

        elif instance.status == 'RETURNED' and old_instance.status != 'RETURNED':
            instance.book.available_copies += 1
            instance.book.save()

        # Send email only if status is approved or rejected
        if subject and message:
            send_mail(subject, message, None, [instance.user.email])