# ProjectPulse AI - Financial Analytics Platform

Intelligent portfolio health and financial performance analyzer for Big 4 consulting firms.

## 🎯 Overview

ProjectPulse AI provides real-time visibility into project profitability, resource utilization, and financial health across the entire project lifecycle. Built with modern technologies and AI-powered insights using Gemma-4-26b.

**Live Demo**: [Coming Soon]

## 🏗️ Technology Stack

### Frontend
- **React 18** + TypeScript
- **Redux Toolkit** for state management
- **Recharts** for data visualization
- **Tailwind CSS** for styling
- **Vite** as build tool

### Backend
- **FastAPI** (Python 3.9+)
- **PostgreSQL 14+** for data persistence
- **SQLAlchemy** for ORM
- **Google Gemma AI** for intelligent insights
- **JWT** for authentication

### Deployment
- **Docker** for containerization
- **Vercel** for frontend deployment
- **Railway/Render** for backend deployment

## 📋 Features

### Dashboard & Analytics
- Real-time KPI cards (portfolio value, active projects, WIP, margin)
- Interactive charts (WIP trends, margin analysis, resource utilization)
- AI-powered insights and anomaly detection
- Financial forecasting and recommendations

### Project Management
- Create and track projects across full lifecycle
- Multi-engagement type support (T&M, Fixed-Cost, Retainer)
- Real-time financial health indicators
- Milestone and invoice tracking

### Resource Management
- Resource registry with billable rates
- Allocation heatmaps
- Utilization analysis
- Rate card management

### Financial Analytics
- WIP aging analysis (0-30, 31-60, 61-90, 90+ days)
- Margin tracking by project, resource, designation
- Invoicing pipeline and aging reports
- Funding and budget analysis

### Invoicing
- Automated invoice generation from milestones
- Invoice status tracking
- Payment recording and reconciliation
- Aging reports and collection status

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.9+
- PostgreSQL 14+ (or Docker)
- Git

### Local Development Setup

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/projectpulse-ai.git
cd projectpulse-ai
```

#### 2. Backend Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your database credentials

# Initialize database
psql -U postgres -f ../database/schema.sql

# Run backend server
uvicorn main:app --reload
# Backend runs on http://localhost:8000
```

#### 3. Frontend Setup
```bash
# In new terminal
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Start dev server
npm run dev
# Frontend runs on http://localhost:5173
```

#### 4. Access Application
- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

#### 5. Login Credentials
```
Email: admin@company.com
Password: password123
```

### Docker Setup (Recommended)

```bash
# Build and run with docker-compose
docker-compose up -d

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop services
docker-compose down
```

**Access**:
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- Database: localhost:5432

## 📚 API Documentation

### Core Endpoints

#### Authentication
```
POST   /api/v1/auth/login          # User login
GET    /api/v1/auth/me             # Get current user
POST   /api/v1/auth/logout         # User logout
```

#### Projects
```
GET    /api/v1/projects            # List all projects
POST   /api/v1/projects            # Create new project
GET    /api/v1/projects/{id}       # Get project details
PUT    /api/v1/projects/{id}       # Update project
DELETE /api/v1/projects/{id}       # Archive project
PATCH  /api/v1/projects/{id}/status # Update status
```

#### Resources
```
GET    /api/v1/resources           # List resources
POST   /api/v1/resources           # Create resource
GET    /api/v1/resources/{id}      # Get resource
DELETE /api/v1/resources/{id}      # Delete resource
GET    /api/v1/resources/utilization/heatmap # Utilization data
```

#### Analytics
```
GET    /api/v1/analytics/dashboard # Get dashboard KPIs
GET    /api/v1/analytics/wip       # WIP analysis
GET    /api/v1/analytics/margin    # Margin analysis
GET    /api/v1/analytics/invoicing # Invoicing status
GET    /api/v1/analytics/funding   # Funding analysis
```

**Full API Documentation**: Available at `http://localhost:8000/docs` (Swagger UI)

## 🌐 Deployment

### Frontend Deployment to Vercel

#### 1. Build Optimized Frontend
```bash
cd frontend
npm run build
```

#### 2. Deploy to Vercel
```bash
# Using Vercel CLI
npm install -g vercel
vercel
```

Or connect GitHub repository to Vercel for automatic deployments.

**Vercel Configuration** (vercel.json):
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "env": {
    "VITE_API_URL": "@projectpulse_api_url"
  }
}
```

### Backend Deployment Options

#### Option A: Railway.app (Recommended)
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

#### Option B: Render.com
1. Connect GitHub repository
2. Select backend folder
3. Configure environment variables
4. Deploy

#### Option C: Docker to Cloud Provider
```bash
# Build Docker image
docker build -t projectpulse-backend -f Dockerfile.backend .

# Push to registry
docker tag projectpulse-backend gcr.io/your-project/projectpulse-backend
docker push gcr.io/your-project/projectpulse-backend

# Deploy (example: Google Cloud Run)
gcloud run deploy projectpulse-backend --image gcr.io/your-project/projectpulse-backend
```

### Environment Variables (Production)

**Frontend (.env)**:
```
VITE_API_URL=https://your-backend-domain.com
VITE_APP_NAME=ProjectPulse AI
```

**Backend (.env)**:
```
DATABASE_URL=postgresql://user:password@prod-db:5432/projectpulse
SECRET_KEY=your-production-secret-key-min-32-chars
GEMMA_API_KEY=your-google-gemma-api-key
ALLOWED_ORIGINS=https://your-frontend-domain.com,https://your-app-domain.com
```

### Database Setup (Production)

#### PostgreSQL on Railway.app
```bash
# Railway automatically provisions PostgreSQL
# Connection string available in dashboard
```

#### Manual PostgreSQL Setup
```bash
# Create database
createdb projectpulse -U postgres

# Import schema
psql projectpulse < database/schema.sql

# Verify
psql projectpulse -c "\\dt"
```

## 🔐 Security Considerations

### Production Checklist
- [ ] Change all default passwords and secrets
- [ ] Enable HTTPS/SSL
- [ ] Configure CORS appropriately
- [ ] Set up database backups
- [ ] Enable database encryption
- [ ] Use environment variables for all secrets
- [ ] Implement rate limiting
- [ ] Set up API key rotation
- [ ] Enable audit logging
- [ ] Regular security updates

### Authentication
- JWT tokens with 30-minute expiration
- Refresh token mechanism (implement on backend)
- Secure password hashing with bcrypt
- Role-based access control (RBAC)

## 📊 Project Structure

```
projectpulse-ai/
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── store/           # Redux store
│   │   ├── services/        # API client
│   │   └── App.tsx
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
├── backend/
│   ├── routers/             # API route handlers
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── services.py          # Business logic
│   ├── auth.py              # Authentication
│   ├── config.py            # Configuration
│   ├── database.py          # Database setup
│   ├── main.py              # FastAPI app
│   └── requirements.txt
├── database/
│   └── schema.sql           # Database schema
├── docker-compose.yml       # Docker orchestration
├── Dockerfile.frontend      # Frontend Docker build
├── Dockerfile.backend       # Backend Docker build
└── README.md
```

## 🧪 Testing

### Frontend Testing
```bash
cd frontend
npm run test          # Run tests
npm run test:watch   # Watch mode
npm run lint         # Linting
```

### Backend Testing
```bash
cd backend
pytest                # Run tests
pytest --cov         # With coverage
```

## 📈 Performance Optimization

- **Frontend**: Code splitting, lazy loading, caching
- **Backend**: Database indexing, query optimization, pagination
- **Database**: Connection pooling, appropriate indexes
- **API**: Response compression, caching headers

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 Governance

This project follows governance principles from the ProjectPulse AI Constitution:

- **Principle I**: AI Transparency - All Gemma insights logged and auditable
- **Principle II**: Financial Integrity - DECIMAL precision, audit trails
- **Principle III**: Architecture - API contracts documented, backward compatible
- **Principle IV**: Testing - 80%+ coverage requirement

See [GOVERNANCE.md](GOVERNANCE.md) for details.

## 📞 Support

- **Documentation**: [Check wiki]
- **Issues**: GitHub Issues
- **Email**: support@projectpulse.ai
- **Slack**: [Join community]

## 📄 License

This project is proprietary software. All rights reserved.

## 🙏 Acknowledgments

- Big 4 consulting practices for domain expertise
- Google Gemma for AI capabilities
- Open source community for excellent libraries

---

**ProjectPulse AI v1.0.0**  
Last updated: September 28, 2026

**Ready to Deploy!** Follow the deployment guide above to get your instance live.
