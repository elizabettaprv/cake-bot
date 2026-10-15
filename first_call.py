# first_call.py — первый вызов Claude API: проверяем, что вся цепочка работает

from dotenv import load_dotenv  # функция, которая читает файл .env
import anthropic                # библиотека Anthropic: собирает и отправляет HTTP-запрос

load_dotenv()  # читает .env и передаёт ANTHROPIC_API_KEY этой программе (только ей, не терминалу)

client = anthropic.Anthropic()  # клиент API; ключ находит сам по имени ANTHROPIC_API_KEY

# Отправляем запрос: это тот же curl, только собранный библиотекой
response = client.messages.create(
    model="claude-haiku-5-5",   # быстрая и дешёвая модель: для коротких фраз её хватает
    max_tokens=1000,             # потолок длины ответа в токенах: защита от слишком длинного (и дорогого) ответа
    messages=[                  # история диалога; модель stateless и видит только то, что здесь
        {"role": "user", "content": "В вашем торте есть орехи?"}
    ],
)

print(response.content[1].text)                         # текст ответа модели
print("Токены на вход:", response.usage.input_tokens)    # сколько стоил вопрос
print("Токены на выход:", response.usage.output_tokens)  # сколько стоил ответ
print("Почему остановилась:", response.stop_reason)  # end_turn = закончила сама, max_tokens = обрезали