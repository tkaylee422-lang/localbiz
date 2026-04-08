# Quick Start Guide - Pho 101 Website

## 🚀 Getting Started in 3 Steps

### Step 1: Open the Website
1. Open your file manager
2. Navigate to: `/Users/kayleetran/Desktop/localbiz/pho101/`
3. Double-click `index.html` to open in browser
4. Or right-click `index.html` → "Open With" → Choose your browser

### Step 2: Test Navigation
- Click the menu items in the header (Home, Menu, About Us, Contact)
- Click the "Back to Home" links on other pages
- Notice the smooth page transitions and hover effects

### Step 3: Add Images (Optional)
- Download images from Pho 101 website: https://pho101oc.com/
- See `IMAGES_GUIDE.md` for detailed image instructions
- Copy images to `images/` folder
- Refresh browser to see images appear

## 📋 File Structure at a Glance

```
Your project is located at:
/Users/kayleetran/Desktop/localbiz/pho101/

Structure:
├── index.html (Home page)
├── menu.html (Menu with 18 items)
├── about.html (Family story + video)
├── contact.html (Contact info + map)
├── css/
│   └── styles.css (All styling)
├── js/
│   └── script.js (Interactivity)
├── images/ (Put photos here)
│   (Currently empty - see IMAGES_GUIDE.md)
├── README.md (Full documentation)
├── IMAGES_GUIDE.md (Image instructions)
└── QUICK_START.md (This file)
```

## ✨ Features to Test

### Home Page
✓ Large banner with restaurant name
✓ Description of the restaurant
✓ Interactive image gallery
  - Click left/right arrows
  - Click dot indicators
  - Auto-rotates every 6 seconds
  - Use keyboard arrows on desktop
  - Swipe on mobile

### Menu Page
✓ 18 menu items in 3 categories:
  - Main Dishes (6 items)
  - Drinks (6 items)
  - Desserts (6 items)
✓ Each item shows: image, name, description, price
✓ Hover effects make cards lift up
✓ Responsive grid layout

### About Us Page
✓ Family history (35+ years, Tran family)
✓ Two image placeholders
✓ Embedded video from restaurant
✓ Information about Vietnamese cuisine

### Contact Page
✓ Full contact information
  - Phone (714) 555-1234
  - Email info@pho101oc.com
  - Address in Garden Grove
  - Business hours
✓ Embedded Google Map
✓ Social media icons
  - Facebook
  - Instagram
  - Google Maps

## 🎨 Styling Features

✓ **Color Scheme**: Dark gray, white, gold, red
✓ **Smooth Transitions**: All pages fade in nicely
✓ **Hover Effects**: 
  - Menu items lift with shadow
  - Buttons glow with color change
  - Images zoom slightly
  - Links change color to red
✓ **Responsive Design**: Works on mobile, tablet, desktop
✓ **Sticky Header**: Navigation always visible
✓ **Professional Feel**: Serif fonts, elegant spacing

## 🔧 Making Changes

### Change Restaurant Information
Edit these files:
- **Contact Info**: Edit `contact.html` (phone, email, hours)
- **Menu Items**: Edit `menu.html` (item names, descriptions, prices)
- **About Text**: Edit `about.html` (family story)

### Change Colors
Edit `css/styles.css` line 10-17:
```css
:root {
  --dark-gray: #2a2a2a;
  --light-gray: #4a4a4a;
  --white: #ffffff;
  --gold: #d4af37;
  --red: #c41e3a;
}
```

### Add Real Video
In `about.html`, change the YouTube link:
```html
src="https://www.youtube.com/embed/YOUR_VIDEO_ID"
```

### Update Menu Prices
Edit the price in `menu.html`:
```html
<div class="menu-item-price">$12.99</div>
```

## 📱 Browser Compatibility

✓ Chrome/Edge (Modern, best performance)
✓ Firefox (Full support)
✓ Safari (Full support)
✓ Mobile browsers (Responsive design)

## ⚡ Performance Tips

1. **Compress Images**: Use TinyPNG.com to reduce file sizes
2. **Cache**: Browser automatically caches CSS/JS
3. **Faster Loading**: 
   - Keep images under 500KB
   - Images load as you scroll
   - Smooth performance on all devices

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Page won't load | Check file path is correct |
| Images not showing | See IMAGES_GUIDE.md |
| Clicked link does nothing | Clear browser cache (Ctrl+Shift+Del) |
| Styles look wrong | Refresh browser (Ctrl+F5) |
| Gallery not working | Use modern browser (Chrome, Firefox, Safari) |

## 📧 Next Steps

1. **Add Real Images**: Follow `IMAGES_GUIDE.md`
2. **Update Menu Items**: Edit prices and descriptions in `menu.html`
3. **Update Contact Info**: Edit phone, email, hours in `contact.html`
4. **Add Real Video**: Replace YouTube video link in `about.html`
5. **Deploy Online**: Upload to web hosting service

## 🌐 Hosting the Website

When ready to publish online, you'll need:
1. **Web Hosting**: GoDaddy, Bluehost, Netlify, Vercel
2. **Custom Domain**: Optional but recommended
3. **Upload Files**: Use FTP or web host's file manager
4. **Test**: Check all links work on live site

## 📞 Support Resources

- **HTML Help**: https://developer.mozilla.org/en-US/docs/Web/HTML
- **CSS Help**: https://developer.mozilla.org/en-US/docs/Web/CSS
- **JavaScript Help**: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- **Google Maps API**: https://developers.google.com/maps
- **Responsive Design**: https://web.dev/responsive-web-design-basics/

## 🎯 Customization Checklist

Before publishing, verify:

- [ ] Added all restaurant photos to `images/` folder
- [ ] Updated phone number in `contact.html`
- [ ] Updated email address in `contact.html`
- [ ] Updated restaurant address in `contact.html`
- [ ] Updated business hours in `contact.html`
- [ ] Updated menu items and prices in `menu.html`
- [ ] Updated family story in `about.html`
- [ ] Added real video link in `about.html`
- [ ] Tested all links work correctly
- [ ] Tested on desktop, tablet, and mobile
- [ ] Compressed all images
- [ ] Updated social media links
- [ ] Verified colors match brand

## 🚀 Launch Checklist

Before going live:

- [ ] All images optimized and compressed
- [ ] All text content reviewed for spelling/grammar
- [ ] All links tested and working
- [ ] Mobile responsiveness tested
- [ ] Browser compatibility tested
- [ ] Page speed acceptable
- [ ] Analytics code added (if needed)
- [ ] Copyright year updated
- [ ] SEO meta tags updated
- [ ] Backup of site created

---

## Questions?

Refer to the full documentation in `README.md` or `IMAGES_GUIDE.md`

**Website Created**: March 2024
**Status**: Ready to customize with your content
**Version**: 1.0
