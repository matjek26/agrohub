# 🚀 AGROHUB Deployment Guide - PythonAnywhere (FREE)

## ✅ Step-by-Step Instructions:

### 1. Create FREE PythonAnywhere Account
- Go to: https://www.pythonanywhere.com/registration/register/beginner/
- Sign up (100% FREE forever)
- Login to your dashboard

### 2. Open Bash Console
- Click "Consoles" tab
- Click "Bash" to open terminal

### 3. Clone Your Repository
```bash
git clone https://github.com/matjek26/agrohub.git
cd agrohub
```

### 4. Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 agrohub-env
```

### 5. Install Requirements
```bash
pip install -r requirements.txt
```

### 6. Setup Database
```bash
python manage.py migrate
python manage.py populate_sample_data
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Configure Web App
- Go to "Web" tab
- Click "Add a new web app"
- Choose "Manual configuration"
- Select "Python 3.10"

### 9. Set Configuration:
**Source code:** `/home/yourusername/agrohub`
**Working directory:** `/home/yourusername/agrohub`
**Virtualenv:** `/home/yourusername/.virtualenvs/agrohub-env`

**WSGI configuration file:** Click and edit, replace with:
```python
import os
import sys

path = '/home/yourusername/agrohub'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 10. Static Files Mapping:
URL: `/static/`
Directory: `/home/yourusername/agrohub/staticfiles/`

URL: `/media/`
Directory: `/home/yourusername/agrohub/media/`

### 11. Reload Web App
Click "Reload" button

### 12. Visit Your Site!
Your site will be live at: **yourusername.pythonanywhere.com**

---

## 🎯 Quick Commands Reference:

### Update Your Site (After GitHub Changes):
```bash
cd ~/agrohub
git pull
python manage.py migrate
python manage.py collectstatic --noinput
# Then reload web app from Web tab
```

### View Logs:
Check error log from Web tab if issues occur

---

## 💡 Tips:
- Free tier allows 1 web app
- No credit card required
- Site never sleeps (always online)
- Perfect for student projects!

## 🆘 Need Help?
- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/
- Django deployment: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
