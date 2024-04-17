from setuptools import setup, find_packages

setup(
    name="ATH",
    version="0.4.9",
    description="""Info: https://discord.com/channels/831614817458323537/1213477275232641044
install:
pip install ATH

upgrade:
pip install --upgrade ATH

functions:
add_numbers(number, number, number, ...)
subtract_numbers(number, number, number, ...)
def multiply_numbers(number, number, number, ...)
divide_numbers(number, number, number, ...)
arithmetic_average(number, number, number, ...)
owl(url)
safe_gk()
safe(message, key)
unsafe(encrypted_message, key)
scr_shot(name, path)
scr_shot_telegram(name, path, bot_id, server_id)
sq_root(number)
tts(thing)
stt()
write(thing)
DB_send(token, server_name, channel_name, message)
DB_read(token, thing, do)
gqrc(content, file_name, size)
abc(var)
onetwothree(var)
threedotonefour(var)
telegram(message, bot_id, server_id)
checksign(path)""",
    packages=find_packages(),
    install_requires=["pyttsx3", "cryptography", "speechrecognition", "asyncio", "discord", "discord.py", "telebot", "pyscreenshot", "python-dotenv", "qrcode[pil]", "numpy", "pydub", "c2pa-python"]
)