message = 'This is my secret message'
key = 13
mode = 'encrypt'
LEFTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()
for symbol in message:
    if symbol in LEFTERS:
        num = LEFTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LEFTERS):
            num = num - len(LEFTERS)
        elif num < 0:
            num = num + len(LEFTERS)

        translated = translated + LEFTERS[num]
    else:
        translated = translated + symbol

print(translated)
