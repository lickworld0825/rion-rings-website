# Rion Rings — Memorial Jewellery Site

Static site deployed to `memorial.myart-rion.com` (see `CNAME`).

## Directory structure (regional versions)

This repo contains **two regional versions** of the site, kept as separate sets of files
so they can be told apart at a glance when deploying or editing:

- **Root directory** (`index.html`, `about.html`, `series-*.html`, etc.)
  → **Dubai / UAE / Kuwait version** (current production site, served at the domain root).
  Languages: English / Arabic / Japanese. Shipping & pricing copy targets the Gulf region
  (DDP shipping to Dubai, UAE & Kuwait).

- **`sg/`**
  → **Singapore version**, served at `memorial.myart-rion.com/sg/`.
  Languages: English / Malay / Japanese. Localized for Singapore (GST 9%, DDP shipping,
  SGD pricing).
  Translation source data lives in `sg/translations/`.

Shared assets (`images/`, `CNAME`, `robots.txt`, `sitemap.xml`, `admin.html`) live at the
repo root and are used by the Dubai/UAE/Kuwait (root) version; the `sg/` pages reference
the same `images/` folder via relative paths.

## Notes for deployment

- Do **not** move the root-level HTML files into a subfolder — they are the live
  production URLs (`memorial.myart-rion.com/index.html`, etc.) and changing their
  location would break existing links, bookmarks, and search-engine indexing.
- When editing copy/pricing/translations, double-check which version (root = Dubai/UAE/
  Kuwait, `sg/` = Singapore) you're in before making changes — the two share the same
  page names (`index.html`, `product.html`, `series-a.html`, ...) but have different
  localized content.
