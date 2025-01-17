from aiogram import html, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from asgiref.sync import sync_to_async

from modul.clientbot import shortcuts
from modul.clientbot.data.states import Download
from modul.models import TaskModel, TaskTypeEnum
from modul.loader import client_bot_router, bot_session
from modul.clientbot.keyboards.reply_kb import download_main_menu, main_menu


@client_bot_router.message(F.text == "Назад", Download.download)
async def music_menu(message: Message, state: FSMContext):
    await message.answer(
        ("Добро пожаловать, {full_name}").format(full_name=html.quote(message.from_user.full_name)),
        reply_markup=await main_menu(message.from_user.id)
    )
    await state.clear()


@client_bot_router.message(F.text == ("🌐 Скачать видео"))  # удалить через неделю
async def music_menu(message: Message, state: FSMContext):
    await message.answer(("Этот пункт изменился, пожалуйста, нажмите /start, чтобы обновить панель"))


@client_bot_router.message(F.text == ("🎥 Скачать видео"))
async def music_menu(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Download.download)
    # await message.answer("Пришлите ссылку на Youtube или ТикТок видео и я его скачаю для вас", reply_markup=await download_main_menu())
    user_name = f"{message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ''}"
    await message.answer(
        ("🤖 Привет, {user_name}! Я бот-загрузчик.\r\n\r\n"
         "Я могу скачать фото/видео/аудио/файлы/архивы с *Youtube, Instagram, TikTok, Facebook, SoundCloud, Vimeo, Вконтакте, Twitter и 1000+ аудио/видео/файловых хостингов*. Просто пришли мне URL на публикацию с медиа или прямую ссылку на файл.").format(
            user_name=user_name),
        reply_markup=await download_main_menu(),
        parse_mode="Markdown"
    )


@sync_to_async
def create_task_model(client, url):
    info = TaskModel.objects.create(client=client, task_type=TaskTypeEnum.DOWNLOAD_MEDIA, data={'url': url})
    return True


@client_bot_router.message(Download.download)
async def youtube_download_handler(message: Message, bot: Bot):
    await message.answer(('📥 Скачиваю...'))
    if not message.text:
        await message.answer(('Пришлите ссылку на видео'))
        return
    if 'streaming' in message.text:
        await message.answer(('Извините, но я не могу скачать стримы'))
        return
    me = await bot.get_me()
    await shortcuts.add_to_analitic_data(me.username, message.text)
    if 'instagram' in message.text:
        new_url = message.text.replace('www.', 'dd')
        await message.answer(
            ('{new_url}\r\nВидео скачано через бота @{username}').format(new_url=new_url, username=me.username))
        return
    client = await shortcuts.get_user(message.from_user.id)
    info = await create_task_model(client, message.text)
