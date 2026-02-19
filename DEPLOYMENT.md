# 🚀 AGROHUB - DEPLOYMENT CHECKLIST

## ✅ Pre-Deployment Checklist

### Local Development Setup
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Database migrations run (`python manage.py migrate`)
- [ ] Superuser account created
- [ ] Sample data loaded (optional)
- [ ] All features tested locally
- [ ] Website runs on localhost:8000
- [ ] Admin panel accessible

### Code Review
- [ ] All secret keys moved to environment variables
- [ ] DEBUG = False in production settings
- [ ] ALLOWED_HOSTS configured
- [ ] Static files collected
- [ ] Media files path configured
- [ ] Database settings updated for production

### Security
- [ ] Strong SECRET_KEY generated
- [ ] CSRF settings configured
- [ ] CORS headers set (if using API)
- [ ] SSL/HTTPS enabled
- [ ] Secure cookies enabled
- [ ] Database credentials secured
- [ ] File upload size limits set
- [ ] Rate limiting configured (optional)

### Content
- [ ] Replace demo data with real products
- [ ] Update company information
- [ ] Add real contact details
- [ ] Upload actual product images
- [ ] Create real user accounts
- [ ] Configure email settings
- [ ] Set up WhatsApp number
- [ ] Update footer links

### Testing
- [ ] Test all forms (login, register, create listing)
- [ ] Test image uploads
- [ ] Test search functionality
- [ ] Test filters
- [ ] Test chatbot responses
- [ ] Test on mobile devices
- [ ] Test on different browsers
- [ ] Test user flows (buyer and seller)
- [ ] Test admin panel
- [ ] Performance testing

---

## 🌐 Production Deployment Steps

### Option 1: Deploy to Heroku

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Steps
1. **Create Heroku app**
```bash
heroku create your-agrohub-name
```

2. **Add PostgreSQL database**
```bash
heroku addons:create heroku-postgresql:mini
```

3. **Create Procfile**
```
web: gunicorn core.wsgi --log-file -
```

4. **Update requirements.txt**
```
# Add to requirements.txt
gunicorn>=20.1.0
dj-database-url>=2.0.0
psycopg2-binary>=2.9.0
whitenoise>=6.5.0
```

5. **Update settings.py for production**
```python
import dj_database_url

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

6. **Deploy**
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

7. **Run migrations**
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

8. **Open your site**
```bash
heroku open
```

---

### Option 2: Deploy to Railway

#### Steps
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your Agrohub repository
6. Add PostgreSQL database
7. Set environment variables:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS`
8. Deploy automatically!

---

### Option 3: Deploy to DigitalOcean App Platform

#### Steps
1. Go to DigitalOcean
2. Create new App
3. Connect GitHub repository
4. Configure:
   - Build command: `pip install -r requirements.txt`
   - Run command: `gunicorn core.wsgi`
5. Add PostgreSQL database
6. Set environment variables
7. Deploy!

---

### Option 4: Traditional VPS (DigitalOcean Droplet, AWS EC2)

#### Steps
1. **Provision server**
   - Ubuntu 22.04 LTS
   - Minimum 1GB RAM

2. **Install dependencies**
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx postgresql
```

3. **Clone repository**
```bash
git clone your-repo-url
cd agrohub
```

4. **Set up virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. **Configure PostgreSQL**
```bash
sudo -u postgres psql
CREATE DATABASE agrohub;
CREATE USER agrohubuser WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE agrohub TO agrohubuser;
\q
```

6. **Configure environment variables**
```bash
export SECRET_KEY='your-secret-key'
export DEBUG=False
export DATABASE_URL='postgresql://user:pass@localhost/agrohub'
```

7. **Run migrations**
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

8. **Set up Gunicorn**
```bash
pip install gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

9. **Configure Nginx**
Create `/etc/nginx/sites-available/agrohub`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /path/to/agrohub;
    }
    
    location /media/ {
        root /path/to/agrohub;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

10. **Enable site and restart Nginx**
```bash
sudo ln -s /etc/nginx/sites-available/agrohub /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

11. **Set up SSL with Let's Encrypt**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## 🔧 Environment Variables

Create a `.env` file (DO NOT commit to Git):

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

# Database
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# AWS S3 (Optional - for media files)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
AWS_S3_REGION_NAME=ap-southeast-1

# Other
SITE_URL=https://your-domain.com
CONTACT_EMAIL=contact@your-domain.com
```

---

## 📊 Post-Deployment Checklist

### Verify Deployment
- [ ] Website is accessible via domain
- [ ] SSL certificate is working (HTTPS)
- [ ] Static files are loading correctly
- [ ] Images are displaying
- [ ] Admin panel is accessible
- [ ] Forms are submitting
- [ ] Database is working
- [ ] Email notifications working (if configured)

### Performance
- [ ] Set up CDN for static files (optional)
- [ ] Enable caching
- [ ] Optimize images
- [ ] Enable Gzip compression
- [ ] Monitor response times
- [ ] Set up database indexing

### Monitoring
- [ ] Set up error tracking (Sentry)
- [ ] Configure logging
- [ ] Set up uptime monitoring
- [ ] Configure backups
- [ ] Set up analytics (Google Analytics)
- [ ] Monitor server resources

### SEO
- [ ] Add meta descriptions
- [ ] Set up sitemap.xml
- [ ] Configure robots.txt
- [ ] Submit to Google Search Console
- [ ] Add Open Graph tags
- [ ] Optimize page titles

### Marketing
- [ ] Create social media accounts
- [ ] Set up Facebook page
- [ ] Set up Instagram account
- [ ] Set up WhatsApp Business
- [ ] Create email marketing list
- [ ] Design marketing materials

---

## 🛡️ Security Best Practices

### Production Settings
```python
# settings.py for production

DEBUG = False
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### Regular Maintenance
- [ ] Update dependencies regularly
- [ ] Monitor security advisories
- [ ] Backup database daily
- [ ] Review logs weekly
- [ ] Update Django and packages
- [ ] Test backup restoration
- [ ] Audit user permissions
- [ ] Review uploaded files

---

## 📈 Scaling Considerations

### When to Scale
- More than 1000 daily active users
- Database queries slowing down
- Server CPU/memory maxing out
- File uploads growing large
- Need high availability

### Scaling Options
1. **Vertical Scaling**: Upgrade server resources
2. **Horizontal Scaling**: Add more servers with load balancer
3. **Database Scaling**: Read replicas, connection pooling
4. **CDN**: Use CloudFlare or AWS CloudFront
5. **Caching**: Redis or Memcached
6. **Queue System**: Celery for background tasks
7. **Media Storage**: AWS S3 or similar

---

## 🆘 Troubleshooting

### Common Issues

**Static files not loading**
- Run `python manage.py collectstatic`
- Check STATIC_ROOT and STATIC_URL settings
- Verify Nginx/Apache configuration

**Database connection errors**
- Check DATABASE_URL format
- Verify database credentials
- Ensure PostgreSQL is running
- Check firewall rules

**500 Internal Server Error**
- Check error logs
- Verify all environment variables
- Run migrations
- Check file permissions

**Images not uploading**
- Check MEDIA_ROOT permissions
- Verify file size limits
- Check disk space
- Review Nginx client_max_body_size

---

## ✅ Launch Day Checklist

### Final Checks
- [ ] All content reviewed and approved
- [ ] Legal pages added (Terms, Privacy Policy)
- [ ] Contact information updated
- [ ] SSL certificate valid
- [ ] Backups configured and tested
- [ ] Monitoring tools active
- [ ] Error tracking enabled
- [ ] Performance optimized
- [ ] Mobile experience tested
- [ ] Browser compatibility verified

### Marketing
- [ ] Social media posts prepared
- [ ] Email announcement ready
- [ ] Press release written
- [ ] Launch video/images prepared
- [ ] Influencers contacted

### Support
- [ ] Support email configured
- [ ] FAQ page created
- [ ] Help documentation ready
- [ ] Customer support trained
- [ ] Incident response plan ready

---

## 🎉 Congratulations!

Your Agrohub marketplace is now live and ready to connect Malaysian farmers and buyers!

### Post-Launch
- Monitor performance closely for first 48 hours
- Respond to user feedback quickly
- Fix any bugs immediately
- Collect user testimonials
- Iterate and improve continuously

---

**Good luck with your launch! 🌾🚀**

For questions, refer to the documentation or Django/Tailwind communities.
