import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="The Sugar Trap Analysis", layout="wide")
st.title("🍩 The Sugar Trap: Market Gap Analysis")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    return pd.read_csv('dashboard_data.csv')

df = load_data()

# --- SIDEBAR: FILTERING ---
st.sidebar.header("Filter Data")
categories = df['primary_category'].unique().tolist()
selected_categories = st.sidebar.multiselect(
    "Select Categories to view:",
    options=categories,
    default=categories
)

# Apply filter
filtered_df = df[df['primary_category'].isin(selected_categories)]

# --- STORY 3: THE MATRIX ---
st.header("1. The Sugar / Protein Matrix")
st.markdown("Visualizing the snack market. The **bottom-right quadrant** (High Protein, Low Sugar) represents the target market gap.")

# Create the interactive Plotly scatter plot
fig_matrix = px.scatter(
    filtered_df,
    x='sugars_100g',
    y='proteins_100g',
    color='primary_category',
    hover_name='product_name', # Shows product name on hover
    labels={'sugars_100g': 'Sugar (g per 100g)', 'proteins_100g': 'Protein (g per 100g)'},
    opacity=0.6
)

# Add reference lines for the "Empty Quadrant" (e.g., Target: >15g Protein, <10g Sugar)
fig_matrix.add_vline(x=10, line_dash="dash", line_color="red", annotation_text="Max Target Sugar (10g)")
fig_matrix.add_hline(y=15, line_dash="dash", line_color="green", annotation_text="Min Target Protein (15g)")

st.plotly_chart(fig_matrix, use_container_width=True)

# --- STORY 6: CANDIDATE'S CHOICE (THE MARKET GAP SIZING) ---
st.header("2. Sizing the Market Gap")
st.markdown("How many products actually exist in our target quadrant (>15g Protein, <10g Sugar)?")

# Filter for the target quadrant
target_quadrant = filtered_df[
    (filtered_df['proteins_100g'] > 15) &
    (filtered_df['sugars_100g'] < 10)
]

# Count products by category in the target quadrant
gap_counts = target_quadrant['primary_category'].value_counts().reset_index()
gap_counts.columns = ['Category', 'Product Count']

fig_bar = px.bar(
    gap_counts,
    x='Category',
    y='Product Count',
    text='Product Count',
    color='Category',
    title="Products in the 'High Protein, Low Sugar' Quadrant"
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- STORY 4 & 5: THE RECOMMENDATION & HIDDEN GEM ---
st.header("3. Strategic Recommendation")

# Highlighted info box for the final business recommendation
st.info("""
**Recommendation:** 
Based on the matrix, the market is saturated with high-sugar confectionery and baked goods. However, there is a distinct lack of **Baked Goods** in the high-protein, low-sugar quadrant. 

To formulate a new product for this gap, text analysis reveals that the top 3 protein sources currently utilized by successful high-protein products are:
1. **Soy**
2. **Pea**
3. **Peanut**

We recommend developing a low-sugar Baked Good utilizing a blend of these proven ingredients.
""")