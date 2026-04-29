// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('selectedTheme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeToggle(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('selectedTheme', newTheme);
  updateThemeToggle(newTheme);
}

function updateThemeToggle(theme) {
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
    themeToggle.title = theme === 'dark' ? 'Light Mode' : 'Dark Mode';
  }
}

// Language Management
function initLanguage() {
  const savedLang = localStorage.getItem('selectedLanguage') || 'en';
  setLanguage(savedLang);
}

function setLanguage(lang) {
  localStorage.setItem('selectedLanguage', lang);
  document.documentElement.lang = lang;
  updatePageTranslations();
  
  // Update language toggle button
  const langToggle = document.getElementById('languageToggle');
  if (langToggle) {
    const langMap = { en: 'EN', fr: 'FR', rw: 'RW' };
    langToggle.textContent = langMap[lang] || 'EN';
  }
}

function cycleLanguage() {
  const currentLang = localStorage.getItem('selectedLanguage') || 'en';
  const languages = ['en', 'fr', 'rw'];
  const currentIndex = languages.indexOf(currentLang);
  const nextIndex = (currentIndex + 1) % languages.length;
  setLanguage(languages[nextIndex]);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  initTheme();
  initLanguage();
});
