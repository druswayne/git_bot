import os
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from aiogram import  F
from aiogram.types import Message
from loader import bot, router



@router.message(F.voice)
async def handle_voice(message: Message):

        file_id = message.voice.file_id

        file = await bot.get_file(file_id)

        file_path = file.file_path


        ogg_path =  f'temp/{message.chat.id}.ogg'

        await bot.download_file(file_path, ogg_path)



        # Конвертируем в WAV используя moviepy
        audio_clip = AudioFileClip(ogg_path)

        wav_path = f'temp/{message.chat.id}.wav'

        audio_clip.write_audiofile(wav_path, fps=44100)

        audio_clip.close()

        # Распознаем речь
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='ru-RU')
            await message.reply(f"Текст из голосового сообщения:\n{text}")
        if os.path.exists(ogg_path):
            os.remove(ogg_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)


