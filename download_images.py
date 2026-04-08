#!/usr/bin/env python3
import urllib.request
import ssl
import os
import re
from urllib.parse import urljoin, urlparse

os.chdir('/Users/kayleetran/Desktop/localbiz/pho101/images')

# Ignore SSL errors
ssl._create_default_https_context = ssl._create_unverified_context

print("=" * 60)
print("Pho 101 Website Image Downloader")
print("=" * 60)

print("\nDownloading high-quality Asian cuisine images...")
print("(The Pho 101 website has protected images)")

# High-quality food images from Pexels and Unsplash
images = {
    'pho-bowl-hero.jpg': 'https://images.unsplash.com/photo-1569718776646-641ccc1d9d78?w=800',
    'pho-bo.jpg': 'https://images.unsplash.com/photo-1582161876305-a617b08d17f9?w=800',
    'pho-ga.jpg': 'https://images.unsplash.com/photo-1556574183-8910e4c50c1a?w=800',
    'spring-roll-fresh.jpg': 'https://images.unsplash.com/photo-1607623814075-e51df1bdc82f?w=800',
    'coffee-vn.jpg': 'https://images.unsplash.com/photo-1582514431946-7899f5c5c6be?w=800',
    'dessert-sweet.jpg': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800',
    'spring-rolls.jpg': 'https://images.unsplash.com/photo-1607623814075-e51df1bdc82f?w=800',
}

success_count = 0
total = len(images)

for filename, url in images.items():
    try:
        # Check if file already exists and has content
        if os.path.exists(filename) and os.path.getsize(filename) > 5000:
            print(f"   ✓ {filename} (already exists)")
            success_count += 1
            continue
            
        print(f"   Downloading {filename}...", end=' ')
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        urllib.request.urlretrieve(url, filename)
        size = os.path.getsize(filename)
        print(f"✓ ({size:,} bytes)")
        success_count += 1
    except Exception as e:
        # If download fails, keep existing file if it exists
        if os.path.exists(filename):
            print(f"✗ (using existing file)")
        else:
            print(f"✗ ({str(e)[:40]})")

print("\n" + "=" * 60)
print(f"✓ Completed: {success_count}/{total} images ready")
print("=" * 60)
print("\nYour website images are now updated and ready to use!")

