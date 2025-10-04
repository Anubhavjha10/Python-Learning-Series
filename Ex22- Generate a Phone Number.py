def get_phone(country, area, first, last):
    return f"{first}-{last}-{country}-{area}"

phone_num = get_phone(country=+91, area=123, first=456, last=789)

print(phone_num)