from classifier import classify   # берём нашу функцию из classifier.py

passed = 0   # сколько совпало
total = 0    # сколько всего фраз

with open("evals/test_set.txt", encoding="utf-8") as f:   # открываем набор
    for line in f:                          # читаем файл по одной строке
        line = line.strip()                 # убираем перенос строки в конце
        if not line:                        # пустую строку пропускаем
            continue
        num, phrase, expected = line.split("|")   # режем строку на три части по |
        actual = classify(phrase)                 # спрашиваем классификатор
        total += 1                                # +1 к счётчику фраз
        if actual == expected:
            passed += 1
            print(f"OK     {num}: {actual}")
        else:
            print(f"ОШИБКА {num}: ждали {expected}, получили {actual}")

print(f"Итого: {passed} из {total}")