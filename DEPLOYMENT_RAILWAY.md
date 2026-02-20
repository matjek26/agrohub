# 🚀 AGROHUB Deployment on Railway (FREE + Custom Domain)

## ✅ Why Railway?
- **FREE** forever (with fair usage)
- Custom domain support (agrohubmy.com)
- Automatic SSL certificate
- Easy deployment from GitHub
- PostgreSQL database included
- Professional and reliable

---

## 📋 STEP-BY-STEP GUIDE

### STEP 1: Prepare Your Project (5 minutes)

#### 1.1 Create `.env` file (for local testing)
Create a file named `.env` in your project root:
```env
SECRET_KEY=your-secret-key-here-change-this
DEBUG=False
ALLOWED_HOSTS=agrohubmy.com,www.agrohubmy.com,.railway.app
DATABASE_URL=sqlite:///db.sqlite3
```

#### 1.2 Update `requirements.txt`
Make sure these are in your requirements.txt:
```
Django>=4.2,<5.0
Pillow>=10.0.0
psycopg2-binary>=2.9.0
python-decouple>=3.8
whitenoise>=6.5.0
gunicorn>=21.0.0
dj-database-url>=2.0.0
```

#### 1.3 Create `railway.json` (optional but recommended)
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

#### 1.4 Update `Procfile`
```
web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi --log-file -
release: python manage.py migrate
```

---

### STEP 2: Update Django Settings (10 minutes)

Update `core/settings.py` to use environment variables:

```python
import os
from pathlib import Path
from decouple import config, Csv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = config('SECRET_KEY', default='django-insecure-agrohub-dev-key-change-in-production')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='agrohubmy.com,www.agrohubmy.com', cast=Csv())

# Add Railway domains
if 'RAILWAY_STATIC_URL' in os.environ:
    ALLOWED_HOSTS += ['.railway.app']

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
        conn_max_age=600
    )
}

# Static files (already configured with WhiteNoise)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
```

---

### STEP 3: Push to GitHub (5 minutes)

If you haven't already:

```bash
git init
git add .
git commit -m "Prepare for Railway deployment"
git branch -M main
git remote add origin https://github.com/yourusername/agrohub.git
git push -u origin main
```

---

### STEP 4: Deploy on Railway (10 minutes)

1. **Go to Railway**: https://railway.app
2. **Sign up** with GitHub account
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your agrohub repository**
6. **Add PostgreSQL Database**:
   - Click "+ New Service"
   - Select "Database" → "PostgreSQL"
   - Railway will auto-link it to your app

7. **Set Environment Variables**:
   Click on your service → Variables → Add:
   ```
   SECRET_KEY = (generate strong key: https://djecrety.ir/)
   DEBUG = False
   ALLOWED_HOSTS = agrohubmy.com,www.agrohubmy.com
   ```
   
   Note: DATABASE_URL is auto-set by Railway

8. **Deploy**: Railway will automatically build and deploy

---

### STEP 5: Configure Custom Domain on Railway (5 minutes)

1. In Railway dashboard, click your service
2. Go to **Settings** tab
3. Scroll to **Domains** section
4. Click **"Add Domain"**
5. Enter: `agrohubmy.com`
6. Click **"Add Domain"** again and add: `www.agrohubmy.com`
7. Railway will show you DNS settings (COPY THESE)

---

### STEP 6: Point Domain on Hostinger (5 minutes)

1. **Login to Hostinger**: https://hpanel.hostinger.com
2. **Go to Domains** → Click on `agrohubmy.com`
3. **Click "DNS / Nameservers"**
4. **Add DNS Records**:

   **For root domain (agrohubmy.com):**
   - Type: `CNAME` or `A Record`
   - Name: `@`
   - Value: (the domain Railway provided, e.g., `your-app.railway.app`)
   - TTL: 3600

   **For www subdomain:**
   - Type: `CNAME`
   - Name: `www`
   - Value: (the domain Railway provided)
   - TTL: 3600

5. **Save Changes**

⏰ **Wait 5-30 minutes** for DNS propagation

---

### STEP 7: Create Superuser & Load Data (5 minutes)

1. In Railway dashboard, click your service
2. Click **"Settings"** → Scroll to **"Service"**
3. Click **"Open Shell"** or use Railway CLI:

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link to your project
railway link

# Run commands
railway run python manage.py createsuperuser
railway run python manage.py populate_sample_data
```

---

## 🎉 YOUR SITE IS LIVE!

Visit: **https://agrohubmy.com**

Admin panel: **https://agrohubmy.com/admin**

---

## 🔄 How to Update Your Site

After making changes locally:

```bash
git add .
git commit -m "Your update message"
git push
```

Railway will automatically:
- Detect changes
- Build new version
- Run migrations
- Deploy updates

---

## 💰 COST BREAKDOWN

### Railway FREE Tier:
- ✅ 500 hours/month (plenty for one site)
- ✅ Custom domains
- ✅ Free SSL certificate
- ✅ PostgreSQL database
- ✅ 1GB RAM, shared CPU
- ✅ 100GB network bandwidth

### If you exceed free tier:
- Pay-as-you-go: ~$5-10/month (only if high traffic)

### Hostinger Domain:
- Your existing domain cost only

**Total Cost: $0/month** (+ domain renewal yearly)

---

## 🆚 COMPARISON WITH OTHER OPTIONS

| Platform | Cost/Month | Custom Domain | Database | SSL | Reliability |
|----------|------------|---------------|----------|-----|-------------|
| **Railway** | **$0** | ✅ Yes | PostgreSQL | ✅ Free | ⭐⭐⭐⭐⭐ |
| PythonAnywhere | $5 | ✅ Yes | MySQL | ✅ Free | ⭐⭐⭐⭐ |
| Render.dev | $0 | ✅ Yes | PostgreSQL | ✅ Free | ⭐⭐⭐⭐ |
| Hostinger VPS | $5-10 | ✅ Yes | Self-setup | Extra $ | ⭐⭐⭐ |
| Heroku | $5-7 | ✅ Yes | PostgreSQL | ✅ Free | ⭐⭐⭐⭐⭐ |

---

## 🐛 Troubleshooting

### Issue: Site not loading after DNS setup
- Wait longer (DNS can take up to 48 hours)
- Check DNS with: https://dnschecker.org

### Issue: Static files not loading
```bash
railway run python manage.py collectstatic --noinput
```

### Issue: Database reset needed
```bash
railway run python manage.py flush
railway run python manage.py migrate
railway run python manage.py populate_sample_data
```

### Issue: View logs
- Railway dashboard → Click service → "Logs" tab

---

## 📞 Need Help?

- Railway Docs: https://docs.railway.app
- Django Docs: https://docs.djangoproject.com
- Community: Railway Discord

---

**🚀 Your AgroHub is now LIVE on the internet!**
