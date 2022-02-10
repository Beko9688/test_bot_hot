from random import randint

from aiogram.dispatcher import FSMContext

from loader import dp, bot
from aiogram import types
from keyboards.inline import menu_callback, restart, get_gift, finish_buttons, throw_dice
from states import Game
from data.answers import answers

number_of_ex_photo = 13


@dp.callback_query_handler(menu_callback.filter(item_name='start_game'))
async def start_game(call: types.CallbackQuery, state: FSMContext):
    number = randint(1, number_of_ex_photo)
    random_photo = open(f'mathematical examples/{number}.png', 'rb')
    await call.message.answer_photo(photo=random_photo, caption='Пример №1 [отправить число]')
    random_photo.close()
    await Game.First.set()
    await state.update_data(number_of_ex=number)


@dp.message_handler(state=Game.First)
async def first_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()

    number_of_ex = data.get('number_of_ex')
    try:
        if int(message.text) == answers.get(number_of_ex):
            await message.answer(text='Правильно ✅')
            number = randint(1, number_of_ex_photo)
            random_photo = open(f'mathematical examples/{number}.png', 'rb')
            await message.answer_photo(photo=random_photo, caption='Пример №2 [отправить число]')
            random_photo.close()
            await Game.Second.set()
            await state.update_data(number_of_ex=number)
        else:
            await state.finish()
            await message.answer(text=' ❌ Не правильно, придется начать заного', reply_markup=restart)
    except ValueError as val_err:
        await message.answer(text='Бля написано же число сука, отправь нормальное число')


@dp.message_handler(state=Game.Second)
async def first_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()

    number_of_ex = data.get('number_of_ex')
    try:
        if int(message.text) == answers.get(number_of_ex):
            await message.answer(text='Правильно ✅')
            number = randint(1, number_of_ex_photo)
            random_photo = open(f'mathematical examples/{number}.png', 'rb')
            await message.answer_photo(photo=random_photo, caption='Пример №3 [отправить число]')
            random_photo.close()
            await Game.Third.set()
            await state.update_data(number_of_ex=number)
        else:
            await state.finish()
            await message.answer(text='❌ Не правильно, придется начать заного', reply_markup=restart)
    except ValueError as val_err:
        await message.answer(text='Бля написано же число сука, отправь нормальное число')


@dp.message_handler(state=Game.Third)
async def first_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()

    number_of_ex = data.get('number_of_ex')
    try:
        if int(message.text) == answers.get(number_of_ex):
            await message.answer(text='Правильно ✅\nПоздравляем вы решили 3 примера правильно!', reply_markup=get_gift)
            await state.finish()
        else:
            await state.finish()
            await message.answer(text='❌ Не правильно, придется начать заного', reply_markup=restart)
    except ValueError as val_err:
        await message.answer(text='Бля написано же число сука, отправь нормальное число')


@dp.callback_query_handler(menu_callback.filter(item_name='get_gift'))
async def get_my_gift(call: types.CallbackQuery):
    number = randint(1, 14)
    random_photo = open(f'gift photo/{number}.png', 'rb')
    await call.message.answer_photo(photo=random_photo, caption='Держи тёлку, ты заслужил 🤙',
                                    reply_markup=finish_buttons)
    await call.message.delete()


@dp.callback_query_handler(menu_callback.filter(item_name='no_show'))
async def get_my_gift(call: types.CallbackQuery):
    await call.answer(text='Ладно если не хочешь тёлок то мы занесли тебя в базу данных для пидоров', show_alert=True)
    await call.message.delete()


@dp.callback_query_handler(menu_callback.filter(item_name='special'))
async def get_my_gift(call: types.CallbackQuery):
    await call.message.answer(text=f'Если выпадет число :<code>{randint(1, 6)}</code>\nТо ты получишь особый приз.',
                              reply_markup=throw_dice)


@dp.callback_query_handler(menu_callback.filter(item_name='throw_dice'))
async def get_my_gift(call: types.CallbackQuery):
    if call.message.dice.value == 5:
        print('-=5=-')
    else:
        print('not -=5=-')
