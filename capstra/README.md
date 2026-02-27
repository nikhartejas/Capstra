# CAPSTRA (MVP v1)

**Tagline:** Structure Your Capital Before You Expose It

CAPSTRA is an AI-powered disciplined trading education platform for novice Indian retail traders.

## Stack
- Frontend: Next.js 14, TypeScript, TailwindCSS
- Backend: FastAPI, PostgreSQL, SQLAlchemy, Redis
- AI: OpenAI API with centralized prompt builder, educational-only guardrails
- Vector DB target: Supabase pgvector (ready for integration in later phase)
- Deployment: Docker + docker-compose

## Project Structure

```
capstra/
├── frontend/
├── backend/
├── docker-compose.yml
└── README.md
```

## Setup

### 1) Environment variables
Create `.env` in `capstra/` (optional for local compose):

```env
OPENAI_API_KEY=
OPENAI_MODEL=gpt-5
```

Backend env used:
- `DATABASE_URL`
- `JWT_SECRET`
- `REDIS_URL`
- `OPENAI_API_KEY`
- `OPENAI_MODEL`

Frontend env used:
- `NEXT_PUBLIC_API_URL`

### 2) Run with Docker

```bash
docker-compose up --build
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Health check: http://localhost:8000/health

## Local run (without Docker)

Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints Summary

### Auth
- `POST /auth/signup`
- `POST /auth/login`

### Core
- `GET /capital/structure/{user_id}`
- `POST /trade/log`
- `POST /mentor/chat`
- `GET /dashboard/{user_id}`

### Example trade log payload
```json
{
  "user_id": 1,
  "symbol": "RELIANCE",
  "entry_price": 100,
  "stop_loss": 95,
  "capital_used": 5000,
  "result": "loss"
}
```

## MVP features implemented
1. JWT signup/login and user profile storage (`risk_profile`, `capital_amount`, `experience_level`, `discipline_score`).
2. Capital Structure Agent with disclaimer guardrail.
3. Discipline scoring engine with +2 adherence / -5 violation bounded to 0..100.
4. Behavioral detection for overtrading, revenge trading, impulse risk.
5. Mentor chat endpoint with safety blocklist and educational framing.
6. Frontend landing and dashboard UI (score, violations, capital allocation, mentor chat).
7. SQLAlchemy models: `users`, `trades`, `discipline_events` with relationships.
8. Trade logging endpoint triggering behavior + discipline updates.
9. Testing script to seed a sample user and simulate 10 trades.

## Testing script
After backend is running:

```bash
python backend/scripts/simulate_trades.py
```

This creates/uses a sample user and logs 10 trades to validate score updates.
