import streamlit as st
import textwrap

st.set_page_config(
    page_title="Internal Tools Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# 1. Custom CSS for Enterprise Styling
# ---------------------------------------------------------
CUSTOM_CSS = """
<style>
/* Remove excess Streamlit top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Header styling */
.portal-header {
    margin-bottom: 1.5rem;
}
.portal-title {
    font-size: 2.1rem;
    font-weight: 700;
    margin-bottom: 0.25rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}
.portal-subtitle {
    font-size: 1rem;
    color: rgba(128, 128, 128, 0.9);
    margin-bottom: 1rem;
}

/* CSS Grid for uniform app cards */
.portal-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1.25rem;
    margin-top: 1.25rem;
}

/* Individual Card */
.portal-card {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.22);
    border-radius: 12px;
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.portal-card:hover {
    transform: translateY(-4px);
    border-color: #6366f1;
    box-shadow: 0 10px 24px -4px rgba(0, 0, 0, 0.12);
}

.card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.85rem;
}

.card-icon {
    font-size: 1.8rem;
    line-height: 1;
}

.card-badge {
    font-size: 0.72rem;
    font-weight: 600;
    padding: 0.25rem 0.65rem;
    border-radius: 9999px;
    background: rgba(99, 102, 241, 0.14);
    color: #6366f1;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.card-title {
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
    color: var(--text-color);
}

.card-desc {
    font-size: 0.88rem;
    color: rgba(128, 128, 128, 0.95);
    line-height: 1.5;
    margin-bottom: 1.25rem;
    flex-grow: 1;
}

/* Launch Button */
.card-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    padding: 0.55rem 1rem;
    font-size: 0.9rem;
    font-weight: 600;
    border-radius: 8px;
    background-color: #4F46E5;
    color: #ffffff !important;
    text-decoration: none !important;
    transition: background-color 0.2s ease;
}

.card-btn:hover {
    background-color: #4338CA;
    color: #ffffff !important;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. Central Registry of Applications
# ---------------------------------------------------------
APPS = [

    {
            "title": "ANRO Master search (Manisha)",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://anro-master-extractor.streamlit.app/",
        },
    {
            "title": "EXIM - COO Invoice to excel",
            "category": "EXIM",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://coo-invoice-to-excel.streamlit.app/",
        },
    {
            "title": "Hsamuel Dashboard",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://hsamuel-dashboard.streamlit.app/",
        },
    {
            "title": "MHJ LINE SHEET (Vinayak)",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://mhj-cost-sheet.streamlit.app/",
        },
    {
            "title": "PO & Style earch from EMR Dump (Mandaar)",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://stylenumber-and-ponumber-extract.streamlit.app/",
        },
    {
                "title": "Image extractor (Manisha)",
                "category": "Sales",
                "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
                "icon": "📦",
                "url": "https://image-extractor-order-confirmation.streamlit.app/",
            },
    {
            "title": "DCB to order details (Manisha)",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://dcb-to-order-details.streamlit.app/",
        },
    {
            "title": "Daily order updater (Vinayak)",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://daily-order-updater.streamlit.app/",
        },
    {
            "title": "Psegoma data split (Rajesh)",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://data-split.streamlit.app/",
    },
    {
            "title": "Costing - Existing & from TWT (Sushil)",
            "category": "Sales",
            "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
            "icon": "📦",
            "url": "https://style-breakup-formatting.streamlit.app/",
        },{
                    "title": "MHJ Order Verification (Vinayak)",
                    "category": "Sales",
                    "desc": "Real-time warehouse stock tracking, threshold notifications, and vendor purchase requests.",
                    "icon": "📦",
                    "url": "https://mhj-order-verification.streamlit.app/",
                }
]

# ---------------------------------------------------------
# 3. Header & Search / Filter Controls
# ---------------------------------------------------------
st.markdown(
    """
    <div class="portal-header">
        <div class="portal-title">⚡ Intergold Portal</div>
        <div class="portal-subtitle">One-click launchpad for all team workflows and dashboards.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

col_search, col_category = st.columns([3, 1])

with col_search:
    query = st.text_input("Search tools", placeholder="🔍 Search by tool name, tag, or description...", label_visibility="collapsed")

categories = ["All Categories"] + sorted(list({app["category"] for app in APPS}))
with col_category:
    selected_cat = st.selectbox("Filter category", categories, label_visibility="collapsed")

# ---------------------------------------------------------
# 4. Filter Logic
# ---------------------------------------------------------
filtered = [
    app for app in APPS
    if (selected_cat == "All Categories" or app["category"] == selected_cat)
    and (query.lower() in app["title"].lower() or query.lower() in app["desc"].lower() or query.lower() in app["category"].lower())
]

# ---------------------------------------------------------
# 5. Render Responsive CSS Grid
# ---------------------------------------------------------
if not filtered:
    st.info("🔍 No applications match your search criteria. Try a different keyword.")
else:
    card_html_list = []
    for app in filtered:
        card = textwrap.dedent(f"""
        <div class="portal-card">
            <div>
                <div class="card-top">
                    <span class="card-icon">{app['icon']}</span>
                    <span class="card-badge">{app['category']}</span>
                </div>
                <div class="card-title">{app['title']}</div>
                <div class="card-desc"></div>
            </div>
            <a href="{app['url']}" target="_blank" rel="noopener noreferrer" class="card-btn">
                Launch Application ↗
            </a>
        </div>
        """).strip()
        card_html_list.append(card)

    # Join and render without whitespace interference
    grid_html = f'<div class="portal-grid">{"".join(card_html_list)}</div>'
    st.markdown(grid_html, unsafe_allow_html=True)

# Optional footer count
st.markdown(f"<div style='margin-top: 2rem; color: gray; font-size: 0.85rem;'>Showing <b>{len(filtered)}</b> of <b>{len(APPS)}</b> available tools</div>", unsafe_allow_html=True)