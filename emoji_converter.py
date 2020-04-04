def emojiConverter(message):
    words = message.split(" ")  # Goes through the string and divides it into as many parts as the number of spaces
    emojis = {
        ":)": "😊",
        ":(": "☹️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emojiConverter(message))
