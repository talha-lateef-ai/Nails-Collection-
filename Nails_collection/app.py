import streamlit as st
from pathlib import Path
from urllib.parse import quote


# ============================================================
# PAGE CONFIGURATION
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

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# GLOBAL DESIGN / CSS
# ============================================================

st.html(
    """
<style>

@import url(
    'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap'
);


/* ============================================================
   VARIABLES
   ============================================================ */

:root {
    --rose: #b0446b;
    --rose-dark: #963957;
    --rose-light: #fff3f7;
    --rose-border: #e2b4c4;

    --dark: #2b2026;
    --muted: #756970;

    --gold: #c79a62;

    --border: #eee1e7;
}


/* ============================================================
   GENERAL PAGE
   ============================================================ */

html,
body,
[data-testid="stAppViewContainer"] {
    font-family: "DM Sans", sans-serif;
}

.block-container {
    max-width: 1180px;
    padding-top: 30px;
    padding-bottom: 60px;
}


/* ============================================================
   HIDE STREAMLIT BRANDING
   ============================================================ */

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

    text-align: center;

    padding: 70px 30px;

    margin-bottom: 55px;

    border-radius: 32px;

    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(255, 214, 227, 0.45),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 80%,
            rgba(230, 213, 245, 0.40),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #fff4f7,
            #ffffff 50%,
            #f8f2ff
        );

    border: 1px solid #efdce4;

    box-shadow:
        0 20px 60px rgba(95, 45, 65, 0.08);
}


.hero-label {
    color: var(--rose);

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
    color: var(--rose);
}


.hero-description {
    max-width: 720px;

    margin: 24px auto 0;

    color: var(--muted);

    font-size: 18px;

    line-height: 1.7;
}


.hero-features {
    margin-top: 30px;

    color: #5f5259;

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
    color: var(--muted);

    font-size: 16px;

    margin-bottom: 25px;
}


/* ============================================================
   PRODUCT IMAGE
   ============================================================ */

[data-testid="stImage"] img {
    border-radius: 18px;

    transition:
        transform 0.35s ease,
        box-shadow 0.35s ease;

    box-shadow:
        0 8px 25px rgba(70, 35, 50, 0.08);
}


[data-testid="stImage"] img:hover {
    transform: translateY(-4px);

    box-shadow:
        0 14px 35px rgba(176, 68, 107, 0.15);
}


/* ============================================================
   PRODUCT INFORMATION
   ============================================================ */

.product-name {
    font-family: "Playfair Display", serif;

    color: var(--dark);

    font-size: 21px;

    font-weight: 700;

    margin-top: 14px;
}


.product-category {
    display: inline-block;

    margin-left: 7px;

    padding: 4px 10px;

    border-radius: 30px;

    background: #fff0f4;

    color: var(--rose);

    font-family: "DM Sans", sans-serif;

    font-size: 10px;

    font-weight: 700;

    letter-spacing: 0.5px;

    vertical-align: middle;
}


.product-price {
    color: var(--rose);

    font-size: 21px;

    font-weight: 700;

    margin-top: 7px;
}


.product-description {
    color: var(--muted);

    font-size: 14px;

    line-height: 1.6;

    min-height: 46px;

    margin-top: 5px;

    margin-bottom: 13px;
}


/* ============================================================
   PREMIUM ORDER BUTTON
   ============================================================ */

div[data-testid="stLinkButton"] a {

    position: relative !important;

    display: flex !important;

    align-items: center !important;

    justify-content: center !important;

    min-height: 48px !important;

    padding: 10px 18px !important;

    border-radius: 14px !important;

    border: 1px solid var(--rose-border) !important;

    background:
        linear-gradient(
            135deg,
            #ffffff 0%,
            #fff5f8 100%
        ) !important;

    color: var(--rose-dark) !important;

    font-family: "DM Sans", sans-serif !important;

    font-size: 14px !important;

    font-weight: 700 !important;

    letter-spacing: 0.2px !important;

    box-shadow:
        0 5px 15px rgba(176, 68, 107, 0.08),
        inset 0 1px 0 rgba(255,255,255,0.9) !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease,
        background 0.25s ease !important;

    text-decoration: none !important;
}


/* Cursor hover */

div[data-testid="stLinkButton"] a:hover {

    transform: translateY(-3px) !important;

    border-color: #b0446b !important;

    background:
        linear-gradient(
            135deg,
            #fffafd 0%,
            #ffe8f0 100%
        ) !important;

    color: #963957 !important;

    box-shadow:
        0 10px 25px rgba(176, 68, 107, 0.18),
        0 0 0 3px rgba(176, 68, 107, 0.055),
        inset 0 1px 0 rgba(255,255,255,1) !important;
}


/* Click effect */

div[data-testid="stLinkButton"] a:active {

    transform:
        translateY(-1px)
        scale(0.985) !important;

    box-shadow:
        0 5px 12px rgba(176, 68, 107, 0.14) !important;
}


/* ============================================================
   WHY CHOOSE US
   ============================================================ */

.feature-box {

    text-align: center;

    padding: 32px 20px;

    min-height: 165px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            #ffffff,
            #fff8fb
        );

    border: 1px solid #f0dfe6;

    box-shadow:
        0 8px 25px rgba(80, 40, 55, 0.05);

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease,
        border-color 0.3s ease;
}


.feature-box:hover {

    transform: translateY(-5px);

    border-color: #e2b4c4;

    box-shadow:
        0 15px 35px rgba(176, 68, 107, 0.10);
}


.feature-icon {

    font-size: 34px;

    margin-bottom: 11px;
}


.feature-title {

    color: var(--dark);

    font-size: 17px;

    font-weight: 700;
}


.feature-description {

    color: var(--muted);

    font-size: 13px;

    line-height: 1.55;

    margin-top: 8px;
}


/* ============================================================
   CTA
   ============================================================ */

.cta {

    text-align: center;

    margin-top: 60px;

    margin-bottom: 25px;

    padding: 52px 25px;

    border-radius: 30px;

    background:
        radial-gradient(
            circle at 20% 30%,
            rgba(210, 155, 175, 0.15),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #291f25,
            #503945
        );

    box-shadow:
        0 18px 45px rgba(45, 25, 35, 0.15);
}


.cta-title {

    color: white;

    font-family: "Playfair Display", serif;

    font-size: 38px;

    font-weight: 700;
}


.cta-description {

    color: #eee1e8;

    font-size: 16px;

    margin-top: 10px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align: center;

    color: #897b83;

    font-size: 13px;

    margin-top: 40px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .hero {
        padding: 45px 18px;

        border-radius: 24px;
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
# HERO SECTION
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
        ✨ Stylish Designs
        &nbsp;&nbsp;&nbsp;
        💎 Premium Look
        &nbsp;&nbsp;&nbsp;
        💗 Affordable Prices
    </div>

</div>
"""
)


# ============================================================
# COLLECTION HEADER
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
# PRODUCT COLLECTION
# ============================================================

columns = st.columns(3, gap="large")


for index, product in enumerate(filtered_products):

    with columns[index % 3]:

        # ----------------------------------------------------
        # IMAGE
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # PRODUCT DETAILS
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # PRODUCT WHATSAPP ORDER
        # ----------------------------------------------------

        order_message = quote(
            f"Hello {STORE_NAME}! "
            f"I would like to order "
            f"{product['name']} "
            f"for PKR {product['price']:,}. "
            f"Please share the order details."
        )


        st.link_button(
            "🛍️  Order This Design",
            f"https://wa.me/{WHATSAPP_NUMBER}?text={order_message}",
            use_container_width=True,
        )


# ============================================================
# WHY CHOOSE US
# ============================================================

st.html(
    """
<div style="height:45px;"></div>

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


feature_columns = st.columns(
    3,
    gap="large",
)


for column, feature in zip(
    feature_columns,
    features,
):

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
# CTA SECTION
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
# GENERAL WHATSAPP ORDER
# ============================================================

general_message = quote(
    "Hello Nails Collection! "
    "I would like to place an order. "
    "Please share the available designs and details."
)


st.link_button(
    "🛍️  Order on WhatsApp",
    f"https://wa.me/{WHATSAPP_NUMBER}?text={general_message}",
    use_container_width=True,
)


# ============================================================
# CONTACT
# ============================================================

st.link_button(
    f"📞  Contact Us · {PHONE}",
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
