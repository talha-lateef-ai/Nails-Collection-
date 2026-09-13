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
# IMAGE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"

# ============================================================
# CUSTOM CSS — PREMIUM THEME
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap');

html,
body,
[data-testid="stAppViewContainer"] {
    font-family: 'DM Sans', sans-serif;
    background: #fffdfb;
}

.block-container {
    max-width: 1180px;
    padding-top: 30px;
    padding-bottom: 50px;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ============================================================
   HERO
   ============================================================ */

.hero-box {
    text-align: center;
    padding: 64px 30px;
    margin-bottom: 45px;
    border-radius: 30px;
    background: linear-gradient(135deg, #fdf1f5, #ffffff 45%, #f6f0fb);
    border: 1px solid #f0dfe6;
    box-shadow: 0 18px 40px -20px rgba(160, 68, 104, 0.25);
    position: relative;
    overflow: hidden;
}

.hero-small {
    color: #b0446b;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 65px;
    font-weight: 700;
    line-height: 1.05;
    color: #2b2026;
    margin-top: 16px;
}

.hero-title span {
    background: linear-gradient(120deg, #b0446b, #cc8a4a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-description {
    max-width: 700px;
    margin: 20px auto;
    color: #70636a;
    font-size: 18px;
    line-height: 1.7;
}

.hero-features {
    margin-top: 28px;
    color: #5d5057;
    font-weight: 600;
    letter-spacing: 0.3px;
}

/* ============================================================
   SECTION
   ============================================================ */

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 700;
    color: #2b2026;
    margin-bottom: 5px;
}

.section-text {
    color: #776a72;
    font-size: 16px;
    margin-bottom: 25px;
}

/* ============================================================
   PRODUCT CARDS
   ============================================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 22px !important;
    border: 1px solid #f0e2e7 !important;
    background: #ffffff;
    padding: 6px;
    box-shadow: 0 10px 28px -18px rgba(60, 30, 45, 0.35);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 38px -18px rgba(160, 68, 104, 0.35);
}

div[data-testid="stImage"] img {
    border-radius: 16px;
}

.product-name {
    font-family: 'Playfair Display', serif;
    font-size: 21px;
    font-weight: 700;
    color: #2b2026;
    margin-top: 14px;
}

.product-category {
    display: inline-block;
    background: linear-gradient(120deg, #fff0f4, #fdf3e6);
    color: #a04468;
    border: 1px solid #f2d9e2;
    border-radius: 30px;
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.4px;
    margin-left: 6px;
}

.product-price {
    color: #a43f64;
    font-size: 22px;
    font-weight: 800;
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
   WHY CHOOSE US
   ============================================================ */

.feature-box {
    text-align: center;
    padding: 30px 18px;
    min-height: 155px;
    border-radius: 20px;
    background: #fffaf9;
    border: 1px solid #f1e2e7;
    box-shadow: 0 8px 22px -16px rgba(60, 30, 45, 0.3);
    transition: transform 0.2s ease;
}

.feature-box:hover {
    transform: translateY(-3px);
}

.feature-icon {
    font-size: 34px;
    margin-bottom: 8px;
}

.feature-title {
    font-size: 17px;
    font-weight: 700;
    color: #2d2328;
}

.feature-description {
    color: #776b72;
    font-size: 13px;
    line-height: 1.5;
    margin-top: 7px;
}

/* ============================================================
   CTA
   ============================================================ */

.cta-box {
    text-align: center;
    margin-top: 45px;
    margin-bottom: 18px;
    padding: 46px 25px;
    border-radius: 28px;
    background: linear-gradient(135deg, #2a2026, #503945);
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 22px 44px -20px rgba(0, 0, 0, 0.45);
}

.cta-title {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 700;
    color: white;
}

.cta-description {
    color: #eee1e8;
    font-size: 16px;
    margin-top: 8px;
}

/* ============================================================
   BUTTONS
   ============================================================ */

div[data-testid="stLinkButton"] {
    margin-top: 8px;
    margin-bottom: 8px;
}

div[data-testid="stLinkButton"] > a {
    border-radius: 12px !important;
    min-height: 46px !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

div[data-testid="stLinkButton"] > a:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 22px -10px rgba(160, 68, 104, 0.55);
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer-text {
    text-align: center;
    color: #897b83;
    font-size: 13px;
    margin-top: 35px;
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {
    .hero-box { padding: 42px 18px; }
    .hero-title { font-size: 45px; }
    .hero-description { font-size: 16px; }
    .section-heading { font-size: 31px; }
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
<div class="hero-box">
    <div class="hero-small">
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
""",
    unsafe_allow_html=True,
)

# ============================================================
# COLLECTION HEADER
# ============================================================

st.markdown(
    '<div class="section-heading">Our Nail Collection</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-text">Find the design that matches your mood, outfit and occasion.</div>',
    unsafe_allow_html=True,
)

# ============================================================
# CATEGORY FILTER
# ============================================================

categories = ["All"] + sorted(
    {product["category"] for product in PRODUCTS}
)

# st.segmented_control requires Streamlit >= 1.32. If you're on an
# older version this line will raise an AttributeError — upgrade with
# `pip install --upgrade streamlit` if that happens.
selected_category = st.segmented_control(
    "Browse by style",
    categories,
    default="All",
    label_visibility="collapsed",
)

# segmented_control returns None if the user deselects everything —
# fall back to "All" instead of showing an empty page.
if not selected_category:
    selected_category = "All"

if selected_category == "All":
    filtered_products = PRODUCTS
else:
    filtered_products = [
        product
        for product in PRODUCTS
        if product["category"] == selected_category
    ]

# ============================================================
# PRODUCT COLLECTION
# ============================================================

if not filtered_products:
    st.info("No designs found in this category yet.")
else:
    columns = st.columns(3, gap="large")

    for index, product in enumerate(filtered_products):

        with columns[index % 3]:

            # Bordered container = the "premium card" wrapper
            with st.container(border=True):

                # Product image
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
    <span class="product-category">
        {product['category']}
    </span>
</div>
""",
                    unsafe_allow_html=True,
                )

                # Price
                st.markdown(
                    f"""
<div class="product-price">
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

                # WhatsApp message
                order_message = quote(
                    f"Hello {STORE_NAME}! "
                    f"I would like to order "
                    f"{product['name']} "
                    f"for PKR {product['price']:,}. "
                    f"Please share the order details."
                )

                # Order button — unique key avoids duplicate-widget
                # errors if products ever share the same name.
                st.link_button(
                    "🛍️ Order This Design",
                    f"https://wa.me/{WHATSAPP_NUMBER}?text={order_message}",
                    use_container_width=True,
                )

# ============================================================
# WHY CHOOSE US
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="section-heading">Why Choose Us?</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-text">Simple, stylish and made for a beautiful experience.</div>',
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

feature_columns = st.columns(3, gap="large")

for column, feature in zip(feature_columns, features):

    icon, title, description = feature

    with column:

        st.markdown(
            f"""
<div class="feature-box">
    <div class="feature-icon">{icon}</div>

    <div class="feature-title">
        {title}
    </div>

    <div class="feature-description">
        {description}
    </div>
</div>
""",
            unsafe_allow_html=True,
        )

# ============================================================
# CALL TO ACTION
# ============================================================

st.markdown(
    """
<div class="cta-box">
    <div class="cta-title">
        Ready to Find Your Favorite?
    </div>

    <div class="cta-description">
        Place your order or contact us for more details.
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Extra spacing
st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

# ============================================================
# GENERAL WHATSAPP ORDER
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
# CONTACT
# ============================================================

st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

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
<div class="footer-text">
    © 2026 {STORE_NAME}
    · Beautiful nails, beautiful style 💅
</div>
""",
    unsafe_allow_html=True,
)
