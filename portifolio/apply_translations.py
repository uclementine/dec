from pathlib import Path

files_to_update = {
    "about.html": [
        ("</ul>\n            </div>", """</ul>
                <div class="theme-language-controls ms-3">
                    <button id="themeToggle" class="btn btn-sm theme-toggle-btn" type="button" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
                    <button id="languageToggle" class="btn btn-sm language-toggle-btn" type="button" onclick="cycleLanguage()" aria-label="Switch language">EN</button>
                </div>
            </div>"""),
        ('href="css/theme.css"', 'DO_NOT_REPLACE'),
        ('href="new.css"', 'href="css/theme.css">\n    <link rel="stylesheet" href="new.css"'),
        ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n    <script src="js/translations.js"></script>\n    <script src="js/theme-language.js"></script>'),
    ],
    "skills.html": [
        ("</ul>\n            </div>", """</ul>
                <div class="theme-language-controls ms-3">
                    <button id="themeToggle" class="btn btn-sm theme-toggle-btn" type="button" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
                    <button id="languageToggle" class="btn btn-sm language-toggle-btn" type="button" onclick="cycleLanguage()" aria-label="Switch language">EN</button>
                </div>
            </div>"""),
        ('href="css/theme.css"', 'DO_NOT_REPLACE'),
        ('href="new.css"', 'href="css/theme.css">\n    <link rel="stylesheet" href="new.css"'),
        ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n    <script src="js/translations.js"></script>\n    <script src="js/theme-language.js"></script>'),
    ],
    "services.html": [
        ("</ul>\n            </div>", """</ul>
                <div class="theme-language-controls ms-3">
                    <button id="themeToggle" class="btn btn-sm theme-toggle-btn" type="button" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
                    <button id="languageToggle" class="btn btn-sm language-toggle-btn" type="button" onclick="cycleLanguage()" aria-label="Switch language">EN</button>
                </div>
            </div>"""),
        ('href="css/theme.css"', 'DO_NOT_REPLACE'),
        ('href="new.css"', 'href="css/theme.css">\n    <link rel="stylesheet" href="new.css"'),
        ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n    <script src="js/translations.js"></script>\n    <script src="js/theme-language.js"></script>'),
    ],
    "project.html": [
        ("</ul>\n            </div>", """</ul>
                <div class="theme-language-controls ms-3">
                    <button id="themeToggle" class="btn btn-sm theme-toggle-btn" type="button" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
                    <button id="languageToggle" class="btn btn-sm language-toggle-btn" type="button" onclick="cycleLanguage()" aria-label="Switch language">EN</button>
                </div>
            </div>"""),
        ('href="css/theme.css"', 'DO_NOT_REPLACE'),
        ('href="new.css"', 'href="css/theme.css">\n    <link rel="stylesheet" href="new.css"'),
        ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n    <script src="js/translations.js"></script>\n    <script src="js/theme-language.js"></script>'),
    ],
    "portifolio.html": [
        ("</ul>\n            </div>", """</ul>
                <div class="theme-language-controls ms-3">
                    <button id="themeToggle" class="btn btn-sm theme-toggle-btn" type="button" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
                    <button id="languageToggle" class="btn btn-sm language-toggle-btn" type="button" onclick="cycleLanguage()" aria-label="Switch language">EN</button>
                </div>
            </div>"""),
        ('href="css/theme.css"', 'DO_NOT_REPLACE'),
        ('href="new.css"', 'href="css/theme.css">\n    <link rel="stylesheet" href="new.css"'),
        ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n    <script src="js/translations.js"></script>\n    <script src="js/theme-language.js"></script>'),
    ],
    "contact.html": [
        ("</ul>\n            </div>", """</ul>
                <div class="theme-language-controls ms-3">
                    <button id="themeToggle" class="btn btn-sm theme-toggle-btn" type="button" onclick="toggleTheme()" aria-label="Toggle theme">☀️</button>
                    <button id="languageToggle" class="btn btn-sm language-toggle-btn" type="button" onclick="cycleLanguage()" aria-label="Switch language">EN</button>
                </div>
            </div>"""),
        ('href="css/theme.css"', 'DO_NOT_REPLACE'),
        ('href="new.css"', 'href="css/theme.css">\n    <link rel="stylesheet" href="new.css"'),
        ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n    <script src="js/translations.js"></script>\n    <script src="js/theme-language.js"></script>'),
    ],
}

nav_map = {
    'href="index.html">Home</a>':'href="index.html" data-i18n="home">Home</a>',
    'href="about.html">About</a>':'href="about.html" data-i18n="about">About</a>',
    'href="skills.html">Skills</a>':'href="skills.html" data-i18n="skills">Skills</a>',
    'href="services.html">Services</a>':'href="services.html" data-i18n="services">Services</a>',
    'href="project.html">Project</a>':'href="project.html" data-i18n="project">Project</a>',
    'href="portifolio.html">Portfolio</a>':'href="portifolio.html" data-i18n="portfolio">Portfolio</a>',
    'href="contact.html">Contact Us</a>':'href="contact.html" data-i18n="contact">Contact Us</a>',
}

for fname, replacements in files_to_update.items():
    path = Path(fname)
    if not path.exists():
        print(f"Skipping {fname} - does not exist")
        continue
    
    text = path.read_text(encoding='utf-8')
    original = text
    
    # Apply replacements
    for old, new in replacements:
        if old != 'DO_NOT_REPLACE' and old in text:
            text = text.replace(old, new)
    
    # Apply nav translations
    for old, new in nav_map.items():
        if old in text:
            text = text.replace(old, new)
    
    # Write if changed
    if text != original:
        path.write_text(text, encoding='utf-8')
        print(f"Updated: {fname}")
    else:
        print(f"No changes: {fname}")

print("Done!")
print("Files processed successfully")
