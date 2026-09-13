import streamlit as st
from pathlib import Path
from urllib.parse import quote
import base64


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Nails Collection",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# STORE SETTINGS
# ============================================================

STORE_NAME = "Nails Collection"
PHONE = "+92 3289718577"
WHATSAPP = "923289718577"


# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "name": "Red Glossy Elegance",
        "price": 1499,
        "category": "Classic",
        "image": "red_glossy.png",
        "description": "Elegant glossy red nails for a bold and timeless look.",
    },
    {
        "name": "Classic French Tips",
        "price": 1299,
        "category": "French",
        "image": "french_tips.png",
        "description": "Clean and timeless French tips for every occasion.",
    },
    {
        "name": "Sunflower Bloom",
        "price": 1699,
        "category": "Floral",
        "image": "sunflower_nails.png",
        "description": "Fresh sunflower-inspired nail art with beautiful floral details.",
    },
    {
        "name": "Pink Bow Nails",
        "price": 1599,
        "category": "Cute",
        "image": "pink_bows.png",
        "description": "Pretty pink nails finished with charming bow details.",
    },
    {
        "name": "Pastel Floral Art",
        "price": 1799,
        "category": "Floral",
        "image": "pastel_art.png",
        "description": "Soft pastel shades paired with delicate floral artwork.",
    },
    {
        "name": "Sky Blue French",
        "price": 1399,
        "category": "French",
        "image": "blue_french.png",
        "description": "Fresh sky-blue French tips for a modern elegant style.",
    },
]


# ============================================================
# PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# IMAGE TO BASE64
# ============================================================

def image_to_base64(image_path):
    """Convert local image into base64 for HTML cards."""

    if not image_path.exists():
        return ""

    image_data = image_path.read_bytes()
    encoded = base64.b64encode(image_data).decode()

    extension = image_path.suffix.lower()

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }

    mime = mime_types.get(
        extension,
        "image/png"
    )

    return f"data:{mime};base64,{encoded}"


# ============================================================
# PREMIUM CSS
# ============================================================

st.html(
    """
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap'
);


/* ============================================================
   GLOBAL
   ============================================================ */

:root {
    --pink: #c04b78;
    --pink-dark: #9f365f;
    --pink-light: #fff1f6;

    --text: #34232d;
    --muted: #766872;

    --gold: #d7a25c;

    --border: #efd7e0;
}


html,
body,
[data-testid="stAppViewContainer"] {
    font-family: "DM Sans", sans-serif;
}


.block-container {
    max-width: 1500px;
    padding-top: 12px;
    padding-bottom: 50px;
}


/* Hide Streamlit UI */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    position: relative;
    overflow: hidden;

    min-height: 315px;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;

    padding: 55px 35px;

    border-radius: 20px;

    margin-bottom: 20px;

    background:
        radial-gradient(
            circle at 15% 50%,
            rgba(255, 215, 228, 0.90),
            transparent 30%
        ),
        radial-gradient(
            circle at 88% 20%,
            rgba(255, 224, 234, 0.90),
            transparent 32%
        ),
        linear-gradient(
            110deg,
            #f8dce5,
            #fff7fa 45%,
            #f7dce6
        );

    border: 1px solid #f0d2dc;

    box-shadow:
        0 12px 35px rgba(118, 51, 78, 0.10);
}


/* Decorative nail-style circles */

.hero::before {
    content: "♡";
    position: absolute;

    left: 8%;
    top: 28%;

    font-family: serif;

    font-size: 90px;

    color: rgba(192, 75, 120, 0.12);

    transform: rotate(-15deg);
}


.hero::after {
    content: "✧";
    position: absolute;

    right: 12%;
    bottom: 25%;

    font-size: 80px;

    color: rgba(192, 75, 120, 0.15);
}


/* Hero content */

.hero-content {
    position: relative;
    z-index: 2;

    max-width: 750px;
}


.hero-label {
    color: var(--pink);

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 5px;

    margin-bottom: 13px;
}


.hero-title {
    font-family: "Playfair Display", serif;

    font-size: 56px;

    line-height: 1.03;

    font-weight: 700;

    color: #472936;
}


.hero-title span {
    color: var(--pink);
}


.hero-description {
    color: #756772;

    font-size: 15px;

    line-height: 1.6;

    max-width: 600px;

    margin: 14px auto;
}


.hero-features {
    color: #8e3f60;

    font-size: 14px;

    font-weight: 700;

    margin-top: 18px;
}


/* ============================================================
   SECTION HEADER
   ============================================================ */

.collection-header {
    text-align: center;

    margin-top: 18px;

    margin-bottom: 15px;
}


.collection-title {
    font-family: "Playfair Display", serif;

    color: #38232e;

    font-size: 38px;

    font-weight: 700;
}


.collection-subtitle {
    color: var(--muted);

    font-size: 14px;

    margin-top: 2px;
}


/* ============================================================
   CATEGORY PILLS
   ============================================================ */

.category-bar {
    display: flex;

    justify-content: center;

    gap: 0;

    margin: 15px auto 22px;

    max-width: 450px;

    overflow: hidden;

    border: 1px solid #ead5df;

    border-radius: 30px;

    background: white;
}


.category {
    flex: 1;

    text-align: center;

    padding: 8px 13px;

    color: #734d5e;

    font-size: 12px;

    font-weight: 600;
}


.category.active {
    color: white;

    background:
        linear-gradient(
            135deg,
            #cf5985,
            #a63d65
        );

    border-radius: 25px;

    box-shadow:
        0 4px 12px rgba(192, 75, 120, 0.25);
}


/* ============================================================
   PRODUCT CARD
   ============================================================ */

.product-card {

    position: relative;

    display: flex;

    gap: 16px;

    min-height: 175px;

    padding: 14px;

    margin-bottom: 18px;

    border-radius: 15px;

    background:
        linear-gradient(
            135deg,
            #ffffff,
            #fffafb
        );

    border: 1px solid #efd9c0;

    box-shadow:
        0 5px 18px rgba(80, 40, 55, 0.07);

    transition:
        transform 0.28s ease,
        box-shadow 0.28s ease,
        border-color 0.28s ease;
}


.product-card:hover {

    transform: translateY(-5px);

    border-color: #dca7bb;

    box-shadow:
        0 14px 32px rgba(176, 68, 107, 0.14);
}


/* Product image */

.product-image {

    width: 155px;

    min-width: 155px;

    height: 165px;

    object-fit: cover;

    border-radius: 12px;

    box-shadow:
        0 5px 14px rgba(70, 30, 50, 0.12);

    transition:
        transform 0.3s ease;
}


.product-card:hover .product-image {
    transform: scale(1.025);
}


/* Product content */

.product-content {

    flex: 1;

    display: flex;

    flex-direction: column;

    justify-content: space-between;

    padding: 2px 2px 2px 0;
}


.product-name {

    color: #38232e;

    font-family: "Playfair Display", serif;

    font-size: 18px;

    font-weight: 700;

    line-height: 1.2;

    padding-right: 20px;
}


.product-category {

    display: inline-block;

    margin-top: 7px;

    padding: 4px 9px;

    border-radius: 20px;

    color: #93405f;

    background: #fce5ed;

    font-size: 10px;

    font-weight: 700;
}


.product-price {

    color: #b4436c;

    font-family: "Playfair Display", serif;

    font-size: 17px;

    font-weight: 700;

    margin-top: 7px;
}


.product-description {

    color: #766873;

    font-size: 12px;

    line-height: 1.5;

    margin-top: 4px;
}


/* Heart */

.heart {

    position: absolute;

    top: 12px;

    right: 14px;

    color: #d94d7e;

    font-size: 22px;

    transition:
        transform 0.25s ease;
}


.product-card:hover .heart {
    transform: scale(1.15);
}


/* ============================================================
   PREMIUM ORDER BUTTON
   ============================================================ */

.order-button {

    display: inline-flex;

    align-items: center;

    justify-content: center;

    gap: 7px;

    width: 185px;

    min-height: 37px;

    margin-top: 8px;

    padding: 8px 14px;

    border-radius: 22px;

    text-decoration: none;

    color: white !important;

    background:
        linear-gradient(
            135deg,
            #e64f88,
            #b53f6a
        );

    border: 1px solid rgba(255,255,255,0.35);

    font-size: 12px;

    font-weight: 700;

    box-shadow:
        0 6px 15px rgba(192, 75, 120, 0.24);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease;
}


.order-button:hover {

    transform:
        translateY(-3px)
        scale(1.02);

    background:
        linear-gradient(
            135deg,
            #ef5d96,
            #c44572
        );

    box-shadow:
        0 10px 25px rgba(192, 75, 120, 0.40),
        0 0 18px rgba(255, 105, 160, 0.25);

    color: white !important;
}


.order-button:active {

    transform:
        translateY(-1px)
        scale(0.98);
}


/* ============================================================
   WHY CHOOSE US
   ============================================================ */

.why-title {
    font-family: "Playfair Display", serif;

    font-size: 37px;

    color: #38232e;

    margin-top: 25px;
}


.why-subtitle {
    color: var(--muted);

    font-size: 14px;

    margin-bottom: 20px;
}


.feature-box {

    text-align: center;

    min-height: 150px;

    padding: 28px 18px;

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            #fff9fb,
            #ffffff
        );

    border: 1px solid #efdce3;

    box-shadow:
        0 5px 18px rgba(70, 35, 50, 0.05);

    transition:
        transform 0.28s ease,
        box-shadow 0.28s ease;
}


.feature-box:hover {

    transform: translateY(-5px);

    box-shadow:
        0 12px 28px rgba(176, 68, 107, 0.12);
}


.feature-icon {
    font-size: 30px;

    margin-bottom: 9px;
}


.feature-title {
    color: #38232e;

    font-size: 16px;

    font-weight: 700;
}


.feature-description {
    color: var(--muted);

    font-size: 12px;

    line-height: 1.5;

    margin-top: 7px;
}


/* ============================================================
   CTA
   ============================================================ */

.cta {

    position: relative;

    overflow: hidden;

    text-align: center;

    margin-top: 32px;

    padding: 28px 20px;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            #302127,
            #603d4c
        );

    border: 1px solid #d29b62;

    box-shadow:
        0 8px 25px rgba(60, 30, 45, 0.15);
}


.cta::before {
    content: "❧";

    position: absolute;

    left: 35px;

    bottom: -15px;

    font-size: 70px;

    color: rgba(255,255,255,0.25);
}


.cta::after {
    content: "❧";

    position: absolute;

    right: 35px;

    bottom: -15px;

    font-size: 70px;

    color: rgba(255,255,255,0.25);

    transform: scaleX(-1);
}


.cta-title {

    position: relative;

    z-index: 2;

    color: white;

    font-family: "Playfair Display", serif;

    font-size: 30px;

    font-weight: 700;
}


.cta-description {

    position: relative;

    z-index: 2;

    color: #f3e5eb;

    font-size: 13px;

    margin-top: 5px;
}


/* ============================================================
   BOTTOM BUTTONS
   ============================================================ */

.bottom-buttons {

    display: flex;

    justify-content: center;

    gap: 18px;

    margin-top: 10px;
}


.bottom-button {

    display: flex;

    align-items: center;

    justify-content: center;

    width: 290px;

    min-height: 43px;

    border-radius: 25px;

    border: 1px solid #d98ba8;

    text-decoration: none;

    color: #71394f !important;

    background: white;

    font-size: 13px;

    font-weight: 600;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease;
}


.bottom-button.primary {

    color: white !important;

    background:
        linear-gradient(
            135deg,
            #e94f89,
            #b63e6b
        );

    border-color: #e94f89;

    box-shadow:
        0 7px 18px rgba(192,75,120,0.25);
}


.bottom-button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 9px 22px rgba(176,68,107,0.20);
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align: center;

    color: #9b8992;

    font-size: 11px;

    margin-top: 25px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 800px) {

    .hero {
        min-height: 300px;

        padding: 45px 20px;
    }

    .hero-title {
        font-size: 43px;
    }

    .hero-label {
        font-size: 10px;

        letter-spacing: 3px;
    }

    .hero-features {
        line-height: 2;
    }

    .product-card {
        min-height: 150px;
    }

    .product-image {
        width: 115px;

        min-width: 115px;

        height: 145px;
    }

    .product-name {
        font-size: 16px;
    }

    .product-description {
        font-size: 11px;
    }

    .order-button {
        width: 160px;

        font-size: 11px;
    }

    .bottom-buttons {
        flex-direction: column;

        align-items: center;

        gap: 8px;
    }

    .bottom-button {
        width: 100%;
    }
}

</style>
"""
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
<div class="hero">

    <div class="hero-content">

        <div class="hero-label">
            ELEGANT • STYLISH • MADE FOR YOU
        </div>

        <div class="hero-title">
            Beautiful Nails.<br>
            <span>Your Style.</span>
        </div>

        <div class="hero-description">
            Discover our curated collection of elegant nail designs,
            created to add a beautiful finishing touch to every look.
        </div>

        <div class="hero-features">
            ✦ Stylish Designs
            &nbsp;&nbsp;&nbsp;&nbsp;
            💎 Premium Look
            &nbsp;&nbsp;&nbsp;&nbsp;
            ♥ Affordable Prices
        </div>

    </div>

</div>
"""
)


# ============================================================
# COLLECTION HEADER
# ============================================================

st.html(
    """
<div class="collection-header">

    <div class="collection-title">
        Our Nail Collection
    </div>

    <div class="collection-subtitle">
        Find the design that matches your mood, outfit and occasion.
    </div>

</div>

<div class="category-bar">

    <div class="category active">
        All
    </div>

    <div class="category">
        Classic
    </div>

    <div class="category">
        Floral
    </div>

    <div class="category">
        French
    </div>

    <div class="category">
        Cute
    </div>

</div>
"""
)


# ============================================================
# PRODUCT CARDS
# ============================================================

columns = st.columns(3, gap="small")


for index, product in enumerate(PRODUCTS):

    image_path = IMAGE_DIR / product["image"]

    image_base64 = image_to_base64(image_path)

    order_text = quote(
        f"Hello {STORE_NAME}! "
        f"I would like to order {product['name']} "
        f"for PKR {product['price']:,}. "
        f"Please share the order details."
    )

    card_html = f"""
<div class="product-card">

    <img
        class="product-image"
        src="{image_base64}"
        alt="{product['name']}"
    >

    <div class="product-content">

        <div>

            <div class="product-name">
                {product['name']}
            </div>

            <span class="product-category">
                {product['category']}
            </span>

            <div class="product-price">
                PKR {product['price']:,}
            </div>

            <div class="product-description">
                {product['description']}
            </div>

        </div>

        <a
            class="order-button"
            href="https://wa.me/{WHATSAPP}?text={order_text}"
            target="_blank"
        >
            ◉ &nbsp; Order This Design &nbsp; →
        </a>

    </div>

    <div class="heart">
        ♡
    </div>

</div>
"""

    with columns[index % 3]:
        st.html(card_html)


# ============================================================
# WHY CHOOSE US
# ============================================================

st.html(
    """
<div style="text-align:center; margin-top:20px;">

    <div class="why-title">
        Why Choose Us?
    </div>

    <div class="why-subtitle">
        Simple, stylish and made for a beautiful experience.
    </div>

</div>
"""
)


features = [
    (
        "✨",
        "Beautiful Designs",
        "Carefully selected styles for classic, cute and modern looks.",
    ),
    (
        "💎",
        "Premium Look",
        "Elegant designs that make your hands stand out.",
    ),
    (
        "💗",
        "Affordable",
        "Stylish nail art at prices that are easy to love.",
    ),
]


feature_columns = st.columns(3, gap="small")


for column, feature in zip(feature_columns, features):

    icon, title, description = feature

    with column:

        st.html(
            f"""
<div class="feature-box">

    <div class="feature-icon">
        {icon}
    </div>

    <div class="feature-title">
        {title}
    </div>

    <div class="feature-description">
        {description}
    </div>

</div>
"""
        )


# ============================================================
# CTA
# ============================================================

st.html(
    """
<div class="cta">

    <div class="cta-title">
        Ready to Find Your Favorite?
    </div>

    <div class="cta-description">
        Place your order or contact us for more details.
    </div>

</div>
"""
)


# ============================================================
# BOTTOM BUTTONS
# ============================================================

general_message = quote(
    "Hello Nails Collection! "
    "I would like to place an order. "
    "Please share the available designs and details."
)


st.html(
    f"""
<div class="bottom-buttons">

    <a
        class="bottom-button primary"
        href="https://wa.me/{WHATSAPP}?text={general_message}"
        target="_blank"
    >
        ◉ &nbsp; Order on WhatsApp &nbsp; →
    </a>

    <a
        class="bottom-button"
        href="tel:{PHONE}"
    >
        ☎ &nbsp; Contact Us · {PHONE}
    </a>

</div>
"""
)


# ============================================================
# FOOTER
# ============================================================

st.html(
    f"""
<div class="footer">

    © 2026 {STORE_NAME}
    · Beautiful nails, beautiful style 💅

</div>
"""
)
