# 🚀 AGROHUB - QUICK START GUIDE

## Prerequisites Check
Before starting, make sure you have:
- ✅ Python 3.8 or higher installed
- ✅ pip (Python package manager)
- ✅ Command line access (PowerShell on Windows)

## Step-by-Step Setup (5 Minutes)

### OPTION 1: Automated Setup (Recommended)

Open PowerShell in the AGROHUB directory and run:

```powershell
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run automated setup script
.\setup.ps1
```

The setup script will:
- Create database tables
- Set up categories
- Create admin account
- Collect static files

### OPTION 2: Manual Setup

```powershell
# 1. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create database
python manage.py makemigrations
python manage.py migrate

# 4. Create superuser
python manage.py createsuperuser
# Enter: email, username, password

# 5. Create categories (optional)
python manage.py shell
```

In the Python shell, paste this:
```python
from marketplace.models import Category

categories = [
    {'name': 'aquaculture', 'display_name': 'Aquaculture', 'order': 1},
    {'name': 'seafoods', 'display_name': 'Seafoods', 'order': 2},
    {'name': 'agro_processed', 'display_name': 'Agro-Processed', 'order': 3},
    {'name': 'courses', 'display_name': 'Courses Offered', 'order': 4},
    {'name': 'tools_rent', 'display_name': 'Tools for Rent', 'order': 5},
    {'name': 'jobs', 'display_name': 'Jobs in Agro', 'order': 6},
]

for cat in categories:
    Category.objects.get_or_create(name=cat['name'], defaults=cat)
    
exit()
```

## Running the Website

```powershell
python manage.py runserver
```

Then open your browser:
- **Main Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

## First Steps After Setup

### 1. Login to Admin Panel
- Go to: http://localhost:8000/admin
- Use the superuser credentials you created

### 2. Add Sample Listings
- Click "Listings" → "Add Listing"
- Fill in:
  - Title (e.g., "Fresh Tilapia Fish")
  - Description
  - Price (e.g., 15.00)
  - Category (select from dropdown)
  - State and District
  - Upload an image
- Click "Save"

### 3. Create Test Accounts
- Go to: http://localhost:8000/users/register/
- Create a Buyer account
- Create a Seller account
- Test the different user experiences

### 4. Test Features

#### Homepage (/)
- ✅ Beautiful hero section with gradient
- ✅ Category cards with icons
- ✅ Trending products section
- ✅ Stats display

#### Product Listing (/listing/<slug>/)
- ✅ Large image gallery
- ✅ Product details
- ✅ Seller information
- ✅ Contact buttons (Chat, WhatsApp, Phone)

#### Search (/search/)
- ✅ Search by keyword
- ✅ Filter by category
- ✅ Filter by state

#### User Profile (/users/profile/)
- ✅ View your listings
- ✅ Edit profile
- ✅ Manage ads

#### AI Chatbot (Bottom-right corner)
- ✅ Click the robot icon
- ✅ Ask about farming tips
- ✅ Ask about MyGAP certification
- ✅ Get product recommendations

## Common Issues & Solutions

### Issue 1: "Module not found"
**Solution**: Make sure virtual environment is activated
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue 2: "No such table"
**Solution**: Run migrations
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Issue 3: Images not showing
**Solution**: Check MEDIA_URL settings and make sure you're running `runserver`

### Issue 4: PowerShell execution policy error
**Solution**: Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Project URLs

| Page | URL | Description |
|------|-----|-------------|
| Homepage | `/` | Main landing page |
| Search | `/search/` | Search and filter products |
| Category | `/category/<slug>/` | View category products |
| Product Detail | `/listing/<slug>/` | Individual product page |
| Create Listing | `/listing/create/` | Post new ad |
| Login | `/users/login/` | User login |
| Register | `/users/register/` | New user signup |
| Profile | `/users/profile/` | User dashboard |
| Admin | `/admin/` | Admin panel |

## Design Highlights

### Color Palette
- 🟢 **Primary**: Emerald Green (#10b981) - Nature, agriculture
- 🔵 **Secondary**: Deep Blue (#3b82f6) - Trust, corporate
- 🟡 **Accent**: Golden Yellow (#facc15) - Action, attention

### Typography
- Font Family: **Poppins** (Google Fonts)
- Weights: 300, 400, 500, 600, 700, 800

### Key UI Elements
- Card-based design (inspired by BookDoc)
- Rounded corners (rounded-2xl, rounded-3xl)
- Gradient backgrounds
- Hover animations
- Responsive grid layouts
- Floating chatbot widget

## Tips for Customization

### Change Colors
Edit [templates/base.html](templates/base.html) - look for `tailwind.config`

### Change Logo
Replace the seedling icon in navbar:
```html
<i class="fas fa-seedling text-white text-2xl"></i>
```

### Add More Categories
Go to Admin Panel → Categories → Add Category

### Customize Chatbot Responses
Edit [chatbot/views.py](chatbot/views.py) - `get_bot_response()` function

## Next Steps

1. **Add Real Data**: Upload actual product images and create listings
2. **Customize Content**: Update homepage text and categories
3. **Test Mobile**: Open on your phone to see responsive design
4. **Add Features**: Implement payment, notifications, etc.
5. **Deploy**: Consider Heroku, Railway, or AWS for production

## Support

Need help? Check:
- 📖 Full README: [README.md](README.md)
- 📁 Project Structure: See folder organization
- 🎨 Design Inspiration: BookDoc, Agrohub Indonesia

## Screenshots

You should see:
1. **Homepage**: Green gradient hero, category cards, trending section
2. **Product Page**: Large images, seller card, action buttons
3. **Chatbot**: Floating robot icon, chat window with AI responses
4. **Modern Design**: Clean, spacious, professional look

---

**Congratulations! Your Agrohub marketplace is ready! 🌾**

Start adding products and watch your agricultural marketplace come to life!
