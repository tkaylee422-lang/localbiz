#!/usr/bin/env python3
import urllib.request
import ssl
import re
import os
from urllib.parse import urljoin

# Ignore SSL errors
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://pho101oc.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0'
}

print("Scraping https://pho101oc.com/ for images...")
print("=" * 60)

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode('utf-8', errors='ignore')
    
    # Extract all image URLs - look for wp-content uploads
    img_pattern = r'(https?://[^"\'\s]*pho101oc\.com[^"\'\s]*\.(?:jpg|jpeg|png|gif|webp))'
    img_urls = re.findall(img_pattern, html, re.IGNORECASE)
    
    print(f"Found {len(img_urls)} images from pho101oc.com:\n")
    
    if img_urls:
        for img_url in img_urls:
            print(f"  {img_url}")
        
        # Try to download the first few
        os.chdir('/Users/kayleetran/Desktop/localbiz/pho101/images')
        print(f"\nDownloading images...")
        
        for idx, img_url in enumerate(img_urls[:10], 1):
            try:
                filename = f"pho101_img_{idx}.jpg"
                print(f"  [{idx}] {filename}...", end=' ')
                req = urllib.request.Request(img_url, headers=headers)
                urllib.request.urlretrieve(url=img_url, filename=filename)
                size = os.path.getsize(filename)
                if size > 10000:
                    print(f"✓ ({size:,} bytes)")
                else:
                    print(f"⚠ Small file ({size} bytes)")
            except Exception as e:
                print(f"✗ ({str(e)[:40]})")
    else:
        print("No direct image URLs found. Let me search more broadly...")
        # Search for any image tags
        all_img_pattern = r'src=["\']([^"\']+)["\']'
        all_urls = re.findall(all_img_pattern, html)
        print(f"Found {len(all_urls)} src attributes:")
        for url_item in all_urls[:15]:
            if 'jpg' in url_item.lower() or 'png' in url_item.lower():
                print(f"  {url_item[:80]}")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
