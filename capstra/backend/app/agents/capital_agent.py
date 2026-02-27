from app.services.prompt_builder import DISCLAIMER


def generate_capital_structure(risk_profile: str, capital_amount: float, experience_level: str) -> dict:
    profile_map = {
        "conservative": {"core": 0.8, "satellite": 0.2, "max_risk": 0.01},
        "moderate": {"core": 0.7, "satellite": 0.3, "max_risk": 0.015},
        "aggressive": {"core": 0.6, "satellite": 0.4, "max_risk": 0.02},
    }
    cfg = profile_map.get(risk_profile.lower(), profile_map["moderate"])
    max_risk_per_trade = capital_amount * cfg["max_risk"]

    return {
        "recommended_allocation": {
            "capital_preservation": round(capital_amount * cfg["core"], 2),
            "active_learning_trades": round(capital_amount * cfg["satellite"], 2),
        },
        "max_risk_per_trade": round(max_risk_per_trade, 2),
        "position_sizing_formula": "Position Size = Max Risk Per Trade / (Entry Price - Stop Loss)",
        "educational_explanation": (
            f"For a {experience_level} {risk_profile} trader, use smaller fixed risk per trade "
            "to survive variance and prioritize process consistency."
        ),
        "disclaimer": DISCLAIMER,
    }
