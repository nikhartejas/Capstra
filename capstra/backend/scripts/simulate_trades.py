"""Seed a sample user and simulate 10 trades for discipline score validation."""
import random
import requests

BASE = "http://localhost:8000"


def main():
    signup = requests.post(
        f"{BASE}/auth/signup",
        json={
            "email": "sample@capstra.ai",
            "password": "Password123!",
            "risk_profile": "moderate",
            "capital_amount": 100000,
            "experience_level": "beginner",
        },
        timeout=10,
    )
    if signup.status_code not in (200, 400):
        raise RuntimeError(signup.text)

    login = requests.post(
        f"{BASE}/auth/login",
        json={"email": "sample@capstra.ai", "password": "Password123!"},
        timeout=10,
    )
    user_id = login.json()["user"]["id"]

    for i in range(10):
        result = "loss" if i % 3 == 0 else "win"
        stop = None if i % 4 == 0 else 95
        payload = {
            "user_id": user_id,
            "symbol": f"NSE_TEST_{i}",
            "entry_price": 100,
            "stop_loss": stop,
            "capital_used": random.choice([3000, 5000, 7000]),
            "result": result,
        }
        resp = requests.post(f"{BASE}/trade/log", json=payload, timeout=10)
        print(i + 1, resp.json())


if __name__ == "__main__":
    main()
