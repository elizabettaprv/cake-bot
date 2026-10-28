from datetime import datetime   # чтобы узнать текущие дату и время
from classifier import classify, PROMPT_FILE, MODEL   # функцию и две константы

passed = 0       # сколько совпало
total = 0        # сколько всего фраз
risk_passed = 0  # НОВОЕ: сколько risk-фраз угадано
risk_total = 0   # НОВОЕ: сколько всего risk-фраз в наборе
errors = []      # НОВОЕ: номера ошибок; [] — пустой список

with open("evals/test_set.txt", encoding="utf-8") as f:   # открываем набор
    for line in f:                          # читаем файл по одной строке
        line = line.strip()                 # убираем перенос строки в конце
        if not line:                        # пустую строку пропускаем
            continue
        num, phrase, expected = line.split("|")   # режем строку на три части по |
        actual = classify(phrase)                 # спрашиваем классификатор
        total += 1                                # +1 к счётчику фраз
        if expected == "risk":                    # НОВОЕ: фраза из зоны риска?
            risk_total += 1                       # НОВОЕ
        if actual == expected:
            passed += 1
            if expected == "risk":                # НОВОЕ: угадали risk
                risk_passed += 1                  # НОВОЕ
            print(f"OK     {num}: {actual}")
        else:
            errors.append(num)                    # НОВОЕ: дописываем номер в список
            print(f"ОШИБКА {num}: ждали {expected}, получили {actual}")

print(f"Итого: {passed} из {total}")
print(f"risk: {risk_passed} из {risk_total}")            # НОВОЕ
print(f"Ошибки: {', '.join(errors) or 'нет'}")           # НОВОЕ
print(f"Промпт: {PROMPT_FILE}, модель: {MODEL}")   # с чем шёл прогон

with open("evals/results.md", "a", encoding="utf-8") as out:   # "a" = append: дописать в конец
    out.write(
        f"| {datetime.now():%Y-%m-%d %H:%M} | {MODEL} | {PROMPT_FILE} "
        f"| {passed}/{total} | {risk_passed}/{risk_total} | {', '.join(errors) or 'нет'} |\n"
    )   # одна строка таблицы; \n — перенос строки в конце