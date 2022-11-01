import json

from aiogram import types
from aiogram.dispatcher import FSMContext

from app.formatters.markup import location as markup
from app.formatters.messages import location as msg
from app.models.chat import Chat
from app.setup import MainState, candidate_places, dp, i18n, selected_place
from app.utils import geonames as geo
from app.utils.desired_kp_solver import get_desired_kp


async def update_location(latitude: float, longitude: float, chat: Chat):
    geonames_data = geo.get_geonames_data(latitude, longitude)
    desired_kp = get_desired_kp(latitude, longitude)
    await chat.update(
        latitude=latitude,
        longitude=longitude,
        geonames_data=json.dumps(geonames_data),
        desired_kp=desired_kp,
    ).apply()
    await dp.bot.send_message(
        chat.id,
        msg.settings_updated(latitude, longitude, geonames_data, desired_kp),
    )


@dp.message_handler(content_types=types.ContentType.LOCATION, state="*")
async def location(message: types.Message, chat: Chat, state: FSMContext):
    await update_location(
        latitude=message.location["latitude"],
        longitude=message.location["longitude"],
        chat=chat,
    )
    await state.reset_state()


@dp.message_handler(commands="location")
async def manual_location(message: types.Message):
    await MainState.location.set()
    await message.answer(
        msg.enter_location(), reply_markup=markup.enter_location()
    )


@dp.message_handler(state=MainState.location)
async def input_location(
    message: types.Message, chat: Chat, state: FSMContext
):
    message_content = message.text.strip()
    places = geo.get_place_suggestions(message_content, i18n.ctx_locale.get())
    if len(places) == 0:
        await message.answer(msg.places_not_found())
        return
    candidate_places.set(chat.id, json.dumps(places))
    selected_place.set(chat.id, 0)
    await state.reset_state()
    await message.answer(
        msg.choose_location(places[0]),
        reply_markup=markup.choose_location(0, len(places)),
    )


@dp.callback_query_handler(
    lambda call: call.data in ["prev", "next", "ok", "cancel"]
)
async def location_callback(call: types.CallbackQuery, chat: Chat):
    places = json.loads(candidate_places.get(chat.id))
    current_id = int(selected_place.get(chat.id))
    if call.data == "prev":
        selected_place.decr(chat.id)
    elif call.data == "next":
        selected_place.incr(chat.id)
    elif call.data == "ok":
        place = places[current_id]
        latitude = float(place["lat"])
        longitude = float(place["lng"])
        await call.message.delete()
        await update_location(latitude, longitude, chat)
        await call.answer()
        return
    else:
        await call.message.delete()
        await call.answer()
        return
    place = places[current_id]
    await call.message.edit_text(
        msg.choose_location(place),
        reply_markup=markup.choose_location(
            current_id,
            len(places),
        ),
    )
    await call.answer()
