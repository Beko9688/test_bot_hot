from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import menu_callback

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Инструкция", callback_data=menu_callback.new(item_name='info')),
         InlineKeyboardButton(text="Начать игру", callback_data=menu_callback.new(item_name='start_game'))]
    ]
)


restart = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать заного", callback_data=menu_callback.new(item_name='start_game'))]
    ]
)

get_gift = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Получить приз", callback_data=menu_callback.new(item_name='get_gift'))]
    ]
)

finish_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Не показывайте мне больше такие фотки", callback_data=menu_callback.new(item_name='no_show'))],
        [InlineKeyboardButton(text="Особая игра", callback_data=menu_callback.new(item_name='special'))],
        [InlineKeyboardButton(text="Хочу ещё раз сыграть", callback_data=menu_callback.new(item_name='start_game'))]
    ]
)

throw_dice = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Кинуть кость", callback_data=menu_callback.new(item_name='throw_dice'))]
    ]
)