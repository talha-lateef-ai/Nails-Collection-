import streamlit as st
from pathlib import Path
from urllib.parse import quote


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
# FAVORITES
# ============================================================

if "favorites" not in st.session_state:
    st.session_state.favorites = set()


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
# IMAGE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# CUSTOM CSS
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

.block-container {
    max-width: 1500px;
    padding-top: 12px;
    padding-bottom: 50px;
}

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
    text-align: center;
    padding: 58px 25px;
    margin-bottom: 22px;

    border-radius: 20px;

    background:
        radial-gradient(
            circle at 15% 50%,
            rgba(255, 215, 228, 0.9),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 25%,
            rgba(255, 225, 235, 0.9),
            transparent 30%
        ),
        linear-gradient(
            110deg,
            #f8dce5,
            #fff7fa 48%,
            #f7dce6
        );

    border: 1px solid #efd0da;

    box-shadow:
        0 12px 35px rgba(118, 51, 78, 0.10);
}

.hero-label {
    color: #b0446b;

    font-family: "DM Sans", sans-serif;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 5px;

    margin-bottom: 12px;
}

.hero-title {
    color: #472936;

    font-family: "Playfair Display", serif;

    font-size: 58px;

    line-height: 1.05;

    font-weight: 700;
}

.hero-title span {
    color: #c04b78;
}

.hero-description {
    max-width: 650px;

    margin: 16px auto;

    color: #756772;

    font-family: "DM Sans", sans-serif;

    font-size: 15px;

    line-height: 1.6;
}

.hero-features {
    color: #8e3f60;

    font-size: 14px;

    font-weight: 700;

    margin-top: 20px;
}


/* ============================================================
   SECTION
   ============================================================ */

.collection-header {
    text-align: center;

    margin-top: 18px;

    margin-bottom: 15px;
}

.collection-title {
    color: #38232e;

    font-family: "Playfair Display", serif;

    font-size: 38px;

    font-weight: 700;
}

.collection-subtitle {
    color: #766872;

    font-size: 14px;
}


/* ============================================================
   PRODUCT CARD
   ============================================================ */

.product-card {
    position: relative;

    padding: 12px;

    border-radius: 16px;

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


/* ============================================================
   PRODUCT IMAGE
   ============================================================ */

.product-image {
    width: 100%;

    height: 220px;

    object-fit: cover;

    border-radius: 13px;

    box-shadow:
        0 6px 18px rgba(70, 30, 50, 0.12);
}


/* ============================================================
   PRODUCT INFO
   ============================================================ */

.product-name {
    color: #38232e;

    font-family: "Playfair Display", serif;

    font-size: 19px;

    font-weight: 700;

    margin-top: 12px;
}

.product-category {
    display: inline-block;

    margin-top: 6px;

    padding: 4px 9px;

    border-radius: 20px;

    background: #fce5ed;

    color: #93405f;

    font-size: 10px;

    font-weight: 700;
}

.product-price {
    color: #b4436c;

    font-family: "Playfair Display", serif;

    font-size: 18px;

    font-weight: 700;

    margin-top: 6px;
}

.product-description {
    color: #766873;

    font-size: 12px;

    line-height: 1.5;

    min-height: 42px;

    margin-top: 4px;
}


/* ============================================================
   ORDER BUTTON
   ============================================================ */

div[data-testid="stLinkButton"] a {

    min-height: 42px !important;

    border-radius: 23px !important;

    border: 1px solid rgba(255,255,255,0.35) !important;

    background:
        linear-gradient(
            135deg,
            #e84f88,
            #b43d69
        ) !important;

    color: white !important;

    font-family: "DM Sans", sans-serif !important;

    font-size: 12px !important;

    font-weight: 700 !important;

    box-shadow:
        0 6px 16px rgba(192,75,120,0.25) !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease !important;
}

div[data-testid="stLinkButton"] a:hover {

    transform:
        translateY(-3px)
        scale(1.01) !important;

    background:
        linear-gradient(
            135deg,
            #f35b96,
            #c34472
        ) !important;

    box-shadow:
        0 10px 25px rgba(192,75,120,0.40),
        0 0 18px rgba(255,105,160,0.25) !important;
}


/* ============================================================
   FAVORITE BUTTON
   ============================================================ */

div[data-testid="stButton"] button {

    min-height: 42px;

    border-radius: 23px;

    border: 1px solid #e2a5ba;

    background: #ffffff;

    color: #b0446b;

    font-family: "DM Sans", sans-serif;

    font-size: 12px;

    font-weight: 700;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease,
        border-color 0.25s ease;
}

div[data-testid="stButton"] button:hover {

    transform: translateY(-3px);

    border-color: #c04b78;

    background: #fff1f6;

    color: #a03760;

    box-shadow:
        0 8px 20px rgba(192,75,120,0.18);
}


/* ============================================================
   FAVORITE COUNT
   ============================================================ */

.favorite-count {
    text-align: center;

    color: #a04468;

    font-size: 13px;

    font-weight: 600;

    margin: 8px 0 18px;
}


/* ============================================================
   WHY CHOOSE US
   ============================================================ */

.why-title {
    text-align: center;

    color: #38232e;

    font-family: "Playfair Display", serif;

    font-size: 37px;

    margin-top: 40px;
}

.why-subtitle {
    text-align: center;

    color: #766872;

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
        0 5px 18px rgba(70,35,50,0.05);

    transition:
        transform 0.28s ease,
        box-shadow 0.28s ease;
}

.feature-box:hover {
    transform: translateY(-5px);

    box-shadow:
        0 12px 28px rgba(176,68,107,0.12);
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
    color: #766872;

    font-size: 12px;

    line-height: 1.5;

    margin-top: 7px;
}


/* ============================================================
   CTA
   ============================================================ */

.cta {
    text-align: center;

    margin-top: 35px;

    padding: 30px 20px;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            #302127,
            #603d4c
        );

    border: 1px solid #d29b62;

    box-shadow:
        0 8px 25px rgba(60,30,45,0.15);
}

.cta-title {
    color: white;

    font-family: "Playfair Display", serif;

    font-size: 30px;

    font-weight: 700;
}

.cta-description {
    color: #f3e5eb;

    font-size: 13px;

    margin-top: 5px;
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

@media (max-width: 700px) {

    .hero-title {
        font-size: 43px;
    }

    .hero {
        padding: 45px 18px;
    }

    .product-image {
        height: 200px;
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
        ✦ Stylish Designs
        &nbsp;&nbsp;&nbsp;
        💎 Premium Look
        &nbsp;&nbsp;&nbsp;
        ♥ Affordable Prices
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
"""
)


# ============================================================
# FAVORITE FILTER
# ============================================================

favorite_count = len(st.session_state.favorites)

if favorite_count > 0:
    st.html(
        f"""
        <div class="favorite-count">
            ❤️ {favorite_count} favorite design{"s" if favorite_count != 1 else ""}
        </div>
        """
    )


# ============================================================
# PRODUCT CARDS
# ============================================================

columns = st.columns(3, gap="small")


for index, product in enumerate(PRODUCTS):

    with columns[index % 3]:

        image_path = IMAGE_DIR / product["image"]

        # ----------------------------------------------------
        # CARD START
        # ----------------------------------------------------

        st.html('<div class="product-card">')

        # Image
        if image_path.exists():

            st.image(
                str(image_path),
                use_container_width=True,
            )

        else:

            st.error(
                f"Image not found: {product['image']}"
            )

        # Product details
        st.html(
            f"""
            <div class="product-name">
                {product["name"]}
            </div>

            <span class="product-category">
                {product["category"]}
            </span>

            <div class="product-price">
                PKR {product["price"]:,}
            </div>

            <div class="product-description">
                {product["description"]}
            </div>
            """
        )

        # ----------------------------------------------------
        # ORDER + FAVORITE BUTTONS
        # ----------------------------------------------------

        order_message = quote(
            f"Hello {STORE_NAME}! "
            f"I would like to order {product['name']} "
            f"for PKR {product['price']:,}. "
            f"Please share the order details."
        )

        # Order button
        st.link_button(
            "🛍️  Order This Design  →",
            f"https://wa.me/{WHATSAPP}?text={order_message}",
            use_container_width=True,
        )

        # Favorite button
        is_favorite = product["name"] in st.session_state.favorites

        if is_favorite:
            favorite_label = "❤️  Added to Favorites"
        else:
            favorite_label = "♡  Add to Favorites"

        if st.button(
            favorite_label,
            key=f"favorite_{index}",
            use_container_width=True,
        ):

            if is_favorite:

                st.session_state.favorites.remove(
                    product["name"]
                )

            else:

                st.session_state.favorites.add(
                    product["name"]
                )

            st.rerun()

        # Card spacing
        st.html("</div>")

        st.html("<div style='height:10px'></div>")


# ============================================================
# WHY CHOOSE US
# ============================================================

st.html(
    """
<div class="why-title">
    Why Choose Us?
</div>

<div class="why-subtitle">
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


feature_columns = st.columns(3, gap="small")


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


bottom_col1, bottom_col2 = st.columns(
    2,
    gap="small"
)


with bottom_col1:

    st.link_button(
        "🛍️  Order on WhatsApp  →",
        f"https://wa.me/{WHATSAPP}?text={general_message}",
        use_container_width=True,
    )


with bottom_col2:

    st.link_button(
        f"☎  Contact Us · {PHONE}",
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
