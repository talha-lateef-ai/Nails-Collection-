import streamlit as st
from pathlib import Path
from urllib.parse import quote

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Nails Collection",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# STORE INFORMATION
# ============================================================

STORE_NAME = "Nails Collection"
PHONE = "+92 3289718577"
WHATSAPP_NUMBER = "923289718577"

# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [
    {
        "name": "Red Glossy Elegance",
        "price": 1499,
        "image": "red_glossy.png",
        "category": "Classic",
        "description": "Elegant glossy red nails for a bold and timeless look.",
    },
    {
        "name": "Sunflower Bloom",
        "price": 1699,
        "image": "sunflower_nails.png",
        "category": "Floral",
        "description": "Fresh sunflower-inspired nail art with beautiful floral details.",
    },
    {
        "name": "Pastel Floral Art",
        "price": 1799,
        "image": "pastel_art.png",
        "category": "Floral",
        "description": "Soft pastel shades paired with delicate floral artwork.",
    },
    {
        "name": "Classic French Tips",
        "price": 1299,
        "image": "french_tips.png",
        "category": "French",
        "description": "Clean and timeless French tips for every occasion.",
    },
    {
        "name": "Pink Bow Nails",
        "price": 1599,
        "image": "pink_bows.png",
        "category": "Cute",
        "description": "Pretty pink nails finished with charming bow details.",
    },
    {
        "name": "Sky Blue French",
        "price": 1399,
        "image": "blue_french.png",
        "category": "French",
        "description": "Fresh sky-blue French tips for a modern elegant style.",
    },
]

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --pink: #b0446b;
    --dark: #2b2026;
    --muted: #756970;
    --light-pink: #fff3f7;
    --border: #eee1e7;
}

/* Hide Streamlit default elements */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main page */

.block-container {
    max-width: 1180px;
    padding-top: 30px;
    padding-bottom: 50px;
}

/* ============================================================
   HERO
   ============================================================ */

.hero {
    text-align: center;
    padding: 65px 25px;
    border-radius: 30px;
    background:
        linear-gradient(
            135deg,
            #fff1f6 0%,
            #ffffff 50%,
            #f7f0ff 100%
        );
    border: 1px solid #f0dfe6;
    margin-bottom: 50px;
}

.hero-label {
    color: var(--pink);
    font-family: "DM Sans", sans-serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 18px;
}

.hero-title {
    font-family: "Playfair Display", serif;
    font-size: 68px;
    line-height: 1.05;
    font-weight: 700;
    color: var(--dark);
}

.hero-title span {
    color: var(--pink);
}

.hero-description {
    max-width: 720px;
    margin: 22px auto 0;
    color: var(--muted);
    font-family: "DM Sans", sans-serif;
    font-size: 18px;
    line-height: 1.7;
}

.hero-features {
    margin-top: 28px;
    color: #5f5259;
    font-family: "DM Sans", sans-serif;
    font-size: 14px;
    font-weight: 600;
}

/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-title {
    font-family: "Playfair Display", serif;
    color: var(--dark);
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 5px;
}

.section-subtitle {
    font-family: "DM Sans", sans-serif;
    color: var(--muted);
    font-size: 16px;
    margin-bottom: 25px;
}

/* ============================================================
   PRODUCT INFORMATION
   ============================================================ */

.product-name {
    font-family: "Playfair Display", serif;
    color: var(--dark);
    font-size: 21px;
    font-weight: 700;
    margin-top: 12px;
}

.product-category {
    display: inline-block;
    margin-left: 7px;
    padding: 4px 9px;
    border-radius: 20px;
    background: #fff0f4;
    color: #a04468;
    font-family: "DM Sans", sans-serif;
    font-size: 11px;
    font-weight: 700;
    vertical-align: middle;
}

.product-price {
    color: #a43f64;
    font-family: "DM Sans", sans-serif;
    font-size: 21px;
    font-weight: 700;
    margin-top: 7px;
}

.product-description {
    color: var(--muted);
    font-family: "DM Sans", sans-serif;
    font-size: 14px;
    line-height: 1.6;
    min-height: 46px;
    margin-top: 5px;
    margin-bottom: 12px;
}

/* ============================================================
   WHY CHOOSE US
   ============================================================ */

.feature-box {
    text-align: center;
    padding: 30px 18px;
    min-height: 160px;
    border-radius: 20px;
    background: #fff9fb;
    border: 1px solid #f1e2e7;
}

.feature-icon {
    font-size: 32px;
    margin-bottom: 10px;
}

.feature-title {
    color: var(--dark);
    font-family: "DM Sans", sans-serif;
    font-size: 17px;
    font-weight: 700;
}

.feature-description {
    color: var(--muted);
    font-family: "DM Sans", sans-serif;
    font-size: 13px;
    line-height: 1.55;
    margin-top: 8px;
}

/* ============================================================
   CTA
   ============================================================ */

.cta {
    text-align: center;
    margin-top: 55px;
    margin-bottom: 20px;
    padding: 48px 25px;
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        #2a2026,
        #503945
    );
}

.cta-title {
    color: white;
    font-family: "Playfair Display", serif;
    font-size: 38px;
    font-weight: 700;
}

.cta-description {
    color: #eee1e8;
    font-family: "DM Sans", sans-serif;
    font-size: 16px;
    margin-top: 10px;
}

/* ============================================================
   BUTTONS
   ============================================================ */

div[data-testid="stLinkButton"] {
    margin-top: 8px;
    margin-bottom: 8px;
}

div[data-testid="stLinkButton"] a {
    border-radius: 12px !important;
    min-height: 48px !important;
    font-family: "DM Sans", sans-serif !important;
    font-weight: 700 !important;
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #897b83;
    font-family: "DM Sans", sans-serif;
    font-size: 13px;
    margin-top: 35px;
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .hero {
        padding: 45px 18px;
    }

    .hero-title {
        font-size: 45px;
    }

    .hero-description {
        font-size: 16px;
    }

    .hero-features {
        line-height: 2;
    }

    .section-title {
        font-size: 31px;
    }

    .cta-title {
        font-size: 30px;
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
        ✨ Stylish Designs&nbsp;&nbsp;&nbsp;
        💎 Premium Look&nbsp;&nbsp;&nbsp;
        💗 Affordable Prices
    </div>

</div>
"""
)

# ============================================================
# COLLECTION TITLE
# ============================================================

st.html(
    """
<div class="section-title">
    Our Nail Collection
</div>

<div class="section-subtitle">
    Find the design that matches your mood, outfit and occasion.
</div>
"""
)

# ============================================================
# CATEGORY FILTER
# ============================================================

categories = ["All"] + sorted(
    {product["category"] for product in PRODUCTS}
)

selected_category = st.segmented_control(
    "Browse by style",
    categories,
    default="All",
    label_visibility="collapsed",
)

if selected_category == "All":
    filtered_products = PRODUCTS
else:
    filtered_products = [
        product
        for product in PRODUCTS
        if product["category"] == selected_category
    ]

# ============================================================
# PRODUCTS
# ============================================================

columns = st.columns(3, gap="large")

for index, product in enumerate(filtered_products):

    with columns[index % 3]:

        # Image
        image_path = IMAGE_DIR / product["image"]

        if image_path.exists():
            st.image(
                str(image_path),
                use_container_width=True,
            )
        else:
            st.error(
                f"Image missing: {product['image']}"
            )

        # Product information
        st.html(
            f"""
<div class="product-name">
    {product["name"]}
    <span class="product-category">
        {product["category"]}
    </span>
</div>

<div class="product-price">
    PKR {product["price"]:,}
</div>

<div class="product-description">
    {product["description"]}
</div>
"""
        )

        # Product-specific WhatsApp message
        message = quote(
            f"Hello {STORE_NAME}! "
            f"I would like to order {product['name']} "
            f"for PKR {product['price']:,}. "
            f"Please share the order details."
        )

        st.link_button(
            "🛍️ Order This Design",
            f"https://wa.me/{WHATSAPP_NUMBER}?text={message}",
            use_container_width=True,
        )

# ============================================================
# WHY CHOOSE US
# ============================================================

st.html("<div style='height:35px'></div>")

st.html(
    """
<div class="section-title">
    Why Choose Us?
</div>

<div class="section-subtitle">
    Simple, stylish and made for a beautiful experience.
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

feature_columns = st.columns(3, gap="large")

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
# GENERAL WHATSAPP BUTTON
# ============================================================

general_message = quote(
    "Hello Nails Collection! "
    "I would like to place an order. "
    "Please share the available designs and details."
)

st.link_button(
    "🛍️ Order on WhatsApp",
    f"https://wa.me/{WHATSAPP_NUMBER}?text={general_message}",
    use_container_width=True,
)

# ============================================================
# CONTACT BUTTON
# ============================================================

st.link_button(
    f"📞 Contact Us · {PHONE}",
    f"tel:{PHONE}",
    use_container_width=True,
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
