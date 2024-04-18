from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from zs_utils.base_support import models


__all__ = [
    "CommonSupportTicketSerializer",
    "CommonCreateSupportTicketSerializer",
    "CommonSupportTicketMessageSerializer",
    "CommonCreateSupportTicketMessageSerializer",
    "CommonSupportTicketMessageFileSerializer",
]


class CommonSupportTicketSerializer(serializers.ModelSerializer):
    user = None
    manager = None

    class Meta:
        model = models.SupportTicket
        fields = [
            "id",
            "number",
            "created",
            "user",
            "manager",
            "status",
            "question_type",
            "subject",
            "unread_messages",
        ]


class CommonCreateSupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SupportTicket
        fields = [
            "question_type",
            "subject",
        ]


class CommonSupportTicketMessageSerializer(serializers.ModelSerializer):
    sender = None
    files = None

    class Meta:
        model = models.SupportTicketMessage
        fields = [
            "id",
            "created",
            "ticket",
            "sender",
            "text",
            "files",
            "is_system",
            "is_viewed",
        ]


class CommonCreateSupportTicketMessageSerializer(serializers.Serializer):
    text = serializers.CharField(required=False, allow_null=True)
    files = None

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        if not (data.get("text") or data.get("files")):
            raise ValidationError({"text": "Обязательное поле, если не задано поле 'files'."})

        return data


class CommonSupportTicketMessageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SupportTicketMessageFile
        fields = [
            "id",
            "ticket_message",
            "file",
        ]
