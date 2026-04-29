import re
from pathlib import Path

files = ["index.html", "about.html", "skills.html", "services.html", "project.html", "portifolio.html", "contact.html"]

for fname in files:
    path = Path(fname)
    if not path.exists():
        continue
    
    text = path.read_text(encoding='utf-8')
    original = text
    
    # Remove duplicate data-i18n attributes (keep only the innermost one)
    # Pattern: <span data-i18n="x"><span data-i18n="y">...
    while '<span data-i18n=' in text and text.count('<span data-i18n=') > text.count('</span>') // 2:
        # Find and remove outer duplicate data-i18n spans
        text = re.sub(r'<span data-i18n="[^"]+">(<span data-i18n="[^"]+">([^<]*)</span>)</span>', r'\1', text)
        # Prevent infinite loops
        if text == original:
            break
        original = text
    
    path.write_text(text, encoding='utf-8')
    print(f"Deduplicated: {fname}")

print("Done!")
