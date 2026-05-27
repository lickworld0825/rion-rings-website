#!/usr/bin/env python3
"""Fix horizontal overflow: hide nav-cta on mobile, add html overflow-x:hidden."""
import os, re

BASE = '/Users/aoyamayuma/rion-rings-website'

HTML_FILES = [
    'rion-rings.html', 'collection.html', 'about.html', 'product.html',
    'shipping.html', 'care.html', 'heritage.html', 'legal.html',
    'order.html', 'faq.html',
    'series-a.html', 'series-b.html', 'series-c.html', 'series-d.html',
    'series-f.html', 'series-g.html', 'series-h.html', 'series-j.html',
]

for filename in HTML_FILES:
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f'  SKIP: {filename}')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Add overflow-x:hidden to html,body rule
    # Look for existing html,body or html { or body { rules
    # Simplest: add to the <style> block early on — find html selector
    if 'html{' in content or 'html {' in content:
        content = content.replace('html{', 'html{overflow-x:hidden;', 1)
        content = content.replace('html {', 'html{overflow-x:hidden;', 1)
    elif '*,*::before,*::after' in content:
        # Insert right after the reset block
        content = content.replace(
            'html{margin:0;padding:0}',
            'html{margin:0;padding:0;overflow-x:hidden}'
        )

    # If still not added, insert a rule at the start of <style>
    if 'overflow-x:hidden' not in content:
        content = content.replace(
            '<style>',
            '<style>\nhtml,body{overflow-x:hidden}'
        )

    # 2. In @media(max-width:1024px) block, add .nav-cta{display:none}
    # Find the media query block and inject
    media_re = re.compile(r'(@media\(max-width:1024px\)\{)')
    if '.nav-cta{display:none}' not in content:
        content = media_re.sub(r'\1.nav-cta{display:none}', content)

    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  Updated: {filename}')
    else:
        print(f'  No change: {filename}')

print('Done!')
