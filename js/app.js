/**
 * Manjunath Boys Mess - Interactive Client Application
 * Features:
 * 1. Live Meal Status Tracker (real-time Open/Closed indicator)
 * 2. Pricing Engine (Default: College Student Offer ₹3,500 / ₹3,000 vs Regular ₹4,500 / ₹4,000)
 * 3. Student ID Verification Photo Preview
 * 4. Mobile Menu Navigation & Touch Optimizations
 * 5. Onboarding Modal & Direct WhatsApp Booking to +91 91130 74896
 * 6. Meal Pause / Leave Request via WhatsApp
 * 7. FAQ Accordion Toggle
 */

if (typeof window === 'undefined' || typeof document === 'undefined') {
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = {};
  }
} else {

// Target WhatsApp and Contact Phone Number
const MESS_PHONE = '+91 91130 74896';
const MESS_WHATSAPP_NUMBER = '919113074896';

// State: Student Offer active by default
let isStudentOffer = true;

const PRICING_DATA = {
  student: {
    fullBoard: '3,500',
    halfBoard: '3,000',
  },
  regular: {
    fullBoard: '4,500',
    halfBoard: '4,000',
  }
};

if (typeof window !== 'undefined' && typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', () => {
    initPricingState();
    initLiveMealStatus();
    initMouseFlashlightEffect();
    initDragAndDrop();
  });
}

/* ==========================================================================
   1. LIVE MEAL SERVING STATUS TRACKER
   ========================================================================== */

function initLiveMealStatus() {
  updateLiveMealStatus();
  // Update every minute
  setInterval(updateLiveMealStatus, 60000);
}

function updateLiveMealStatus() {
  const statusText = document.getElementById('liveStatusText');
  const pulseDot = document.getElementById('statusPulseDot');
  if (!statusText) return;

  const now = new Date();
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const timeInMinutes = hours * 60 + minutes;

  // 7:30 AM (450m) to 9:30 AM (570m) -> Breakfast
  const bStart = 7 * 60 + 30;
  const bEnd = 9 * 60 + 30;

  // 12:30 PM (750m) to 2:30 PM (870m) -> Lunch
  const lStart = 12 * 60 + 30;
  const lEnd = 14 * 60 + 30;

  // 7:45 PM (1185m) to 10:00 PM (1320m) -> Dinner
  const dStart = 19 * 60 + 45;
  const dEnd = 22 * 60;

  if (timeInMinutes >= bStart && timeInMinutes <= bEnd) {
    statusText.innerHTML = '🟢 <strong>Serving Now:</strong> Fresh Morning Breakfast with Hot Tea (Till 9:30 AM)';
    if (pulseDot) pulseDot.style.backgroundColor = '#16A34A';
  } else if (timeInMinutes >= lStart && timeInMinutes <= lEnd) {
    statusText.innerHTML = '🟢 <strong>Serving Now:</strong> Wholesome Lunch with Unlimited Rice & Sambar (Till 2:30 PM)';
    if (pulseDot) pulseDot.style.backgroundColor = '#16A34A';
  } else if (timeInMinutes >= dStart && timeInMinutes <= dEnd) {
    statusText.innerHTML = '🟢 <strong>Serving Now:</strong> Dinner with Guaranteed Hot Chapati Fix (Till 10:00 PM)';
    if (pulseDot) pulseDot.style.backgroundColor = '#16A34A';
  } else if (timeInMinutes < bStart) {
    statusText.innerHTML = '⏳ <strong>Next Up:</strong> Morning Breakfast & Tea starting at 7:30 AM';
    if (pulseDot) pulseDot.style.backgroundColor = '#FF6803';
  } else if (timeInMinutes < lStart) {
    statusText.innerHTML = '⏳ <strong>Next Up:</strong> Wholesome Afternoon Lunch starting at 12:30 PM';
    if (pulseDot) pulseDot.style.backgroundColor = '#FF6803';
  } else if (timeInMinutes < dStart) {
    statusText.innerHTML = '⏳ <strong>Next Up:</strong> Dinner with Night Chapati Fix starting at 7:45 PM';
    if (pulseDot) pulseDot.style.backgroundColor = '#FF6803';
  } else {
    statusText.innerHTML = '🌙 <strong>Kitchen Closed:</strong> Opens tomorrow at 7:30 AM for Breakfast & Tea';
    if (pulseDot) pulseDot.style.backgroundColor = '#64748B';
  }
}

/* ==========================================================================
   2. MOBILE NAVIGATION DRAWER
   ========================================================================== */

function toggleMobileMenu() {
  const drawer = document.getElementById('mobileNavDrawer');
  if (drawer) {
    drawer.classList.toggle('open');
  }
}

function closeMobileMenu() {
  const drawer = document.getElementById('mobileNavDrawer');
  if (drawer) {
    drawer.classList.remove('open');
  }
}

/* ==========================================================================
   3. PRICING ENGINE STATE MANAGEMENT
   ========================================================================== */

function initPricingState() {
  updatePricingUI();
}

function setPricingMode(isStudent) {
  isStudentOffer = isStudent;
  updatePricingUI();

  if (isStudentOffer) {
    highlightVerificationGateway();
  }
}

function togglePricing() {
  isStudentOffer = !isStudentOffer;
  updatePricingUI();

  if (isStudentOffer) {
    highlightVerificationGateway();
  }
}

function highlightVerificationGateway() {
  const verifElement = document.getElementById('verification');
  if (verifElement) {
    verifElement.style.boxShadow = '0 0 0 3px #FF6803';
    setTimeout(() => {
      verifElement.style.boxShadow = 'none';
    }, 1500);
  }
}

function updatePricingUI() {
  const toggleBtn = document.getElementById('pricingToggle');
  const labelStudent = document.getElementById('labelStudent');
  const labelRegular = document.getElementById('labelRegular');
  const priceFullBoard = document.getElementById('priceFullBoard');
  const priceHalfBoard = document.getElementById('priceHalfBoard');
  const discountBannerFull = document.getElementById('discountBannerFull');
  const discountBannerHalf = document.getElementById('discountBannerHalf');
  const idNoticeFull = document.getElementById('idNoticeFull');
  const idNoticeHalf = document.getElementById('idNoticeHalf');
  const modalCheckbox = document.getElementById('modalStudentCheckbox');

  if (isStudentOffer) {
    // Student Offer (DEFAULT on load)
    if (toggleBtn) {
      toggleBtn.classList.remove('regular-mode');
      toggleBtn.setAttribute('aria-checked', 'false');
    }
    if (labelStudent) labelStudent.classList.add('active');
    if (labelRegular) labelRegular.classList.remove('active');

    if (priceFullBoard) priceFullBoard.textContent = PRICING_DATA.student.fullBoard;
    if (priceHalfBoard) priceHalfBoard.textContent = PRICING_DATA.student.halfBoard;

    if (discountBannerFull) {
      discountBannerFull.style.display = 'flex';
      discountBannerFull.innerHTML = '<span class="discount-check">✓</span> Special Student Offer Applied (Regular: ₹4,500)';
    }
    if (discountBannerHalf) {
      discountBannerHalf.style.display = 'flex';
      discountBannerHalf.innerHTML = '<span class="discount-check">✓</span> Special Student Offer Applied (Regular: ₹4,000)';
    }

    if (idNoticeFull) idNoticeFull.style.display = 'inline-flex';
    if (idNoticeHalf) idNoticeHalf.style.display = 'inline-flex';

    if (modalCheckbox) modalCheckbox.checked = true;
  } else {
    // Regular / Non-Student Rates
    if (toggleBtn) {
      toggleBtn.classList.add('regular-mode');
      toggleBtn.setAttribute('aria-checked', 'true');
    }
    if (labelStudent) labelStudent.classList.remove('active');
    if (labelRegular) labelRegular.classList.add('active');

    if (priceFullBoard) priceFullBoard.textContent = PRICING_DATA.regular.fullBoard;
    if (priceHalfBoard) priceHalfBoard.textContent = PRICING_DATA.regular.halfBoard;

    if (discountBannerFull) discountBannerFull.style.display = 'none';
    if (discountBannerHalf) discountBannerHalf.style.display = 'none';

    if (idNoticeFull) idNoticeFull.style.display = 'none';
    if (idNoticeHalf) idNoticeHalf.style.display = 'none';

    if (modalCheckbox) modalCheckbox.checked = false;
  }

  updateModalPriceDisplay();
}

/* ==========================================================================
   4. STUDENT ID CARD VERIFICATION GATEWAY
   ========================================================================== */

function triggerFileInput() {
  const fileInput = document.getElementById('studentIdInput');
  if (fileInput) fileInput.click();
}

function handleIdFileSelect(event) {
  const file = event.target.files[0];
  if (file) {
    processUploadedFile(file);
  }
}

function processUploadedFile(file) {
  const dropzone = document.getElementById('dropzone');
  const statusCard = document.getElementById('uploadStatusCard');
  const statusFileName = document.getElementById('statusFileName');
  const idCardPreview = document.getElementById('idCardPreview');

  if (statusFileName) statusFileName.textContent = file.name;

  if (file.type.startsWith('image/')) {
    const reader = new FileReader();
    reader.onload = (e) => {
      if (idCardPreview) idCardPreview.src = e.target.result;
      if (dropzone) dropzone.style.display = 'none';
      if (statusCard) statusCard.style.display = 'flex';
    };
    reader.readAsDataURL(file);
  } else {
    if (idCardPreview) {
      idCardPreview.src = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="%23FF6803" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>';
    }
    if (dropzone) dropzone.style.display = 'none';
    if (statusCard) statusCard.style.display = 'flex';
  }

  // Automatically activate student offer pricing if not active
  if (!isStudentOffer) {
    isStudentOffer = true;
    updatePricingUI();
  }
}

function resetIdUpload() {
  const dropzone = document.getElementById('dropzone');
  const statusCard = document.getElementById('uploadStatusCard');
  const fileInput = document.getElementById('studentIdInput');

  if (fileInput) fileInput.value = '';
  if (dropzone) dropzone.style.display = 'block';
  if (statusCard) statusCard.style.display = 'none';
}

function initDragAndDrop() {
  const dropzone = document.getElementById('dropzone');
  if (!dropzone) return;

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, preventDefaults, false);
  });

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => {
      dropzone.style.borderColor = 'var(--color-primary-action)';
      dropzone.style.backgroundColor = '#fff4ec';
    }, false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, () => {
      dropzone.style.borderColor = 'rgba(255, 104, 3, 0.5)';
      dropzone.style.backgroundColor = '#fffaf6';
    }, false);
  });

  dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
      processUploadedFile(files[0]);
    }
  });
}

/* ==========================================================================
   5. TACTILE MOUSE FLASHLIGHT GLOW
   ========================================================================== */

function initMouseFlashlightEffect() {
  const cards = document.querySelectorAll('.glow-card, .btn-primary, .btn-secondary');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });
}

/* ==========================================================================
   6. ONBOARDING & SUBSCRIPTION MODAL (Direct to WhatsApp +91 91130 74896)
   ========================================================================== */

function openJoinModal(planName = 'Full Board') {
  const modal = document.getElementById('joinModal');
  const planSelect = document.getElementById('modalPlanSelect');
  const modalCheckbox = document.getElementById('modalStudentCheckbox');

  if (planSelect && planName) {
    planSelect.value = planName;
  }

  if (modalCheckbox) {
    modalCheckbox.checked = isStudentOffer;
  }

  updateModalPriceDisplay();
  if (modal) {
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function closeJoinModal() {
  const modal = document.getElementById('joinModal');
  if (modal) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

window.addEventListener('click', (e) => {
  const modal = document.getElementById('joinModal');
  if (e.target === modal) {
    closeJoinModal();
  }
});

function toggleModalStudentCheck() {
  const modalCheckbox = document.getElementById('modalStudentCheckbox');
  if (modalCheckbox) {
    isStudentOffer = modalCheckbox.checked;
    updatePricingUI();
  }
}

function updateModalPriceDisplay() {
  const planSelect = document.getElementById('modalPlanSelect');
  const modalFinalPrice = document.getElementById('modalFinalPrice');
  const modalDiscountNote = document.getElementById('modalDiscountNote');
  const modalCheckbox = document.getElementById('modalStudentCheckbox');
  const isStudent = modalCheckbox ? modalCheckbox.checked : isStudentOffer;

  if (!planSelect || !modalFinalPrice) return;

  const isFull = planSelect.value === 'Full Board';
  let price = '';
  let discountNoteText = '';

  if (isFull) {
    price = isStudent ? '₹3,500 / month' : '₹4,500 / month';
    discountNoteText = '✓ ₹1,000 College Student Offer applied upon College ID verification (Regular: ₹4,500)';
  } else {
    price = isStudent ? '₹3,000 / month' : '₹4,000 / month';
    discountNoteText = '✓ ₹1,000 College Student Offer applied upon College ID verification (Regular: ₹4,000)';
  }

  modalFinalPrice.textContent = price;

  if (modalDiscountNote) {
    modalDiscountNote.textContent = discountNoteText;
    modalDiscountNote.style.display = isStudent ? 'block' : 'none';
  }
}

function handleFormSubmit(event) {
  event.preventDefault();

  const name = document.getElementById('studentName').value.trim();
  const phone = document.getElementById('studentPhone').value.trim();
  const plan = document.getElementById('modalPlanSelect').value;
  const diet = document.getElementById('dietPreference').value;
  const modalCheckbox = document.getElementById('modalStudentCheckbox');
  const isStudent = modalCheckbox ? modalCheckbox.checked : isStudentOffer;

  const rate = isStudent
    ? (plan === 'Full Board' ? '₹3,500/month (College Student Offer)' : '₹3,000/month (College Student Offer)')
    : (plan === 'Full Board' ? '₹4,500/month (Regular Rate)' : '₹4,000/month (Regular Rate)');

  const message = `Hello Manjunath Boys Mess!
I would like to join the mess.
• Name: ${name}
• Phone: ${phone}
• Selected Plan: ${plan}
• Dietary Preference: ${diet}
• Student Status: ${isStudent ? 'College Student (Will present valid College ID Card)' : 'Regular / Non-Student'}
• Monthly Fee: ${rate}
• Promises Noted: Morning Tea Included & Daily Night Chapati Fix Guaranteed.`;

  // WhatsApp Web API redirect to +91 91130 74896
  const whatsappUrl = `https://wa.me/${MESS_WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
  
  alert(`Booking details prepared for ${name}!\n\nPlan: ${plan} (${rate})\n\nRedirecting to WhatsApp to send your registration to Manjunath Boys Mess (+91 91130 74896)...`);
  
  closeJoinModal();
  window.open(whatsappUrl, '_blank');
}

/* ==========================================================================
   7. MEAL PAUSE & LEAVE REQUEST GENERATOR
   ========================================================================== */

function sendLeaveNotice() {
  const studentName = prompt('Enter your full name registered at Manjunath Boys Mess:');
  if (!studentName || !studentName.trim()) return;

  const startDate = prompt('From which date are you taking leave? (e.g. Tomorrow / 28 Sept):');
  if (!startDate || !startDate.trim()) return;

  const endDate = prompt('Until which date will you be away? (e.g. 2 Oct):');
  if (!endDate || !endDate.trim()) return;

  const leaveMsg = `Hello Manjunath Boys Mess!
• Student Name: ${studentName.trim()}
• Leave Notice / Meal Pause Request
• From: ${startDate.trim()}
• Until: ${endDate.trim()}
Please pause my meal count during these days. Thank you!`;

  const whatsappUrl = `https://wa.me/${MESS_WHATSAPP_NUMBER}?text=${encodeURIComponent(leaveMsg)}`;
  window.open(whatsappUrl, '_blank');
}

/* ==========================================================================
   8. FAQ ACCORDION TOGGLE
   ========================================================================== */

function toggleFaq(buttonElement) {
  const faqItem = buttonElement.closest('.faq-item');
  if (!faqItem) return;

  const isOpen = faqItem.classList.contains('active');

  // Close all FAQs
  document.querySelectorAll('.faq-item').forEach(item => {
    item.classList.remove('active');
  });

  // Toggle current
  if (!isOpen) {
    faqItem.classList.add('active');
  }
}

/* ==========================================================================
   9. PERSISTENT DEVELOPER TASKBAR LIVE CLOCK
   ========================================================================== */

function initTaskbarClock() {
  const clockEl = document.getElementById('taskbarClock');
  if (!clockEl) return;

  function updateClock() {
    const now = new Date();
    clockEl.textContent = now.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: true
    });
  }

  updateClock();
  setInterval(updateClock, 1000);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initTaskbarClock);
} else {
  initTaskbarClock();
}

// Expose handlers to window scope for inline HTML event attributes
window.openJoinModal = openJoinModal;
window.closeJoinModal = closeJoinModal;
window.toggleMobileMenu = toggleMobileMenu;
window.closeMobileMenu = closeMobileMenu;
window.setPricingMode = setPricingMode;
window.togglePricing = togglePricing;
window.triggerFileInput = triggerFileInput;
window.handleIdFileSelect = handleIdFileSelect;
window.resetIdUpload = resetIdUpload;
window.sendLeaveNotice = sendLeaveNotice;
window.toggleFaq = toggleFaq;
window.handleFormSubmit = handleFormSubmit;
window.updateModalPriceDisplay = updateModalPriceDisplay;
window.toggleModalStudentCheck = toggleModalStudentCheck;
window.initTaskbarClock = initTaskbarClock;

} // end browser environment block

