# Pho 101 - Restaurant Website

A sophisticated, interactive website for Pho 101 restaurant in Garden Grove, Orange County. Built with HTML, CSS, and JavaScript featuring smooth page transitions, hover effects, and a responsive design.

## 🎨 Design Features

- **Color Scheme**: Dark Gray, White, Gold, and Red
- **Smooth Transitions**: All pages and elements feature elegant fade-in animations
- **Hover Effects**: Buttons, images, and interactive elements respond to mouse hover
- **Responsive Design**: Adapts beautifully to mobile, tablet, and desktop screens
- **Gallery**: Interactive image gallery with manual and auto-advance functionality
- **Modern Typography**: Sophisticated serif fonts for elegant presentation

## 📁 Directory Structure

```
pho101/
├── index.html           # Home page
├── menu.html            # Menu page with grid layout
├── about.html           # About Us page with family history and video
├── contact.html         # Contact page with map and contact info
├── css/
│   └── styles.css       # All CSS styles and animations
├── js/
│   └── script.js        # Interactive functionality
├── images/              # Image files (see below)
└── README.md            # This file
```

## 🖼️ Images Needed

Place the following images in the `images/` folder:

### Home Page Gallery
- `dish1.jpg` - Beef Pho (Pho Bo)
- `dish2.jpg` - Chicken Pho (Pho Ga)
- `dish3.jpg` - Spring Rolls
- `dish4.jpg` - Vietnamese Salad
- `dish5.jpg` - Banh Mi Sandwich

### Menu Page - Main Dishes
- `pho-bo.jpg` - Beef Pho
- `pho-ga.jpg` - Chicken Pho
- `pho-vegetarian.jpg` - Vegetarian Pho
- `com-tam.jpg` - Broken Rice with Chicken
- `banh-mi.jpg` - Vietnamese Sandwich
- `spring-rolls.jpg` - Fresh Spring Rolls

### Menu Page - Drinks
- `iced-latte.jpg` - Vietnamese Iced Coffee
- `fresh-juice.jpg` - Fresh Fruit Juice
- `sugar-cane.jpg` - Sugar Cane Juice
- `thai-tea.jpg` - Thai Tea
- `lychee-drink.jpg` - Lychee Drink
- `soft-drink.jpg` - Soft Drinks

### Menu Page - Desserts
- `mango-sticky-rice.jpg` - Mango Sticky Rice
- `che.jpg` - Vietnamese Sweet Soup
- `ice-cream.jpg` - Egg Custard Ice Cream
- `stuffed-banana.jpg` - Fried Banana
- `flan.jpg` - Caramel Flan
- `sesame-balls.jpg` - Fried Sesame Balls

### About Us Page
- `banner.jpg` - Banner image (optional, for background)
- `restaurant.jpg` - Restaurant interior
- `staff.jpg` - Staff and family photo

### Image Specifications
- **Recommended Resolution**: 800x600px or larger
- **Format**: JPG, PNG, or WebP
- **Optimization**: Compress images for faster loading (use tools like TinyPNG)

## 🚀 How to Use

1. **Open in Browser**: Open `index.html` in your web browser
2. **Navigation**: Use the header menu to navigate between pages
3. **Gallery**: 
   - Click arrow buttons to navigate manually
   - Click dots to jump to specific slides
   - Images auto-advance every 6 seconds
   - Use arrow keys for keyboard navigation
   - Swipe on mobile devices for touch navigation

## 📱 Features

- **Sticky Header**: Navigation stays visible while scrolling
- **Page Transitions**: Smooth fade-in effects when loading pages
- **Hover Effects**: 
  - Navigation links highlight in gold
  - Buttons scale and glow on hover
  - Images zoom slightly on hover
  - Menu items lift up with enhanced shadows
- **Interactive Gallery**: Auto-playing with manual controls
- **Responsive Layout**: Adapts to all screen sizes
- **Contact Integration**: 
  - Clickable phone and email links
  - Embedded Google Map
  - Social media links to Facebook, Instagram, and Google Maps

## 🎯 Sections

### Home Page
- Large banner with restaurant name and tagline
- Restaurant description highlighting 35+ years of family tradition
- Auto-playing image gallery of signature dishes
- CTA button to view full menu

### Menu Page
- Organized into three sections: Main Dishes, Drinks, Desserts
- Grid layout with 12-18 items total
- Each item displays: image, name, description, and price
- Hover effects reveal product details

### About Us Page
- Family history and restaurant background
- Two image placeholders (restaurant and staff)
- Embedded video from restaurant channel
- Information about Vietnamese cuisine heritage

### Contact Page
- Embedded Google Map showing Garden Grove location
- Complete contact information:
  - Phone number (clickable)
  - Email address (clickable)
  - Physical address
  - Hours of operation
- Social media icons linking to:
  - Facebook
  - Instagram
  - Google Maps

## 🔧 Customization

### Change Colors
Edit the CSS variables in `css/styles.css`:
```css
:root {
  --dark-gray: #2a2a2a;
  --light-gray: #4a4a4a;
  --white: #ffffff;
  --gold: #d4af37;
  --red: #c41e3a;
  --accent-dark: #1a1a1a;
}
```

### Update Contact Information
Edit the following files with your actual contact details:
- `contact.html` - Phone, email, address, hours
- `menu.html` - Prices and menu items

### Modify Gallery Speed
Edit `js/script.js`:
```javascript
setInterval(() => {
  changeSlide(1);
}, 6000);  // Change 6000 to desired milliseconds
```

## 📝 Menu Items Reference

**Reference Data from Pho 101 OC Website:**
- Restaurant: Pho 101, Orange County
- Location: Garden Grove, CA
- Family: Tran family
- History: 35+ years, three generations
- Founded: 1989
- Specialty: Authentic Vietnamese Pho and cuisine
- Social Media:
  - Facebook: Pho101-1281717348589895
  - Instagram: eatpho101

## 💡 Tips

1. **Add Real Photos**: Download high-quality images from the actual Pho 101 website or social media
2. **Optimize Images**: Use image compression tools to improve page load speed
3. **Test Responsiveness**: Open in different browser sizes and devices
4. **Video**: Replace the YouTube video embed in `about.html` with a real restaurant video
5. **SEO**: Add meta descriptions and keywords to each page
6. **Analytics**: Add Google Analytics tracking code to monitor visitor behavior

## 🔐 Future Enhancements

- Add online ordering system
- Implement email newsletter signup
- Add photo gallery swiper library
- Implement lazy loading for images
- Add customer reviews/testimonials
- Create reservation system
- Add multi-language support

## 📄 License

This website template is created for Pho 101 restaurant. All rights reserved.

## 📧 Support

For questions or customizations, contact the web development team.

---

**Last Updated**: March 2024
**Version**: 1.0
