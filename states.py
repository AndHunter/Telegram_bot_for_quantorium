from aiogram.fsm.state import StatesGroup, State


class CertificateStates(StatesGroup):
    waiting_for_name = State()  # Ожидание ввода ФИО
