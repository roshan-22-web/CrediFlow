import streamlit as st
import requests

# Set page style to look like a clean client-facing web portal
st.set_page_config(page_title="CrediFlow Customer Portal", layout="centered")

st.markdown("""
    <style>
    /* Global Canvas Styling */
    .stApp { background: radial-gradient(circle at top right, #001f3f, #000000); color: #ffffff; }
    
    /* Glowing Glassmorphic Container Cards */
    .portal-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* High-Performance Neon Pulse Trigger Button */
    .stButton>button {
        background: linear-gradient(135deg, #0077ff, #00ff88) !important;
        color: #020408 !important; 
        font-weight: 700 !important; 
        width: 100%; 
        height: 3.4em;
        font-size: 1.05em !important;
        border: none !important;
        border-radius: 10px !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 255, 136, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏦 CrediFlow FinTech Application Gateway")
st.write("Submit your financial and employment parameters securely to initiate our automated underwriting verification sequence.")
st.divider()

st.subheader("📋 Secure Loan Application Form")

# --- SECTION 1: PERSONAL & KYC DETAILS ---
st.markdown("#### 👤 Personal Identification")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Legal Identity Name", placeholder="e.g., Ruban John")
with col2:
    email = st.text_input("Primary Email Address", placeholder="e.g., ruban@example.com")

pan_card = st.text_input("Permanent Account Number (PAN)", placeholder="e.g., ABCDE1234F", max_chars=10)

st.markdown("<br>", unsafe_allow_html=True)

# --- SECTION 2: EMPLOYMENT & INCOME MATRIX ---
st.markdown("#### 💼 Employment & Income Profile")
col3, col4 = st.columns(2)
with col3:
    emp_type = st.selectbox("Employment Classification", ["Salaried", "Self-Employed", "Business Owner"])
with col4:
    company = st.text_input("Current Employer / Organization Name", placeholder="e.g., Tech Solutions Ltd")

col5, col6 = st.columns(2)
with col5:
    income = st.number_input("Gross Monthly Revenue / Net Salary (₹)", min_value=0, value=75000, step=5000)
with col6:
    debt = st.number_input("Existing Monthly Debt Obligations / EMIs (₹)", min_value=0, value=15000, step=1000)

st.markdown("<br>", unsafe_allow_html=True)

# --- SECTION 3: REQUESTED LOAN PARAMETERS ---
st.markdown("#### 💰 Loan Capital Requirements")
col7, col8 = st.columns(2)
with col7:
    loan_amount = st.number_input("Requested Loan Amount (₹)", min_value=10000, max_value=10000000, value=500000, step=50000)
with col8:
    tenure = st.slider("Requested Repayment Tenure (Months)", min_value=6, max_value=84, value=36, step=6)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- PIPELINE DISPATCH ENGINE ---
if st.button("🚀 TRANSMIT SECURE LOAN APPLICATION"):
    # Robust data validation checks
    if not name.strip() or not email.strip() or len(pan_card.strip()) != 10:
        st.error("❌ Validation Error: Please fill in all identification fields. Ensure your PAN card is exactly 10 alphanumeric characters.")
    elif income <= 0 or loan_amount <= 0:
        st.error("❌ Financial Paradox: Gross Monthly Income and Requested Loan Amount must be greater than zero.")
    else:
        # Constructing the exact data payload map required by the backend pipeline nodes
        payload = {
            "applicant_name": name.strip(),
            "email_id": email.strip(),
            "pan_number": pan_card.strip().upper(),
            "employment_type": emp_type,
            "organization_name": company.strip() if company else "N/A",
            "monthly_income": income,
            "monthly_debt_obligations": debt,
            "requested_loan_amount": loan_amount,
            "repayment_tenure_months": tenure
        }
        
        # Target endpoint for your backend n8n router network
        webhook_url = "https://roshan22.app.n8n.cloud/webhook/assess-loan"
        
        try:
            with st.spinner("Encrypting data packages and transmitting over TLS mesh down cluster socket..."):
                response = requests.post(webhook_url, json=payload)
            if response.status_code == 200:
                st.success("✅ Application Dispatched Successfully! Your transaction hash has been broadcasted to the FinOps Audit Trail.")
                st.balloons()
            else:
                st.error(f"Ingress Gateway rejected handshake session. HTTP Error Return Code: {response.status_code}")
        except Exception as e:
            st.error(f"System Transport Layer Network Exception: {e}")

st.markdown('</div>', unsafe_allow_html=True)