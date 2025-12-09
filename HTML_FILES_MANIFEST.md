# GitHub Pages Site Structure

## Files in Repository

All HTML files are located in the `docs/` folder:

### Main Pages (HTML)
- **index.html** - Homepage with navigation and card layout
- **python-theory.html** - Python learning modules guide
- **algorithms.html** - Algorithms and data structures guide
- **numpy-tutorials.html** - NumPy tutorials and learning path
- **getting-started.html** - Clone, setup, and installation guide
- **404.html** - Custom error page

### Configuration & Assets
- **_config.yml** - Jekyll configuration file
- **robots.txt** - SEO configuration for search engines
- **assets/css/style.css** - Shared CSS styling

### Documentation (Markdown - Optional)
- **index.md** - Home page markdown version
- **python-theory.md** - Python theory markdown version
- **algorithms.md** - Algorithms markdown version
- **numpy-tutorials.md** - NumPy markdown version
- **getting-started.md** - Getting started markdown version
- **404.md** - 404 page markdown version

## How to View

### Option 1: GitHub Pages (Recommended)
Visit: **https://sonuparsad1.github.io/algorithms/**

The site is deployed from the `/docs` folder.

### Option 2: View in Repository
Visit the docs folder directly on GitHub:
https://github.com/sonuparsad1/algorithms/tree/main/docs

### Option 3: Local Testing
1. Clone the repository
2. Open `docs/index.html` in your browser directly
3. Navigate using links on the page

## File Details

### Size Information
```
index.html                ~7.5 KB
python-theory.html       ~7.6 KB
algorithms.html          ~6.8 KB
numpy-tutorials.html     ~7.2 KB
getting-started.html    ~10.1 KB
404.html                 ~5.7 KB
_config.yml              ~898 B
style.css               ~4.0 KB
robots.txt              ~220 B
```

## All Files Committed ✅

Every HTML file has been:
1. Created locally
2. Staged with `git add`
3. Committed with descriptive message
4. Pushed to GitHub remote

Last commit: `57d3d83` - feat: Replace Jekyll markdown with standalone HTML pages for GitHub Pages

## Verification

To verify files are in the repository, run:
```bash
git ls-tree -r HEAD docs/
```

Output shows all files are tracked in git.
