SIGNS = {
    "овен": "♈️Овен: ",
    "телец": "♉️Телец: ",
    "близнецы": "♊️Близнецы: ",
    "рак": "♋️Рак: ",
    "лев": "♌️Лев: ",
    "дева": "♍️Дева: ",
    "весы": "♎️Весы: ",
    "скорпион": "♏️Скорпион: ",
    "стрелец": "♐️Стрелец: ",
    "козерог": "♑️Козерог: ",
    "водолей": "♒️Водолей: ",
    "рыбы": "♓️Рыбы: ",
}
SIGNS_TEXT = ', '.join(SIGNS)
WRONG_MESSAGE = f"""Не слышу, что ты там пишешь.
Тегаешь меня <@1177181921961312337> и пишешь свой знак:
{SIGNS_TEXT}
"""
VK_ERROR = "Что то облачно на небе, тучи звезды загораживают, может позже?"
NO_SIGN = """
Сегодня эльфы обмазали обьектив телескопа прокисшим йогуртом, мне не известо,
что звезды говорят о тебе сегодня
"""
WRONG_SPLITTER = """
Сегодня возможен конец света, потому что какой-то чушпан поменял алгоритм
разделения гороскопов
"""
WRONG_SIGN = f"""Ты толи писать не умеешь, толи знаков не знаешь, вот они:
{SIGNS_TEXT}
"""
CREATOR_ERROR = "Передайте моему создателю, что он чушпан"
