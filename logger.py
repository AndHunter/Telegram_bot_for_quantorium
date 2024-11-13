from datetime import datetime

recent_messages = {}


def log(message):
    """Функция для логирования сообщений."""
    msg_id = getattr(message, 'message_id', None)

    if msg_id and msg_id in recent_messages:
        return

    if msg_id:
        recent_messages[msg_id] = True

    with open('log.txt', 'a', encoding="utf-8") as log_file:
        if isinstance(message, str):
            msg = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n"
        else:
            user_info = (f"{message.from_user.first_name or ''} "
                         f"{message.from_user.last_name or ''} "
                         f"(@{message.from_user.username or 'нет_никнейма'}, "
                         f"id: {message.from_user.id})").strip()
            msg = (f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - "
                   f"Сообщение от {user_info}: {message.text}\n")
        log_file.write(msg)
