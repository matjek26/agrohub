# 🎨 AGROHUB - Visual Feature Guide

## What You'll See in the Interface

---

## 📍 HOMEPAGE - Interactive Malaysia Map

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│              🗺️  Explore by Location                         │
│    Discover agricultural products across Malaysia            │
│                                                               │
│  ┌─────────────────────────────┬────────────────────────┐   │
│  │                              │  📋 Browse by State     │   │
│  │         [MALAYSIA MAP]       │                         │   │
│  │    ┌────┐     ┌─────┐       │  ▸ Johor               │   │
│  │    │Perlis│   │Sabah │      │  ▸ Kedah               │   │
│  │    │Kedah │   └─────┘       │  ▸ Kelantan            │   │
│  │  ┌─┴─────┴┐  ┌──────┐       │  ▸ Melaka              │   │
│  │  │Penang  │  │Sarawak│      │  ▸ Negeri Sembilan     │   │
│  │  │Perak   │  └───────┘      │  ▸ Pahang              │   │
│  │  │Selangor│                  │  ▸ Penang              │   │
│  │  │ [KL]   │  ┌────────┐     │  ▸ Perak               │   │
│  │  │Melaka  │  │Kelantan│     │  ▸ Perlis              │   │
│  │  └─┬──────┤  │Treng.  │     │  ▸ Sabah               │   │
│  │    │Johor │  │Pahang  │     │  ▸ Sarawak             │   │
│  │    └──────┘  └────────┘     │  ▸ Selangor            │   │
│  │                              │  ▸ Terengganu          │   │
│  │   (Hover states to preview) │  ▸ Kuala Lumpur        │   │
│  │   (Click to view products)  │                         │   │
│  └─────────────────────────────┴────────────────────────┘   │
│                                                               │
│      👆 Click on any state to view listings                  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Color Scheme:**
- States: Green/Blue gradient (Primary colors)
- KL: Yellow/Orange (Accent - capital city)
- Hover: Darker shade
- Background: Light blue-green gradient

**Interactions:**
- 🖱️ Hover = Show state name + "Click to view listings"
- 👆 Click = Navigate to search results for that state
- 📱 Fully responsive on mobile

---

## 📝 CREATE LISTING - Availability Selector

```
┌─────────────────────────────────────────────────────────────┐
│  POST FREE AD                                                 │
│  Reach thousands of potential buyers across Malaysia          │
│                                                               │
│  ... [Other form fields: Title, Description, Price] ...      │
│                                                               │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 📅 Bulan Availability / Available Months              │  │
│  │    (Pilih bila produk anda available)                 │  │
│  │                                                        │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │ ☑ ♾️ Sentiasa Ada (Year-round availability)    │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │                                                        │  │
│  │  Select Months:                                       │  │
│  │  ┌────────┬────────┬────────┬────────┐              │  │
│  │  │ □ Jan  │ □ Feb  │ □ Mac  │ □ Apr  │              │  │
│  │  ├────────┼────────┼────────┼────────┤              │  │
│  │  │ □ Mei  │ □ Jun  │ □ Jul  │ □ Ogos │              │  │
│  │  ├────────┼────────┼────────┼────────┤              │  │
│  │  │ □ Sep  │ □ Okt  │ □ Nov  │ □ Dis  │              │  │
│  │  └────────┴────────┴────────┴────────┘              │  │
│  │                                                        │  │
│  │  📅 Pilih bulan bila produk anda ready untuk dijual  │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                               │
│  ... [Location, Images, etc.] ...                            │
│                                                               │
│  [✓ Post Listing]  [Cancel]                                  │
└─────────────────────────────────────────────────────────────┘
```

**Visual Features:**
- White background with subtle borders
- Selected months: Green background + Green border
- Unselected: Gray border
- Hover: Border changes to lighter green
- "Sentiasa Ada" checkbox: Disables month selection when checked
- Responsive grid: 3 columns on mobile, 4 on desktop

---

## 📦 PRODUCT DETAIL PAGE - Availability Display

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│  [Product Image]          ┌─────────────────────────────┐   │
│                           │  RM 45.00                   │   │
│  [Thumbnails]             │  📍 Johor, Johor Bahru      │   │
│                           │                             │   │
│                           │  Fresh Prawns - Quality A   │   │
│  Description:             │                             │   │
│  High quality prawns...   │  👤 Seller Info             │   │
│                           │  [Profile Picture]          │   │
│  ⚠️ Safety Tips           │  Ahmad Fishery              │   │
│  • Meet in public         │  ✓ Verified                 │   │
│  • Inspect before buy     │  🏢 Aquaculture Supplier    │   │
│                           │                             │   │
│                           │  [💬 Chat with Seller]      │   │
│                           │  [📱 WhatsApp Seller]       │   │
│                           │  [📞 Call Seller]           │   │
│                           │                             │   │
│                           │  ─────────────────────────  │   │
│                           │  👁️ 250     ⏰ 2 days ago   │   │
│                           │  Views        Posted        │   │
│                           │  ─────────────────────────  │   │
│                           │                             │   │
│                           │  ┌─────────────────────┐   │   │
│                           │  │ ✅ Available Months │   │   │
│                           │  │                     │   │   │
│                           │  │ Jan, Feb, Mac, Apr, │   │   │
│                           │  │ Mei, Jun, Ogos      │   │   │
│                           │  │                     │   │   │
│                           │  └─────────────────────┘   │   │
│                           └─────────────────────────────┘   │
│                                                               │
│  Similar Products:                                           │
│  [Product] [Product] [Product] [Product]                     │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Availability Badge Design:**
- Light green gradient background
- Calendar check icon (✅)
- White rounded card
- Clear, readable text
- Positioned below seller stats
- Automatically hides if no availability set
- Shows "Sentiasa Ada (Year-round)" if checked
- Shows comma-separated months if specific months selected

---

## 🎨 COLOR PALETTE

```
Primary Colors (Agricultural Green):
🟢 Primary-600: #059669 (Dark Green)
🟢 Primary-400: #34D399 (Medium Green)
🟢 Primary-50:  #ECFDF5 (Light Green Background)

Accent Colors (Energy Yellow):
🟡 Accent-400:  #FBBF24 (Bright Yellow)
🟡 Accent-500:  #F59E0B (Orange Yellow)

Map Colors:
🗺️ States: Primary gradient
📍 KL: Accent yellow (capital)
⚪ Borders: White stroke
💧 Background: Blue-green gradient

Availability Section:
✅ Background: Green-50 → Emerald-50 gradient
📅 Icon: Green-600
📝 Text: Gray-700 / Gray-900
```

---

## 📱 RESPONSIVE BEHAVIOR

### Desktop (1200px+):
- Map: 2/3 width, List: 1/3 width
- Months: 4 columns
- Full map visible

### Tablet (768px - 1199px):
- Map: Full width, List below
- Months: 3 columns
- Scrollable list

### Mobile (< 768px):
- Stack everything vertically
- Months: 3 columns
- Simplified map
- Touch-friendly buttons

---

## ✨ ANIMATIONS & INTERACTIONS

### Map Interactions:
```javascript
Hover State:
  • Color: Primary-400 → Primary-600
  • Transition: 300ms smooth
  • Cursor: pointer
  • Tooltip appears

Click Action:
  • Navigate to: /search?state=<state_name>
  • Smooth page transition
```

### Month Selector:
```javascript
"Sentiasa Ada" Checked:
  • Month grid opacity: 0.5
  • Pointer events: none
  • All months: unchecked & disabled

Month Selected:
  • Background: Primary-50
  • Border: Primary-600 (2px)
  • Visual feedback immediate
```

---

## 🎯 KEY VISUAL IMPROVEMENTS

1. **Professional Design**
   - Consistent color scheme
   - Smooth animations
   - Modern UI components

2. **User-Friendly**
   - Clear labels in Bahasa & English
   - Intuitive interactions
   - Visual feedback

3. **Mobile Optimized**
   - Touch-friendly targets
   - Responsive layouts
   - Fast loading

4. **Accessibility**
   - High contrast text
   - Large click areas
   - Clear iconography

---

## 📸 VISUAL HIERARCHY

```
Homepage:
1. Hero Section (Largest)
2. Categories (Medium)
3. 🆕 INTERACTIVE MAP (Large) ← NEW!
4. Trending Products (Medium)
5. Features (Small)
6. CTA (Medium)

Create Listing:
1. Title & Category
2. Description & Price
3. 🆕 AVAILABILITY SECTION ← NEW!
4. Location
5. Images
6. Submit

Product Detail:
1. Images (Left/Top)
2. Price & Title
3. Seller Info
4. Action Buttons
5. Stats (Views, Posted)
6. 🆕 AVAILABILITY BADGE ← NEW!
7. Similar Products
```

---

## 🎉 EXPERIENCE FLOW

### Seller Journey with New Features:
```
1. Click "Post Free Ad"
   ↓
2. Fill basic info (title, description, price)
   ↓
3. 🆕 Select availability months
   • Choose "Sentiasa Ada" OR
   • Pick specific harvest months
   ↓
4. Add location & images
   ↓
5. Submit listing
   ↓
6. 🎉 Buyers see availability info!
```

### Buyer Journey with Map:
```
1. Visit homepage
   ↓
2. 🆕 See interactive map section
   ↓
3. Hover over home state (e.g., "Johor")
   ↓
4. Click to view products
   ↓
5. Browse local products
   ↓
6. Click product to see details
   ↓
7. 🆕 Check availability months
   ↓
8. Contact seller if timing works!
```

---

## 💡 PRO TIPS FOR USERS

### For Sellers:
✓ **Be Specific**: Select exact months for seasonal products
✓ **Use "Sentiasa Ada"**: For year-round products like processed goods
✓ **Update Regularly**: Change availability as seasons change
✓ **Attract Buyers**: Clear availability = more confident buyers

### For Buyers:
✓ **Check Map First**: Find products near you
✓ **Verify Availability**: Before contacting seller
✓ **Plan Ahead**: Know when seasonal items will be ready
✓ **Regional Shopping**: Explore different states for variety

---

**Live Demo**: http://127.0.0.1:8000/
**Last Updated**: February 5, 2026

🎨 **Enjoy the beautiful new interface!** 🚀

