# 🚀 ProjectPulse AI - Deployment Quick Start

## ⏱️ 5-Minute Deploy

### Step 1: Demo Locally (30 seconds)
```bash
docker-compose up -d
open http://localhost:5173
# Email: admin@company.com | Password: password123
```

### Step 2: Deploy Frontend to Vercel (2 minutes)
```bash
npm install -g vercel
cd frontend
vercel --prod
```

### Step 3: Deploy Backend to Railway (2 minutes)
```bash
npm install -g @railway/cli
railway login
cd backend
railway up
```

### Step 4: Update Environment (1 minute)
- In Vercel: Set `VITE_API_URL` to backend URL
- In Railway: Set `DATABASE_URL` to PostgreSQL URL

✅ **Done! Your app is live**

---

## 📋 Deployment Checklist

### Before Deployment
- [ ] Code pushed to GitHub
- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Database backup scheduled
- [ ] SSL certificate ready
- [ ] DNS records configured

### Frontend (Vercel)
- [ ] Build command: `npm run build`
- [ ] Output directory: `dist`
- [ ] Environment: `VITE_API_URL`
- [ ] Region: US (or your region)
- [ ] Auto-deploy on push enabled

### Backend (Railway/Render)
- [ ] Database: PostgreSQL created
- [ ] Environment variables set
- [ ] Health check: `/health`
- [ ] Port: `8000`
- [ ] Auto-deploy on push enabled

### Database (Railway/Render/AWS RDS)
- [ ] PostgreSQL 14+
- [ ] Backup daily enabled
- [ ] Connection string in env
- [ ] Schema imported
- [ ] Demo user created

### Post-Deployment
- [ ] Test login
- [ ] Check API endpoints at /docs
- [ ] Verify database connection
- [ ] Test all features
- [ ] Check logs for errors
- [ ] Monitor performance

---

## 🔑 Environment Variables

### Frontend (.env in Vercel)
```
VITE_API_URL=https://your-backend-domain.com
VITE_APP_NAME=ProjectPulse AI
```

### Backend (.env in Railway)
```
DATABASE_URL=postgresql://user:pass@db-host:5432/projectpulse
SECRET_KEY=<generate-random-32-char-string>
GEMMA_API_KEY=<your-google-gemma-key>
ALLOWED_ORIGINS=https://your-frontend-domain.com
```

---

## 🌍 Domain Setup

### Frontend Domain
1. Buy domain (namecheap.com, godaddy.com)
2. Add to Vercel (Settings → Domains)
3. Update DNS records
4. SSL auto-enabled by Vercel

### Backend Domain
1. Get domain or use subdomain
2. Update API_URL in frontend .env
3. Configure in Railway/Render
4. SSL included in platform

### Example
```
Frontend: https://app.projectpulse.ai
Backend: https://api.projectpulse.ai
```

---

## ✅ Verification Steps

After deployment:
```bash
# 1. Test login
curl https://your-api-domain.com/api/v1/auth/login \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@company.com","password":"password123"}'

# 2. Check health
curl https://your-api-domain.com/health

# 3. Test frontend
open https://your-app-domain.com
```

---

## 🆘 Troubleshooting

### Frontend won't load
- Check browser console for errors
- Verify `VITE_API_URL` is correct
- Check CORS settings on backend

### API returns 401
- Verify JWT secret is same on backend
- Check token expiration
- Clear browser cache

### Database connection fails
- Verify `DATABASE_URL` format
- Check PostgreSQL is running
- Verify firewall allows connection
- Test connection: `psql $DATABASE_URL`

### CORS errors
- Add frontend URL to `ALLOWED_ORIGINS` in backend
- Restart backend service
- Clear browser cache

### Performance issues
- Check database indexes
- Enable caching headers
- Use CDN for static files
- Monitor API response times

---

## 📞 Support

- **Docs**: See README_DEPLOYMENT.md
- **API Docs**: https://your-api-domain.com/docs
- **Issues**: GitHub Issues
- **Email**: support@projectpulse.ai

---

## 🎯 Success Metrics

After deployment, monitor:
- ✅ Uptime: 99.9%+
- ✅ API latency: <200ms
- ✅ Frontend load: <1s
- ✅ Error rate: <0.1%
- ✅ Database connections: <50
- ✅ Daily active users

---

**Ready to deploy? Start with `docker-compose up -d` then follow steps above!**

Last updated: September 28, 2026
