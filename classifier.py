import anthropic                     # библиотека для Claude API
from dotenv import load_dotenv       # читает .env

load_dotenv()                        # кладёт ключ из .env в окружение
client = anthropic.Anthropic()       # клиент сам находит ключ

# Промпт храним в файле, а не в коде: менять его можно без правки Python.
# encoding="utf-8" обязателен на Windows, иначе кириллица превратится в кашу.
with open("prompts/classifier_v1.txt", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def classify(message):
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=20,               # нужна одна метка, длинный ответ не нужен
        system=SYSTEM_PROMPT,        # твой промпт как инструкция модели
        messages=[{"role": "user", "content": message}],  # фраза клиента
    )
    # В content могут быть блоки разных типов (помнишь ThinkingBlock).
    # Берём первый текстовый.
    for block in response.content:
        if block.type == "text":
            return block.text.strip()
    return None

print(classify("Можно торт без орехов на субботу?"))
print(classify("Хочу торт с орехами на субботу"))