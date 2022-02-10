from loader import dp
from aiogram import types
from keyboards.inline import menu_callback


@dp.callback_query_handler(menu_callback.filter(item_name='info'))
async def info(call: types.CallbackQuery):
    text = '📜 info\nСуть игры заключается в том чтобы решить математические примеры одним ответом. ' \
           'За каждый правильный ответ тебя ждет награда.\n\n'\
           'Один раунд 3 примера'
    await call.answer(text=text, show_alert=True)


@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await message.answer(text='<code>Немнго о боте.</code>\nБот на данный момент находится на стадии разработки.\n'\
                              'В дальнейшем в нем будет <i>запись</i> и <i>алгоритмизация</i> рейтингов.'\
                         'Также происходит заполнение <b>базы примеров.</b>')