from aiogram.fsm.state import StatesGroup, State


class CertificateStates(StatesGroup):
    """Состояния для обработки сертификатов."""
    waiting_for_name = State()


class ManualCertificateStates(StatesGroup):
    """Состояния для ручного создания сертификатов."""
    waiting_for_name = State()
    waiting_for_group = State()
    waiting_for_date = State()
