import os
from PIL import Image, ImageDraw, ImageFont
from typing import Optional


def create_certificate(
        name: str,
        group: str,
        date: str,
        image_path: str = 'certificat_kvantorium.jpg',
        output_dir: str = 'certificates'
) -> Optional[str]:
    """
    Создаёт сертификат с заданными параметрами и сохраняет его в указанной директории.

    :param name: ФИО участника.
    :param group: Название группы.
    :param date: Дата выдачи сертификата.
    :param image_path: Путь до шаблона изображения сертификата.
    :param output_dir: Директория для сохранения готового сертификата.
    :return: Путь до созданного сертификата или None в случае ошибки.
    """
    os.makedirs(output_dir, exist_ok=True)

    try:
        group_dict = {
            "РК": "Промробоквантум",
            "МК": "МедиаКвантум",
            "АК": "Аэроквантум",
            "БК": "Биоквантум",
            "IT": "IT-Квантум",
            "НК": "Наноквантум",
            "Х": "Хайтек",
            "Ф": "Фотоника",
            "VR": "VR / AR",
            "ПК": "Промышленный дизайн",
            "КК": "Космоквантум"
        }

        group_name = group_dict.get(group[:2], group_dict.get(group[:1], 'Неизвестная группа'))

        if group.split()[0].endswith("Б"):
            level = "базовый уровень"
        elif group.split()[0].endswith("ПД"):
            level = "продвинутый уровень"
        elif group.split()[0].endswith("П"):
            level = "проектный уровень"
        else:
            level = "неизвестный уровень"

        image = Image.open(image_path)

        font_group = ImageFont.truetype("arial.ttf", 15)
        font_date = ImageFont.truetype("arial.ttf", 15)
        font_main = ImageFont.truetype("arial.ttf", 30)

        drawer = ImageDraw.Draw(image)
        main_text = (
            f"Настоящим подтверждается, что\n"
            f"{name}\n"
            f"прошел(а) обучение по направлению\n"
            f"{group_name}, {level}\n"
            f"в объеме 64 часа"
        )

        drawer.multiline_text((213, 234), main_text, font=font_main, fill='black', align='center')
        drawer.text((100, 470), group, font=font_group, fill='black')
        drawer.text((437, 600), date, font=font_date, fill='black')

        output_path = os.path.join(output_dir, f'{name.replace(" ", "_")}_certificate.jpg')
        image.save(output_path)

        print(f"Сертификат сохранён: {output_path}")
        return output_path

    except Exception as e:
        print(f"Ошибка при создании сертификата: {e}")
        return None
