# Reglas:
# - El email debe contener "@"
# - El username debe tener al menos 5 caracteres

def validate_user(user):

    results = []

    # Validación de email
    email_valid = "@" in user["email"]

    if email_valid:
        results.append(("email_format", "PASS", "Email válido"))
    else:
        results.append(("email_format", "FAIL", "Email inválido"))

    # Validación de username
    username_valid = len(user["username"]) >= 5

    if username_valid:
        results.append(("username_length", "PASS", "Longitud válida"))
    else:
        results.append((
    "username_length",
    "FAIL",
    f"Username '{user['username']}' tiene {len(user['username'])} caracteres. Se requieren mínimo 5."
    ))

    # El usuario es válido solo si todas las reglas se cumplen
    is_valid = email_valid and username_valid

    return is_valid, results