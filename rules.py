import re
def detect_rule_intent(message):  
    low = message.lower()             
    if "аллерг" in low or "орех" in low:             
        return "risk"   
    if re.search(r"\bстоп\b", low) or "отмена" in low or "передумал" in low:
        return "stop"
    return None  
print(detect_rule_intent("А в медовике есть ОРЕХИ?"))
print(detect_rule_intent("У меня аллергия, можно торт?"))
print(detect_rule_intent("У меня аллергия, передумал заказывать?"))
print(detect_rule_intent("Сколько стоит торт на 20 человек?"))
print(detect_rule_intent("Стоп, я не хочу заказывать"))
print(detect_rule_intent("Хочу стопку блинчиков"))
