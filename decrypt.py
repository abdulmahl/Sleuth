def lasso_letter(letter, shift_amount ):
    letter_code = ord(letter.lower())
    a_ascii = ord("a")
    alphabet_size = 26
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    decoded_letter = chr(true_letter_code)
    return decoded_letter

def lasso_word(word, shift_amount):
    decoded_word = ""
    for letter in word:
        decoded_letter = lasso_letter(letter, shift_amount)
        decoded_word += decoded_letter
    return decoded_word

print( "Shifting terra by 13 gives: \n" + lasso_word( "ybhvfn", 13 ))
print( "Shifting Ncevy by 13 gives: \n" + lasso_word( "Ncevy", 13 ) )
print( "Shifting gpvsui by 25 gives: \n" + lasso_word( "gpvsui", 25 ) )
print( "Shifting ugflgkg by -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lasso_word( "wjmmf", -1 ) )

