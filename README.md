# AI Booking System for Small Businesses

A comprehensive, AI-powered booking system built with Python and FastAPI, designed specifically for small businesses. Features intelligent scheduling, natural language processing for booking queries, and automated notifications.

## ✨ Features

### 📋 Core Features
- 📅 Calendar management with staff availability
- 📝 Appointment scheduling and management
- 💳 Payment processing with Stripe integration
- 🔔 Automated email confirmations and reminders
- 🤖 AI-powered chatbot for natural language booking queries
- 📊 Business analytics and insights
- 👥 Multi-staff and multi-service support
- 🔐 User authentication and authorization

### 🧠 AI Capabilities
- Natural language booking queries ("I need a haircut on Monday morning")
- Intelligent availability suggestions
- Conversation-based booking assistance
- Business performance insights
- Automated booking detail extraction
- Availability slot ranking

## 🛠 Tech Stack

- **Backend**: FastAPI, Python 3.11
- **Database**: Supabase (PostgreSQL)
- **AI**: OpenAI GPT-4
- **Payments**: Stripe
- **Email**: SMTP (Gmail)
- **Deployment**: Docker, Docker Compose

## 📁 Project Structure

```
ai-booking-system/
├── app/
│   ├── routes/
│   │   ├── users.py           # User authentication
│   │   ├── services.py        # Service management
│   │   ├── staff.py           # Staff management
│   │   ├── bookings.py        # Booking operations
│   │   ├── payments.py        # Payment processing
│   │   ├── availability.py    # Availability management
│   │   ├── business.py        # Business management
│   │   └── ai.py              # AI endpoints
│   ├── services/
│   │   ├── ai.py              # AI service with OpenAI
│   │   ├── business.py        # Business logic
│   │   └── analytics.py       # Analytics service
│   ├── utils/
│   │   ├── auth.py            # Authentication utilities
│   │   ├── notifications.py   # Email notifications
│   │   └── scheduling.py      # Background jobs
│   ├── main.py                # FastAPI app
│   ├── models.py              # Pydantic models
│   └── database.py            # Database connection
├── database/
│   └── schema.sql             # Database schema
├── config.py                  # Configuration
├── requirements.txt           # Dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (optional)
- Supabase account
- OpenAI API key
- Stripe account

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-booking-system.git
cd ai-booking-system
```

2. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up Supabase**
   - Create a Supabase project
   - Run the schema from `database/schema.sql` in your Supabase SQL editor
   - Get your API URL and key

5. **Run the application**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Using Docker

```bash
docker-compose up --build
```

## 📚 API Endpoints

### Authentication
- `POST /api/users/register` - Register new user
- `POST /api/users/login` - Login user
- `GET /api/users/me` - Get current user
- `PUT /api/users/me` - Update profile

### Services
- `POST /api/services/` - Create service
- `GET /api/services/{business_id}` - List services
- `GET /api/services/{service_id}/detail` - Get service details
- `PUT /api/services/{service_id}` - Update service
- `DELETE /api/services/{service_id}` - Delete service

### Staff
- `POST /api/staff/` - Add staff member
- `GET /api/staff/{business_id}` - List staff
- `GET /api/staff/{staff_id}/detail` - Get staff details
- `PUT /api/staff/{staff_id}` - Update staff
- `POST /api/staff/{staff_id}/services` - Add service to staff
- `DELETE /api/staff/{staff_id}` - Delete staff

### Availability
- `POST /api/availability/` - Set availability
- `GET /api/availability/{staff_id}` - Get availability
- `GET /api/availability/service/{service_id}/available-slots` - Get available slots
- `GET /api/availability/staff/{staff_id}/available-dates` - Get available dates

### Bookings
- `POST /api/bookings/` - Create booking
- `GET /api/bookings/{business_id}` - List bookings
- `GET /api/bookings/customer/{customer_id}` - Customer bookings
- `GET /api/bookings/{booking_id}/detail` - Get booking details
- `PUT /api/bookings/{booking_id}` - Update booking
- `GET /api/bookings/staff/{staff_id}/upcoming` - Staff upcoming bookings

### Payments
- `POST /api/payments/` - Create payment
- `GET /api/payments/booking/{booking_id}` - Get payment
- `POST /api/payments/{payment_id}/refund` - Refund payment
- `GET /api/payments/business/{business_id}/revenue` - Get revenue

### Business Management
- `POST /api/business/` - Create business
- `GET /api/business/{business_id}` - Get business details
- `PUT /api/business/{business_id}` - Update business
- `GET /api/business/owner/{owner_id}` - Get owner's businesses
- `GET /api/business/{business_id}/stats` - Get business statistics

### AI
- `POST /api/ai/process-booking-query` - Process natural language query
- `POST /api/ai/chat` - Chat with AI assistant
- `POST /api/ai/suggest-availability` - Get AI suggestions
- `GET /api/ai/business/{business_id}/analytics` - Business insights
- `POST /api/ai/extract-booking-details` - Extract booking details

## 🔧 Environment Variables

```env
# Supabase
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# OpenAI
OPENAI_API_KEY=your_openai_key

# Stripe
STRIPE_SECRET_KEY=your_stripe_secret
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable

# Email
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# JWT
SECRET_KEY=your_secret_key

# URLs
API_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000
```

## 📝 Usage Examples

### Register a User
```bash
curl -X POST "http://localhost:8000/api/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "name": "John Doe",
    "password": "secure_password"
  }'
```

### Create a Business
```bash
curl -X POST "http://localhost:8000/api/business/" \
  -H "Content-Type: application/json" \
  -d '{
    "owner_id": "user_uuid",
    "name": "My Salon",
    "phone": "123-456-7890",
    "email": "salon@example.com",
    "address": "123 Main St",
    "city": "New York",
    "timezone": "America/New_York"
  }'
```

### Process Booking Query
```bash
curl -X POST "http://localhost:8000/api/ai/process-booking-query" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "I need a haircut on Monday morning",
    "business_id": "business_uuid"
  }'
```

### Chat with AI
```bash
curl -X POST "http://localhost:8000/api/ai/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "business_uuid",
    "message": "What time slots are available next week?"
  }'
```

## 🗄️ Database Schema

The system uses the following tables:
- `users` - User accounts
- `businesses` - Business information
- `services` - Services offered
- `staff` - Staff members
- `staff_services` - Many-to-many relationship
- `availability` - Staff availability schedules
- `bookings` - Appointment bookings
- `payments` - Payment records
- `notifications` - Email notifications log
- `ai_conversations` - AI conversation history

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 💬 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 🎯 Future Features

- [ ] SMS notifications
- [ ] Video call integration
- [ ] Advanced analytics dashboard
- [ ] Mobile app (React Native)
- [ ] Multi-language support
- [ ] Webhook support
- [ ] API rate limiting
- [ ] Admin dashboard
- [ ] Review/rating system
- [ ] Waitlist management
