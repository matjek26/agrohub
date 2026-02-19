# 🌾 AGROHUB - Malaysia's Largest Online Agromarketplace

A modern, beautiful Django-based agricultural marketplace connecting farmers, suppliers, and buyers across Malaysia.

## 🎨 Design Features

- **Emerald Green Theme**: Representing agriculture and nature
- **Deep Blue Accents**: Professional corporate feel (Magna Cita branding)
- **Golden Yellow CTAs**: High-contrast call-to-action buttons
- **Modern Card-Based Layout**: Clean, spacious design inspired by BookDoc
- **Responsive Design**: Mobile-first approach using Tailwind CSS
- **AI Chatbot Widget**: Floating assistant powered by Magna Cita AI

## 🚀 Quick Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Navigate to project directory:**
```powershell
cd d:\AGROHUB
```

2. **Create virtual environment:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. **Install dependencies:**
```powershell
pip install -r requirements.txt
```

4. **Run migrations:**
```powershell
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser:**
```powershell
python manage.py createsuperuser
```

6. **Load initial categories (optional):**
```powershell
python manage.py shell
```
Then in the Python shell:
```python
from marketplace.models import Category

categories = [
    {'name': 'aquaculture', 'display_name': 'Aquaculture', 'description': 'Fish farming and aquatic products'},
    {'name': 'seafoods', 'display_name': 'Seafoods', 'description': 'Fresh seafood products'},
    {'name': 'agro_processed', 'display_name': 'Agro-Processed', 'description': 'Processed agricultural goods'},
    {'name': 'courses', 'display_name': 'Courses Offered', 'description': 'Agricultural training and courses'},
    {'name': 'tools_rent', 'display_name': 'Tools for Rent', 'description': 'Agricultural equipment rental'},
    {'name': 'jobs', 'display_name': 'Jobs in Agro', 'description': 'Career opportunities in agriculture'},
]

for cat in categories:
    Category.objects.get_or_create(**cat)

exit()
```

7. **Run development server:**
```powershell
python manage.py runserver
```

8. **Access the website:**
Open your browser and go to: `http://localhost:8000`

## 📁 Project Structure

```
AGROHUB/
├── core/                   # Project settings
├── marketplace/            # Main marketplace app
├── users/                  # Authentication & profiles
├── chatbot/                # AI chatbot functionality
├── templates/              # HTML templates
│   ├── base.html          # Base layout
│   ├── marketplace/       # Marketplace pages
│   ├── users/             # Auth pages
│   └── includes/          # Reusable components
├── media/                  # Uploaded images
├── static/                 # Static files
└── manage.py
```

## 🎯 Key Features

### 1. **Homepage**
- Hero section with gradient background
- Category cards with icons
- Trending products section
- Stats display (40K+ products, 10K+ sellers, 2M+ users)
- Feature highlights

### 2. **Categories**
- Aquaculture (Fish & Aquatic)
- Seafoods (Fresh Seafood)
- Agro-Processed (Processed Goods)
- Courses Offered (Training Programs)
- Tools for Rent (Equipment Rental)
- Jobs in Agro (Career Opportunities)

### 3. **Product Listings**
- High-quality image gallery
- Detailed product information
- Seller verification badges
- Multiple contact options (Chat, WhatsApp, Phone)
- View count tracking
- Related products suggestions

### 4. **User Authentication**
- Beautiful login/register pages
- Two user types: Buyer and Seller/Company
- Profile management
- Listing management dashboard

### 5. **AI Chatbot**
- Floating widget (bottom-right)
- Powered by Magna Cita AI
- Helps with farming tips, MyGAP certification, product recommendations
- Real-time chat interface

### 6. **Search & Filters**
- Full-text search
- Filter by category
- Filter by state/location
- Responsive grid layout

## 🎨 Color Scheme

- **Primary (Emerald Green)**: `#10b981` - Agriculture, nature
- **Secondary (Deep Blue)**: `#3b82f6` - Trust, professionalism
- **Accent (Golden Yellow)**: `#facc15` - Action, attention
- **Backgrounds**: White, Gray-50, Gradient overlays

## 🌟 Admin Panel

Access the admin panel at: `http://localhost:8000/admin`

Features:
- Manage users and profiles
- Approve/moderate listings
- Manage categories
- View chatbot conversations
- Analytics dashboard

## 📱 Mobile Responsive

All pages are fully responsive with:
- Mobile-first design approach
- Touch-friendly buttons
- Optimized images
- Collapsible navigation

## 🔒 Security Features

- CSRF protection
- Secure password hashing
- User authentication required for posting
- Image upload validation
- XSS protection

## 🚧 Future Enhancements

- [ ] Payment integration
- [ ] Advanced AI chatbot with NLP
- [ ] Email notifications
- [ ] SMS alerts
- [ ] Social media integration
- [ ] Rating & review system
- [ ] Advanced analytics
- [ ] Multi-language support (Bahasa Malaysia)
- [ ] Progressive Web App (PWA)

## 👨‍💻 Development

### Adding Sample Data

To add sample listings via admin panel:
1. Go to `http://localhost:8000/admin`
2. Login with superuser credentials
3. Navigate to "Listings"
4. Click "Add Listing"
5. Fill in the details and upload images

### Customizing Design

- Colors: Edit `tailwind.config` in [base.html](templates/base.html)
- Fonts: Change Google Fonts link in `<head>`
- Icons: Using Font Awesome 6.5.1

## 📄 License

Powered by Magna Cita Sdn. Bhd.

## 🤝 Support

For support, contact:
- Email: contact@agrohub.my
- Phone: +60 12-345 6789

---

**Built with ❤️ for Malaysian Farmers and Agribusiness**
