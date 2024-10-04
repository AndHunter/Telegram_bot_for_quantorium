from aiogram.types import Message
from keyboard import keyboard_start, keyboard_help, keyboard_free_courses, keyboard_how_to_get

link_site, text_site = 'https://kvantorium-perm.ru/', "сайте"
link_site_, text_site_ = 'https://kvantorium-perm.ru/', "сайт"
link_vk, text_vk = 'https://vk.com/kvantorium.fotonika', 'VK'
link_youtube, text_youtube = 'https://www.youtube.com/channel/UC8Q99tRVe6T-zzsjBI89RWQ/videos', 'Youtube'
link_tg, text_tg = 'https://t.me/kvantoriumperm', 'Telegram'
async def first_cmd(message: Message):
    await message.answer('Здравствуйте, вас приветствует помощник по учебному заведению "Кванториум Фотоника".',
                         reply_markup=keyboard_start)


async def help_cmd(message: Message):
    await message.answer(f"""
    
    Наш {f"<a href=\"{link_site_}\">{text_site_}</a>"}
    
    Наш телефон
    +7 (342) 214-42-69
    
    Наша почта
    KvantoriumPerm@gmail.com
        
    Мы здесь
    Пермь, ул.25 октября, 64/1

    Мы открыты
    пн-сб, 9:00–21:00

    Наши соцсети
    {f"<a href=\"{link_vk}\">{text_vk}</a>"} | {f"<a href=\"{link_youtube}\">{text_youtube}</a>"} | {f"<a href=\"{link_tg}\">{text_tg}</a>"}
    """, reply_markup=keyboard_help, parse_mode="HTML")

async def free_courses_cmd(message: Message):
    await message.answer("""
    Вы выбрали бесплатные курсы,
выберите пожалуйста действие на клавиатуре.
    """, reply_markup=keyboard_free_courses)

async def how_to_get_cmd(message: Message):
    await message.answer(f"Вам нужно пройти тесты для вступления, на нашем сайте {f"<a href=\"{link_site}\">{text_site}</a>"}", parse_mode="HTML", reply_markup=keyboard_how_to_get)

async def handler_command(message: Message):
    if message.text.lower() == "информация":
        await help_cmd(message)
    elif message.text.lower() == "назад":
        await first_cmd(message)
    elif message.text.lower() == "бесплатные курсы":
        await free_courses_cmd(message)
    elif message.text.lower() == "как попасть":
        await how_to_get_cmd(message)
