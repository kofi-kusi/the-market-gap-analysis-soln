# 🍩 The Sugar Trap: Market Gap Analysis

**Live Interactive Dashboard:** [Insert Your Streamlit URL Here]

## 📊 Executive Summary
This project analyzes the global Open Food Facts database to identify strategic market gaps for a new health-conscious snack product. By engineering a memory-efficient pipeline to process the raw dataset, mapping unstructured category tags, and visualizing the competitive landscape, the analysis reveals two key insights:

1. **The Market Gap:** The market is heavily saturated with high-sugar confectionery and salty snacks. However, there is a distinct lack of products in the "High-Protein (>15g) and Low-Sugar (<10g)" quadrant, specifically within the **Baked Goods** category. 
2. **Formulation Strategy:** Text analysis of 4,651 existing high-protein products shows a decisive industry shift toward plant-based proteins. The top three protein sources utilized in successful high-protein snacks are **Soy (928 products), Pea (755 products), and Peanut (588 products)**.

**Strategic Recommendation:** Formulate a new low-sugar, high-protein Baked Good utilizing a Soy/Pea protein blend to aggressively capture this untapped market segment.

---

## Technical Notes

Handling the raw 3GB+ dataset required strict memory management and robust data cleaning strategies.

* **Memory-Optimized Ingestion:** Bypassed local memory constraints by forcing tab-separation parsing (`sep='\t'`) on the `.csv` extension, utilizing the `usecols` parameter to load only the 5 required columns, and chunking the initial load to 500,000 rows.
* **Data Scrubbing & Domain Logic:** * Dropped records missing critical matrix identifiers (Product Name, Sugar, Protein).
    * Enforced biological reality by filtering out anomalous rows where sugar or protein exceeded 100g per 100g serving.
* **Unstructured Data Mapping:** Standardized over 5,000 chaotic, comma-separated nutritional tags into 5 clean business categories using Python string manipulation and prioritized keyword mapping.
* **Text Analysis:** Utilized Pandas vectorized string operations (`.str.contains()`) to efficiently extract and quantify target protein keywords from the raw `ingredients_text` column.
* **Deployment Stack:** Built end-to-end in Python using Pandas for transformations, Plotly Express for interactive visualizations, and Streamlit Community Cloud for public deployment.

---

## 🌟 Candidate's Choice (Story 6)

**What I built:** "Sizing the Market Gap" Bar Chart.
For the final dashboard visualization, I engineered a dynamic bar chart that filters the dataset strictly down to our target "Empty Quadrant" (products with >15g Protein and <10g Sugar) and counts the exact number of existing products by category.

**The Business Value:** While the primary scatter plot is excellent for showing the overall distribution of the market, it can be difficult to quantify the density of overlapping data points. This final visualization directly answers the immediate business question: *"Exactly how many competitors currently exist in our target niche?"* By sizing the gap, we can definitively prove to stakeholders that entering the high-protein Baked Goods space faces significantly less direct competition than trying to launch another Energy Bar.

---

## Running the Project Locally

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```