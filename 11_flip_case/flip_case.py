def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    flip = ""
    for char in phrase:
        if char.lower() == to_swap:
            if char.isupper():
                flip += char.lower()
            else:
                flip += char.upper()
        else:
            flip += char
    return flip