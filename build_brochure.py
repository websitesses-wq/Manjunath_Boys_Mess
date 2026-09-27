import base64
import os
from html2image import Html2Image
from PIL import Image

def get_base64(filepath):
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            ext = filepath.split(".")[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

logo_b64 = get_base64("assets/rajeshwari_logo.jpg")
food_b64 = get_base64("assets/chapathi_uuta.jpg")
qr_wa_b64 = get_base64("assets/qr_whatsapp_clean.png")
qr_map_b64 = get_base64("assets/qr_maps_clean.png")

# Common CSS for the brochure sheet
brochure_css = """
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      --gold-100: #FFF6E5;
      --gold-200: #FDE8BF;
      --gold-300: #F7D488;
      --gold-400: #E6BE64;
      --gold-500: #D4AF37;
      --gold-600: #B8860B;
      --gold-700: #8C651A;
      --gold-gradient: linear-gradient(135deg, #FFF0CA 0%, #D4AF37 45%, #9E741B 100%);
      
      --brown-900: #100804;
      --brown-850: #180D07;
      --brown-800: #24140B;
      --brown-700: #331C0F;
      --card-bg: rgba(36, 19, 10, 0.92);
      
      --text-main: #FDFBF7;
      --text-cream: #F5E8D8;
      --text-muted: #C4AF97;
      --text-gold: #ECC371;

      --accent-green: #34D399;
    }

    .brochure-sheet {
      width: 1240px;
      height: 1754px;
      position: relative;
      background: radial-gradient(circle at 50% 0%, #341A0D 0%, #1A0D06 50%, #0E0603 100%);
      border: 2px solid #5C381B;
      box-sizing: border-box;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 30px 36px 26px;
      font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif;
      color: var(--text-main);
      -webkit-font-smoothing: antialiased;
    }

    /* Metallic Gold Double Frame */
    .brochure-sheet::before {
      content: '';
      position: absolute;
      inset: 12px;
      border: 1px solid rgba(212, 175, 55, 0.35);
      pointer-events: none;
      z-index: 1;
    }

    .brochure-sheet::after {
      content: '';
      position: absolute;
      inset: 16px;
      border: 1px solid rgba(212, 175, 55, 0.15);
      pointer-events: none;
      z-index: 1;
    }

    /* Corner Gold Ornaments */
    .corner-decor {
      position: absolute;
      width: 28px;
      height: 28px;
      border-color: var(--gold-400);
      pointer-events: none;
      z-index: 2;
    }
    .corner-tl { top: 16px; left: 16px; border-top: 3px solid; border-left: 3px solid; }
    .corner-tr { top: 16px; right: 16px; border-top: 3px solid; border-right: 3px solid; }
    .corner-bl { bottom: 16px; left: 16px; border-bottom: 3px solid; border-left: 3px solid; }
    .corner-br { bottom: 16px; right: 16px; border-bottom: 3px solid; border-right: 3px solid; }

    .bg-glow {
      position: absolute;
      border-radius: 50%;
      filter: blur(120px);
      pointer-events: none;
      z-index: 0;
    }
    .bg-glow-top {
      top: -120px;
      left: 50%;
      transform: translateX(-50%);
      width: 600px;
      height: 600px;
      background: rgba(212, 175, 55, 0.12);
    }
    .bg-glow-mid {
      top: 800px;
      right: -80px;
      width: 500px;
      height: 500px;
      background: rgba(184, 134, 11, 0.08);
    }

    .content-layer {
      position: relative;
      z-index: 3;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: space-between;
    }

    /* 1. TOP STRIP */
    .top-badge-strip {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(212, 175, 55, 0.25);
    }

    .fssai-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(212, 175, 55, 0.1);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 4px 12px;
      border-radius: 6px;
    }

    .fssai-text {
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: var(--gold-200);
    }
    .fssai-text span {
      color: #FFFFFF;
      font-weight: 800;
    }

    .location-tag-top {
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: var(--gold-300);
    }

    .academic-pill {
      background: var(--gold-gradient);
      color: #1A0D06;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 12px;
      border-radius: 20px;
      letter-spacing: 0.8px;
    }

    /* 2. HERO BRAND BANNER */
    .hero-banner {
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      gap: 22px;
      padding: 8px 0;
    }

    .logo-frame {
      width: 96px;
      height: 96px;
      border-radius: 50%;
      padding: 3px;
      background: var(--gold-gradient);
      box-shadow: 0 0 22px rgba(212, 175, 55, 0.35);
      flex-shrink: 0;
    }

    .logo-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 50%;
      border: 2px solid #1A0E07;
      display: block;
    }

    .brand-headings {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .brand-eyebrow {
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 2.5px;
      color: var(--gold-400);
      text-transform: uppercase;
    }

    .brand-main-title {
      font-family: 'Cinzel', serif;
      font-size: 2.45rem;
      font-weight: 900;
      line-height: 1.05;
      letter-spacing: 0.8px;
      background: linear-gradient(135deg, #FFFFFF 0%, #FDE4A9 35%, #D4AF37 70%, #AA781C 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 2px 18px rgba(212, 175, 55, 0.25);
    }

    .brand-tagline {
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--text-cream);
    }

    .brand-locality {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--gold-300);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .hero-contact-badge {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 6px;
    }

    .phone-callout {
      background: rgba(43, 23, 14, 0.9);
      border: 1px solid var(--gold-500);
      border-radius: 8px;
      padding: 6px 14px;
      text-align: right;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }

    .phone-label {
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: var(--gold-300);
    }

    .phone-num {
      font-size: 1.18rem;
      font-weight: 800;
      color: #FFFFFF;
      letter-spacing: 0.5px;
    }

    .whatsapp-instant-pill {
      background: #25D366;
      color: #063A17;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 16px;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    /* 3. FOUR CORE PILLARS */
    .pillars-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin: 4px 0 6px;
    }

    .pillar-card {
      background: linear-gradient(180deg, rgba(50, 26, 14, 0.75) 0%, rgba(28, 14, 7, 0.85) 100%);
      border: 1px solid rgba(212, 175, 55, 0.28);
      border-radius: 8px;
      padding: 8px 10px;
      display: flex;
      align-items: center;
      gap: 8px;
      position: relative;
      overflow: hidden;
    }

    .pillar-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 2px;
      background: var(--gold-gradient);
    }

    .pillar-icon-box {
      width: 32px;
      height: 32px;
      border-radius: 6px;
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid rgba(212, 175, 55, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      flex-shrink: 0;
    }

    .pillar-info h4 {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--gold-200);
      margin-bottom: 1px;
    }

    .pillar-info p {
      font-size: 0.68rem;
      font-weight: 400;
      color: var(--text-cream);
      line-height: 1.2;
    }

    /* SECTION RIBBON */
    .section-ribbon {
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 4px 0;
    }

    .ribbon-line {
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.4), transparent);
    }

    .ribbon-title {
      font-family: 'Cinzel', serif;
      font-size: 0.88rem;
      font-weight: 800;
      letter-spacing: 1.8px;
      text-transform: uppercase;
      color: var(--gold-300);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .ribbon-diamond {
      color: var(--gold-400);
      font-size: 0.7rem;
    }

    /* 4. DAILY MEALS GRID + REAL FOOD IMAGE */
    .meals-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 240px;
      gap: 10px;
    }

    .meal-box {
      background: var(--card-bg);
      border: 1px solid rgba(212, 175, 55, 0.28);
      border-radius: 10px;
      padding: 10px 12px 8px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .meal-box.highlight-fix {
      border-color: var(--gold-400);
      box-shadow: 0 0 16px rgba(212, 175, 55, 0.15);
      background: linear-gradient(180deg, rgba(54, 29, 16, 0.92) 0%, rgba(32, 16, 8, 0.95) 100%);
    }

    .meal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
    }

    .meal-tag-timing {
      font-size: 0.67rem;
      font-weight: 700;
      color: var(--gold-300);
      background: rgba(212, 175, 55, 0.12);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid rgba(212, 175, 55, 0.25);
    }

    .meal-name {
      font-size: 0.94rem;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .meal-guarantee-pill {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 0.64rem;
      font-weight: 800;
      color: var(--gold-100);
      background: linear-gradient(90deg, #9C741E, #694C10);
      padding: 2px 6px;
      border-radius: 4px;
      margin-bottom: 6px;
    }

    .meal-items-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 6px;
    }

    .meal-items-list li {
      font-size: 0.71rem;
      color: var(--text-cream);
      display: flex;
      align-items: flex-start;
      gap: 5px;
      line-height: 1.22;
    }

    .meal-items-list li span.bullet {
      color: var(--gold-400);
      font-weight: 800;
    }

    .meal-footnote {
      font-size: 0.65rem;
      font-style: italic;
      color: var(--text-muted);
      border-top: 1px dashed rgba(212, 175, 55, 0.2);
      padding-top: 4px;
    }

    .food-showcase-box {
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      border: 2px solid var(--gold-500);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      background: #1C0F08;
    }

    .food-img {
      width: 100%;
      height: 100%;
      min-height: 140px;
      object-fit: cover;
      display: block;
    }

    .food-overlay-badge {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(180deg, transparent 0%, rgba(20, 10, 5, 0.95) 40%, #140A05 100%);
      padding: 14px 8px 6px;
      text-align: center;
    }

    .food-badge-title {
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--gold-300);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .food-badge-desc {
      font-size: 0.65rem;
      color: var(--text-cream);
    }

    .dietary-strip {
      background: rgba(43, 24, 14, 0.65);
      border: 1px solid rgba(212, 175, 55, 0.2);
      border-radius: 6px;
      padding: 6px 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      margin: 4px 0;
    }

    .dietary-strip-icon {
      font-size: 1rem;
    }

    .dietary-strip-text {
      font-size: 0.7rem;
      color: var(--text-cream);
      line-height: 1.25;
    }

    .dietary-strip-text strong {
      color: var(--gold-300);
    }

    /* 5. PRICING & SUBSCRIPTION PLANS */
    .pricing-wrap {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }

    .plan-card {
      background: linear-gradient(180deg, rgba(44, 23, 12, 0.95) 0%, rgba(24, 12, 6, 0.95) 100%);
      border: 1.5px solid rgba(212, 175, 55, 0.35);
      border-radius: 12px;
      padding: 12px 16px 10px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }

    .plan-card.plan-featured {
      border: 2px solid var(--gold-400);
      box-shadow: 0 0 25px rgba(212, 175, 55, 0.2);
      background: linear-gradient(180deg, rgba(54, 28, 15, 0.98) 0%, rgba(28, 14, 7, 0.98) 100%);
    }

    .plan-pill-tag {
      position: absolute;
      top: -9px;
      left: 16px;
      background: var(--gold-gradient);
      color: #1A0D06;
      font-size: 0.65rem;
      font-weight: 800;
      padding: 2px 10px;
      border-radius: 16px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
    }

    .plan-header-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-top: 2px;
      margin-bottom: 4px;
    }

    .plan-title-block h3 {
      font-family: 'Cinzel', serif;
      font-size: 1.22rem;
      font-weight: 800;
      color: #FFFFFF;
      letter-spacing: 0.5px;
    }

    .plan-meals-covered {
      font-size: 0.74rem;
      color: var(--gold-300);
      font-weight: 600;
    }

    .student-price-wrap {
      display: flex;
      align-items: baseline;
      justify-content: flex-end;
      gap: 2px;
    }

    .price-currency {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--gold-400);
    }

    .price-val {
      font-size: 2.05rem;
      font-weight: 900;
      color: #FFFFFF;
      line-height: 1;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .price-period {
      font-size: 0.74rem;
      color: var(--gold-200);
      font-weight: 600;
    }

    .regular-strike {
      font-size: 0.7rem;
      color: #94A3B8;
      text-decoration: line-through;
      text-align: right;
    }

    .student-savings-badge {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(34, 197, 94, 0.12);
      border: 1px solid rgba(34, 197, 94, 0.35);
      border-radius: 5px;
      padding: 3px 8px;
      margin-bottom: 6px;
    }

    .student-savings-text {
      font-size: 0.68rem;
      font-weight: 800;
      color: #4ADE80;
    }

    .id-required-tag {
      font-size: 0.66rem;
      font-weight: 700;
      color: var(--gold-200);
    }

    .plan-bullets {
      list-style: none;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4px 10px;
    }

    .plan-bullets li {
      font-size: 0.69rem;
      color: var(--text-cream);
      display: flex;
      align-items: center;
      gap: 5px;
      line-height: 1.2;
    }

    .plan-bullets li span.chk {
      color: #4ADE80;
      font-weight: 900;
      font-size: 0.76rem;
    }
    .plan-bullets li span.cross {
      color: #F87171;
      font-weight: 900;
      font-size: 0.76rem;
    }

    /* Savings Comparison Bar */
    .savings-comparison-strip {
      background: linear-gradient(90deg, #2A160C 0%, #3B2011 50%, #2A160C 100%);
      border: 1px solid var(--gold-500);
      border-radius: 8px;
      padding: 6px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin: 4px 0;
    }

    .compare-side {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .compare-label {
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .compare-num-bad {
      font-size: 0.98rem;
      font-weight: 800;
      color: #F87171;
      text-decoration: line-through;
    }

    .compare-num-good {
      font-size: 1.15rem;
      font-weight: 900;
      color: #4ADE80;
    }

    .save-highlight-pill {
      background: var(--gold-gradient);
      color: #1A0D06;
      font-size: 0.74rem;
      font-weight: 900;
      padding: 4px 14px;
      border-radius: 16px;
      letter-spacing: 0.4px;
      box-shadow: 0 2px 10px rgba(212, 175, 55, 0.4);
    }

    /* 6. ESSENTIAL CONVENIENCES */
    .facilities-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin: 2px 0;
    }

    .facility-box {
      background: rgba(36, 18, 9, 0.75);
      border: 1px solid rgba(212, 175, 55, 0.22);
      border-radius: 8px;
      padding: 7px 9px;
    }

    .facility-box h5 {
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--gold-300);
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .facility-box p {
      font-size: 0.66rem;
      color: var(--text-cream);
      line-height: 1.22;
    }

    /* 7. FOOTER CONTACT, QR CODES & DUAL BAR */
    .brochure-footer {
      background: linear-gradient(180deg, #180D06 0%, #100803 100%);
      border: 1px solid rgba(212, 175, 55, 0.35);
      border-radius: 10px;
      padding: 10px 16px;
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: center;
      gap: 16px;
      margin-top: 2px;
    }

    .qr-block {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(212, 175, 55, 0.25);
      border-radius: 6px;
      padding: 5px 8px;
    }

    .qr-frame {
      width: 58px;
      height: 58px;
      background: #FFFFFF;
      padding: 3px;
      border-radius: 5px;
      flex-shrink: 0;
    }

    .qr-img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
    }

    .qr-desc {
      display: flex;
      flex-direction: column;
      gap: 1px;
    }

    .qr-tag {
      font-size: 0.62rem;
      font-weight: 800;
      color: var(--gold-400);
      text-transform: uppercase;
      letter-spacing: 0.6px;
    }

    .qr-action-title {
      font-size: 0.74rem;
      font-weight: 800;
      color: #FFFFFF;
    }

    .qr-hint {
      font-size: 0.64rem;
      color: var(--text-muted);
    }

    .footer-center-info {
      text-align: center;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .address-highlight {
      font-size: 0.77rem;
      font-weight: 700;
      color: var(--text-cream);
    }

    .landmark-sub {
      font-size: 0.7rem;
      color: var(--gold-300);
      font-weight: 600;
    }

    .contact-cta-line {
      font-size: 0.74rem;
      color: var(--text-main);
      font-weight: 700;
    }
    .contact-cta-line span {
      color: var(--gold-400);
      font-weight: 800;
    }

    .payment-modes-pill {
      font-size: 0.66rem;
      color: var(--text-muted);
    }
"""

brochure_inner_html = f"""
    <!-- Decorative Ornaments -->
    <div class="corner-decor corner-tl"></div>
    <div class="corner-decor corner-tr"></div>
    <div class="corner-decor corner-bl"></div>
    <div class="corner-decor corner-br"></div>
    <div class="bg-glow bg-glow-top"></div>
    <div class="bg-glow bg-glow-mid"></div>

    <div class="content-layer">

      <!-- 1. TOP BADGES STRIP -->
      <div class="top-badge-strip">
        <div class="fssai-badge">
          <span style="color:var(--gold-400); font-size:0.9rem;">🛡️</span>
          <span class="fssai-text">FSSAI CERTIFIED MESS // LIC NO: <span>21224010000492</span></span>
        </div>
        <div class="location-tag-top">OPP. MORE SUPER MARKET &bull; JUST 15 MINS FROM BIET &bull; DAVANAGERE</div>
        <div class="academic-pill">🎓 STUDENT OFFER 2026</div>
      </div>

      <!-- 2. BRAND HERO HEADER -->
      <div class="hero-banner">
        <div class="logo-frame">
          <img src="{logo_b64}" alt="Rajeshwari Boys Mess Logo" class="logo-img">
        </div>
        <div class="brand-headings">
          <span class="brand-eyebrow">Davanagere's Trusted Home-Cooked Mess</span>
          <h1 class="brand-main-title">RAJESHWARI BOYS MESS</h1>
          <p class="brand-tagline">Clean, Hygienic &amp; Wholesome Meals Tailored for College Students</p>
          <div class="brand-locality">
            📍 #42, Opp. More Super Market, Davanagere - 577004 (Just 15 mins from BIET Campus)
          </div>
        </div>
        <div class="hero-contact-badge">
          <div class="phone-callout">
            <div class="phone-label">Direct Mess Inquiries</div>
            <div class="phone-num">+91 96115 57696</div>
          </div>
          <div class="whatsapp-instant-pill">
            💬 WhatsApp Seat Booking Available
          </div>
        </div>
      </div>

      <!-- 3. THE 4 OPERATIONAL COMMITMENTS / PILLARS -->
      <div class="pillars-strip">
        <div class="pillar-card">
          <div class="pillar-icon-box">☕</div>
          <div class="pillar-info">
            <h4>Morning Tea Included</h4>
            <p>Freshly brewed hot tea served daily with breakfast unconditionally.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-icon-box">🫓</div>
          <div class="pillar-info">
            <h4>Night Chapati Fix</h4>
            <p>Fresh, soft handmade wheat chapatis guaranteed every single dinner.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-icon-box">🍗</div>
          <div class="pillar-info">
            <h4>Veg &amp; Non-Veg Days</h4>
            <p>Chicken &amp; Egg only on scheduled days. Separate vessels for pure veg.</p>
          </div>
        </div>
        <div class="pillar-card">
          <div class="pillar-icon-box">🎓</div>
          <div class="pillar-info">
            <h4>College Student Offer</h4>
            <p>Direct subsidized monthly board for all BIET, GMIT, DRM &amp; BDT students.</p>
          </div>
        </div>
      </div>

      <!-- 4. SECTION DIVIDER: DAILY MEAL SCHEDULE -->
      <div class="section-ribbon">
        <div class="ribbon-line"></div>
        <div class="ribbon-title">
          <span class="ribbon-diamond">&#9670;</span>
          HONEST DAILY MEALS &amp; DINING SCHEDULE
          <span class="ribbon-diamond">&#9670;</span>
        </div>
        <div class="ribbon-line"></div>
      </div>

      <!-- 5. THREE MEAL CARDS + REAL FOOD PHOTO -->
      <div class="meals-grid">
        
        <!-- Breakfast -->
        <div class="meal-box">
          <div>
            <div class="meal-header">
              <span class="meal-tag-timing">⏰ 07:30 AM &ndash; 09:30 AM</span>
            </div>
            <h3 class="meal-name">☕ Breakfast + Tea</h3>
            <div class="meal-guarantee-pill">✓ Tea Included Every Day</div>
            <ul class="meal-items-list">
              <li><span class="bullet">&bull;</span> Freshly cooked morning tiffins</li>
              <li><span class="bullet">&bull;</span> Idli Vada, Dosa, Poori, Upma, Avalakki</li>
              <li><span class="bullet">&bull;</span> Hot cup of authentic fresh tea</li>
              <li><span class="bullet">&bull;</span> Quick service for 8:00 AM college rush</li>
            </ul>
          </div>
          <div class="meal-footnote">*Morning tea unconditionally provided daily</div>
        </div>

        <!-- Lunch -->
        <div class="meal-box">
          <div>
            <div class="meal-header">
              <span class="meal-tag-timing">⏰ 12:30 PM &ndash; 02:30 PM</span>
            </div>
            <h3 class="meal-name">🍲 Wholesome Lunch</h3>
            <div class="meal-guarantee-pill">✓ Unlimited Rice &amp; Sambar</div>
            <ul class="meal-items-list">
              <li><span class="bullet">&bull;</span> Pure Veg: Steamed Rice, Sambar, Rasam</li>
              <li><span class="bullet">&bull;</span> Fresh Vegetable Palya, Curd / Buttermilk</li>
              <li><span class="bullet">&bull;</span> Chicken / Egg Curry on scheduled days</li>
              <li><span class="bullet">&bull;</span> Unlimited refills during dining hours</li>
            </ul>
          </div>
          <div class="meal-footnote">*Dedicated separate vessels for pure veg</div>
        </div>

        <!-- Dinner -->
        <div class="meal-box highlight-fix">
          <div>
            <div class="meal-header">
              <span class="meal-tag-timing">⏰ 07:45 PM &ndash; 10:00 PM</span>
            </div>
            <h3 class="meal-name">🫓 Night Chapati Fix</h3>
            <div class="meal-guarantee-pill" style="background: var(--gold-gradient); color: #1A0D06;">★ Every Night Guaranteed</div>
            <ul class="meal-items-list">
              <li><span class="bullet">&bull;</span> Soft handmade wheat chapatis nightly</li>
              <li><span class="bullet">&bull;</span> Delicious rich curry / gravy</li>
              <li><span class="bullet">&bull;</span> Hot steamed rice with Dal &amp; Rasam</li>
              <li><span class="bullet">&bull;</span> Late plate reserve kept until 10:30 PM</li>
            </ul>
          </div>
          <div class="meal-footnote">*Night chapatis are guaranteed every single night</div>
        </div>

        <!-- Real Food Showcase Image -->
        <div class="food-showcase-box">
          <img src="{food_b64}" alt="Authentic Rajeshwari Mess Meal" class="food-img">
          <div class="food-overlay-badge">
            <div class="food-badge-title">Handmade Fresh Chapatis</div>
            <div class="food-badge-desc">Prepared fresh on iron tawas every dinner</div>
          </div>
        </div>

      </div>

      <!-- Dietary Policy Strip -->
      <div class="dietary-strip">
        <span class="dietary-strip-icon">🍗</span>
        <div class="dietary-strip-text">
          <strong>Honest Dietary Policy &mdash; No False Promises:</strong> Non-veg is served only on scheduled weekly rotation days (Wed &amp; Sun) and is strictly restricted to <strong>fresh Chicken &amp; Egg only</strong>. Pure vegetarian meals are prepared in dedicated separate vessels with 100% dietary respect for all students.
        </div>
      </div>

      <!-- 6. SECTION DIVIDER: SUBSCRIPTION PLANS -->
      <div class="section-ribbon">
        <div class="ribbon-line"></div>
        <div class="ribbon-title">
          <span class="ribbon-diamond">&#9670;</span>
          MONTHLY SUBSCRIPTION PLANS &bull; SPECIAL STUDENT OFFER
          <span class="ribbon-diamond">&#9670;</span>
        </div>
        <div class="ribbon-line"></div>
      </div>

      <!-- 7. TWO PRICING PLANS SIDE-BY-SIDE -->
      <div class="pricing-wrap">
        
        <!-- Full Board -->
        <div class="plan-card plan-featured">
          <div class="plan-pill-tag">★ MOST POPULAR &bull; ALL 3 MEALS</div>
          <div class="plan-header-row">
            <div class="plan-title-block">
              <h3>FULL BOARD PLAN</h3>
              <div class="plan-meals-covered">Breakfast (with Morning Tea) + Lunch + Dinner (with Chapati Fix)</div>
            </div>
            <div class="plan-price-block">
              <div class="student-price-wrap">
                <span class="price-currency">₹</span>
                <span class="price-val">3,500</span>
                <span class="price-period">/ month</span>
              </div>
              <div class="regular-strike">Regular: ₹4,500 / month</div>
            </div>
          </div>

          <div class="student-savings-badge">
            <span class="student-savings-text">🎉 Special College Student Subsidy: SAVE ₹1,000/MO</span>
            <span class="id-required-tag">🪪 College ID Required</span>
          </div>

          <ul class="plan-bullets">
            <li><span class="chk">&#10003;</span> Daily Breakfast with Hot Morning Tea</li>
            <li><span class="chk">&#10003;</span> Wholesome Lunch with Unlimited Refills</li>
            <li><span class="chk">&#10003;</span> Guaranteed Night Handmade Chapatis</li>
            <li><span class="chk">&#10003;</span> Veg &amp; Chicken/Egg Non-Veg on fixed days</li>
            <li><span class="chk">&#10003;</span> Festival Special Feasts included free</li>
            <li><span class="chk">&#10003;</span> Up to 5 days Meal Pause Credit for exams</li>
          </ul>
        </div>

        <!-- Half Board -->
        <div class="plan-card">
          <div class="plan-pill-tag" style="background: rgba(212, 175, 55, 0.2); color: var(--gold-200); border: 1px solid var(--gold-500);">COLLEGE TIME SAVER &bull; 2 MEALS</div>
          <div class="plan-header-row">
            <div class="plan-title-block">
              <h3>HALF BOARD PLAN</h3>
              <div class="plan-meals-covered">Wholesome Lunch + Night Dinner (with Guaranteed Chapati Fix)</div>
            </div>
            <div class="plan-price-block">
              <div class="student-price-wrap">
                <span class="price-currency">₹</span>
                <span class="price-val">3,000</span>
                <span class="price-period">/ month</span>
              </div>
              <div class="regular-strike">Regular: ₹4,000 / month</div>
            </div>
          </div>

          <div class="student-savings-badge">
            <span class="student-savings-text">🎉 Special College Student Subsidy: SAVE ₹1,000/MO</span>
            <span class="id-required-tag">🪪 College ID Required</span>
          </div>

          <ul class="plan-bullets">
            <li><span class="cross">&#10005;</span> Morning Breakfast not included</li>
            <li><span class="chk">&#10003;</span> Wholesome Lunch with Unlimited Refills</li>
            <li><span class="chk">&#10003;</span> Guaranteed Night Handmade Chapatis</li>
            <li><span class="chk">&#10003;</span> Veg &amp; Chicken/Egg Non-Veg on fixed days</li>
            <li><span class="chk">&#10003;</span> Festival Special Feasts included free</li>
            <li><span class="chk">&#10003;</span> Late Dinner Reserve for lab / library return</li>
          </ul>
        </div>

      </div>

      <!-- Student Savings Comparison Strip -->
      <div class="savings-comparison-strip">
        <div class="compare-side">
          <span class="compare-label">Outside Hotel Food (~₹250/day):</span>
          <span class="compare-num-bad">₹7,500 / mo</span>
        </div>
        <div class="save-highlight-pill">
          💰 YOU SAVE OVER ₹4,000 EVERY MONTH WITH RAJESHWARI MESS!
        </div>
        <div class="compare-side">
          <span class="compare-label">Rajeshwari Full Board:</span>
          <span class="compare-num-good">₹3,500 / mo</span>
        </div>
      </div>

      <!-- 8. ESSENTIAL STUDENT CONVENIENCES & POLICIES -->
      <div class="facilities-grid">
        <div class="facility-box">
          <h5>🪪 College ID Verification</h5>
          <p>Valid for BIET, GMIT, DRM, BDT &amp; all colleges. Present ID card at counter or WhatsApp to lock student rate.</p>
        </div>
        <div class="facility-box">
          <h5>📝 5-Day Meal Pause Credit</h5>
          <p>Traveling home for holidays or exams? Pause meals for up to 5 days with 12 hours prior WhatsApp notice.</p>
        </div>
        <div class="facility-box">
          <h5>💧 RO Purified Safe Water</h5>
          <p>Multi-stage industrial RO purified water facility ensuring 100% clean and healthy drinking water for boarders.</p>
        </div>
        <div class="facility-box">
          <h5>🕒 Late Plate Reservation</h5>
          <p>Dinner plates (with hot chapatis) kept safe until 10:30 PM for students attending late college labs or library.</p>
        </div>
      </div>

      <!-- 9. FOOTER: ADDRESS, DUAL QR CODES & BOOKING -->
      <div class="brochure-footer">
        
        <!-- WhatsApp QR -->
        <div class="qr-block">
          <div class="qr-frame">
            <img src="{qr_wa_b64}" alt="Scan to WhatsApp" class="qr-img">
          </div>
          <div class="qr-desc">
            <span class="qr-tag">SCAN TO BOOK SEAT</span>
            <div class="qr-action-title">WhatsApp Booking</div>
            <div class="qr-hint">+91 96115 57696</div>
          </div>
        </div>

        <!-- Center Address & Call -->
        <div class="footer-center-info">
          <div class="address-highlight">#42, Opposite More Super Market, Davanagere - 577004</div>
          <div class="landmark-sub">Just 15 mins from BIET Campus &bull; Near Student Hostels &amp; PGs</div>
          <div class="contact-cta-line">
            Direct Phone / WhatsApp: <span>+91 96115 57696</span> &bull; FSSAI Lic: <span>21224010000492</span>
          </div>
          <div class="payment-modes-pill">
            Accepted Payments: Google Pay, PhonePe, Paytm (UPI: +91 96115 57696) &amp; Cash Counter
          </div>
        </div>

        <!-- Google Maps QR -->
        <div class="qr-block">
          <div class="qr-frame">
            <img src="{qr_map_b64}" alt="Scan for Google Maps" class="qr-img">
          </div>
          <div class="qr-desc">
            <span class="qr-tag">SCAN TO NAVIGATE</span>
            <div class="qr-action-title">Google Maps</div>
            <div class="qr-hint">Directions to Mess</div>
          </div>
        </div>

      </div>

    </div>
"""

# 1. STANDALONE CAPTURE TEMPLATE (NO TOOLBAR, ZERO MARGINS, EXACT 1240x1754 A4)
capture_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1240, initial-scale=1.0">
  <title>Rajeshwari Boys Mess Brochure</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body {{
      margin: 0;
      padding: 0;
      width: 1240px;
      height: 1754px;
      overflow: hidden;
      background: #0E0603;
    }}
    {brochure_css}
  </style>
</head>
<body>
  <div class="brochure-sheet" id="brochureSheet">
    {brochure_inner_html}
  </div>
</body>
</html>
"""

with open("brochure_capture.html", "w", encoding="utf-8") as f:
    f.write(capture_html)
print("Saved brochure_capture.html")

# 2. INTERACTIVE VIEWER TEMPLATE (WITH TOP TOOLBAR & DOWNLOAD BUTTON)
viewer_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rajeshwari Boys Mess Davanagere | Official A4 Brochure</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
  <style>
    body {{
      background: #080402;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 24px 15px 40px;
      min-height: 100vh;
    }}

    .action-toolbar {{
      width: 100%;
      max-width: 1240px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      background: linear-gradient(90deg, #1C0F08, #2E170C);
      border: 1px solid rgba(212, 175, 55, 0.35);
      border-radius: 12px;
      padding: 14px 22px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }}

    .toolbar-title {{
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: #F7D488;
      letter-spacing: 1px;
    }}

    .toolbar-actions {{
      display: flex;
      gap: 12px;
    }}

    .btn-action {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s ease;
      border: none;
    }}

    .btn-download {{
      background: linear-gradient(135deg, #FFF0CA 0%, #D4AF37 45%, #9E741B 100%);
      color: #1A0D06;
      box-shadow: 0 4px 15px rgba(212, 175, 55, 0.35);
    }}

    .btn-download:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
    }}

    .btn-print {{
      background: rgba(255, 255, 255, 0.08);
      color: #FDE8BF;
      border: 1px solid rgba(212, 175, 55, 0.3);
    }}

    .btn-print:hover {{
      background: rgba(212, 175, 55, 0.15);
      border-color: #E6BE64;
    }}

    .btn-pic {{
      background: #25D366;
      color: #063A17;
      text-decoration: none;
    }}

    @media print {{
      body {{
        padding: 0;
        background: transparent;
      }}
      .action-toolbar {{
        display: none !important;
      }}
      .brochure-sheet {{
        box-shadow: none;
        border: none;
        width: 100% !important;
        height: 100% !important;
        page-break-after: avoid;
        page-break-inside: avoid;
      }}
    }}

    {brochure_css}
  </style>
</head>
<body>

  <!-- FLOATING ACTION TOOLBAR -->
  <div class="action-toolbar" id="topToolbar">
    <div class="toolbar-title">RAJESHWARI BOYS MESS &mdash; OFFICIAL A4 BROCHURE</div>
    <div class="toolbar-actions">
      <a href="rajeshwari_boys_mess_brochure_a4.png" download="Rajeshwari_Boys_Mess_Brochure_A4.png" class="btn-action btn-download">
        📥 Download Picture (PNG)
      </a>
      <a href="rajeshwari_boys_mess_brochure_a4.jpg" download="Rajeshwari_Boys_Mess_Brochure_A4.jpg" class="btn-action btn-print">
        🖼️ Download JPG
      </a>
      <button type="button" class="btn-action btn-print" onclick="window.print()">
        🖨️ Print / Save PDF
      </button>
    </div>
  </div>

  <!-- A4 BROCHURE CONTAINER -->
  <div class="brochure-sheet" id="brochureSheet">
    {brochure_inner_html}
  </div>

  <script>
    // Browser-side High-Res PNG Download using html2canvas fallback
    function downloadBrochurePNG() {{
      const sheet = document.getElementById('brochureSheet');
      html2canvas(sheet, {{
        scale: 2,
        useCORS: true,
        backgroundColor: '#0E0603'
      }}).then(canvas => {{
        const link = document.createElement('a');
        link.download = 'Rajeshwari_Boys_Mess_Brochure_A4.png';
        link.href = canvas.toDataURL('image/png', 1.0);
        link.click();
      }});
    }}
  </script>
</body>
</html>
"""

with open("brochure.html", "w", encoding="utf-8") as f:
    f.write(viewer_html)
print("Saved brochure.html")

# 3. RENDER CLEAN HIGH-RES A4 PICTURE FROM brochure_capture.html
print("Rendering clean A4 brochure picture without toolbar...")
hti = Html2Image(
    browser_executable='C:/Program Files/Google/Chrome/Application/chrome.exe',
    output_path='.'
)

hti.screenshot(
    html_file='brochure_capture.html',
    save_as='rajeshwari_boys_mess_brochure_a4.png',
    size=(1240, 1754)
)

if os.path.exists("rajeshwari_boys_mess_brochure_a4.png"):
    file_size = os.path.getsize("rajeshwari_boys_mess_brochure_a4.png")
    print(f"Rendered PNG successfully! File size: {file_size} bytes")
    
    # Save JPG version as well
    im = Image.open("rajeshwari_boys_mess_brochure_a4.png")
    rgb_im = im.convert('RGB')
    rgb_im.save("rajeshwari_boys_mess_brochure_a4.jpg", quality=95)
    print("Saved JPG version: rajeshwari_boys_mess_brochure_a4.jpg (", os.path.getsize("rajeshwari_boys_mess_brochure_a4.jpg"), "bytes)")
    
    # Also save a copy named brochure.png and brochure.jpg for simple convenience
    im.save("brochure.png")
    rgb_im.save("brochure.jpg", quality=95)
    print("Saved brochure.png and brochure.jpg")
else:
    print("PNG render failed!")
