import streamlit as st
from pathlib import Path
from urllib.parse import quote

# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Nails Collection",
    page_icon="💅",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# 2. STORE INFORMATION
# ============================================================

STORE_NAME = "Nails Collection"
PHONE = "+92 3289718577"
WHATSAPP_NUMBER = "923289718577"


# ============================================================
# 3. PRODUCT COLLECTION
# ============================================================

PRODUCTS = [
    {
        "name": "Red Glossy Elegance",
        "price": 1499,
        "image": "red_glossy.png",
        "description": "Elegant glossy red nails for a bold and classic look.",
    },
    {
        "name": "Sunflower Bloom",
        "price": 1699,
        "image": "sunflower_nails.png",
        "description": "Beautiful sunflower-inspired nail art with a fresh floral style.",
    },
    {
        "name": "Pastel Floral Art",
        "price": 1799,
        "image": "pastel_art.png",
        "description": "Soft pastel colors combined with delicate floral details.",
    },
    {
        "name": "Classic French Tips",
        "price": 1299,
        "image": "french_tips.png",
        "description": "A clean and timeless French-tip design for every occasion.",
    },
    {
        "name": "Pink Bow Nails",
        "price": 1599,
        "image": "pink_bows.png",
        "description": "Cute pink nails with charming bow details and a stylish finish.",
    },
    {
        "name": "Sky Blue French",
        "price": 1399,
        "image": "blue_french.png",
        "description": "Fresh sky-blue French tips for a modern and elegant appearance.",
    },
]


# ============================================================
# 4. FILE PATHS
# ============================================================

# This fixes the Streamlit Cloud image-path error.
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"


# ============================================================
# 5. CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 19px;
        margin-bottom: 30px;
    }

    .price {
        font-size: 22px;
        font-weight: 700;
        margin: 8px 0;
    }

    .description {
        font-size: 16px;
        min-height: 55px;
        margin-bottom: 12px;
    }

    .contact-box {
        text-align: center;
        padding: 25px;
        margin-top: 35px;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.35);
    }

    .footer {
        text-align: center;
        margin-top: 35px;
        padding: 15px;
        opacity: 0.75;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 6. HERO SECTION
# ============================================================

st.markdown(
    f"""
    <div class="main-title">💅 {STORE_NAME}</div>
    <div class="subtitle">
        Discover beautiful, stylish and elegant nail designs made
        to complete your look.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 7. COLLECTION HEADING
# ============================================================

st.markdown("## ✨ Our Nail Collection")
st.write("Choose your favorite design and click **Order** to place your order.")


# ============================================================
# 8. PRODUCT DISPLAY
# ============================================================

columns = st.columns(3)

for index, product in enumerate(PRODUCTS):

    with columns[index % 3]:

        image_path = IMAGE_DIR / product["image"]

        if image_path.exists():
            st.image(
                str(image_path),
                use_container_width=True,
            )
        else:
            st.error(f"Image not found: {product['image']}")

        st.markdown(f"### {product['name']}")

        st.markdown(
            f"<div class='price'>PKR {product['price']:,}</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<div class='description'>{product['description']}</div>",
            unsafe_allow_html=True,
        )

        # Create a separate WhatsApp order message for each product.
        message = quote(
            f"Hello {STORE_NAME}! "
            f"I would like to order: "
            f"{product['name']} "
            f"(PKR {product['price']:,})."
        )

        # ORDER BUTTON ONLY under each product.
        st.link_button(
            "🛍️ Order",
            f"https://wa.me/{WHATSAPP_NUMBER}?text={message}",
            use_container_width=True,
        )

        st.divider()


# ============================================================
# 9. CONTACT SECTION
#    CONTACT BUTTON APPEARS ONLY ONCE
# ============================================================

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

# ONE CONTACT BUTTON ONLY — at the bottom.
st.link_button(
    "📞 Contact: +92 3289718577",
    f"tel:{PHONE}",
    use_container_width=True,
)


# ============================================================
# 10. FOOTER
# ============================================================

st.markdown(
    f"""
    <div class="footer">
        © 2026 {STORE_NAME} · Beautiful nails, beautiful style 💅
    </div>
    """,
    unsafe_allow_html=True,
)
