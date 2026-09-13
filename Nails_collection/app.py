import streamlit as st
from pathlib import Path
from urllib.parse import quote

# ============================================================
# Nails Collection — Professional Streamlit Website
# ============================================================

st.set_page_config(
    page_title="Nails Collection | Beautiful Nails, Your Style",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------- Store Info -----------------------------

STORE_NAME = "Nails Collection"
PHONE = "+92 3289718577"
WHATSAPP_NUMBER = "923289718577"

# ----------------------------- Products -----------------------------

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

# ----------------------------- Paths -----------------------------

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"

# ----------------------------- Custom CSS -----------------------------

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

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* ---------- Hero ---------- */

    .hero {
        padding: 55px 25px 45px;
        text-align: center;
        border-radius: 28px;
        background: linear-gradient(
            135deg,
            #fff4f7 0%,
            #ffffff 48%,
            #f8f3ff 100%
        );
        border: 1px solid #f3e3e9;
        margin-bottom: 35px;
    }

    .eyebrow {
        color: #b14d72;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: clamp(42px, 6vw, 72px);
        line-height: 1.05;
        margin: 0;
        color: #251b22;
    }

    .hero h1 span {
        color: #b14d72;
    }

    .hero p {
        max-width: 680px;
        margin: 18px auto 0;
        color: #6f6269;
        font-size: 18px;
        line-height: 1.7;
    }

    .trust-row {
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
        margin-top: 26px;
        color: #5f5159;
        font-size: 14px;
        font-weight: 600;
    }

    /* ---------- Section ---------- */

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 36px;
        color: #2a2026;
        margin: 12px 0 4px;
    }

    .section-subtitle {
        color: #776b72;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* ---------- Product Card ---------- */

    .card {
        background: #ffffff;
        border: 1px solid #eee4e8;
        border-radius: 20px;
        padding: 12px 12px 18px;
        margin-bottom: 24px;
        box-shadow: 0 8px 25px rgba(46, 27, 37, 0.06);
    }

    .product-name {
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: 700;
        color: #2b2026;
        margin: 14px 4px 5px;
    }

    .badge {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        background: #fff0f4;
        color: #a04468;
        font-size: 12px;
        font-weight: 700;
        margin-left: 4px;
    }

    .product-description {
        color: #74686f;
        line-height: 1.55;
        min-height: 48px;
        margin: 0 4px 8px;
        font-size: 14px;
    }

    .price {
        color: #a63f65;
        font-size: 21px;
        font-weight: 700;
        margin: 7px 4px 14px;
    }

    /* ---------- Feature Boxes ---------- */

    .feature-box {
        text-align: center;
        padding: 25px 16px;
        border-radius: 18px;
        background: #fff9fb;
        border: 1px solid #f1e4e8;
        min-height: 145px;
    }

    .feature-icon {
        font-size: 30px;
        margin-bottom: 8px;
    }

    .feature-title {
        font-weight: 700;
        color: #2d2328;
        margin-bottom: 5px;
    }

    .feature-text {
        color: #776b72;
        font-size: 13px;
        line-height: 1.5;
    }

    /* ---------- Contact ---------- */

    .contact-panel {
        margin-top: 35px;
        padding: 35px 25px;
        border-radius: 25px;
        text-align: center;
        background: linear-gradient(
            135deg,
            #2a2026,
            #4a3540
        );
        color: white;
    }

    .contact-panel h2 {
        font-family: 'Playfair Display', serif;
        font-size: 34px;
        margin: 0 0 8px;
    }

    .contact-panel p {
        color: #eee2e8;
        margin-bottom: 20px;
    }

    /* ---------- Footer ---------- */

    .footer {
        text-align: center;
        color: #897c83;
        font-size: 13px;
        padding: 30px 0 5px;
    }

    /* ---------- Buttons ---------- */

    div.stButton > button,
    div[data-testid="stLinkButton"] > a {
        border-radius: 12px !important;
        min-height: 45px !important;
        font-weight: 700 !important;
        border: 1px solid #e6cbd5 !important;
    }

    @media (max-width: 700px) {

        .hero {
            padding: 38px 16px;
        }

        .hero p {
            font-size: 16px;
        }

        .section-title {
            font-size: 30px;
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

        <div class="eyebrow">
            Elegant • Stylish • Made for You
        </div>

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
# COLLECTION
# ============================================================

st.markdown(
    '<div class="section-title">Our Nail Collection</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-subtitle">
        Find the design that matches your mood, outfit and occasion.
    </div>
    """,
    unsafe_allow_html=True,
)

# Categories

categories = ["All"] + sorted(
    {product["category"] for product in PRODUCTS}
)

selected_category = st.segmented_control(
    "Browse by style",
    categories,
    default="All",
    label_visibility="collapsed",
)

# Filter products

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

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True,
        )

        # Image

        image_path = IMAGE_DIR / product["image"]

        if image_path.exists():

            st.image(
                str(image_path),
                use_container_width=True,
            )

        else:

            st.warning(
                f"Image not found: {product['image']}"
            )

        # Product information

        st.markdown(
            f"""
            <div class="product-name">
                {product['name']}
                <span class="badge">
                    {product['category']}
                </span>
            </div>

            <div class="price">
                PKR {product['price']:,}
            </div>

            <div class="product-description">
                {product['description']}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # WhatsApp order message

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

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
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
    """
    <div class="section-subtitle">
        Simple, stylish and made for a beautiful experience.
    </div>
    """,
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

        st.markdown(
            f"""
            <div class="feature-box">

                <div class="feature-icon">
                    {icon}
                </div>

                <div class="feature-title">
                    {title}
                </div>

                <div class="feature-text">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# CONTACT / CTA
# ============================================================

st.markdown(
    """
    <div class="contact-panel">

        <h2>
            Ready to Find Your Favorite?
        </h2>

        <p>
            Place your order or contact us for more details.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)

# WhatsApp

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

# Phone

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
        © 2026 {STORE_NAME}
        · Beautiful nails, beautiful style 💅
    </div>
    """,
    unsafe_allow_html=True,
)
