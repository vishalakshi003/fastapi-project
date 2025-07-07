import phonenumbers

def validate_phone(v: str) -> str:
    try:
        parsed = phonenumbers.parse(v, "IN")
        if not phonenumbers.is_valid_number(parsed):
            raise ValueError("Invalid phone number")
    except Exception:
        raise ValueError("Invalid phone number")
    return v


