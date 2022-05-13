def encrypt(text, n):  # шифрування
    if n <= 0: return text
    if not text: return text

    res_str = text
    for n in range(n):  # looping over number of general iterations
        first_part, second_part = "", ""  # creating parts for odd and not odd
        text = res_str  # coping
        for letter in range(len(text)):  # lopping over text
            if letter % 2 == 0:  # if odd then
                first_part += text[letter].lower()  # add to first part
            else:
                second_part += text[letter].lower()  # add to second part
            res_str = second_part + first_part  # concatinate
    return res_str


def decrypt(encrypted_text, n, res_str=""):  # дешифрування
    if n <= 0: return encrypted_text
    if not encrypted_text: return encrypted_text

    for number in range(n):
        first_part, second_part = [], []  # exactly the same but for parts using lists
        for i in range(len(encrypted_text)):
            if i >= len(encrypted_text) // 2:
                second_part.append(encrypted_text[i])
            else:
                first_part.append(encrypted_text[i])

        for i, b in zip(second_part, first_part):  # lopping over zip with parts
            res_str += i + b  # conctatinating two parts
        encrypted_text = res_str

    if n > 1:  # selecting data we need
        return res_str[len(res_str) // n:].capitalize()
    else:
        return res_str.capitalize()


if __name__ == "__main__":
    print(decrypt(encrypt("Abcd", 1), 1))  # Abcd
    print(decrypt(encrypt("Abcd", 2), 2))  # Abcd

    print(encrypt("Abcdefghij", 1))  # bdfhjacegi
    print(decrypt("bdfhjacegi", 1))  # Abcdefghij
