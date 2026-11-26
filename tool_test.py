# tool_test.py — первый вызов tool use: захочет ли модель вызвать save_lead
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()                      # берёт ключ API из .env
client = anthropic.Anthropic()     # клиент для запросов к Claude

# описание инструмента читаем из файла, как спецификацию
with open("tools/save_lead.json", encoding="utf-8") as f:
    save_lead = json.load(f)

# строка «Сегодня» — та самая, что даёт модели точку отсчёта для дат
system = "Ты консультант кондитерской. Сегодня: 2026-11-26, четверг. Часовой пояс: Europe/Madrid."

message = "Здравствуйте, я Анна. Хочу шоколадный торт на день рождения в эту субботу. Да, оформите заявку."

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    system=system,
    tools=[save_lead],             # передаём модели список доступных инструментов
    messages=[{"role": "user", "content": message}],
)

print("stop_reason:", response.stop_reason)
for block in response.content:     # ответ состоит из блоков: текст и/или вызов инструмента
    print(block.type, "→", block.model_dump())