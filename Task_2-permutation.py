def generate_permutation_key(phrase):
    """
    Функція для генерування порядку перестановки на основі ключової фрази.
    """
    sorted_phrase = sorted(list(phrase))
    return [sorted_phrase.index(char) for char in phrase]

def encrypt(text, key):
    """
    Функція шифрування тексту з використанням алгоритму перестановки.
    """
    # Розбивання тексту на рядки відповідно до довжини ключа
    rows = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    # Заповнення останнього рядка пробілами (за необхідності)
    rows[-1] = rows[-1].ljust(len(key))
    
    # Шифрування, перемішуючи стовпчики за ключем
    encrypted = ''
    for index in sorted(range(len(key)), key=lambda x: key[x]):
        encrypted += ''.join(row[index] for row in rows)
    return encrypted

def decrypt(text, key):
    """
    Функція дешифрування тексту з використанням алгоритму перестановки.
    """
    num_rows = len(text) // len(key)
    # Розбивання тексту на стовпці
    columns = [text[i * num_rows:(i + 1) * num_rows] for i in range(len(key))]
    # Повернення порядку колонок до оригінального
    reordered_columns = [''] * len(key)
    for i, col_index in enumerate(sorted(range(len(key)), key=lambda x: key[x])):
        reordered_columns[col_index] = columns[i]
    
    # Дешифрування та з'єднання стовпчиків
    decrypted = ''.join(''.join(row) for row in zip(*reordered_columns)).rstrip()
    return decrypted

# Ключова фраза
key_phrase = "SECRET"
key = generate_permutation_key(key_phrase)

# Текст для шифрування
plaintext = """
The artist is the creator of beautiful things. To reveal art and conceal the artist is 
art's aim. The critic is he who can translate into another manner or a new material his 
impression of beautiful things. The highest, as the lowest, form of criticism is a mode 
of autobiography. Those who find ugly meanings in beautiful things are corrupt without 
being charming. This is a fault. Those who find beautiful meanings in beautiful things 
are the cultivated. For these there is hope. They are the elect to whom beautiful things 
mean only Beauty. There is no such thing as a moral or an immoral book. Books are well 
written, or badly written. That is all. The nineteenth-century dislike of realism is the 
rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of 
Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of 
man forms part of the subject matter of the artist, but the morality of art consists in 
the perfect use of an imperfect medium. No artist desires to prove anything. Even things 
that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an 
artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can 
express everything. Thought and language are to the artist instruments of an art. Vice 
and virtue are to the artist materials for an art. From the point of view of form, the 
type of all the arts is the art of the musician. From the point of view of feeling, the 
actor's craft is the type. All art is at once surface and symbol. Those who go beneath 
the surface do so at their peril. Those who read the symbol do so at their peril. It is 
the spectator, and not life, that art really mirrors. Diversity of opinion about a work 
of art shows that the work is new, complex, vital. When critics disagree the artist is 
in accord with himself. We can forgive a man for making a useful thing as long as he does 
not admire it. The only excuse for making a useless thing is that one admires it intensely. 
All art is quite useless.
"""

character_count=len(plaintext)
print(">>> кількість символів у тексті для шифрування становить -", character_count, " символів")
print("")

# Шифрування
encrypted_text = encrypt(plaintext, key)
print("Зашифрований текст:", encrypted_text[:200]) # для зручності обмежуємо кількість виведення шифрованого тексту

character_count2=len(encrypted_text)
print(">>> кількість символів у зашифрованому тексті становить -", character_count2, " символів")
print("")

# Дешифрування
decrypted_text = decrypt(encrypted_text, key)
print("Розшифрований текст:", decrypted_text[:200]) # для зручності обмежуємо кількість виведення розшифрованого тексту

character_count3=len(decrypted_text)
print(">>> кількість символів у розшифрованому тексті становить -", character_count3, " символів")