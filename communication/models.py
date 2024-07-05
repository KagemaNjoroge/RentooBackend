import datetime
from django.db import models
from authentication.models import CustomUser
from .firebase_init import db


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="received_messages"
    )
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def save_to_firestore(self):
        message_ref = db.collection("messages").document()
        message_data = {
            "sender": self.sender.username,
            "recipient": self.recipient.username,          
            "body": self.body,
            "sent_at": datetime.datetime.now().isoformat(),
            "read": self.read,
        }
        message_ref.set(message_data)

    def save(self, *args, **kwargs):
        self.save_to_firestore()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender} to {self.recipient}: {self.subject}"


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def save_to_firestore(self):
        notification_ref = db.collection("notifications").document()
        notification_data = {
            "user": self.user.username,
            "message": self.message,
            "created_at": datetime.datetime.now().isoformat(),
            "read": self.read,
        }
        notification_ref.set(notification_data)

    def save(self, *args, **kwargs):
        self.save_to_firestore()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}: {self.message}"
