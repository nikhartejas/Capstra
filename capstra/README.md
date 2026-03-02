# CAPSTRA (MVP V1)

**Tagline:** Education Before Exposure

Capstra is a structured pre-market education SaaS platform designed to prepare Indian retail participants before they deploy capital into financial markets. It is a risk-first readiness system, not a trading signal or stock recommendation platform.

## Product Positioning
- **Primary users:** Indian retail participants (new demat account holders, novice traders, working professionals, Tier 2 & Tier 3 aspirants).
- **Secondary users:** Young professionals and parents guiding children into financial markets.
- **Core transformation:** Users move from emotionally driven market curiosity to disciplined, risk-aware, structured market readiness.

## MVP V1 Scope
### Included
1. User authentication (email + OTP or magic link).
2. Onboarding and behavioral risk profiling.
3. Financial readiness assessment engine.
4. 4-5 structured foundation learning modules.
5. MCQ-based quiz engine.
6. Risk awareness + readiness scoring.
7. Rule-based track recommendation (Investor Track / Trader Track).
8. Upgrade unlock logic.
9. Razorpay integration for India.
10. Downloadable certificate (PDF).
11. Admin dashboard for content and scoring thresholds.

### Excluded in V1
- Live mentoring.
- Trading journal.
- Advanced analytics.
- Broker integration.
- Community forums.
- Mobile app.

## Technology Stack (Target)
- **Frontend:** Next.js 14 (App Router), TypeScript, TailwindCSS, shadcn/ui, Zustand.
- **Backend:** Supabase (Auth + PostgreSQL), Prisma ORM, Next.js server actions/API routes.
- **AI layer:** OpenAI API only for behavioral feedback summaries.
- **Recommendation logic:** Rule-based (non-autonomous, non-RAG).

## Architecture
Modular clean architecture in a scalable monolith:
- Presentation layer
- Domain logic layer
- Application services layer
- Infrastructure layer

Designed to scale to the first 100k users.

## UX and Tone
- Institutional, minimal, serious.
- Dark professional theme with dashboard-style layouts.
- Fully responsive and SEO-aware landing pages.
- English first, architecture-ready for multilingual expansion.

## Guardrails
- No stock tips, calls, or prediction logic anywhere in the system.
- Reinforces a calm, risk-first mentorship style.
- Strictly “Education Before Exposure.”

## Deployment
- Vercel for frontend + server actions.
- Supabase hosted database.
- `.env.example` template included.
- Production-oriented baseline security practices.
- Docker is not required for MVP.

## Monetization
- Entry Program: ₹999–₹2,499.
- Track Upgrade: ₹4,999–₹9,999.
- Role-based content unlocking after payment confirmation.

## Long-term Vision
Capstra aims to become India’s standard pre-market readiness certification layer, with a path toward broker partnerships, certification licensing, multilingual expansion, and advanced risk engines.
