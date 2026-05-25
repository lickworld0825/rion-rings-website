#!/usr/bin/env python3
"""Update nav menus in all existing HTML pages to the canonical structure."""
import re, os

BASE = '/Users/aoyamayuma/rion-rings-website'

# Pages and their "active" menu item (0-indexed position in the 8-item menu)
# Menu order: 0=Home, 1=Collection, 2=About, 3=Order, 4=FAQ, 5=Shipping, 6=Care, 7=Contact
PAGES = {
    'rion-rings.html': 0,
    'collection.html': 1,
    'about.html': 2,
    'product.html': None,   # no active item
    'shipping.html': 5,
    'care.html': 6,
    'heritage.html': None,  # not in main menu
    'legal.html': None,
}

MENU_ITEMS = [
    ('rion-rings.html',     '01', 'Home'),
    ('collection.html',     '02', 'Collection'),
    ('about.html',          '03', 'About <em>Rion</em>'),
    ('order.html',          '04', 'How to <em>Order</em>'),
    ('faq.html',            '05', 'FAQ'),
    ('shipping.html',       '06', 'Shipping &amp; <em>Returns</em>'),
    ('care.html',           '07', 'Care <em>Guide</em>'),
    ('rion-rings.html#contact', '08', 'Contact'),
]

def build_menu_links(active_idx):
    lines = []
    for i, (href, num, label) in enumerate(MENU_ITEMS):
        active = ' class="menu-active"' if i == active_idx else ''
        lines.append(f'        <a href="{href}"{active} onclick="closeMenu()"><span class="menu-num">{num}</span><span>{label}</span></a>')
    return '\n'.join(lines)

# Regex to match the entire <nav class="menu-links">...</nav> block
NAV_RE = re.compile(
    r'(<nav class="menu-links">)\s*\n(.*?)(\s*</nav>)',
    re.DOTALL
)

def fix_page(filename, active_idx):
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f'  SKIP (not found): {filename}')
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_links = build_menu_links(active_idx)
    replacement = f'\\1\n{new_links}\\3'
    new_content, count = NAV_RE.subn(replacement, content, count=1)

    if count == 0:
        print(f'  WARN no nav match: {filename}')
        return

    # Also fix any stray footer/inline faq links
    new_content = new_content.replace('href="rion-rings.html#faq"', 'href="faq.html"')
    # Fix care.html btn that links to faq
    # (Already covered by above replace)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  Updated: {filename}')

for filename, active_idx in PAGES.items():
    fix_page(filename, active_idx)

print('Done!')
