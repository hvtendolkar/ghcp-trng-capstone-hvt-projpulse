# ProjectPulse AI - PRD
## Intelligent Portfolio Health & Financial Performance Analyzer

**Product Name:** ProjectPulse AI  
**Version:** 1.0  
**Date:** September 27, 2026  
**Target Users:** Partners, Directors, Associate Directors, Senior Managers at Big 4 Firms  
**Status:** Requirements Definition

---

## 1. Overview and Goals

### 1.1 Executive Summary
ProjectPulse AI is an intelligent portfolio health and financial performance analyzer designed to help senior leadership at Big 4 IT consulting firms manage the financial aspects of their project portfolios. The platform enables real-time visibility into project profitability, resource utilization, and financial health across the entire project lifecycle—from opportunity identification through contract completion.

### 1.2 Problem Statement
Senior managers at Big 4 firms currently lack a centralized, AI-driven platform to:
- Track project financial metrics across the opportunity-to-completion lifecycle
- Visualize real-time project profitability and margin performance
- Manage resource allocation and billable hour tracking against WBS codes
- Identify financial risks (WIP aging, funding shortfalls, margin erosion)
- Predict invoicing status and cash flow implications
- Make data-driven decisions on resource planning and project pricing

### 1.3 Goals
1. **Financial Transparency:** Provide real-time dashboards showing project profitability, margin, WIP, and invoicing status
2. **Intelligent Insights:** Use AI to detect anomalies, predict invoice delays, and recommend optimization actions
3. **Operational Efficiency:** Automate financial tracking, WBS reconciliation, and milestone-based invoicing
4. **Resource Optimization:** Enable data-driven decisions on resource allocation, skill mix, and billing rates
5. **Risk Management:** Proactively identify financial risks (aging WIP, funding constraints, margin threats)

### 1.4 Key Benefits
- **Reduced Financial Risk:** Early detection of WIP aging and funding issues
- **Improved Margins:** AI-driven insights on resource allocation and pricing optimization
- **Time Savings:** Automated invoice tracking and WBS reconciliation
- **Better Decision-Making:** Comprehensive financial dashboards and predictive analytics
- **Scalability:** Support for multi-project portfolio management across large consulting firms

---

## 2. Architecture

### 2.1 High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      React-TypeScript Frontend                   │
│  (Dashboards, Forms, Reports, Real-time Analytics Visualizations)|
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FastAPI Backend (Python)                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ • Project Management APIs                              │   │
│  │ • Resource & Billing APIs                              │   │
│  │ • WBS Tracking APIs                                    │   │
│  │ • Invoice & Milestone Management APIs                  │   │
│  │ • Financial Calculation & Analytics APIs               │   │
│  └─────────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                    ┌──────┴──────┐
                    ▼             ▼
        ┌─────────────────┐  ┌──────────────────┐
        │   PostgreSQL    │  │  Gemma AI Engine │
        │    Database     │  │  (Google AI API) │
        └─────────────────┘  └──────────────────┘
```

### 2.2 Data Ingestion & Retrieval Flow

```
┌────────────────────────────────────────────────────────────────┐
│  DATA INGESTION FLOW                                            │
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User Input (Web Form)                                         │
│  ├─ Project Details (Type, Dates, Funding)                    │
│  ├─ Resource List (Name, Designation, Billable Rate)          │
│  ├─ Monthly Allocation (Hours/Month by Resource)              │
│  └─ Billing Config (WBS Code, Invoice Terms)                  │
│            ▼                                                    │
│  FastAPI Endpoints                                             │
│  ├─ Validate Input                                             │
│  ├─ Normalize Data                                             │
│  └─ Store in PostgreSQL                                        │
│            ▼                                                    │
│  Gemma AI Processing                                           │
│  ├─ Analyze Project Financials                                │
│  ├─ Predict Risks & Anomalies                                 │
│  └─ Generate Recommendations                                  │
│            ▼                                                    │
│  Database Storage                                              │
│  └─ Persist Insights & Audit Trail                            │
│                                                                  │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│  DATA RETRIEVAL & ANALYTICS FLOW                                │
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Dashboard Request (Frontend)                                  │
│            ▼                                                    │
│  FastAPI Analytics Endpoints                                   │
│  ├─ Query Aggregated Financials                               │
│  ├─ Calculate KPIs (WIP, Margin, Invoicing %)                 │
│  └─ Fetch AI Insights                                         │
│            ▼                                                    │
│  Database Queries                                              │
│  ├─ Raw Project Data                                           │
│  ├─ Resource Allocations                                       │
│  ├─ Invoice Milestones                                         │
│  └─ WBS Tracking Records                                       │
│            ▼                                                    │
│  AI Enrichment (Optional)                                      │
│  ├─ Real-time Anomaly Detection                               │
│  ├─ Predictive Invoicing Analysis                             │
│  └─ Optimization Recommendations                              │
│            ▼                                                    │
│  Response Formatting                                           │
│  └─ JSON to Frontend for Visualization                        │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
```

### 2.3 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | React 18+, TypeScript, Redux/Context API | User Interface, State Management |
| **Backend** | Python 3.9+, FastAPI | REST API, Business Logic |
| **AI/ML** | Gemma-4-26b-a4b-it (Google AI Studio) | Financial Analysis, Anomaly Detection, Recommendations |
| **Database** | PostgreSQL 14+ | Persistent Data Storage |
| **Authentication** | JWT Tokens | API Security & User Sessions |
| **Deployment** | Docker, Kubernetes (Future) | Containerization & Orchestration |

---

## 3. Detailed Requirements by Component

### 3.1 Frontend (React-TypeScript)

#### 3.1.1 Core Pages & Features

**A. Dashboard/Home Page**
- **Overview Cards:**
  - Total Portfolio Value (in billable hours or revenue)
  - Active Projects Count
  - Total WIP Amount
  - Average Margin (%)
  - Invoicing Status Summary

- **Charts & Visualizations:**
  - Project Portfolio Distribution (Pie/Donut: Fixed-Cost vs. T&M)
  - WIP Trend Over Time (Line Chart)
  - Margin Performance by Project (Bar Chart)
  - Resource Utilization Heatmap (by Designation & Billable Rate)
  - Invoicing Pipeline (Stage breakdown)

- **AI Insights Panel:**
  - Top Risks (WIP Aging, Funding Gaps)
  - Anomalies Detected (margin dips, hour overruns)
  - Optimization Recommendations
  - Predictive Alerts (e.g., "3 projects at risk of margin erosion")

**B. Project Management Page**
- **Project List View:**
  - Table with: Project Name, Status (Opportunity/Active/Completed), Financial Health (Color indicator), Margin, WIP, Last Updated
  - Filters: By Status, By Profitability, By Date Range, By Resource Lead
  - Sort: By Name, By Margin, By WIP, By Status

- **Project Creation Wizard (Multi-step Form):**
  - Step 1: Basic Info (Name, Code, Description, Engagement Type, Start/End Dates)
  - Step 2: Billing Model (Fixed-Cost / T&M, Budget, Contract Terms)
  - Step 3: Resource Allocation (Add resources, set designation, billable rate, monthly hours)
  - Step 4: Funding & Terms (Available Funding, Invoice Milestones, Payment Terms)
  - Step 5: Review & Submit

- **Project Detail Page:**
  - Overview: Project name, status, dates, financial summary
  - Resource Tab: List of resources, allocation hours, billable rates, YTD billed hours
  - Financials Tab: Revenue, Cost, Margin, WIP, Invoicing Status
  - WBS Tab: WBS codes, hours tracked, cost allocation
  - Invoices Tab: Milestone list, invoice status, dates
  - AI Insights Tab: AI-generated analysis, risks, recommendations

**C. Resource Management Page**
- **Resource Registry:**
  - Table: Resource Name, Designation, Default Billable Rate, Projects Assigned, YTD Hours Billed
  - Add/Edit/Delete Resource functionality
  - Bulk Import (CSV)

- **Resource Allocation View:**
  - Heatmap: Resources vs. Projects, showing allocated hours/month
  - Utilization Analysis: Over-allocated vs. under-allocated resources
  - Rate Card Management: By Designation, by Client, historical rates

**D. Financial Analytics Page**
- **KPI Dashboard:**
  - WIP Analysis: Total WIP, WIP by Age Bucket (0-30, 31-60, 61-90, 90+ days), WIP Trend
  - Margin Analysis: By Project, By Resource, By Designation
  - Invoicing Analysis: Invoiced vs. Uninvoiced, Invoice Aging, Collection Status
  - Funding Analysis: Available Funding, Utilization Rate, Shortfall Risk

- **Reports:**
  - Project Profitability Report (all projects ranked by margin %)
  - Resource Utilization Report (hours logged vs. allocated)
  - WIP Aging Report (sortable by age, risk level)
  - Invoicing & Receivables Report (aging, payment status)
  - Downloadable formats: PDF, Excel, CSV

**E. Invoice & Milestone Tracking Page**
- **Invoice Master List:**
  - Table: Invoice #, Project, Amount, Date, Due Date, Status (Draft/Issued/Paid/Overdue)
  - Filter/Search by: Status, Date Range, Project, Amount Range
  - Bulk Actions: Mark as Sent, Mark as Paid, Generate Reminder

- **Invoice Detail View:**
  - Summary: Invoice #, Project, Amount, Tax, Total
  - Line Items: Resource name, designation, hours, rate, subtotal
  - Milestones: Associated project milestones
  - Payment Tracking: Invoice date, due date, payment date, status
  - Document Attachment: Uploaded PDF/attachment

- **Milestone Management:**
  - Create/Edit Milestone: Trigger, Percentage Allocation, Invoice Amount
  - Auto-Generate Invoices: Based on milestone completion

**F. Settings & Configuration Page**
- **System Settings:**
  - Company Details (Name, Logo, Currency, Fiscal Year)
  - Billing Configuration (Invoice Terms, Default Payment Days)
  - Financial Year Setup

- **User Management:**
  - User List: Name, Role, Status, Last Login
  - Add/Edit/Delete Users
  - Role-Based Access Control (Partner, Director, AD, Senior Manager, Analyst, Viewer)

- **Integration Settings:**
  - Google AI API Key Configuration
  - Database Connection Settings
  - Audit Trail Configuration

#### 3.1.2 UI/UX Requirements
- **Responsive Design:** Mobile-friendly on tablets, optimized for desktop (1920x1080+)
- **Accessibility:** WCAG 2.1 AA compliance, keyboard navigation, screen reader support
- **Performance:** Page load < 2 seconds, smooth chart animations, lazy-loaded components
- **Theme:** Light/Dark mode support
- **Real-time Updates:** WebSocket support for live data refresh (optional, Phase 2)

---

### 3.2 Backend (Python/FastAPI)

#### 3.2.1 Core API Endpoints

**A. Project Management Endpoints**
```
POST   /api/v1/projects                    # Create new project
GET    /api/v1/projects                    # List all projects
GET    /api/v1/projects/{project_id}       # Get project details
PUT    /api/v1/projects/{project_id}       # Update project
DELETE /api/v1/projects/{project_id}       # Archive/delete project
PATCH  /api/v1/projects/{project_id}/status # Update project status
```

**B. Resource Management Endpoints**
```
POST   /api/v1/resources                   # Create resource
GET    /api/v1/resources                   # List resources
GET    /api/v1/resources/{resource_id}     # Get resource details
PUT    /api/v1/resources/{resource_id}     # Update resource
DELETE /api/v1/resources/{resource_id}     # Archive resource
GET    /api/v1/resources/utilization       # Get utilization analytics
```

**C. Resource Allocation Endpoints**
```
POST   /api/v1/allocations                 # Add resource to project
GET    /api/v1/allocations                 # List allocations
PUT    /api/v1/allocations/{allocation_id} # Update allocation
DELETE /api/v1/allocations/{allocation_id} # Remove allocation
GET    /api/v1/allocations/heatmap         # Get heatmap data
```

**D. WBS Tracking Endpoints**
```
POST   /api/v1/wbs                         # Create WBS code
GET    /api/v1/wbs                         # List WBS codes
PUT    /api/v1/wbs/{wbs_id}                # Update WBS
DELETE /api/v1/wbs/{wbs_id}                # Delete WBS
POST   /api/v1/wbs/{wbs_id}/hours          # Log billed hours to WBS
GET    /api/v1/wbs/{wbs_id}/tracking       # Get WBS tracking details
```

**E. Invoice & Milestone Endpoints**
```
POST   /api/v1/milestones                  # Create milestone
GET    /api/v1/milestones                  # List milestones
PUT    /api/v1/milestones/{milestone_id}   # Update milestone
DELETE /api/v1/milestones/{milestone_id}   # Delete milestone
PATCH  /api/v1/milestones/{milestone_id}/status # Update milestone status

POST   /api/v1/invoices                    # Create invoice
GET    /api/v1/invoices                    # List invoices
GET    /api/v1/invoices/{invoice_id}       # Get invoice details
PUT    /api/v1/invoices/{invoice_id}       # Update invoice
DELETE /api/v1/invoices/{invoice_id}       # Delete invoice
PATCH  /api/v1/invoices/{invoice_id}/status # Update invoice status
POST   /api/v1/invoices/{invoice_id}/payment # Record payment
GET    /api/v1/invoices/aging              # Get aging report
```

**F. Financial Analytics Endpoints**
```
GET    /api/v1/analytics/dashboard         # Get dashboard KPIs
GET    /api/v1/analytics/wip               # Get WIP analysis
GET    /api/v1/analytics/margin            # Get margin analysis
GET    /api/v1/analytics/invoicing         # Get invoicing status
GET    /api/v1/analytics/funding           # Get funding analysis
GET    /api/v1/analytics/project/{id}      # Get project financials
```

**G. AI Insights Endpoints**
```
POST   /api/v1/ai/analyze-project          # AI analysis of project
POST   /api/v1/ai/detect-anomalies         # Anomaly detection
POST   /api/v1/ai/recommendations          # Get recommendations
POST   /api/v1/ai/predict-risks            # Risk prediction
GET    /api/v1/ai/insights                 # Retrieve stored insights
```

**H. Authentication & Authorization Endpoints**
```
POST   /api/v1/auth/login                  # User login
POST   /api/v1/auth/logout                 # User logout
POST   /api/v1/auth/refresh                # Refresh JWT token
GET    /api/v1/auth/me                     # Get current user info
```

#### 3.2.2 Business Logic Components

**A. Financial Calculations Engine**
- **WIP Calculation:** Sum of (Resource Cost * Billed Hours Not Yet Invoiced)
- **Margin Calculation:** (Revenue - Total Cost) / Revenue * 100
- **Cost Calculation:** Sum of (Billable Rate * Billed Hours) for all resources
- **Revenue Calculation:** Contract Value (Fixed) or Sum of (Billable Rate * Hours Allocated) (T&M)
- **Invoice Amount:** Based on Milestone % allocation or Actual Hours
- **Funding Analysis:** Available Funding - (Invoiced + WIP)

**B. WBS Tracking Logic**
- Map each billed hour to a specific WBS code
- Aggregate hours and costs by WBS code
- Compare WBS allocation vs. actual
- Identify variance and over/under-utilization

**C. Invoice Generation Logic**
- Create invoices based on milestones (percentage or date-triggered)
- Auto-calculate line items from resource allocation and hours
- Apply discounts (if applicable)
- Track invoice status: Draft → Issued → Paid

**D. Anomaly Detection Logic**
- Identify WIP > X days old without invoicing
- Flag margin < target threshold
- Detect resource over-allocation
- Identify funding shortfalls
- Alert on invoice payment delays

**E. Risk Assessment Logic**
- Score project risk: (WIP Aging, Margin Erosion, Funding Gap, Schedule Risk)
- Classify: Low, Medium, High, Critical
- Generate alerts with recommended actions

#### 3.2.3 Data Models (Core Entities)

**Project**
```
- project_id (UUID)
- name (String)
- code (String)
- description (Text)
- status (Enum: Opportunity, Active, On-Hold, Completed, Archived)
- engagement_type (Enum: Time & Material, Fixed-Cost, Retainer)
- start_date (Date)
- end_date (Date)
- contract_value (Decimal) [for Fixed-Cost]
- budget (Decimal)
- available_funding (Decimal)
- currency (String: USD, EUR, etc.)
- client_name (String)
- billing_manager (String)
- created_by (UUID)
- created_at (Timestamp)
- updated_at (Timestamp)
```

**Resource**
```
- resource_id (UUID)
- name (String)
- email (String)
- designation (String: Partner, Director, AD, Senior Manager, Manager, Senior Consultant, Consultant, Analyst)
- default_billable_rate (Decimal)
- cost_rate (Decimal)
- availability_status (Enum: Available, Partially Available, Not Available)
- skills (JSON Array)
- created_at (Timestamp)
- updated_at (Timestamp)
```

**ResourceAllocation**
```
- allocation_id (UUID)
- project_id (UUID, FK)
- resource_id (UUID, FK)
- designation (String) [may differ from resource's default]
- billable_rate_override (Decimal) [if different from resource's default]
- monthly_hours_allocation (Decimal)
- start_date (Date)
- end_date (Date)
- total_allocated_hours (Decimal)
- YTD_billed_hours (Decimal)
- created_at (Timestamp)
- updated_at (Timestamp)
```

**WBSCode**
```
- wbs_id (UUID)
- project_id (UUID, FK)
- code (String, e.g., "1.1.2")
- description (String)
- allocated_hours (Decimal)
- allocated_budget (Decimal)
- created_at (Timestamp)
- updated_at (Timestamp)
```

**BilledHours**
```
- billed_hours_id (UUID)
- allocation_id (UUID, FK)
- wbs_id (UUID, FK)
- invoice_id (UUID, FK, nullable)
- hours_logged (Decimal)
- date_logged (Date)
- description (String)
- cost_amount (Decimal) [hours_logged * billable_rate]
- status (Enum: Draft, Approved, Billed, Invoiced)
- created_at (Timestamp)
- updated_at (Timestamp)
```

**Milestone**
```
- milestone_id (UUID)
- project_id (UUID, FK)
- name (String)
- description (Text)
- trigger_type (Enum: Date, Percentage Complete, Manual)
- trigger_value (String or Decimal)
- invoice_percentage (Decimal) [% of total contract value to invoice]
- invoice_amount (Decimal) [fixed amount or calculated]
- target_date (Date)
- actual_date (Date, nullable)
- status (Enum: Pending, Triggered, Invoiced, Completed)
- created_at (Timestamp)
- updated_at (Timestamp)
```

**Invoice**
```
- invoice_id (UUID)
- invoice_number (String, unique)
- project_id (UUID, FK)
- milestone_id (UUID, FK, nullable)
- invoice_date (Date)
- due_date (Date)
- total_amount (Decimal)
- tax_amount (Decimal)
- tax_rate (Decimal, %)
- discount_amount (Decimal, nullable)
- net_amount (Decimal) [total_amount - discount + tax]
- status (Enum: Draft, Issued, Sent, Partially Paid, Paid, Overdue, Cancelled)
- payment_date (Date, nullable)
- payment_method (Enum: Bank Transfer, Check, Card, etc.)
- notes (Text)
- attachment_url (String, nullable)
- created_by (UUID)
- created_at (Timestamp)
- updated_at (Timestamp)
```

**FinancialInsight** (AI-Generated)
```
- insight_id (UUID)
- project_id (UUID, FK)
- insight_type (Enum: Anomaly, Risk, Recommendation, Prediction)
- title (String)
- description (Text)
- severity (Enum: Low, Medium, High, Critical)
- recommendation (Text)
- created_by_model (String: "Gemma-4-26b")
- created_at (Timestamp)
- ttl (Integer, seconds before auto-delete)
```

---

### 3.3 AI Engine (Gemma-4-26b-a4b-it)

#### 3.3.1 AI Capabilities

**A. Project Financial Analysis**
- Analyze project profitability trajectory
- Assess resource allocation efficiency
- Identify cost overruns and margin threats
- Predict project completion costs

**B. Anomaly Detection**
- WIP Aging anomalies (identify invoices stuck in WIP > target days)
- Margin anomalies (sudden drops or concerning trends)
- Resource utilization anomalies (over-allocation, idle resources)
- Invoice payment anomalies (late payments, overdue amounts)

**C. Predictive Analytics**
- Predict invoice payment dates (based on historical patterns)
- Forecast project completion cost and margin
- Identify projects at risk of profitability erosion
- Predict resource bottlenecks

**D. Optimization Recommendations**
- Resource reallocation suggestions to improve margin
- Pricing recommendations for future engagements
- Billing strategy suggestions (milestone timing, T&M vs. Fixed)
- Cost reduction opportunities

**E. Natural Language Insights**
- Generate executive summaries of portfolio health
- Explain anomalies in plain English
- Provide actionable recommendations
- Create alert narratives for stakeholders

#### 3.3.2 AI Integration Points

**Trigger Points for AI Analysis:**
1. New project creation (initial financial analysis)
2. Monthly data refresh (trend analysis, anomaly detection)
3. Resource allocation changes (impact analysis)
4. Invoice milestone completion (financial forecast)
5. On-demand: User requests AI analysis via UI

**Gemma AI Processing Flow:**
```
Input Data (Project Financials)
         ↓
Prompt Engineering (Structured Prompts)
         ↓
Gemma API Call (Google AI Studio)
         ↓
Response Processing (Parse JSON/Text)
         ↓
Store Insights (PostgreSQL)
         ↓
Surface to UI (Dashboard, Alerts, Reports)
```

#### 3.3.3 Prompts & Templates

**Example Prompts:**
- "Analyze project {project_name} financial health. Current WIP: ${wip}, Margin: {margin}%, Resource Cost: ${cost}. Provide 3 specific risks and 2 recommendations."
- "Detect anomalies in invoice aging for portfolio. Projects with invoice {aging_days} days old: {project_list}. Which are concerning?"
- "Recommend optimal resource allocation for project {project_id} to maximize margin while meeting timeline."

---

### 3.4 Database Schema

#### 3.4.1 PostgreSQL Schema Overview

**Tables:**
- `projects`
- `resources`
- `resource_allocations`
- `wbs_codes`
- `billed_hours`
- `milestones`
- `invoices`
- `invoice_line_items`
- `financial_insights`
- `users`
- `audit_logs`

**Indexes:**
- project_id, resource_id, status (composite) on billed_hours
- invoice_id, status, due_date on invoices
- project_id, created_at on financial_insights (for time-range queries)

**Relationships:**
```
Projects
  ├── 1:M ResourceAllocations
  ├── 1:M WBSCodes
  ├── 1:M Milestones
  ├── 1:M Invoices
  └── 1:M FinancialInsights

Resources
  └── 1:M ResourceAllocations

ResourceAllocations
  └── 1:M BilledHours

BilledHours
  ├── N:1 WBSCodes
  └── N:1 Invoices

Milestones
  └── 1:M Invoices

Invoices
  └── 1:M InvoiceLineItems
```

---

## 4. Configuration and Environment Variables

### 4.1 Backend Configuration (.env)

```
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/projectpulse_db
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=40

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_PREFIX=/api/v1
DEBUG=False
LOG_LEVEL=INFO

# Security
JWT_SECRET_KEY=your-secret-key-change-this-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com

# Google AI / Gemma
GOOGLE_AI_API_KEY=your-google-ai-api-key
GEMMA_MODEL_NAME=gemma-4-26b-a4b-it
GEMMA_API_ENDPOINT=https://generativelanguage.googleapis.com/v1beta/models

# Application
APP_NAME=ProjectPulse AI
APP_VERSION=1.0.0
CURRENCY_DEFAULT=USD
FISCAL_YEAR_START_MONTH=1

# Email (for notifications, Phase 2)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@company.com
SMTP_PASSWORD=your-password

# Logging
LOG_FILE_PATH=/var/log/projectpulse/app.log
LOG_MAX_BYTES=10485760
LOG_BACKUP_COUNT=5

# Performance
REQUEST_TIMEOUT_SECONDS=30
CACHE_TTL_SECONDS=300
```

### 4.2 Frontend Configuration (.env)

```
# API
REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_API_TIMEOUT=30000

# Environment
REACT_APP_ENV=development
REACT_APP_VERSION=1.0.0

# Feature Flags
REACT_APP_ENABLE_DARK_MODE=true
REACT_APP_ENABLE_EXPORT_PDF=true
REACT_APP_ENABLE_REAL_TIME_UPDATES=false

# Analytics (Future)
REACT_APP_ANALYTICS_ID=your-analytics-id
```

---

## 5. New Dependencies

### 5.1 Backend (Python) Dependencies

**Core Framework:**
```
fastapi==0.104.1
uvicorn==0.24.0
python-dotenv==1.0.0
pydantic==2.5.0
pydantic-settings==2.1.0
```

**Database:**
```
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
alembic==1.12.1
```

**Authentication & Security:**
```
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.1.1
```

**AI/ML Integration:**
```
google-generativeai==0.3.0
```

**Utilities:**
```
python-multipart==0.0.6
python-dateutil==2.8.2
requests==2.31.0
pytz==2023.3
```

**Testing:**
```
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
httpx==0.25.2
```

**Development:**
```
black==23.12.0
flake8==6.1.0
isort==5.13.2
mypy==1.7.1
```

**Production:**
```
gunicorn==21.2.0
```

### 5.2 Frontend (React-TypeScript) Dependencies

**Core:**
```
react==18.2.0
react-dom==18.2.0
typescript==5.3.3
```

**State Management:**
```
@reduxjs/toolkit==1.9.7
react-redux==8.1.3
```

**UI Components & Charts:**
```
@mui/material==5.14.13
@mui/icons-material==5.14.13
@mui/x-data-grid==6.18.0
recharts==2.10.3
date-fns==2.30.0
```

**Forms:**
```
react-hook-form==7.49.0
```

**Routing:**
```
react-router-dom==6.20.1
```

**API & HTTP:**
```
axios==1.6.2
```

**Styling:**
```
emotion==11.11.1
@emotion/react==11.11.1
@emotion/styled==11.11.0
```

**Utilities:**
```
lodash-es==4.17.21
classnames==2.3.2
decimal.js==10.4.3
```

**Development:**
```
@types/react==18.2.38
@types/react-dom==18.2.17
@types/node==20.10.0
eslint==8.55.0
prettier==3.1.1
```

---

## 6. File and Folder Structure

### 6.1 Backend Directory Structure

```
projectpulse-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                          # FastAPI app initialization
│   ├── config.py                        # Configuration management
│   ├── database.py                      # Database connection & session
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── router.py                # Main router aggregator
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── projects.py
│   │   │   │   ├── resources.py
│   │   │   │   ├── allocations.py
│   │   │   │   ├── wbs.py
│   │   │   │   ├── invoices.py
│   │   │   │   ├── milestones.py
│   │   │   │   ├── analytics.py
│   │   │   │   ├── ai_insights.py
│   │   │   │   └── auth.py
│   │   │   │
│   │   │   └── dependencies.py          # Dependency injection
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── db_models.py                 # SQLAlchemy ORM models
│   │   └── schemas.py                   # Pydantic request/response schemas
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── project_service.py
│   │   ├── resource_service.py
│   │   ├── invoice_service.py
│   │   ├── wbs_service.py
│   │   ├── financial_calculator.py      # WIP, margin, cost calculations
│   │   ├── anomaly_detector.py          # Anomaly detection logic
│   │   ├── risk_assessor.py             # Risk scoring & assessment
│   │   └── ai_service.py                # Gemma AI integration
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── auth_middleware.py
│   │   ├── error_handler.py
│   │   └── logging_middleware.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   ├── validators.py
│   │   └── helpers.py
│   │
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py                  # Pytest fixtures
│       ├── test_projects.py
│       ├── test_invoices.py
│       ├── test_financial_calc.py
│       ├── test_ai_service.py
│       └── integration/
│           └── test_end_to_end.py
│
├── migrations/                          # Alembic DB migrations
│   ├── env.py
│   ├── alembic.ini
│   └── versions/
│       └── 001_initial_schema.py
│
├── .env.example                         # Example environment variables
├── .gitignore
├── requirements.txt                     # Python dependencies
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── README.md
└── main.py                              # Entry point for running app
```

### 6.2 Frontend Directory Structure

```
projectpulse-frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
│
├── src/
│   ├── index.tsx
│   ├── App.tsx                          # Main App component
│   ├── config/
│   │   ├── api.ts                       # API client configuration
│   │   ├── constants.ts                 # App constants (roles, statuses, etc.)
│   │   └── theme.ts                     # MUI theme configuration
│   │
│   ├── types/
│   │   ├── models.ts                    # TypeScript interfaces for data models
│   │   ├── api.ts                       # API request/response types
│   │   └── index.ts
│   │
│   ├── api/
│   │   ├── apiClient.ts                 # Axios instance configuration
│   │   ├── endpoints/
│   │   │   ├── projects.ts
│   │   │   ├── resources.ts
│   │   │   ├── invoices.ts
│   │   │   ├── analytics.ts
│   │   │   ├── ai-insights.ts
│   │   │   └── auth.ts
│   │   └── hooks/
│   │       ├── useProjects.ts
│   │       ├── useResources.ts
│   │       ├── useInvoices.ts
│   │       └── useAnalytics.ts
│   │
│   ├── redux/
│   │   ├── store.ts
│   │   ├── slices/
│   │   │   ├── projectSlice.ts
│   │   │   ├── resourceSlice.ts
│   │   │   ├── invoiceSlice.ts
│   │   │   ├── authSlice.ts
│   │   │   └── uiSlice.ts
│   │   └── hooks.ts
│   │
│   ├── components/
│   │   ├── common/
│   │   │   ├── Header.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Footer.tsx
│   │   │   ├── Layout.tsx
│   │   │   ├── LoadingSpinner.tsx
│   │   │   ├── ErrorBoundary.tsx
│   │   │   ├── ConfirmDialog.tsx
│   │   │   └── NotificationSnackbar.tsx
│   │   │
│   │   ├── dashboard/
│   │   │   ├── Dashboard.tsx             # Main dashboard page
│   │   │   ├── KPICards.tsx
│   │   │   ├── PortfolioChart.tsx
│   │   │   ├── WIPTrendChart.tsx
│   │   │   ├── MarginChart.tsx
│   │   │   ├── ResourceUtilizationHeatmap.tsx
│   │   │   ├── InvoicingPipelineChart.tsx
│   │   │   └── AIInsightsPanel.tsx
│   │   │
│   │   ├── projects/
│   │   │   ├── ProjectList.tsx
│   │   │   ├── ProjectDetail.tsx
│   │   │   ├── ProjectForm.tsx           # Creation/Edit form with steps
│   │   │   ├── ProjectTabs/
│   │   │   │   ├── OverviewTab.tsx
│   │   │   │   ├── ResourceTab.tsx
│   │   │   │   ├── FinancialsTab.tsx
│   │   │   │   ├── WBSTab.tsx
│   │   │   │   ├── InvoicesTab.tsx
│   │   │   │   └── InsightsTab.tsx
│   │   │   └── ProjectCard.tsx
│   │   │
│   │   ├── resources/
│   │   │   ├── ResourceList.tsx
│   │   │   ├── ResourceForm.tsx
│   │   │   ├── ResourceUtilizationView.tsx
│   │   │   ├── RateCardManagement.tsx
│   │   │   └── BulkImportResources.tsx
│   │   │
│   │   ├── analytics/
│   │   │   ├── AnalyticsDashboard.tsx
│   │   │   ├── WIPAnalysis.tsx
│   │   │   ├── MarginAnalysis.tsx
│   │   │   ├── InvoicingAnalysis.tsx
│   │   │   ├── FundingAnalysis.tsx
│   │   │   └── ReportGenerator.tsx
│   │   │
│   │   ├── invoices/
│   │   │   ├── InvoiceList.tsx
│   │   │   ├── InvoiceDetail.tsx
│   │   │   ├── InvoiceForm.tsx
│   │   │   ├── InvoicePreview.tsx
│   │   │   └── AgingReport.tsx
│   │   │
│   │   ├── settings/
│   │   │   ├── SettingsPage.tsx
│   │   │   ├── SystemSettings.tsx
│   │   │   ├── UserManagement.tsx
│   │   │   └── IntegrationSettings.tsx
│   │   │
│   │   └── auth/
│   │       ├── LoginPage.tsx
│   │       ├── LoginForm.tsx
│   │       └── ProtectedRoute.tsx
│   │
│   ├── utils/
│   │   ├── formatters.ts                # Date, currency formatting
│   │   ├── validators.ts
│   │   ├── calculations.ts              # Client-side calculations
│   │   ├── errorHandler.ts
│   │   └── localStorageManager.ts
│   │
│   ├── styles/
│   │   ├── globals.css
│   │   └── theme.css
│   │
│   └── pages/
│       ├── NotFound.tsx
│       └── Unauthorized.tsx
│
├── .env.example
├── .gitignore
├── package.json
├── tsconfig.json
├── README.md
└── docker/
    ├── Dockerfile
    └── nginx.conf
```

---

## 7. Acceptance Criteria

### Phase 1: MVP (Months 1-3)

#### 7.1.1 Functional Acceptance Criteria

**Project Management:**
- [ ] User can create a new project with basic info (name, type, dates, funding)
- [ ] User can add resources to a project with designation and billable rate
- [ ] User can define monthly hour allocations per resource per project
- [ ] Project status transitions work correctly (Opportunity → Active → Completed)
- [ ] Project list displays with filters (status, date range, profitability)
- [ ] Project detail page shows all relevant information

**Financial Calculations:**
- [ ] WIP calculation is accurate (sum of uninvoiced costs)
- [ ] Margin calculation is accurate (revenue - cost / revenue * 100)
- [ ] Project profitability dashboard displays correctly
- [ ] Financial summaries are updated in real-time (within cache TTL)

**Invoice & Milestone Management:**
- [ ] User can create milestones with percentage or date triggers
- [ ] Invoices are auto-generated when milestones are triggered
- [ ] Invoice status transitions work (Draft → Issued → Paid)
- [ ] Invoice aging report shows invoices overdue > X days
- [ ] User can record payments and mark invoices as paid

**WBS Tracking:**
- [ ] User can create WBS codes for a project
- [ ] User can log billed hours to a WBS code
- [ ] WBS tracking shows allocated vs. actual hours
- [ ] WBS cost allocation is accurate

**AI Insights:**
- [ ] Gemma AI successfully analyzes sample project financial data
- [ ] Anomaly detection identifies WIP > 60 days old
- [ ] Risk predictions highlight margin < 15%
- [ ] AI recommendations are displayed on dashboard
- [ ] AI insights can be retrieved via API and displayed in UI

**Authentication & Security:**
- [ ] User login works with JWT token generation
- [ ] Expired tokens trigger re-authentication
- [ ] API endpoints require valid JWT
- [ ] User roles are enforced (Partner, Director, AD, etc.)

**Reporting:**
- [ ] Project Profitability Report can be generated and exported to CSV/PDF
- [ ] WIP Aging Report accurately lists projects by WIP age
- [ ] Invoicing Report shows status breakdown (Paid, Unpaid, Overdue)
- [ ] Reports are downloadable and printable

#### 7.1.2 Performance Acceptance Criteria

- [ ] Dashboard loads in < 2 seconds
- [ ] Chart rendering completes in < 1 second
- [ ] API responses complete in < 500ms (95th percentile)
- [ ] Database queries use appropriate indexes (< 100ms for standard queries)
- [ ] Frontend handles 100+ projects without lag

#### 7.1.3 UI/UX Acceptance Criteria

- [ ] All pages are responsive on desktop (1920x1080) and tablet (768px)
- [ ] Color contrast meets WCAG AA standards
- [ ] Form validation provides clear error messages
- [ ] Navigation is intuitive with breadcrumb trails
- [ ] Loading states are shown during data fetches
- [ ] Success/error notifications appear after actions

#### 7.1.4 Testing Acceptance Criteria

- [ ] Unit tests cover 80%+ of business logic (financial calculations, anomaly detection)
- [ ] Integration tests cover 70%+ of API endpoints
- [ ] E2E tests cover critical user journeys (project creation → invoice → payment)
- [ ] All critical paths pass automated tests
- [ ] Manual testing by stakeholders confirms business requirements

#### 7.1.5 Documentation Acceptance Criteria

- [ ] API documentation available via Swagger/OpenAPI
- [ ] Setup guide for local development
- [ ] Database schema documented
- [ ] AI prompt templates documented
- [ ] User guide for main features
- [ ] Admin guide for system configuration

### Phase 2: Enhanced Features (Months 4-6)

**Future Phase 2 Acceptance Criteria:**
- [ ] Real-time WebSocket updates for dashboard
- [ ] Email notifications for invoice aging & financial alerts
- [ ] Advanced forecasting & predictive analytics
- [ ] Budget vs. Actual variance analysis
- [ ] Bulk operations (import projects, update allocations)
- [ ] Advanced role-based access control with custom permissions
- [ ] Integration with ERP systems (SAP, Oracle)
- [ ] Mobile app (iOS/Android)

---

## 8. Out of Scope / Future Improvements

### 8.1 Out of Scope for MVP

**Features:**
- Multi-tenant support (single tenant initially)
- Real-time collaboration (commenting, chat on projects)
- Expense tracking and cost management
- Equipment/asset management
- Integration with time-tracking systems (e.g., Jira, Asana)
- Advanced forecast models (ML-based predictions)
- Compliance & audit trail (basic audit logging only)
- Custom workflow automation
- Advanced user analytics

**Technical:**
- High-availability setup (single instance initially)
- Disaster recovery & backup strategy
- API rate limiting & throttling
- Advanced caching strategies (Redis)
- GraphQL API (REST only in MVP)
- Kubernetes deployment (Docker Compose initially)

### 8.2 Future Enhancements (Phase 2+)

**Business Features:**
1. **Variance Analysis:** Budget vs. Actual by project and WBS, with drill-down capability
2. **Capacity Planning:** Resource capacity forecasting, skill gap analysis
3. **Bench Management:** Tracking unallocated resources, utilization trending
4. **Contract Management:** Digital contract repository, renewal alerts
5. **Budget Forecasting:** ML-based budget predictions for future projects
6. **Multi-Currency Support:** Handle projects across different currencies with FX rates
7. **Discount & Promotion Management:** Apply project-level discounts, volume-based pricing
8. **Customer Portal:** Self-service invoice viewing, payment status for clients
9. **Mobile App:** Native iOS/Android apps for on-the-go dashboards

**Technical Enhancements:**
1. **Real-time Collaboration:** WebSocket-based live updates, change notifications
2. **Advanced Caching:** Redis for dashboard caching, query result caching
3. **Event-Driven Architecture:** Kafka/RabbitMQ for async processing, notifications
4. **Advanced Security:** OAuth2/OpenID Connect, SSO integration, MFA
5. **Compliance:** GDPR compliance, data retention policies, encryption at rest
6. **Integration Connectors:** SAP, Oracle, Salesforce, Workday connectors
7. **Custom Dashboards:** User-definable dashboards, saved views
8. **Advanced Analytics:** Cohort analysis, trend analysis, predictive models
9. **Workflow Automation:** Approval workflows, auto-escalation rules
10. **BI Integration:** Tableau, Power BI integration for advanced analytics

### 8.3 Known Limitations (MVP)

- Single-tenant only (no account isolation)
- No offline support
- No time-zone handling (assumes server time-zone)
- Limited to 1M+ rows of transaction data (scaling needed for larger firms)
- AI insights refreshed on-demand (no scheduled batch processing)
- No user-level audit trail (action tracking only at API level)
- Support for English language only (no i18n)

---

## 9. Success Metrics & KPIs

### 9.1 Business Metrics

- **Adoption:** 80%+ of target user base (partners/directors) using platform within 6 months
- **User Engagement:** Average daily active users (DAU) > 50% of registered users
- **Time Savings:** Reduce manual financial reporting time by 70%
- **Decision Quality:** Increase in data-driven decisions (tracked via survey)
- **Error Reduction:** Reduce invoice discrepancies by 90%
- **Margin Improvement:** Deliver average 2-3% margin improvement on analyzed projects

### 9.2 Technical Metrics

- **API Uptime:** 99.5%+ availability
- **Performance:** 95th percentile API response time < 500ms
- **Dashboard Load Time:** < 2 seconds for 95% of requests
- **Data Accuracy:** 100% accuracy on financial calculations (verified quarterly)
- **AI Insight Quality:** 90%+ relevance score (user feedback)
- **Bug Rate:** < 1 critical bug per 10K transactions

### 9.3 User Satisfaction Metrics

- **Net Promoter Score (NPS):** > 50
- **User Satisfaction Score:** > 4.0/5.0
- **Support Ticket Resolution Time:** < 24 hours for critical issues
- **Training Completion Rate:** > 90% of users complete onboarding

---

## 10. Glossary & Definitions

| Term | Definition |
|------|-----------|
| **WIP (Work in Progress)** | Costs incurred for services delivered but not yet invoiced to the client |
| **WIP Aging** | Time elapsed since services were delivered and WIP was created without invoicing |
| **Margin** | (Revenue - Cost) / Revenue * 100; percentage profit on a project |
| **Billable Rate** | Hourly rate charged to the client for a specific resource/designation |
| **Cost Rate** | Internal cost per hour for a resource (determines profit margin) |
| **WBS Code** | Work Breakdown Structure code; hierarchical code for project cost tracking |
| **T&M (Time & Material)** | Billing model where client is charged for actual hours + expenses |
| **Fixed-Cost** | Billing model with pre-determined total project price regardless of hours |
| **Milestone** | Predefined trigger point for invoice generation (date, completion %, manual) |
| **Resource Allocation** | Assignment of a resource to a project with specific hours and duration |
| **Invoice Aging** | Time elapsed since invoice was issued without payment |
| **Engagement Type** | Classification: Engagement, Project, Retainer, SOW, etc. |
| **Big 4** | Top 4 global management consulting firms (Deloitte, PwC, EY, KPMG) |
| **Portfolio** | Collection of all projects managed by the firm |
| **Financial Health** | Composite score of margin, WIP, funding, and invoice status |

---

## 11. Assumptions & Constraints

### 11.1 Assumptions

- Users have basic proficiency with financial concepts (WIP, margin, invoicing)
- Financial data is available in structured format (not scattered across systems)
- Internet connectivity is reliable (no offline mode needed)
- Gemma API availability and quota are sufficient for anticipated usage
- PostgreSQL is available in the deployment environment
- All project stakeholders can access web browsers (no legacy system requirement)

### 11.2 Constraints

- **Budget:** Limited resources; MVP focuses on core financial tracking
- **Timeline:** 6 months to MVP; advanced features deferred to Phase 2
- **Scale:** MVP targets firms with 50-500 active projects (1M transactions)
- **Compliance:** No HIPAA/PCI DSS requirements (standard B2B data)
- **Integration:** Limited integration focus (Phase 1 to Phase 2)
- **Localization:** English language only for MVP

---

## 12. Development Roadmap

### Phase 1: MVP (Weeks 1-12)

| Week | Component | Deliverable |
|------|-----------|-------------|
| 1-2 | Setup & Infrastructure | Dev environment, Docker setup, CI/CD pipeline |
| 3-4 | Backend Core | Database schema, project APIs, authentication |
| 5-6 | Financial Calculations | WIP, margin, cost calculation engines |
| 7-8 | Frontend Setup | React project structure, auth flow, layout components |
| 9-10 | AI Integration | Gemma API integration, anomaly detection, insights |
| 11-12 | Testing & Polish | Unit tests, integration tests, UI refinement, documentation |

### Phase 2: Enhancements (Months 4-6)

- Advanced analytics & forecasting
- Real-time updates & notifications
- Multi-currency & advanced invoicing
- ERP integrations
- Mobile app MVP

---

## Appendix A: Sample API Response Format

### Project Detail Response
```json
{
  "project_id": "uuid-123",
  "name": "Client X Digital Transformation",
  "code": "PRJ-2024-001",
  "status": "Active",
  "engagement_type": "Time & Material",
  "start_date": "2024-01-01",
  "end_date": "2024-12-31",
  "contract_value": 500000,
  "available_funding": 450000,
  "financial_summary": {
    "total_revenue": 250000,
    "total_cost": 180000,
    "wip": 45000,
    "margin_percent": 28.0,
    "invoiced": 205000,
    "uninvoiced_wip": 45000
  },
  "resources": [
    {
      "allocation_id": "uuid-456",
      "resource_name": "John Smith",
      "designation": "Senior Manager",
      "billable_rate": 500,
      "monthly_allocation": 160,
      "ytd_billed_hours": 1280,
      "ytd_revenue": 640000
    }
  ],
  "ai_insights": {
    "financial_health_score": 8.5,
    "risks": ["Margin trending down 2% from last month"],
    "recommendations": ["Consider reallocating junior resources to improve margin"]
  },
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-09-27T14:30:00Z"
}
```

---

## Appendix B: Gemma AI Integration Example

### Sample AI Request Prompt
```
Analyze the following project financial data and provide 3 key insights:

Project: Client X Digital Transformation
- Status: Active (6 months in)
- Contract Value: $500,000 (T&M)
- Total Revenue Recognized: $250,000
- Total Cost: $180,000
- WIP: $45,000 (avg. 45 days old)
- Available Funding: $450,000
- Resource Utilization: 92% (high)
- Margin: 28%

Provide:
1. Financial risk assessment
2. Anomalies detected
3. Actionable recommendations to improve margin
```

### Sample AI Response
```json
{
  "analysis": {
    "financial_health_score": 8.5,
    "risks": [
      {
        "type": "Margin Threat",
        "severity": "High",
        "description": "Senior Manager allocation at 160 hrs/month exceeds project capacity; contributing to margin pressure",
        "recommendation": "Shift 40 hours/month to junior resources; same outcome, 30% cost reduction"
      }
    ],
    "anomalies": [
      {
        "type": "WIP Aging",
        "severity": "Medium",
        "description": "45 days average WIP age; approaching 60-day threshold for Big 4 practices",
        "recommendation": "Investigate invoicing delays; 2 invoices pending client approval"
      }
    ],
    "recommendations": [
      "Reallocate 40 hours/month from Senior Manager to Senior Consultant (saves $4,000/month)"
    ]
  },
  "confidence_score": 0.92
}
```

---

## Document Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-09-27 | Project Team | Initial PRD for ProjectPulse AI MVP |

---

## Sign-Off

This PRD is approved for implementation of Phase 1 (MVP).

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Manager | [Name] | ____________ | [Date] |
| Technology Lead | [Name] | ____________ | [Date] |
| Sponsor/Director | [Name] | ____________ | [Date] |

---

**Document End**
