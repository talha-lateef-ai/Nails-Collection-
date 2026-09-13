import streamlit as st
from pathlib import Path
from urllib.parse import quote

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Nails Collection | Beautiful Nails, Your Style",
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
# IMAGE PATH
# ============================================================

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* Hide Streamlit branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ============================================================
   HERO
   ============================================================ */

.hero {
    padding: 60px 25px 50px;
    text-align: center;
    border-radius: 30px;
    background: linear-gradient(
        135deg,
        #fff2f6 0%,
        #ffffff 50%,
        #f7f1ff 100%
    );
    border: 1px solid #f1dfe6;
    margin-bottom: 45px;
}

.eyebrow {
    color: #ad456c;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(44px, 6vw, 74px);
    line-height: 1.05;
    margin: 0;
    color: #281d23;
}

.hero h1 span {
    color: #b24b70;
}

.hero p {
    max-width: 700px;
    margin: 22px auto 0;
    color: #70636a;
    font-size: 18px;
    line-height: 1.7;
}

.trust-row {
    display: flex;
    justify-content: center;
    gap: 35px;
    flex-wrap: wrap;
    margin-top: 28px;
    color: #5e5158;
    font-size: 14px;
    font-weight: 600;
}

/* ============================================================
   SECTION TITLES
   ============================================================ */

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    color: #2a2026;
    margin: 10px 0 5px;
}

.section-subtitle {
    color: #776a72;
    font-size: 16px;
    margin-bottom: 25px;
}

/* ============================================================
   PRODUCT
   ============================================================ */

.product-card {
    background: #ffffff;
    border: 1px solid #eee2e7;
    border-radius: 22px;
    padding: 12px;
    margin-bottom: 25px;
    box-shadow: 0 8px 28px rgba(50, 30, 40, 0.07);
}

.product-name {
    font-family: 'Playfair Display', serif;
    font-size: 21px;
    font-weight: 700;
    color: #2b2026;
    margin-top: 14px;
}

.badge {
    display: inline-block;
    padding: 5px 10px;
    margin-left: 6px;
    border-radius: 50px;
    background: #fff0f4;
    color: #a04468;
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 700;
    vertical-align: middle;
}

.price {
    color: #a43f64;
    font-size: 21px;
    font-weight: 700;
    margin: 8px 0;
}

.product-description {
    color: #756970;
    font-size: 14px;
    line-height: 1.6;
    min-height: 45px;
    margin-bottom: 15px;
}

/* ============================================================
   FEATURE BOXES
   ============================================================ */

.feature-box {
    text-align: center;
    padding: 28px 18px;
    border-radius: 20px;
    background: #fff9fb;
    border: 1px solid #f1e2e7;
    min-height: 160px;
}

.feature-icon {
    font-size: 32px;
    margin-bottom: 10px;
}

.feature-title {
    font-size: 17px;
    font-weight: 700;
    color: #2d2328;
    margin-bottom: 7px;
}

.feature-text {
    color: #776b72;
    font-size: 13px;
    line-height: 1.55;
}

/* ============================================================
   CTA
   ============================================================ */

.contact-panel {
    margin-top: 40px;
    padding: 42px 25px;
    border-radius: 28px;
    text-align: center;
    background: linear-gradient(
        135deg,
        #2a2026,
        #503945
    );
    color: white;
}

.contact-panel h2 {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    margin: 0 0 10px;
}

.contact-panel p {
    color: #eee1e8;
    font-size: 16px;
    margin: 0;
}

/* ============================================================
   BUTTONS
   ============================================================ */

div[data-testid="stLinkButton"] > a {
    border-radius: 12px !important;
    min-height: 45px !important;
    font-weight: 700 !important;
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    color: #897b83;
    font-size: 13px;
    padding: 32px 0 5px;
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .hero {
        padding: 42px 18px;
        border-radius: 22px;
    }

    .hero p {
        font-size: 16px;
    }

    .trust-row {
        gap: 15px;
    }

    .section-title {
        font-size: 31px;
    }

}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
<div class="hero">
    <div class="eyebrow">Elegant • Stylish • Made for You</div>

    <h1>
        Beautiful Nails.<br>
        <span>Your Style.</span>
    </h1>

    <p>
        Discover our curated collection of elegant nail designs,
        created to add a beautiful finishing touch to every look.
    </p>

    <div class="trust-row">
        <span>✨ Stylish Designs</span>
        <span>💎 Premium Look</span>
        <span>💗 Affordable Prices</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# COLLECTION HEADER
# ============================================================

st.markdown(
    '<div class="section-title">Our Nail Collection</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">Find the design that matches your mood, outfit and occasion.</div>',
    unsafe_allow_html=True,
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
# PRODUCT GRID
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
                f"Image not found: {product['image']}"
            )

        # Product name
        st.markdown(
            f"""
<div class="product-name">
    {product['name']}
    <span class="badge">{product['category']}</span>
</div>
""",
            unsafe_allow_html=True,
        )

        # Price
        st.markdown(
            f"""
<div class="price">
    PKR {product['price']:,}
</div>
""",
            unsafe_allow_html=True,
        )

        # Description
        st.markdown(
            f"""
<div class="product-description">
    {product['description']}
</div>
""",
            unsafe_allow_html=True,
        )

        # WhatsApp order
        message = quote(
            f"Hello {STORE_NAME}! "
            f"I would like to order "
            f"{product['name']} "
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

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Why Choose Us?</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-subtitle">Simple, stylish and made for a beautiful experience.</div>',
    unsafe_allow_html=True,
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

feature_columns = st.columns(3)

for column, feature in zip(feature_columns, features):

    icon, title, description = feature

    with column:

        feature_html = f"""
<div class="feature-box">
    <div class="feature-icon">{icon}</div>
    <div class="feature-title">{title}</div>
    <div class="feature-text">{description}</div>
</div>
"""

        st.markdown(
            feature_html,
            unsafe_allow_html=True,
        )

# ============================================================
# CONTACT / CTA
# ============================================================

st.markdown(
    """
<div class="contact-panel">
    <h2>Ready to Find Your Favorite?</h2>
    <p>Place your order or contact us for more details.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# WHATSAPP BUTTON
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

st.markdown(
    f"""
<div class="footer">
    © 2026 {STORE_NAME} · Beautiful nails, beautiful style 💅
</div>
""",
    unsafe_allow_html=True,
)
