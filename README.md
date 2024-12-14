# 📚 Кванториум - Telegram Бот

Этот проект представляет собой Telegram-бота для записи на курсы в Кванториуме, выдачи сертификатов и общения с администраторами.

## 🚀 Функционал
- Запись на курсы
- Выдача сертификатов
- Поддержка и обратная связь через админ-панель
- Интерактивные кнопки для навигации

## 🛠️ Технологии
- [Python](https://www.python.org/) — язык программирования
- [Aiogram](https://docs.aiogram.dev/en/latest/) — для работы с Telegram Bot API
- [PostgreSQL](https://www.postgresql.org/) — база данных для хранения информации
- [Google Sheets API](https://developers.google.com/sheets) — для интеграции с Google Таблицами

## 📦 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/AndHunter/Telegram_bot_for_quantorium.git
2. Перейдите в папку с проектом:
   ```bash
   cd Telegram_bot_for_quantorium
3. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   # Для Windows:
   venv\Scripts\activate
   # Для Linux/macOS:
   source venv/bin/activate

4. Установите зависимости:
   ```bash
   pip3 install -r requirements.txt
## 🔑 Настройка

1. Для работы с ботом вам потребуется создать и настроить .env файл для хранения переменных окружения, таких как токен бота, идентификатор администратора, ссылки и другие данные.
   ```bash
     BOT_TOKEN=your_telegram_bot_token
     ADMIN_ID=your_admin_telegram_id
     DATABASE_URL=your_postgresql_database_url
     GOOGLE_SHEET_ID=your_google_sheet_id
     TOKEN=your_telegram_bot_token
     ADMIN_ID=your_admin_id
     LINK_SITE=your_site_link
     TEXT_SITE=your_site_text
     LINK_VK=your_vk_link
     TEXT_VK=your_vk_text
     LINK_YOUTUBE=your_youtube_link
     TEXT_YOUTUBE=your_youtube_text
     LINK_TG=your_tg_link
     TEXT_TG=your_tg_text

## ⚙️ Структура проекта
1. main.py: Запускает бота и управляет основными операциями.
2. keyboard.py: Определяет кнопки для взаимодействия с пользователем через клавиатуру.
3. certificates_cmd.py: Содержит логику команд, связанных с выдачей сертификатов.
4. draw_certificat.py: Генерирует сертификаты.
5. db_output.py: Управляет взаимодействием с базой данных PostgreSQL.
6. logger.py: Реализует логирование действий и ошибок бота.
7. states.py: Управляет состояниями и переходами в пользовательских взаимодействиях.
8. config.py: Содержит конфигурационные данные и настройки бота.
## 🧑‍💻 Вклад в проект
   Если вы хотите внести свой вклад в проект, пожалуйста, откройте Pull Request или создайте Issue для обсуждения.

## 📬 Контакты
   Если у вас возникли вопросы или предложения, вы можете связаться с разработчиком через следующие каналы:

- [Email](KvantoriumPerm@gmail.com) — почта кванториума
- [VK](https://vk.com/kvantorium.fotonika) — VK кванториума
- [Telegram](https://t.me/kvantoriumperm) — TG кванториума
- [Youtube](https://www.youtube.com/channel/UC8Q99tRVe6T-zzsjBI89RWQ/videos) — Youtube кванториума
## Поддержка автора

Если вам нравится этот проект и вы хотите поддержать меня, вы можете сделать это, отправив криптовалюту на мой кошелек.

### Мой криптовалютный кошелек:
- **Toncoin (Ton):** `UQBydsQ86XvHhac8ex3MHLiMHOX7QUrZVFXRdYvBXAWugAkg`
- **USDT TRC - 20 (USDT):** `TEQpJL5RT5VadNpsTpG9Z8jAdZ8d3uvNa7`

Спасибо за вашу поддержку!
