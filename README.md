# WellnessConnect - AI-Powered Health Concierge Platform

WellnessConnect is a WhatsApp-based AI health concierge that pre-qualifies leads, schedules appointments, and provides personalized wellness recommendations for healthcare clinics.

## Features

- **AI Chatbot Integration**: WhatsApp Business integration with intelligent health assessments
- **Smart Lead Qualification**: Automatic categorization by treatment type and urgency
- **Personalized Content Delivery**: Targeted wellness content in multiple languages
- **Automated Follow-up**: Post-treatment care reminders and wellness plan delivery
- **White-label Ready**: Scalable solution for multiple clinics

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` and configure your settings
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python -m src.database.migrations`
5. Start the application: `python main.py`

## Docker Setup

```bash
docker-compose up -d
```

## API Documentation

- Webhook endpoint: `/api/webhook`
- Appointments: `/api/appointments`
- Analytics: `/api/analytics`
- White-label: `/api/whitelabel`

## Testing

```bash
pytest tests/
```

## License

Proprietary - The Wellness London