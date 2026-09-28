#!/bin/bash

# ProjectPulse AI Setup Script
# This script sets up the complete application for local development

set -e

echo "🚀 ProjectPulse AI Setup"
echo "========================"

# Check prerequisites
echo "✓ Checking prerequisites..."
command -v python3 >/dev/null 2>&1 || { echo "Python 3 is required but not installed."; exit 1; }
command -v node >/dev/null 2>&1 || { echo "Node.js is required but not installed."; exit 1; }
command -v psql >/dev/null 2>&1 || { echo "PostgreSQL is required but not installed."; exit 1; }

# Backend Setup
echo ""
echo "📦 Setting up Backend..."
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file (update with your config)"
else
    echo "✓ .env file already exists"
fi

cd ..

# Frontend Setup
echo ""
echo "📦 Setting up Frontend..."
cd frontend

# Install dependencies
npm install

# Create .env file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✓ Created .env file"
else
    echo "✓ .env file already exists"
fi

cd ..

# Database Setup
echo ""
echo "🗄️  Setting up Database..."
psql -U postgres -c "CREATE DATABASE projectpulse;" 2>/dev/null || echo "✓ Database already exists"
psql -U postgres -d projectpulse -f database/schema.sql

echo ""
echo "✅ Setup Complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Update backend/.env with your configuration"
echo "2. Start backend: cd backend && source venv/bin/activate && uvicorn main:app --reload"
echo "3. Start frontend: cd frontend && npm run dev"
echo "4. Open http://localhost:5173 in your browser"
echo "5. Login with admin@company.com / password123"
echo ""
echo "📚 Documentation: See README_DEPLOYMENT.md"
