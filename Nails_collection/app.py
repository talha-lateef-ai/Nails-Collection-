import streamlit as st
from pathlib import Path
from urllib.parse import quote


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Nails_collection",
    page_icon="💅",
    layout="wide",
)


# =========================================================
# Store Information
# =========================================================

STORE_NAME = "Nails_collection"
PHONE = "+92 3289718577"
WHATSAPP_NUMBER = "923289718577"


# =========================================================
# Product Collection
# =========================================================

PRODUCTS = [
    {
        "name": "Red Glossy Elegance",
        "price": 1499,
        "image": "red_glossy.png",
        "description": (
            "A bold, glossy red nail design for an elegant "
            "and confident look."
        ),
    },
    {
        "name": "Sunflower Bloom",
        "price": 1699,
        "image": "sunflower_nails.png",
        "description": (
            "A soft nude design decorated with beautiful "
            "yellow sunflower details."
        ),
    },
    {
        "name": "Pastel Floral Art",
        "price": 1799,
        "image": "pastel_art.png",
        "description": (
            "A playful pastel collection with delicate "
            "floral and artistic details."
        ),
    },
    {
        "name": "Classic French Tips",
        "price": 1299,
        "image": "french_tips.png",
        "description": (
            "A clean and timeless French-tip style that "
            "works for any occasion."
        ),
    },
    {
        "name": "Pink Bow Nails",
        "price": 1599,
        "image": "pink_bows.png",
        "description": (
            "A soft pink manicure finished with cute, "
            "elegant bow details."
        ),
    },
    {
        "name": "Sky Blue French",
        "price": 1399,
        "image": "blue_french.png",
        "description": (
            "Fresh sky-blue French tips for a simple, "
            "modern and stylish look."
        ),
    },
]


# =========================================================
# File Paths
# =========================================================

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"


# =========================================================
# Custom CSS
# =========================================================

st.markdown(
    """
    <style>

    .main {
        background: #fff8fb;
    }

    .hero {
        text-align: center;
        padding: 2rem 1rem 2.5rem;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #ffe6f0,
            #fff7fb
        );
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.15rem;
        color: #5f5360;
        max-width: 720px;
        margin: auto;
    }

    .price {
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0.4rem 0 0.8rem;
    }

    .description {
        color: #665c65;
        min-height: 70px;
    }

    .contact-box {
        text-align: center;
        padding: 2rem;
        border-radius: 20px;
        background: #ffffff;
        border: 1px solid #f0dce5;
        margin-top: 2rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Hero Section
# =========================================================

st.markdown(
    f"""
    <div class="hero">
        <h1>💅 {STORE_NAME}</h1>

        <p>
            Discover beautiful nail designs made for every
            mood and occasion. Browse our collection, choose
            your favorite style, and contact us to place your order.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Collection Heading
# =========================================================

st.subheader("✨ Our Nail Collection")

st.write(
    "Choose a design below. Prices shown are dummy prices "
    "and can be changed in the PRODUCTS list."
)


# =========================================================
# Product Display
# =========================================================

columns = st.columns(3)

for index, product in enumerate(PRODUCTS):

    with columns[index % 3]:

        # -----------------------------
        # Image Path
        # -----------------------------

        image_path = IMAGE_DIR / product["image"]

        # Check whether image exists
        if image_path.exists():

            st.image(
                str(image_path),
                use_container_width=True,
            )

        else:

            st.error(
                f"Image not found: {product['image']}"
            )

        # -----------------------------
        # Product Name
        # -----------------------------

        st.markdown(
            f"### {product['name']}"
        )

        # -----------------------------
        # Product Price
        # -----------------------------

        st.markdown(
            f"""
            <div class="price">
                PKR {product['price']:,}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # -----------------------------
        # Product Description
        # -----------------------------

        st.markdown(
            f"""
            <div class="description">
                {product['description']}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # -----------------------------
        # Contact Button
        # -----------------------------

        st.link_button(
            "📞 Contact",
            f"tel:{PHONE}",
            use_container_width=True,
        )

        # -----------------------------
        # Order Button
        # -----------------------------

        message = quote(
            f"Hello {STORE_NAME}! "
            f"I would like to order: "
            f"{product['name']} "
            f"(PKR {product['price']:,})."
        )

        st.link_button(
            "🛍️ Order",
            f"https://wa.me/{WHATSAPP_NUMBER}?text={message}",
            use_container_width=True,
        )

        st.divider()


# =========================================================
# Contact Section
# =========================================================

st.markdown(
    f"""
    <div class="contact-box">

        <h2>📞 Ready to order?</h2>

        <p>
            For questions, custom designs, or orders,
            contact us at <b>{PHONE}</b>.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Footer
# =========================================================

st.caption(
    "© 2026 Nails_collection • "
    "Prices displayed are sample/dummy prices."
)
