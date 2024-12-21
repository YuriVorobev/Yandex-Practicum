class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    last_index = len(alphabet) - 1

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        
        for letter in original_text.lower():
            if letter in CipherMaster.alphabet:
                letter_index = CipherMaster.alphabet.index(letter)
                new_index = letter_index + shift
                if new_index > CipherMaster.last_index:
                    new_index = 0 + new_index % (len(CipherMaster.alphabet))
                new_letter = CipherMaster.alphabet[new_index]
            else:
                new_letter = letter
            result.append(new_letter)
        
        return ''.join(result)
    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        
        for letter in cipher_text:
            letter = letter.lower()
            if letter in CipherMaster.alphabet:
                letter_index = CipherMaster.alphabet.index(letter)
                new_index = letter_index - shift
                if new_index < 0:
                    new_index = len(CipherMaster.alphabet) + letter_index + shift
                elif new_index > CipherMaster.last_index:
                    new_index = 0 + new_index % (len(CipherMaster.alphabet))
                new_letter = CipherMaster.alphabet[new_index]
                    
            else:
                new_letter = letter
            result.append(new_letter)
        
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))