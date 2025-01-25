from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart, Command
from .data_fetch import ResponseMethod
from .tokenGen import generate_token
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup



cmd = Router()

# Обработчик команды /start
@cmd.message(CommandStart())  # Указываем, что обрабатываем команду /start
async def command_start_handler(message: Message):
    resp = ResponseMethod()  # Инициализация вашего класса запросов
    try:
        user_id = message.chat.id
        user_status = await resp.get_response(f'api/v1/user-exsist{user_id}')
        if user_status == 'NOT_FOUND':
            token = generate_token(user_id)
            data = {
                'telegram_id': user_id,
                'username': message.chat.username,
                'full_name': message.chat.full_name,
                'token': token
            }
            await resp.post_response(f'api/v1/register', data)
            await message.reply(
                f'Для проверки IMEI воспользуйтесь командой /check')
        else:
            await message.reply(
                f'Для проверки IMEI воспользуйтесь командой /check')

    except Exception as e:
        await message.reply(
            f'Кажется что-то пошло не так :(, обратитесь пожалуйста к администратору')



# Определяем состояния
class Form(StatesGroup):
    waiting_for_imei = State()

@cmd.message(Command('check'))
async def check_imei(message: Message, state: FSMContext):
    await message.reply(f'введите номер IMEI устройства')
    await state.set_state(Form.waiting_for_imei)



# Обработчик ввода IMEI
@cmd.message(Form.waiting_for_imei)
async def process_imei(message: Message, state: FSMContext):
    imei = message.text  # Получаем текст, введённый пользователем

    # Проверяем IMEI (например, длина или формат)
    if not imei.isdigit() or len(imei) != 15:
        await message.reply("Неверный формат IMEI. Попробуйте ещё раз:")
        return

    # Если IMEI корректен
    await message.reply(f"IMEI: {imei} принят в обработку.")
    try:
        resp = ResponseMethod()
        token = generate_token(message.chat.id)
        answer = await resp.post_response(f'api/v1/check-imei', {'imei': imei}, token)
        await message.reply(
            f'{answer}')
    except Exception as e:
        await message.reply(
            f'Кажется что-то пошло не так :(, обратитесь пожалуйста к администратору {e}')

    # Сбрасываем состояние
    await state.clear()