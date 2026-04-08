#!/bin/bash
cd /Users/kayleetran/Desktop/localbiz/pho101/images

echo "Downloading actual images from Pho 101 website..."
echo "=================================================="

# Download each image from pho101oc.com
declare -A images=(
    ["pho-bowl-hero.jpg"]="https://pho101oc.com/wp-content/uploads/2017/03/shutterstock_397328149.png"
    ["spring-roll-fresh.jpg"]="https://pho101oc.com/wp-content/uploads/2014/12/shutterstock_337040987-1.png"
    ["pho-noodles.jpg"]="https://pho101oc.com/wp-content/uploads/2014/12/shutterstock_552124468.png"
    ["pho-ingredients.jpg"]="https://pho101oc.com/wp-content/uploads/2014/12/shutterstock_133305233.png"
    ["restaurant-interior.jpg"]="https://pho101oc.com/wp-content/uploads/2014/12/shutterstock_323538716-copy.png"
    ["pho-ga.jpg"]="https://pho101oc.com/wp-content/uploads/2017/03/shutterstock_397328149.png"
    ["coffee-vn.jpg"]="https://pho101oc.com/wp-content/uploads/2014/12/shutterstock_552124468.png"
    ["dessert-sweet.jpg"]="https://pho101oc.com/wp-content/uploads/2014/12/shutterstock_133305233.png"
)

count=0
for filename in "${!images[@]}"; do
    url="${images[$filename]}"
    echo -n "  Downloading $filename... "
    curl -L -o "$filename" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" "$url" 2>/dev/null
    
    if [ -f "$filename" ]; then
        size=$(stat -f%z "$filename" 2>/dev/null || stat -c%s "$filename" 2>/dev/null)
        if [ "$size" -gt 10000 ]; then
            echo "✓ ($(numfmt --to=iec-i --suffix=B $size 2>/dev/null || echo "${size} bytes"))"
            ((count++))
        else
            echo "✗ (too small: $size bytes)"
        fi
    else
        echo "✗ (failed)"
    fi
done

echo ""
echo "=================================================="
echo "✓ Downloaded $count images from pho101oc.com"
echo "=================================================="
