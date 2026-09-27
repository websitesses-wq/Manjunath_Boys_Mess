// Rajeshwari Boys Mess - Client Script Entry Bridge
if (typeof window === 'undefined' || typeof document === 'undefined') {
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = {};
  }
} else {
  // Safe browser delegate to js/app.js if directly referenced
  if (!window.openJoinModal) {
    const script = document.createElement('script');
    script.src = 'js/app.js';
    document.head.appendChild(script);
  }
}
