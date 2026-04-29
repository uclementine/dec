// Visitor Counter System - Netlify Compatible
(function() {
    'use strict';
    
    class VisitorCounter {
        constructor() {
            this.storageKey = 'portfolio_visitor_count';
            this.lastVisitKey = 'portfolio_last_visit';
            this.visitorLogsKey = 'portfolio_visitor_logs';
            
            // Check localStorage availability
            if (!this.isLocalStorageAvailable()) {
                console.warn('localStorage not available');
                return;
            }
            
            // Wait for DOM to be ready before initializing
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => this.init());
            } else {
                this.init();
            }
        }

        isLocalStorageAvailable() {
            try {
                const test = '__test__';
                localStorage.setItem(test, test);
                localStorage.removeItem(test);
                return true;
            } catch(e) {
                return false;
            }
        }

        init() {
            this.recordVisit();
            this.displayCounter();
        }

        recordVisit() {
            try {
                const now = new Date();
                const today = now.toDateString();
                const lastVisit = localStorage.getItem(this.lastVisitKey);
                
                let count = parseInt(localStorage.getItem(this.storageKey)) || 0;
                
                if (lastVisit !== today) {
                    count++;
                    localStorage.setItem(this.storageKey, count.toString());
                    localStorage.setItem(this.lastVisitKey, today);
                }

                this.logVisitor({
                    timestamp: now.toISOString(),
                    date: today,
                    time: now.toLocaleTimeString(),
                    userAgent: navigator.userAgent,
                    language: navigator.language,
                    screen: `${window.innerWidth}x${window.innerHeight}`
                });
            } catch(e) {
                console.error('Error recording visit:', e);
            }
        }

        logVisitor(data) {
            try {
                let logs = JSON.parse(localStorage.getItem(this.visitorLogsKey)) || [];
                logs.push(data);
                if (logs.length > 100) logs.shift();
                localStorage.setItem(this.visitorLogsKey, JSON.stringify(logs));
            } catch(e) {
                console.error('Error logging visitor:', e);
            }
        }

        getCount() {
            try {
                return parseInt(localStorage.getItem(this.storageKey)) || 0;
            } catch(e) {
                return 0;
            }
        }

        getLogs() {
            try {
                return JSON.parse(localStorage.getItem(this.visitorLogsKey)) || [];
            } catch(e) {
                return [];
            }
        }

        displayCounter() {
            try {
                const count = this.getCount();
                const counterElements = document.querySelectorAll('[data-visitor-counter]');
                counterElements.forEach(el => {
                    el.textContent = count.toLocaleString();
                    el.setAttribute('title', `Total profile views: ${count}`);
                });
            } catch(e) {
                console.error('Error displaying counter:', e);
            }
        }

        clearData() {
            if (confirm('Clear all visitor data?')) {
                try {
                    localStorage.removeItem(this.storageKey);
                    localStorage.removeItem(this.lastVisitKey);
                    localStorage.removeItem(this.visitorLogsKey);
                    location.reload();
                } catch(e) {
                    console.error('Error clearing data:', e);
                }
            }
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            window.visitorCounter = new VisitorCounter();
        });
    } else {
        window.visitorCounter = new VisitorCounter();
    }
})();
