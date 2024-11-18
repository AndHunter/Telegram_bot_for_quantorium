import os
from PIL import Image, ImageDraw, ImageFont
from typing import Optional

#TODO доделать границы отрисовки
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
        image = Image.open(image_path)

        font_name = ImageFont.truetype("arial.ttf", 35)
        font_group = ImageFont.truetype("arial.ttf", 25)
        font_date = ImageFont.truetype("arial.ttf", 15)

        drawer = ImageDraw.Draw(image)
        drawer.text((270, 250), name, font=font_name, fill='black')
        drawer.text((80, 350), group, font=font_group, fill='black')
        drawer.text((440, 600), date, font=font_date, fill='blue')

        output_path = os.path.join(output_dir, f'{name.replace(" ", "_")}_certificate.jpg')
        image.save(output_path)

        print(f"Сертификат сохранён: {output_path}")
        return output_path

    except Exception as e:
        print(f"Ошибка при создании сертификата: {e}")
        return None
