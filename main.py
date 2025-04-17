from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date


print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Maestro 70007922896063621"))
print(get_mask_card_number('2022154687962548'))
print(get_mask_account('14751428002000200035'))