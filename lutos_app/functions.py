def capitalize_words(input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
