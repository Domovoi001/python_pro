def get_hidden_card(card_number, base=4):
    last_digits = card_number[12:]
    return f'{"*" * base}{last_digits}'