from app.models.user import User


DISCLAIMER = (
    "Disclaimer: This is educational guidance only, not investment advice. "
    "No guaranteed profits and no direct buy/sell recommendations."
)


def build_mentor_prompt(user: User, violations: list[str]) -> str:
    violation_text = ", ".join(violations[-5:]) if violations else "None"
    return (
        "You are a disciplined capital mentor. Encourage structure, not thrill.\n"
        "Only provide educational framing. Never provide direct stock tips.\n"
        f"User experience level: {user.experience_level}\n"
        f"Discipline score: {user.discipline_score}\n"
        f"Capital size: {user.capital_amount}\n"
        f"Recent violations: {violation_text}\n"
        f"{DISCLAIMER}"
    )


def is_blocked_message(message: str) -> bool:
    blocked = [
        "guaranteed profit strategy",
        "tell me what to buy now",
    ]
    lower = message.lower()
    return any(b in lower for b in blocked)
