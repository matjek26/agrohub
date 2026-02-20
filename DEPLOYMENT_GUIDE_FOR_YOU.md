# 🚀 Deploy AgroHub to agrohubmy.com - SIMPLE GUIDE

## ✅ What You Have:
- ✅ Domain: agrohubmy.com (Hostinger)
- ✅ GitHub: https://github.com/matjek26/agrohub
- ✅ Code ready on your computer

## 🎯 What We'll Do:
1. Deploy on **Railway** (FREE hosting)
2. Point your Hostinger domain to Railway
3. Site live at agrohubmy.com

**Total Cost: RM 0/month** 🎉

---

## 📋 STEP 1: Update Your GitHub Code (5 minutes)

Your code is ready! Just push the latest changes:

### Open PowerShell in VS Code and run:
```powershell
# Make sure you're in the project folder
cd D:\AGROHUB

# Check git status
git status

# Add all new files
git add .

# Commit changes
git commit -m "Add Railway deployment files"

# Push to GitHub
git push origin main
```

✅ **Done!** Your GitHub is updated.

---

## 📋 STEP 2: Deploy on Railway (15 minutes)

### 2.1 Sign Up on Railway
1. Go to: **https://railway.app**
2. Click **"Login"**
3. Choose **"Login with GitHub"**
4. Authorize Railway to access your GitHub

### 2.2 Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose **matjek26/agrohub**
4. Wait 2-3 minutes for deployment

### 2.3 Add PostgreSQL Database
1. Click **"+ New"** button
2. Select **"Database"**
3. Choose **"Add PostgreSQL"**
4. Railway will automatically connect it!

### 2.4 Set Environment Variables
1. Click on your **agrohub service** (not database)
2. Click **"Variables"** tab
3. Click **"+ New Variable"** and add these:

```
SECRET_KEY = django-insecure-a1b2c3d4e5f6g7h8i9j0-change-this-to-something-random
DEBUG = False
ALLOWED_HOSTS = agrohubmy.com,www.agrohubmy.com
```

⚠️ **IMPORTANT**: Generate a better SECRET_KEY:
- Go to: **https://djecrety.ir/**
- Copy the key
- Replace the SECRET_KEY value above

4. Click **"Deploy"** or wait for auto-deploy

### 2.5 Create Admin User
1. Click on your service
2. Go to **"Settings"** tab
3. Scroll to **"Service"** section
4. You'll see a domain like: `agrohub-production-xxxx.up.railway.app`
5. Click **"Open in New Tab"** to test

The site should load! (might look broken without static files, that's OK)

### 2.6 Run Database Commands
1. In Railway dashboard, click your service
2. Go to **"Settings"** tab
3. Under **"Service"**, find **"Deployments"**
4. Click **"View Logs"**

To create superuser, we need Railway CLI:

**Option A: Use Railway CLI (Recommended)**
In your VS Code PowerShell:
```powershell
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link to your project
railway link

# Create superuser
railway run python manage.py createsuperuser

# Load sample data (optional)
railway run python manage.py populate_sample_data
```

**Option B: Without CLI**
- Go to your Railway service
- Click "Settings" → "Deployments" 
- Click on latest deployment → "View Logs"
- You can add superuser later through Django admin migrations

---

## 📋 STEP 3: Connect Your Domain (10 minutes)

### 3.1 Get Railway Domain Settings
1. In Railway dashboard, click your **agrohub service**
2. Click **"Settings"** tab
3. Scroll to **"Networking"** section
4. Under **"Custom Domain"**, click **"+ Add Domain"**
5. Type: `agrohubmy.com` → Click **"Add"**
6. Click **"+ Add Domain"** again
7. Type: `www.agrohubmy.com` → Click **"Add"**

Railway will show you DNS settings (might be a CNAME or A record).

**Example:**
```
Domain: agrohubmy.com
CNAME: agrohub-production-xxxx.up.railway.app
```

**COPY THIS INFO!**

### 3.2 Update DNS on Hostinger
1. Go to: **https://hpanel.hostinger.com**
2. Login with your account
3. Click **"Domains"** in the left menu
4. Click on **"agrohubmy.com"**
5. Click **"DNS / Name Servers"** tab
6. Look for **"Manage DNS Records"**

### 3.3 Add DNS Records

**Delete any existing A or CNAME records for @ and www first!**

**Add These Records:**

**Record 1 (Root domain):**
- Type: `CNAME` (or `A` if Railway gives you an IP)
- Name: `@` (this means root domain)
- Points to: `agrohub-production-xxxx.up.railway.app` (from Railway)
- TTL: `3600` or `1 hour`

**Record 2 (WWW subdomain):**
- Type: `CNAME`
- Name: `www`
- Points to: `agrohub-production-xxxx.up.railway.app` (same as above)
- TTL: `3600`

7. Click **"Save"** or **"Add Record"**

### 3.4 Wait for DNS Propagation
- Takes **5-30 minutes** (sometimes up to 48 hours)
- Check status: https://dnschecker.org
- Enter: agrohubmy.com

---

## 🎉 STEP 4: Your Site is LIVE!

After DNS propagates, visit:
- **https://agrohubmy.com**
- **https://www.agrohubmy.com**

Both should work! 🎊

### Access Admin Panel:
- **https://agrohubmy.com/admin**
- Login with the superuser you created

---

## 🔧 TROUBLESHOOTING

### Problem: "DisallowedHost" error
**Solution**: Add Railway's default domain to ALLOWED_HOSTS
1. In Railway Variables, update:
```
ALLOWED_HOSTS = agrohubmy.com,www.agrohubmy.com,agrohub-production-xxxx.up.railway.app
```

### Problem: Static files not loading (no CSS)
**Solution**: 
```powershell
railway run python manage.py collectstatic --noinput
```
Then redeploy in Railway dashboard

### Problem: Database is empty
**Solution**: 
```powershell
railway run python manage.py populate_sample_data
```

### Problem: DNS not working after 1 hour
**Solution**: 
- Check Hostinger DNS settings are correct
- Make sure you deleted old A records
- Try: https://dnschecker.org
- Contact Hostinger support if needed

---

## 📱 TEST YOUR SITE

### Things to Test:
- ✅ Homepage loads
- ✅ Can register new account
- ✅ Can login
- ✅ Can create listing (for sellers)
- ✅ Can search products
- ✅ Can upload images
- ✅ Chatbot works
- ✅ Admin panel accessible

---

## 🔄 HOW TO UPDATE YOUR SITE LATER

After making changes locally:

```powershell
# Save changes
git add .
git commit -m "Updated feature X"
git push origin main
```

Railway will **automatically**:
- Detect changes
- Build new version
- Run migrations
- Deploy updates

**No manual work needed!** 🚀

---

## 💰 COST BREAKDOWN

| Item | Cost |
|------|------|
| Domain (agrohubmy.com) | ~RM 30-50/year (already paid) |
| Railway Hosting | **RM 0/month** |
| SSL Certificate | **FREE** (auto) |
| PostgreSQL Database | **Included FREE** |
| Email (@agrohubmy.com) | **Included** (Hostinger) |
| **TOTAL** | **RM 0/month** 🎉 |

---

## ❓ WHY NOT BUY HOSTINGER HOSTING?

### Hostinger Hosting vs Railway:

| Feature | Railway (FREE) | Hostinger Shared |
|---------|---------------|------------------|
| **Price** | RM 0 | RM 15-30/month |
| **Django Support** | ✅ Perfect | ⚠️ Limited |
| **Database** | PostgreSQL | MySQL |
| **Auto-deploy** | ✅ Yes | ❌ Manual |
| **SSL** | ✅ Free | ✅ Free |
| **GitHub Integration** | ✅ Yes | ❌ No |
| **Easy Updates** | ✅ Git push | ❌ Manual FTP |

**Railway is BETTER and FREE!**

---

## 📞 NEED HELP?

### Common Questions:

**Q: Do I need GitHub?**
A: YES, for Railway automatic deployments. You already have it! ✅

**Q: Can Malaysian users access it fast?**
A: YES! Railway uses CDN, fast worldwide including Malaysia.

**Q: What if I exceed Railway free tier?**
A: Free tier is 500 hours/month. Your site uses ~1 hour = always running.
You won't exceed it for a small-medium site.

**Q: Can I use Hostinger email?**
A: YES! Your email service (contact@agrohubmy.com) still works.

**Q: If I want to move to Hostinger hosting later?**
A: YES, you can. Just export database and redeploy. Keep domain same.

---

## 🎯 SUMMARY

1. ✅ Your domain is good (no mistake!)
2. ✅ Don't buy Hostinger hosting (save money)
3. ✅ Use Railway (FREE, better, easier)
4. ✅ Just point domain (DNS records)
5. ✅ Site goes live in 30 minutes

**You're ready! Follow the steps above. I'm here if you need help!**

---

**Malaysian users will access agrohubmy.com perfectly! 🇲🇾**

Good luck! 🚀
