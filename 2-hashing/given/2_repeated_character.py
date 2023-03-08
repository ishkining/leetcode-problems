def repeated_character(s: str) -> str:
    seen = set()
    for character in s:
        if character in seen:
            return character
        seen.add(character)

    return ' '
