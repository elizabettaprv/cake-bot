import re
def detect_rule_intent(message):  
    low = message.lower()             
    if "аллерг" in low or "непереносим" in low:             
        return "risk"   
    if re.search(r"\bстоп\b", low) or "отмена" in low or "передумал" in low:
        return "stop"
    return None  


print(detect_rule_intent("торты без глютена?"))                        # risk
print(detect_rule_intent("сыпь после эклера, что в креме?"))           # risk
print(detect_rule_intent("хочу заказать торт без орехов на субботу"))  # risk
print(detect_rule_intent("хочу медовик, аллергия на фундук"))          # risk
print(detect_rule_intent("у вас свой рецепт крема, с орехами?"))       # risk
print(detect_rule_intent("у ребёнка алергия на молоко — в чём можно заказать торт?"))  # risk
print(detect_rule_intent("А в медовике есть ОРЕХИ?"))                  # risk
print(detect_rule_intent("У меня непереносимость меда, можно торт?"))  # risk
print(detect_rule_intent("У меня аллергия, передумал заказывать?"))    # risk
