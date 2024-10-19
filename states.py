from aiogram.fsm.state import StatesGroup, State


class CertificateStates(StatesGroup):
    """Состояния для обработки сертификатов."""
    waiting_for_name = State()
