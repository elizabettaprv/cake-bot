import json 
import anthropic                     # библиотека для Claude API
from dotenv import load_dotenv       # читает .env

load_dotenv()                        # кладёт ключ из .env в окружение
client = anthropic.Anthropic()       # клиент сам находит ключ

# Промпт храним в файле, а не в коде: менять его можно без правки Python.
# encoding="utf-8" обязателен на Windows, иначе кириллица превратится в кашу.
with open("prompts/classifier_v1.txt", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

LABELS = ["risk", "order", "facts", "general", "other"]   # пять меток из спецификации

def classify(message):
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1000,                 # с запасом: размышление тоже сюда входит
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": message}],
        output_config={
            "effort": "low",             # задача простая, долго думать не нужно
            "format": {                  # ответ строго по схеме
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string", "enum": LABELS}
                    },
                    "required": ["label"],
                    "additionalProperties": False,
                },
            },
        },
    )
    for block in response.content:
        if block.type == "text":
            data = json.loads(block.text)   # текст '{"label": "risk"}' → словарь Python
            return data["label"]             # из словаря берём значение метки
    return None
   

print(classify("Можно торт без орехов на субботу?"))
print(classify("Хочу торт с орехами на субботу"))
print(classify("Подскажите, сколько ехать до Валенсии?"))