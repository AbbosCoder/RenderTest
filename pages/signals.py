# pages/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactMessage
from .utils import send_telegram_message  # Telegram uchun yuborish funksiyasini import qilish

# Telegram bot tokeni va admin chat ID
BOT_TOKEN = '7811597017:AAFjXgBZwsV_taaXHfaBr7EDJXIefWKsPzk'
ADMIN_CHAT_ID = '762725479'

@receiver(post_save, sender=ContactMessage)
def send_message_to_telegram(sender, instance, created, **kwargs):
    if created:  # Faqat yangi xabar saqlanganda
        message = f"""
<b>📩 Yangi xabar!</b>

👤 Ism: {instance.name}
📧 Email: {instance.email}
📌 Mavzu: {instance.subject}

📝 Xabar:
{instance.message}
"""
        send_telegram_message(BOT_TOKEN, ADMIN_CHAT_ID, message)
