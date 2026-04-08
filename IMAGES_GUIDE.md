# Image Setup Guide for Pho 101 Website

## Where to Get Images

### Option 1: Download from Pho 101's Official Website
Visit https://pho101oc.com/ and download their official photos:
1. Right-click on images on their website
2. Select "Save image as..."
3. Save to the `images/` folder with the appropriate filename

### Option 2: Use Stock Photos
If official images aren't available, use high-quality stock photos:

**Recommended Stock Photo Sites:**
- Unsplash (unsplash.com) - Free
- Pexels (pexels.com) - Free
- Pixabay (pixabay.com) - Free
- Shutterstock (shutterstock.com) - Paid
- Getty Images (gettyimages.com) - Paid

**Search Terms:**
- "Vietnamese pho bowl"
- "Vietnamese restaurant interior"
- "Vietnamese coffee"
- "Spring rolls food"
- "Restaurant kitchen"
- "Banh mi sandwich"
- "Restaurant staff"
- "Asian cuisine"

### Option 3: Take Your Own Photos
If you have access to the restaurant, take photographs of:
- Finished dishes
- Restaurant interior and ambiance
- Staff and family members
- Kitchen preparation
- Popular items

## Image File Naming Convention

Keep the filenames as specified in the requirements:
```
images/
├── banner.jpg
├── dish1.jpg through dish5.jpg
├── pho-bo.jpg
├── pho-ga.jpg
├── pho-vegetarian.jpg
├── com-tam.jpg
├── banh-mi.jpg
├── spring-rolls.jpg
├── iced-latte.jpg
├── fresh-juice.jpg
├── sugar-cane.jpg
├── thai-tea.jpg
├── lychee-drink.jpg
├── soft-drink.jpg
├── mango-sticky-rice.jpg
├── che.jpg
├── ice-cream.jpg
├── stuffed-banana.jpg
├── flan.jpg
├── sesame-balls.jpg
├── restaurant.jpg
└── staff.jpg
```

## Image Specifications

### Recommended Dimensions:
- **Gallery Images**: 800×600px or 1000×750px
- **Menu Item Images**: 400×300px or 600×450px
- **Full-width Sections**: 1200×400px or 1920×600px
- **Profile/Staff Photos**: 500×400px to 600×500px

### File Format:
- **Preferred**: JPG (smaller file size, good for photos)
- **Supported**: PNG (for images with transparency)
- **Modern**: WebP (best compression, if supported)

### File Size:
- Keep images under 500KB each for optimal loading speed
- Large images should be 200-400KB
- Small images should be 50-150KB

## Image Optimization Tools

### Free Online Tools:
1. **TinyPNG** (tinypng.com) - Compress PNG/JPG
2. **Compressor.io** (compressor.io) - Batch compression
3. **Imagecompressor.com** (imagecompressor.com) - Online compression
4. **Pixlr** (pixlr.com) - Online image editor

### Desktop Tools:
1. **ImageMagick** (Command-line tool)
2. **GIMP** (Free image editor)
3. **Photoshop** (Paid)
4. **Lightroom** (Adobe, paid)

### Command Line Optimization (ImageMagick):
```bash
# Resize and compress:
convert dish1.jpg -resize 800x600 -quality 85 dish1.jpg

# Batch resize all JPGs:
for img in *.jpg; do
  convert "$img" -resize 800x600 -quality 85 "optimized_$img"
done
```

## How to Add Images

### Method 1: Simple File Copy
1. Place images in the `images/` folder with correct filenames
2. Open `index.html` in your browser to verify
3. Images will automatically appear

### Method 2: Using File Manager
1. Open Finder (Mac) or File Explorer (Windows)
2. Navigate to `pho101/images/`
3. Copy images into the folder
4. Refresh browser to see changes

### Method 3: Command Line
```bash
# Navigate to projects folder
cd /Users/kayleetran/Desktop/localbiz/pho101/images

# Copy images from source folder (replace PATH with actual path)
cp /path/to/source/images/* .
```

## Placeholder Images (While Waiting for Real Photos)

If you don't have images yet, you can use placeholder services:

### Using Placeholder Services:
Add this to temporarily display placeholders in HTML:
```html
<img src="https://via.placeholder.com/800x600?text=Pho+Bowl" alt="Description">
```

### Popular Services:
- Placeholder.com - `https://placeholder.com/800×600`
- Lorem Picsum - `https://picsum.photos/800/600`
- DummyImage - `https://dummyimage.com/800x600/000/fff`

## Responsive Images Optimization

For better performance, you can add responsive images:
```html
<img 
  srcset="
    images/dish1-small.jpg 480w,
    images/dish1-medium.jpg 800w,
    images/dish1-large.jpg 1200w"
  sizes="(max-width: 600px) 480px,
         (max-width: 1000px) 800px,
         1200px"
  src="images/dish1.jpg"
  alt="Pho Bo - Beef Pho">
```

## Troubleshooting

### Images Not Showing?
1. Check filename spelling (case-sensitive on Mac/Linux)
2. Verify file extension (.jpg, .png)
3. Check that files are in `images/` folder
4. Try clearing browser cache (Ctrl+Shift+Delete)
5. Try different browser

### Images Look Blurry?
1. Use higher resolution source images
2. Check image dimensions match CSS
3. Recompress with different quality settings
4. Try JPG quality 85-90% instead of 70%

### Page Loading Slowly?
1. Compress images to smaller file sizes
2. Use appropriate image dimensions
3. Enable browser caching
4. Consider lazy loading images

## Additional Resources

- **Vietnamese Cuisine Education**: https://pho101oc.com/
- **Image Optimization Guide**: https://web.dev/image-optimization/
- **Responsive Images**: https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images
- **Web Performance**: https://web.dev/performance/

---

## Contact Information

For more assistance with image selection or optimization, refer to the main README.md file.

**Last Updated**: March 2024
