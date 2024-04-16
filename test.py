#ВАРІАНТ 19
У роботі №3, у файлі test.py модифікувати тест test_sword_with_random_rarity та дописати перевірку що рідкісність меча не може бути рівною None


def test_sword_with_random_rarity(sword):
    """Тестуємо меч з використання фікстур"""
    assert hasattr(sword, 'rarity'), f"В обєкта неправильно встановлено атрибут рідкісності!"
    assert isinstance(sword.rarity, str), "Назва типу рідкісності має бути словом/стрічкою."
    assert sword.rarity in Swords.rarity_map.keys(), f"Рідкісність меча {sword.rarity} не відповідає заданим {Swords.rarity_map.keys()}"
    assert isinstance(sword, Swords), f"Обєкт що тестується класу {type(sword)} має бути мечем класу {type(Swords)}"

Оновлена частина коду:
def test_sword_with_random_rarity(sword):
    """Тестуємо меч з використання фікстур"""
    assert hasattr(sword, 'rarity'), "Атрибут рідкісності не був встановлений для меча!"
    assert isinstance(sword.rarity, str), "Назва типу рідкісності має бути словом/стрічкою."
    assert sword.rarity is not None, "Рідкісність меча не може бути None."
    assert sword.rarity in Swords.rarity_map.keys(), f"Рідкісність меча {sword.rarity} не відповідає заданим {Swords.rarity_map.keys()}"
    assert isinstance(sword, Swords), f"Об'єкт, що тестується, має бути мечем класу {type(Swords)}"

