#!/usr/bin/env python3
"""Transform US site to a target country site."""
import sys, re, glob

CONFIGS = {
    'uk': {
        'country':       'United Kingdom',
        'country_abbr':  'UK',
        'country_iso':   'GB',
        'domain':        'uk.myart-rion.com',
        'currency':      'GBP',
        'ls_key':        'rion_uk_lang',
        'cookie_key':    'rion_uk_cookies_accepted',
        'ga':            'G-PLACEHOLDER_UK',
        'tax_announce':  'No Import Duties · VAT Included',
        'price_note':    'Free UK Shipping · VAT Included',
        'price_note_ja': '英国へ無料配送・VAT込み',
        'series_ddp':    'Free UK Shipping · VAT Incl.',
        'series_ddp_ja': '英国へ無料配送・VAT込み',
        'consumer_law':  'UK consumer protection laws',
        'coverage':      'all of the United Kingdom',
        'ja_country':    '英国',
        'ja_currency':   'GBP',
        'format_price':  "return '£' + n.toLocaleString('en-GB');",
        'page_title_suffix': 'UK',
        'prod_prices': {
            5100: 4000, 5200: 4100, 5400: 4300,
            5900: 4700, 6000: 4700, 6100: 4800,
            6200: 4900, 6400: 5100, 6500: 5100,
            6600: 5200, 6700: 5300, 6800: 5400,
            6900: 5500, 7200: 5700, 7300: 5800,
            7400: 5800, 7500: 5900, 7600: 6000,
            7700: 6100, 7800: 6200, 7900: 6200,
            8000: 6300, 8200: 6500, 8300: 6600,
        },
        'html_prices': {
            '$5,100': '£4,000', '$5,200': '£4,100', '$5,400': '£4,300',
            '$5,900': '£4,700', '$6,000': '£4,700', '$6,100': '£4,800',
            '$6,200': '£4,900', '$6,400': '£5,100', '$6,500': '£5,100',
            '$6,600': '£5,200', '$6,700': '£5,300', '$6,800': '£5,400',
            '$6,900': '£5,500', '$7,200': '£5,700', '$7,300': '£5,800',
            '$7,400': '£5,800', '$7,500': '£5,900', '$7,600': '£6,000',
            '$7,700': '£6,100', '$7,800': '£6,200', '$7,900': '£6,200',
            '$8,000': '£6,300', '$8,200': '£6,500', '$8,300': '£6,600',
            '$20,000': '£15,800', '$21,000': '£16,600',
            '$65': '£51', '$25': '£20', '+$7': '+£6',
        },
        'price_min': '£4,000',
    },
    'ca': {
        'country':       'Canada',
        'country_abbr':  'Canada',
        'country_iso':   'CA',
        'domain':        'ca.myart-rion.com',
        'currency':      'CAD',
        'ls_key':        'rion_ca_lang',
        'cookie_key':    'rion_ca_cookies_accepted',
        'ga':            'G-PLACEHOLDER_CA',
        'tax_announce':  'No Import Duties · GST/HST May Apply',
        'price_note':    'Free Canada Shipping · No Duties',
        'price_note_ja': 'カナダへ無料配送・関税なし',
        'series_ddp':    'Free Canada Shipping · No Duties',
        'series_ddp_ja': 'カナダへ無料配送・関税なし',
        'consumer_law':  'Canadian consumer protection laws',
        'coverage':      'all of Canada',
        'ja_country':    'カナダ',
        'ja_currency':   'CAD',
        'format_price':  "return 'CA$' + n.toLocaleString('en-CA');",
        'page_title_suffix': 'Canada',
        'prod_prices': {
            5100: 6900, 5200: 7100, 5400: 7300,
            5900: 8000, 6000: 8200, 6100: 8300,
            6200: 8400, 6400: 8700, 6500: 8800,
            6600: 9000, 6700: 9100, 6800: 9200,
            6900: 9400, 7200: 9800, 7300: 9900,
            7400: 10100, 7500: 10200, 7600: 10300,
            7700: 10500, 7800: 10600, 7900: 10700,
            8000: 10900, 8200: 11200, 8300: 11300,
        },
        'html_prices': {
            '$5,100': 'CA$6,900', '$5,200': 'CA$7,100', '$5,400': 'CA$7,300',
            '$5,900': 'CA$8,000', '$6,000': 'CA$8,200', '$6,100': 'CA$8,300',
            '$6,200': 'CA$8,400', '$6,400': 'CA$8,700', '$6,500': 'CA$8,800',
            '$6,600': 'CA$9,000', '$6,700': 'CA$9,100', '$6,800': 'CA$9,200',
            '$6,900': 'CA$9,400', '$7,200': 'CA$9,800', '$7,300': 'CA$9,900',
            '$7,400': 'CA$10,100', '$7,500': 'CA$10,200', '$7,600': 'CA$10,300',
            '$7,700': 'CA$10,500', '$7,800': 'CA$10,600', '$7,900': 'CA$10,700',
            '$8,000': 'CA$10,900', '$8,200': 'CA$11,200', '$8,300': 'CA$11,300',
            '$20,000': 'CA$27,200', '$21,000': 'CA$28,600',
            '$65': 'CA$88', '$25': 'CA$34', '+$7': '+CA$10',
        },
        'price_min': 'CA$6,900',
    },
    'nl': {
        'country':       'Netherlands',
        'country_abbr':  'Netherlands',
        'country_iso':   'NL',
        'domain':        'nl.myart-rion.com',
        'currency':      'EUR',
        'ls_key':        'rion_nl_lang',
        'cookie_key':    'rion_nl_cookies_accepted',
        'ga':            'G-PLACEHOLDER_NL',
        'tax_announce':  'No Import Duties · VAT Included',
        'price_note':    'Free NL Shipping · VAT Included',
        'price_note_ja': 'オランダへ無料配送・VAT込み',
        'series_ddp':    'Free NL Shipping · VAT Incl.',
        'series_ddp_ja': 'オランダへ無料配送・VAT込み',
        'consumer_law':  'Dutch consumer protection laws',
        'coverage':      'the Netherlands',
        'ja_country':    'オランダ',
        'ja_currency':   'EUR',
        'format_price':  "return '€' + n.toLocaleString('en-GB');",
        'page_title_suffix': 'Netherlands',
        'prod_prices': {
            5100: 4700, 5200: 4800, 5400: 5000,
            5900: 5400, 6000: 5500, 6100: 5600,
            6200: 5700, 6400: 5900, 6500: 6000,
            6600: 6100, 6700: 6200, 6800: 6300,
            6900: 6300, 7200: 6600, 7300: 6700,
            7400: 6800, 7500: 6900, 7600: 7000,
            7700: 7100, 7800: 7200, 7900: 7300,
            8000: 7400, 8200: 7500, 8300: 7600,
        },
        'html_prices': {
            '$5,100': '€4,700', '$5,200': '€4,800', '$5,400': '€5,000',
            '$5,900': '€5,400', '$6,000': '€5,500', '$6,100': '€5,600',
            '$6,200': '€5,700', '$6,400': '€5,900', '$6,500': '€6,000',
            '$6,600': '€6,100', '$6,700': '€6,200', '$6,800': '€6,300',
            '$6,900': '€6,300', '$7,200': '€6,600', '$7,300': '€6,700',
            '$7,400': '€6,800', '$7,500': '€6,900', '$7,600': '€7,000',
            '$7,700': '€7,100', '$7,800': '€7,200', '$7,900': '€7,300',
            '$8,000': '€7,400', '$8,200': '€7,500', '$8,300': '€7,600',
            '$20,000': '€18,400', '$21,000': '€19,300',
            '$65': '€60', '$25': '€23', '+$7': '+€6',
        },
        'price_min': '€4,700',
    },
    'ch': {
        'country':       'Switzerland',
        'country_abbr':  'Switzerland',
        'country_iso':   'CH',
        'domain':        'ch.myart-rion.com',
        'currency':      'CHF',
        'ls_key':        'rion_ch_lang',
        'cookie_key':    'rion_ch_cookies_accepted',
        'ga':            'G-PLACEHOLDER_CH',
        'tax_announce':  'No Import Duties · Swiss VAT May Apply',
        'price_note':    'Free Switzerland Shipping · No Duties',
        'price_note_ja': 'スイスへ無料配送・関税なし',
        'series_ddp':    'Free Switzerland Shipping · No Duties',
        'series_ddp_ja': 'スイスへ無料配送・関税なし',
        'consumer_law':  'Swiss consumer protection laws',
        'coverage':      'Switzerland',
        'ja_country':    'スイス',
        'ja_currency':   'CHF',
        'format_price':  "return 'CHF' + n.toLocaleString('en-GB');",
        'page_title_suffix': 'Switzerland',
        'prod_prices': {
            5100: 4600, 5200: 4700, 5400: 4900,
            5900: 5300, 6000: 5400, 6100: 5500,
            6200: 5600, 6400: 5800, 6500: 5900,
            6600: 5900, 6700: 6000, 6800: 6100,
            6900: 6200, 7200: 6500, 7300: 6600,
            7400: 6700, 7500: 6800, 7600: 6800,
            7700: 6900, 7800: 7000, 7900: 7100,
            8000: 7200, 8200: 7400, 8300: 7500,
        },
        'html_prices': {
            '$5,100': 'CHF4,600', '$5,200': 'CHF4,700', '$5,400': 'CHF4,900',
            '$5,900': 'CHF5,300', '$6,000': 'CHF5,400', '$6,100': 'CHF5,500',
            '$6,200': 'CHF5,600', '$6,400': 'CHF5,800', '$6,500': 'CHF5,900',
            '$6,600': 'CHF5,900', '$6,700': 'CHF6,000', '$6,800': 'CHF6,100',
            '$6,900': 'CHF6,200', '$7,200': 'CHF6,500', '$7,300': 'CHF6,600',
            '$7,400': 'CHF6,700', '$7,500': 'CHF6,800', '$7,600': 'CHF6,800',
            '$7,700': 'CHF6,900', '$7,800': 'CHF7,000', '$7,900': 'CHF7,100',
            '$8,000': 'CHF7,200', '$8,200': 'CHF7,400', '$8,300': 'CHF7,500',
            '$20,000': 'CHF18,000', '$21,000': 'CHF18,900',
            '$65': 'CHF59', '$25': 'CHF23', '+$7': '+CHF6',
        },
        'price_min': 'CHF4,600',
    },
}


def replace_prices_html(content, html_prices):
    for usd, local in sorted(html_prices.items(), key=lambda x: -len(x[0])):
        content = content.replace(usd, local)
    return content


def replace_prices_js(content, prod_prices):
    def repl(m):
        num = int(m.group(1))
        return f'price:{prod_prices[num]}' if num in prod_prices else m.group(0)
    return re.sub(r'price:(\d+)', repl, content)


def transform_file(path, cfg):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    country      = cfg['country']
    abbr         = cfg['country_abbr']
    iso          = cfg['country_iso']
    domain       = cfg['domain']
    currency     = cfg['currency']
    ls_key       = cfg['ls_key']
    cookie_key   = cfg['cookie_key']
    ga           = cfg['ga']
    tax_announce = cfg['tax_announce']
    price_note   = cfg['price_note']
    price_note_ja= cfg['price_note_ja']
    series_ddp   = cfg['series_ddp']
    series_ddp_ja= cfg['series_ddp_ja']
    consumer_law = cfg['consumer_law']
    coverage     = cfg['coverage']
    ja_country   = cfg['ja_country']
    ja_currency  = cfg['ja_currency']
    format_price = cfg['format_price']
    title_suffix = cfg['page_title_suffix']
    price_min    = cfg['price_min']

    # ── 1. Keys & IDs ─────────────────────────────────────────────────────────
    content = content.replace('rion_us_cookies_accepted', cookie_key)
    content = content.replace('rion_us_lang', ls_key)
    content = content.replace('G-Z72DT8WF7E', ga)
    content = content.replace('us.myart-rion.com', domain)

    # ── 2. Prices ─────────────────────────────────────────────────────────────
    content = replace_prices_html(content, cfg['html_prices'])
    content = replace_prices_js(content, cfg['prod_prices'])
    content = content.replace('price-usd', 'price-local')

    # ── 3. formatPrice JS function ────────────────────────────────────────────
    content = content.replace(
        "return '$' + n.toLocaleString('en-US');",
        format_price
    )

    # ── 4. Specific USD phrases (before blanket) ──────────────────────────────
    content = content.replace('all-inclusive USD pricing', f'all-inclusive {currency} pricing')
    content = content.replace('all-inclusive USD price', f'all-inclusive {currency} price')
    content = content.replace('pricing in USD', f'pricing in {currency}')
    content = content.replace('All prices in USD.', f'All prices in {currency}.')
    content = content.replace('All prices in USD,', f'All prices in {currency},')
    content = content.replace('All prices in USD', f'All prices in {currency}')
    content = content.replace('all prices in USD', f'all prices in {currency}')
    content = content.replace('prices in USD', f'prices in {currency}')
    content = content.replace('USD 5,100–20,000+', f'{currency} {price_min}–20,000+')
    content = content.replace('"currenciesAccepted":"USD"', f'"currenciesAccepted":"{currency}"')
    content = content.replace('"areaServed":["US","JP"]', f'"areaServed":["{iso}","JP"]')
    content = re.sub(r'"priceRange":"[^"]*"',
                     f'"priceRange":"{currency} {price_min}–20,000+"', content)
    # Remove trailing USD from already-converted prices
    content = re.sub(r'(£[\d,]+|€[\d,]+|CA\$[\d,]+|CHF[\d,]+)\s*USD', r'\1', content)
    # Price table column headers
    content = content.replace('Price (USD) · All-Inclusive', f'Price ({currency}) · All-Inclusive')
    content = content.replace('Price (USD) · Free shipping · No import duties',
                               f'Price ({currency}) · Free shipping · No import duties')

    # ── 5. Japanese USD references ────────────────────────────────────────────
    content = content.replace('最終USDお支払い', f'最終{ja_currency}お支払い')
    content = content.replace('価格はすべてUSD表示', f'価格はすべて{ja_currency}表示')
    content = content.replace('価格はすべてUSD', f'価格はすべて{ja_currency}')
    content = content.replace('USD全込み価格', f'{ja_currency}全込み価格')
    content = content.replace('USD条件', f'{ja_currency}条件')
    content = content.replace('USD表示', f'{ja_currency}表示')
    # Blanket USD (safe after all specifics; catches Japanese embedded USD)
    content = content.replace(' USD', f' {currency}')
    content = content.replace('USD ', f'{currency} ')

    # ── 6. Page title suffix "| US" / "| United States" ──────────────────────
    content = re.sub(r'\|\s*United States', f'| {title_suffix}', content)
    content = re.sub(r'\|\s*US\b', f'| {title_suffix}', content)

    # ── 7. JSON-LD areaServed (catch-all after specific replace above) ────────
    content = content.replace('"US"', f'"{iso}"')

    # ── 8. Japanese country name replacements (specific before catch-all) ─────
    content = content.replace('アメリカ中のご家族に信頼されています', f'{ja_country}中のご家族に信頼されています')
    content = content.replace('アメリカ中からの実際のお声', f'{ja_country}中からの実際のお声')
    content = content.replace('アメリカのご自宅への無料お届けまで', f'{ja_country}のご自宅への無料お届けまで')
    content = content.replace('アメリカのご住所へ郵送', f'{ja_country}のご住所へ郵送')
    content = content.replace('アメリカのご住所', f'{ja_country}のご住所')
    content = content.replace('アメリカ全土への無料配送', f'{ja_country}への無料配送')
    content = content.replace('アメリカ全土の', f'{ja_country}全土の')
    content = content.replace('アメリカ全土', f'{ja_country}全土')
    content = content.replace('アメリカへの保険付き無料配送込み', f'{ja_country}への保険付き無料配送込み')
    content = content.replace('アメリカへの保険付き無料配送', f'{ja_country}への保険付き無料配送')
    content = content.replace('アメリカへ保険付き無料配送', f'{ja_country}へ保険付き無料配送')
    content = content.replace('アメリカへ無料・保険付き配送', f'{ja_country}へ無料・保険付き配送')
    content = content.replace('アメリカへ無料配送', f'{ja_country}へ無料配送')
    content = content.replace('アメリカへ、', f'{ja_country}へ、')
    content = content.replace('アメリカへ直接', f'{ja_country}へ直接')
    content = content.replace('アメリカへお届け', f'{ja_country}へお届け')
    content = content.replace('アメリカへ', f'{ja_country}へ')
    content = content.replace('アメリカ', ja_country)

    # ── 9. Japanese "米国" (US abbreviation) ──────────────────────────────────
    content = content.replace('米国消費者向け情報', f'{ja_country}消費者向け情報')
    content = content.replace('米国の連邦・州消費者保護法を遵守しています',
                               f'{ja_country}の消費者保護法を遵守しています')
    content = content.replace('すべての米国輸入関税・税金はRionが負担します',
                               f'すべての{ja_country}輸入関税・税金はRionが負担します')
    content = content.replace('米国無料配送', f'{ja_country}無料配送')
    content = content.replace('米国', ja_country)

    # ── 10. Japanese DDP cleanup ─────────────────────────────────────────────
    content = content.replace('お届け時の追加料金なし（DDP条件）', 'お届け時の追加料金なし')
    content = content.replace('・DDP条件', '')

    # ── 11. English country name replacements ─────────────────────────────────
    content = content.replace('United States of America', country)
    content = content.replace('United States', country)
    content = content.replace('the USA', f'the {abbr}')
    content = content.replace('the US', f'the {abbr}')
    content = content.replace('Free Shipping to the USA', f'Free Shipping to the {abbr}')
    content = content.replace('Free shipping to the USA', f'Free shipping to the {abbr}')
    content = content.replace('shipping to the USA', f'shipping to the {abbr}')
    content = content.replace('all 50 US states, Washington D.C., and US territories', coverage)
    content = content.replace('all 50 US states, Washington D.C., and UK territories', coverage)
    content = content.replace('Free US Shipping', f'Free {abbr} Shipping')
    content = content.replace('Free US shipping', f'Free {abbr} shipping')
    content = content.replace('US import duties', f'{abbr} import duties')
    content = content.replace('US Import Duties', f'{abbr} Import Duties')
    content = content.replace('US sizes', 'standard sizes')
    content = content.replace('US address', f'{abbr} address')
    content = content.replace('US ring size', 'standard ring size')
    content = content.replace('US ring gauge', 'ring gauge')
    content = content.replace('US 1 – 12 (half sizes available) · Ring gauge included in kit',
                               'Sizes 1–12 (half sizes available) · Ring gauge included in kit')
    content = content.replace('US 1 – 12 · Ring gauge included in kit',
                               'Sizes 1–12 · Ring gauge included in kit')
    content = content.replace('US 1 – 12, half sizes available · Ring gauge included in kit',
                               'Sizes 1–12, half sizes available · Ring gauge included in kit')
    content = content.replace('US 6½', '6½')
    content = content.replace('US territories', f'{abbr} territories')
    content = content.replace('Free to all US states', f'Free to the {abbr}')

    # Fix "to all of the <country>" after country name replace
    content = content.replace(f'to all of the {country}', f'to {country}')

    # ── 12. Tax wording ───────────────────────────────────────────────────────
    content = content.replace('No Import Duties · Sales Tax May Apply', tax_announce)
    content = content.replace('Sales Tax May Apply', '')

    # ── 13. Legal page specifics ──────────────────────────────────────────────
    content = content.replace('US Consumer Information', f'{country} Consumer Information')
    content = content.replace(
        'US consumers retain applicable federal and state consumer protection rights',
        f'Customers retain applicable {consumer_law}'
    )
    content = content.replace(
        'US sales comply with applicable federal and state consumer protection laws',
        f'Sales comply with applicable {consumer_law}'
    )
    content = content.replace(
        'applicable US consumer law requires otherwise',
        f'applicable {consumer_law} requires otherwise'
    )
    content = content.replace(
        'Prices shown are in GBP and do not include applicable US state sales tax. '
        'Where required by law, sales tax will be calculated based on your delivery address '
        'and added to your Stripe invoice before payment is due.',
        f'Prices shown are in {currency} and include all applicable taxes where required.'
    )
    # Handle the Sales Tax column header in legal.html table
    content = content.replace('<th data-i18n="th_tax">Sales Tax</th>',
                               f'<th data-i18n="th_tax">Tax</th>')
    content = content.replace("th_tax: 'Sales Tax'", "th_tax: 'Tax'")
    # Bank transfer USD or JPY
    content = content.replace('Bank transfer (USD or JPY accepted)',
                               f'Bank transfer ({currency} or JPY accepted)')
    # US → Japan data transfer section
    content = content.replace('7. International Data Transfer (US → Japan)',
                               f'7. International Data Transfer ({abbr} → Japan)')
    content = content.replace('7. International Data Transfer (US &rarr; Japan)',
                               f'7. International Data Transfer ({abbr} &rarr; Japan)')
    content = content.replace('priv7_h: \'7. International Data Transfer (US → Japan)\'',
                               f"priv7_h: '7. International Data Transfer ({abbr} → Japan)'")
    # "Name, US shipping address" in legal
    content = content.replace('Name, US shipping address', f'Name, {abbr} shipping address')
    # s2_intro US consumers reference
    content = content.replace(
        'US consumers retain applicable federal and state consumer protection rights.',
        f'Customers retain applicable {consumer_law}.'
    )
    content = content.replace('No extra charges on delivery (DDP terms)', 'No extra charges on delivery')

    # ── 14. product.html price note ──────────────────────────────────────────
    content = content.replace('Free US Shipping &middot; No Import Duties · Sales Tax May Apply', price_note)
    content = content.replace('Free US Shipping · No Import Duties · Sales Tax May Apply', price_note)
    content = content.replace('Free UK Shipping &middot; No Import Duties · Sales Tax May Apply', price_note)

    # ── 15. Series page DDP line ─────────────────────────────────────────────
    content = content.replace("price_ddp:'Free US Shipping · No Duties'", f"price_ddp:'{series_ddp}'")
    content = content.replace("price_ddp:'アメリカへ無料配送・関税なし'", f"price_ddp:'{series_ddp_ja}'")

    # ── 16. Collection page price-table label ────────────────────────────────
    content = re.sub(
        r'Series ([A-Z]) — Price by Material \(USD · Free US Shipping · No Import Duties · Sales Tax May Apply\)',
        lambda m: f'Series {m.group(1)} — Price by Material ({currency} · Free {abbr} Shipping · No Import Duties)',
        content
    )

    # ── 17. Collection page note bar ─────────────────────────────────────────
    content = content.replace(
        '✦ All prices in USD · Free insured shipping · No US import duties · DDP terms',
        f'✦ All prices in {currency} · Free insured shipping · No import duties'
    )

    # ── 18. Collection sticky bar ────────────────────────────────────────────
    content = re.sub(
        r'From \$5,100[^<·]*· Free [A-Za-z]+ shipping · No import duties',
        f'From {price_min} · Free {abbr} shipping · No import duties',
        content
    )

    # ── 19. Announce bar ─────────────────────────────────────────────────────
    content = re.sub(
        r'Free Shipping to the ' + re.escape(abbr) + r' &nbsp;·&nbsp; <span>[^<]*</span>',
        f'Free Shipping to the {abbr} &nbsp;·&nbsp; <span>{tax_announce}</span>',
        content
    )

    # ── 20. Trust strip (i18n JS) ────────────────────────────────────────────
    content = re.sub(r"trust_duties:'[^']*'", f"trust_duties:'{tax_announce}'", content)

    # ── 21. faq.html US-SPECIFIC sections ────────────────────────────────────
    # The tab label for US-specific FAQs
    content = content.replace("tab_usa: 'US-Specific'", f"tab_usa: '{abbr}-Specific'")
    content = content.replace("tab_usa: 'US在住のお客様'", f"tab_usa: '{ja_country}在住のお客様'")

    # ── 22. Shipping page coverage ───────────────────────────────────────────
    content = re.sub(
        r'Free DDP shipping to all of the United Kingdom',
        f'Free DDP shipping to {coverage}', content
    )
    content = re.sub(
        r'Free DDP shipping to [^<\n]+',
        f'Free DDP shipping to {coverage}', content
    )

    # ── 23. order.html specific ──────────────────────────────────────────────
    content = content.replace(
        'A sizing gauge is included in your hair kit — so you can confirm your exact US ring size before production begins. Half sizes available (sizes 1–12).',
        f'A ring sizing gauge is included in your hair kit — confirm your exact size before production begins. Half sizes available (sizes 1–12).'
    )

    # ── 24. Remove orphaned DDP references ───────────────────────────────────
    content = content.replace(' (DDP terms)', '')
    content = content.replace('(DDP terms)', '')
    content = content.replace(' · DDP terms', '')
    content = content.replace(' DDP terms', '')

    # ── 25. Birthstone JS textContent setter ─────────────────────────────────
    stone_price = cfg['html_prices'].get('$25', '$25')
    content = content.replace("'+ $25 per stone'", f"'+ {stone_price} per stone'")

    # ── 26. Sizing spec text ─────────────────────────────────────────────────
    content = content.replace(
        "US ring gauge (sizes 1–12) sent in your collection kit. Or tell us your US size if you already know.",
        "Ring gauge (sizes 1–12) sent in your collection kit. Or tell us your size if you already know."
    )
    content = content.replace(
        "A US ring gauge (sizes 1–12, including half sizes) is included in your hair collection kit. Simply try each ring on and tell us which fits. If you already know your US ring size — for example \"US 6½\" — just let us know and you can skip the gauge entirely.",
        "A ring size gauge (sizes 1–12, including half sizes) is included in your hair collection kit. Simply try each ring on and tell us which fits. If you already know your ring size, just let us know and you can skip the gauge entirely."
    )
    content = content.replace(
        "A ring size gauge is included in your hair collection kit — shipped to your UK address. Simply try the gauge and confirm your US size when you return your hair. We work in standard sizes 1 through 12, with half sizes available. If you already know your size, just let us know at the time of order.",
        f"A ring size gauge is included in your hair collection kit — shipped to your {abbr} address. Simply try the gauge and confirm your size when you return your hair. We work in standard sizes 1 through 12, with half sizes available. If you already know your size, just let us know at the time of order."
    )
    # faq.html inline answer about ring size
    content = content.replace(
        'ヘアキットに米国サイズのリングゲージ（サイズ1〜12・ハーフサイズ含む）が同封されています。試着して合うものをお知らせください。すでに米国リングサイズをご存知の場合（例：「US 6½」）は、お知らせいただければゲージは不要です。',
        'ヘアキットにリングゲージ（サイズ1〜12・ハーフサイズ含む）が同封されています。試着して合うものをお知らせください。すでにリングサイズをご存知の場合は、お知らせいただければゲージは不要です。'
    )

    # ── 27. faq.html US-territory shipping note ──────────────────────────────
    content = content.replace(
        'Yes. We ship free via DHL Express to all 50 US states, Washington D.C., and UK territories including Puerto Rico, Guam, the UK Virgin Islands, and American Samoa. All shipments are DDP — no import duties or customs fees regardless of your location within the UK.',
        f'Yes. We ship free via DHL Express to {coverage}. All shipments are DDP — no import duties or customs fees.'
    )

    # ── 28. faq.html us-badge ────────────────────────────────────────────────
    content = content.replace(
        '<div class="us-badge">US Customers</div>',
        f'<div class="us-badge">{abbr} Customers</div>'
    )

    # ── 29. series-f "All prices in US Dollars" ──────────────────────────────
    content = content.replace(
        'All prices in <em>US Dollars</em>',
        f'All prices in <em>{currency}</em>'
    )

    # ── 30. product.html specSizingVal HTML (uses &middot; not ·) ────────────
    content = content.replace(
        'US 1 – 12 (half sizes available) &middot; Ring gauge included in kit',
        'Sizes 1–12 (half sizes available) · Ring gauge included in kit'
    )

    # ── 31. shipping.html "US Territories" section ───────────────────────────
    content = content.replace(
        '<h3 data-i18n="cov3_title">US Territories</h3>',
        f'<h3 data-i18n="cov3_title">{abbr} Shipping Coverage</h3>'
    )
    content = content.replace(
        "cov3_title:'US Territories',cov3_body:'Puerto Rico · Guam · USVI · American Samoa',cov3_meta:'DDP · No duties · Free DHL Express'",
        f"cov3_title:'{abbr} Shipping Coverage',cov3_body:'Free DHL Express · Fully Insured',cov3_meta:'DDP · No duties · Free DHL Express'"
    )

    # ── 32. legal.html pricing row "priced individually in USD" ─────────────
    content = content.replace(
        'Each piece is priced individually in <strong>USD</strong>. Prices displayed on the Collection page are exclusive of any applicable state sales tax.',
        f'Each piece is priced individually in <strong>{currency}</strong>. Prices displayed on the Collection page are all-inclusive.'
    )

    # ── 33. order.html Japanese "最終的なUSD価格" ────────────────────────────
    content = content.replace('最終的なUSD価格', f'最終的な{ja_currency}価格')

    # ── 34. Clean up double spaces ────────────────────────────────────────────
    content = re.sub(r'  +', ' ', content)

    return content


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in CONFIGS:
        print(f'Usage: python3 transform_country.py [{"|".join(CONFIGS)}]')
        sys.exit(1)

    code = sys.argv[1]
    cfg = CONFIGS[code]
    print(f'Transforming to {cfg["country"]} ({code.upper()})...')

    html_files = glob.glob('*.html')
    for path in html_files:
        print(f'  {path}')
        new_content = transform_file(path, cfg)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    print(f'Done! {len(html_files)} files transformed.')


if __name__ == '__main__':
    main()
