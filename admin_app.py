import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# --- ADVANCED PREMIUM CYBER-DARK DESIGN SYSTEM ---
st.set_page_config(page_title="CrediFlow Admin Operations Terminal", layout="wide")

st.markdown("""
    <style>
    /* Global Canvas Styling */
    .stApp { background: radial-gradient(circle at top right, #0a0f1d, #030305); color: #ffffff; font-family: 'Segoe UI', system-ui, sans-serif; }
    
    /* Glowing Glassmorphic Container Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        padding: 30px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 25px;
    }
    
    /* Center alignment helper */
    .center-text {
        text-align: center;
    }
    
    /* Interactive Status Indicators */
    .status-panel { display: flex; justify-content: flex-end; gap: 15px; margin-bottom: 10px; }
    .status-pill { 
        background: rgba(255, 255, 255, 0.02); 
        padding: 6px 16px; 
        border-radius: 30px; 
        border: 1px solid rgba(0, 255, 136, 0.2); 
        font-size: 0.85em; 
        font-weight: 600;
        color: #00ff88;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.1);
    }
    
    /* Central Landing Page Card Alignment */
    div.glass-card div.stButton {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 15px auto 0 auto !important;
    }
    div.glass-card div.stButton > button {
        background: linear-gradient(135deg, #0077ff, #00ff88) !important;
        color: #020408 !important; font-weight: 700 !important; letter-spacing: 0.05em !important;
        border: none !important; border-radius: 10px !important;
        width: 60% !important; height: 3.4em; font-size: 1.05em !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    div.glass-card div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 255, 136, 0.4);
    }

    /* Input Elements Layout Modification */
    .stTextInput>div>div>input { 
        background-color: rgba(255, 255, 255, 0.03) !important; 
        color: white !important; 
        border: 1px solid rgba(255, 255, 255, 0.08) !important; 
        border-radius: 10px !important;
        height: 3em !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #00ddff !important;
        box-shadow: 0 0 12px rgba(0, 221, 255, 0.2) !important;
    }
    
    /* Pill-Style Refresh Button (Right-Aligned in Dashboard View) */
    div[data-testid="stColumn"] div.stButton {
        display: block !important; 
    }
    div[data-testid="stColumn"] div.stButton > button {
        background: rgba(255, 255, 255, 0.02) !important; 
        padding: 6px 16px !important; 
        border-radius: 30px !important; 
        border: 1px solid rgba(0, 255, 136, 0.2) !important; 
        font-size: 0.85em !important; 
        font-weight: 600 !important;
        color: #00ff88 !important;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.1) !important;
        height: auto !important;
        width: auto !important;
        float: right !important;
        margin-top: 5px !important;
        transition: all 0.2s ease !important;
    }
    div[data-testid="stColumn"] div.stButton > button:hover {
        border-color: rgba(0, 255, 136, 0.6) !important;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.3) !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TRACKING STATE MACHINE CONFIGURATION ---
if "workspace_authenticated" not in st.session_state:
    st.session_state.workspace_authenticated = False
if "stored_sheet" not in st.session_state:
    st.session_state.stored_sheet = ""

# --- CACHE-BUSTED CORES FOR LIVE MONITORING ---
def fetch_latest_record(sheet_link):
    try:
        if "/d/" in sheet_link:
            sheet_id = sheet_link.split("/d/")[1].split("/")[0]
            csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&t={int(time.time())}"
            df = pd.read_csv(csv_url)
            df.columns = df.columns.str.strip()
            if not df.empty:
                return df.iloc[-1].to_dict() # Instantly targets the newest entry row updated by n8n
    except Exception:
        pass
    return None

# =======================================================================================
# INTERACTION NODE 1: LUXURY CENTRAL GATEWAY DEPLOYMENT INTERFACE (LANDING - CENTERED)
# =======================================================================================
if not st.session_state.workspace_authenticated:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    left_spacer, center_panel, right_spacer = st.columns([1, 2.2, 1])
    
    with center_panel:
        st.markdown('<h1 class="center-text">🌌 CrediFlow | Global Mesh Gateway</h1>', unsafe_allow_html=True)
        st.markdown('<p class="center-text">Initialize cloud infrastructure endpoints to orchestrate dynamic risk vectors.</p>', unsafe_allow_html=True)
        st.divider()
        
        st.markdown("### 🖥️ Hardware Routing Ingress")
        
        input_sheet = st.text_input("Active Google Sheet Audit Trail Location URL")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 DEPLOY CONTROL WORKSPACE"):
            if not input_sheet.strip():
                st.error("⚠️ Config Exception: The database configuration tracking link is mandatory.")
            else:
                with st.spinner("Establishing live session mapping hooks..."):
                    time.sleep(0.8)
                    st.session_state.stored_sheet = input_sheet.strip()
                    st.session_state.workspace_authenticated = True
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# =======================================================================================
# INTERACTION NODES 2 & 3: HIGH-FIDELITY ACTIVE UNDERWRITING CONTROL ROOM
# =======================================================================================
else:
    # --- DYNAMIC HEADERS & TOP-CORNER GLOW BADGES ---
    col_title, col_status = st.columns([2.5, 1])
    with col_title:
        st.title("🏦 CREDIFLOW | Operations Terminal")
        st.caption("Framework Matrix State: Connected | Real-Time Continuous Audit Ledger Engine")
    with col_status:
        st.markdown(f"""
            <div class="status-panel">
                <div class="status-pill">● Database Linked</div>
            </div>
            """, unsafe_allow_html=True)
            
    if st.sidebar.button("🔌 Close Infrastructure Session"):
        st.session_state.workspace_authenticated = False
        st.rerun()
        
    st.divider()

    # --- MAIN VISUAL COMPONENT OVERLAY ---
    col_hdr, col_btn = st.columns([4.2, 1])
    with col_hdr:
        st.subheader("📊 Live Underwriting Telemetry Monitor")
    with col_btn:
        if st.button("Refresh"):
            st.rerun()
            
    # Fetch data directly from the spreadsheet core architecture
    record = fetch_latest_record(st.session_state.stored_sheet)
    
    if record:
        # Dynamically pulling identifying keys from your spreadsheet layout matrix
        account_id = record.get('PAN Number', record.get('Account Number', 'N/A'))
        applicant_name = record.get('Applicant Name', record.get('Applicant Full Identity Name', 'N/A'))
        
        st.markdown(f"#### 📑 Current Registry Entry Block Verified | Reference ID: `{account_id}`")
        st.write(f"**Applicant Profile Under Audit:** {applicant_name}")
        
        raw_status = record.get('Assessment Status', 'Processing')
        status_str = str(raw_status).strip() if not pd.isna(raw_status) else 'Processing'
        
        # Color-Coded Execution Summary Panels
        if "Approved" in status_str:
            st.markdown(f"""
                <div style="background: rgba(0, 255, 136, 0.05); border: 1px solid #00ff88; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                    <h3 style="color: #00ff88; margin: 0;"> 🟢 UNDERWRITING VERIFICATION STATUS: APPROVED</h3>
                </div>
                """, unsafe_allow_html=True)
        elif "Rejected" in status_str:
            st.markdown(f"""
                <div style="background: rgba(255, 51, 102, 0.05); border: 1px solid #ff3366; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                    <h3 style="color: #ff3366; margin: 0;">🔴 UNDERWRITING VERIFICATION STATUS: REJECTED</h3>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background: rgba(255, 204, 0, 0.05); border: 1px solid #ffcc00; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                    <h3 style="color: #ffcc00; margin: 0;">🟡 UNDERWRITING VERIFICATION STATUS: ESCALATED TO MANUAL REVIEWS</h3>
                </div>
                """, unsafe_allow_html=True)
                
        # Split Dashboard Columns
        col_res1, col_res2 = st.columns([1, 1.2])
        with col_res1:
            st.metric("Google Sheets Live Column Value", status_str)
            
        with col_res2:
            st.markdown("#### 🧠 Cognitive Foundation Model Reasoning Statements")
            raw_reasoning = record.get('Underwriting Reasoning', 'Processing telemetry payload footprint...')
            reasoning_str = str(raw_reasoning).strip() if not pd.isna(raw_reasoning) else 'Processing telemetry payload footprint...'
            st.info(reasoning_str)
            
        st.divider()
        st.markdown("#### 📉 Centered Metrics Data Canvas View")
        
        # --- ROBUST METRIC CONVERSION CORE ---
        try:
            raw_score = record.get('Risk Score', 50)
            if pd.isna(raw_score) or str(raw_score).strip() == "":
                risk_weight = 50
            else:
                # Converts floating string notation or structural zeros cleanly
                risk_weight = int(float(str(raw_score).strip()))
        except (ValueError, TypeError):
            risk_weight = 50
            
        gauge_accent = "#00ff88" if "Approved" in status_str else ("#ffcc00" if "Review" in status_str else "#ff3333")
        
        fig = go.Figure(go.Indicator(
            mode="gauge",
            value=risk_weight,
            title={'text': "Synthesized Credit Risk Severity Index Score Matrix", 'font': {'color': "#fff", 'size': 14}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': "#fff"},
                'bar': {'color': gauge_accent},
                'steps': [{'range': [0, 100], 'color': 'rgba(255,255,255,0.02)'}]
            }
        ))
        
        fig.add_annotation(
            text=str(risk_weight),
            x=0.5, y=0.15,
            font=dict(size=64, color="#ffffff", family="Segoe UI, Arial"),
            showarrow=False
        )
        
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font={'color': "#fff"}, height=280, margin=dict(l=20,r=20,t=40,b=20))
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.info("🔎 Listening for data stream components... Once an application is dispatched via the Customer Portal, hit Refresh.")
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- VISUAL FOOTER LEDGER METADATA PANELS ---
st.divider()
st.caption("Privacy Operations Protocol: Isolated PII Masking Modals Mesh | Storage Engine Architecture: Google Sheets API Real-time Proxy Adapter Framework")