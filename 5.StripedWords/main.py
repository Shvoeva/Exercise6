import re

text = input('\n\tВведите текст: ')
upper_text = text.upper()
split_text = re.split('[ ,.!?;:()\[\]"\'`\-_|/]+', upper_text)

vowels = ('A', 'E', 'I', 'O', 'U', 'Y')
striped_words_number = 0

for i in split_text:
    is_striped_word = True

    if (not i.isalpha()) or (len(i) <= 1):
        continue

    if i[0] in vowels:
        word_start_with_vowel = 1
    else:
        word_start_with_vowel = 0

    for j in range(len(i) - word_start_with_vowel):
        letter_index = j + word_start_with_vowel
        is_letter_even = not (j % 2)

        if is_letter_even and i[letter_index] in vowels:
            is_striped_word = False
            break

        if not (is_letter_even or i[letter_index] in vowels):
            is_striped_word = False
            break

    if is_striped_word:
        striped_words_number += 1

print(f'\tЧисло полосатых слов: {striped_words_number}')
