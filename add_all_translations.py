from pathlib import Path

pages = {
    "index.html": [
        ("// About Me", '// <span data-i18n="aboutMe">About Me</span>'),
        ("Who I Am", '<span data-i18n="whoIAm">Who I Am</span>'),
        ("Learn More", '<span data-i18n="aboutMe">Learn More</span>'),
    ],
    "about.html": [
        ("// Who am I?", '// <span data-i18n="whoIAm">Who am I?</span>'),
        ("My Journey", 'My <span data-i18n="professionalBackground">Journey</span>'),
        ("My Philosophy", 'My <span data-i18n="whatIDo">Philosophy</span>'),
        ("View My Work", '<span data-i18n="viewMyWork">View My Work</span>'),
        ("Let's Talk", '<span data-i18n="getInTouchBtn">Let\'s Talk</span>'),
    ],
    "skills.html": [
        ("Software Development Skills", '<span data-i18n="mySkills">Software Development Skills</span>'),
        ("Below is a categorized overview of my technical skills", '<span data-i18n="skillsOverview">Below is a categorized overview of my technical skills</span>'),
        ("Frontend Development", '<span data-i18n="frontendTechnologies">Frontend Development</span>'),
        ("Backend Development", '<span data-i18n="backendTechnologies">Backend Development</span>'),
        ("HTML & CSS", '<span data-i18n="frontendTechnologies">HTML & CSS</span>'),
        ("JavaScript", '<span data-i18n="frontendTechnologies">JavaScript</span>'),
        ("Bootstrap", '<span data-i18n="frontendTechnologies">Bootstrap</span>'),
        ("Python", '<span data-i18n="backendTechnologies">Python</span>'),
        ("Java", '<span data-i18n="backendTechnologies">Java</span>'),
        ("Node.js", '<span data-i18n="backendTechnologies">Node.js</span>'),
    ],
    "services.html": [
        ("Services I Offer", '<span data-i18n="servicesIOffer">Services I Offer</span>'),
        ("Web Design", '<span data-i18n="webDesign">Web Design</span>'),
        ("Web Development", '<span data-i18n="webDevelopment">Web Development</span>'),
        ("Responsive Design", '<span data-i18n="responsiveDesign">Responsive Design</span>'),
        ("Database Design", '<span data-i18n="databaseDesign">Database Design</span>'),
        ("SEO Optimization", '<span data-i18n="seoOptimization">SEO Optimization</span>'),
        ("UI/UX Design", '<span data-i18n="uiuxDesign">UI/UX Design</span>'),
        ("Website Maintenance", '<span data-i18n="servicesIOffer">Website Maintenance</span>'),
    ],
    "project.html": [
        ("Featured Projects", '<span data-i18n="project">Featured Projects</span>'),
        ("View Details", '<span data-i18n="viewMyWork">View Details</span>'),
    ],
    "portifolio.html": [
        ("My Portfolio", '<span data-i18n="portfolio">My Portfolio</span>'),
        ("View Project", '<span data-i18n="viewMyWork">View Project</span>'),
    ],
    "contact.html": [
        ("Send me a message", '<span data-i18n="contactUs">Send me a message</span>'),
        ("Contact Us", '<span data-i18n="contactUs">Contact Us</span>'),
        ("Call me for quick discussions", '<span data-i18n="callMeForQuick">Call me for quick discussions</span>'),
        ("Send me an email anytime", '<span data-i18n="sendMeEmail">Send me an email anytime</span>'),
        ("Based in East Africa", '<span data-i18n="basedInEastAfrica">Based in East Africa</span>'),
        ("Send Message", '<span data-i18n="sendMessage">Send Message</span>'),
        ("Enter your name", '<span data-i18n="enterYourName">Enter your name</span>'),
        ("your@email.com", '<span data-i18n="yourEmail">your@email.com</span>'),
        ("+250 ...", '<span data-i18n="enterPhone">+250 ...</span>'),
        ("What is this about?", '<span data-i18n="whatIsThis">What is this about?</span>'),
        ("Tell me about your project...", '<span data-i18n="tellMeAbout">Tell me about your project...</span>'),
    ],
}

for fname, replacements in pages.items():
    path = Path(fname)
    if not path.exists():
        print(f"Skipping {fname} - does not exist")
        continue
    
    text = path.read_text(encoding='utf-8')
    original_text = text
    
    for old, new in replacements:
        # Only replace if not already translated
        if old in text and f'data-i18n=' not in old:
            text = text.replace(old, new)
    
    if text != original_text:
        path.write_text(text, encoding='utf-8')
        print(f"Updated translations in: {fname}")
    else:
        print(f"Already translated: {fname}")

print("\nTranslation update complete!")
