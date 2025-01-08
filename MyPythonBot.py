import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import TOKEN

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Отправь мне ссылку на видео с YouTube, и я пришлю его тебе.')

def download_video(url: str) -> str:
    from pytube import YouTube
    yt = YouTube(url)
    video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    
    if not video:
        video = yt.streams.get_lowest_resolution()

    video_file_path = video.download(output_path='downloads')
    return video_file_path


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text
    if 'youtube.com/watch' in url or 'youtu.be/' in url:
        try:
            await update.message.reply_text('Скачиваю видео, подождите...')
            video_file_path = download_video(url)
            await update.message.reply_video(video=open(video_file_path, 'rb'))
            os.remove(video_file_path)  # Удаляем файл после отправки
        except Exception as e:
            await update.message.reply_text(f'Произошла ошибка: {e}')
    else:
        await update.message.reply_text('Пожалуйста, отправьте действительную ссылку на видео с YouTube.')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Обрабатываем все текстовые сообщения

    application.run_polling()

if __name__ == '__main__':
    main()