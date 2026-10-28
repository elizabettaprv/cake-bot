from rules import detect_rule_intent   # слой 1: правила
from classifier import classify        # слой 2: модель


def route(message):
    rule = detect_rule_intent(message)  # сначала правила: бесплатно и надёжно
    if rule is not None:                # правила что-то нашли (risk или stop)
        return rule                     # модель не зовём
    label = classify(message)           # правила промолчали: спрашиваем модель
    if label is None:                   # модель не ответила или ответ не разобрался
        return "risk"                   # не знаем, о чём вопрос: отдаём человеку
    return label                        # обычный случай: метка от модели


if __name__ == "__main__":              # этот блок работает, только если запустить router.py напрямую
    for msg in ["У меня аллергия на орехи", "Стоп, передумала", "Можно медовик на субботу?"]:
        print(msg, "→", route(msg))