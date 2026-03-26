import streamlit as st
import pandas as pd

# ==========================================
# 1. 頁面與全域設定 (手機 App 化)
# ==========================================
st.set_page_config(page_title="2025 東京自駕行", page_icon="📱", layout="centered")

# 注入原生 App 風格的 CSS
st.markdown("""
    <style>
    /* 隱藏預設頂部，讓畫面更乾淨 */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 卡片基礎設計 (圓角、陰影、無邊框感) */
    .app-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 18px;
        margin-bottom: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* 分類卡片左側識別色 */
    .card-spot { border-left: 6px solid #5E5CE6; }     /* 景點：紫色 */
    .card-food { border-left: 6px solid #FF9F0A; }     /* 餐廳：橘色 */
    .card-transit { border-left: 6px solid #32ADE6; background: #F2F2F7; } /* 交通：淺灰藍 */

    /* 導遊攻略標籤設計 */
    .tag {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.8em;
        font-weight: 700;
        margin-right: 6px;
        margin-bottom: 8px;
    }
    .tag-food { background: #FFF0E6; color: #FF9F0A; }
    .tag-buy { background: #EAEBFE; color: #5E5CE6; }
    .tag-alert { background: #FFEBEE; color: #FF3B30; }
    .tag-story { background: #E8F5E9; color: #34C759; }

    /* 滿版導航按鈕 */
    .nav-btn {
        display: block;
        background: #007AFF;
        color: white !important;
        text-align: center;
        padding: 14px;
        border-radius: 14px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.05em;
        margin-top: 16px;
    }
    .nav-btn:active { opacity: 0.8; }
    
    h3 { margin-top: 0; color: #1C1C1E; font-size: 1.4em; font-weight: 700; }
    p { color: #3A3A3C; font-size: 0.95em; line-height: 1.6; margin-bottom: 8px; }
    </style>
""", unsafe_allow_html=True)

st.title("📱 2025 東京自駕專屬")

# ==========================================
# 2. 底部導覽列設計 (使用 Tabs 模擬)
# ==========================================
tab1, tab2, tab3, tab4, tab_tools = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "🧰 工具"])

# ==========================================
# 3. 每日行程卡片
# ==========================================
with tab1:
    st.info("🌤️ 今日天氣：18°C 晴時多雲 | 降雨機率 10%")
    
    st.markdown("""
    <div class="app-card card-transit">
        <h3>🚗 13:05 成田機場取車</h3>
        <p>抵達後前往航廈租車櫃檯辦理手續，確認 ETC 卡與導航設定。</p>
        <a href="https://www.google.com/maps/dir/?api=1&destination=WING+HOTEL+AKABANE&travelmode=driving" target="_blank" class="nav-btn">🚗 導航至飯店 (約需 1 小時)</a>
    </div>

    <div class="app-card card-spot">
        <h3>🌇 谷中銀座商店街</h3>
        <p><span class="tag tag-story">故事：充滿昭和風情的貓咪老街</span></p>
        <p><span class="tag tag-food">必吃美食：鈴木肉餅 (超多汁)</span> <span class="tag tag-buy">必買伴手禮：貓咪尾巴雞蛋糕</span></p>
        <p>著名的「夕陽階梯」，傍晚來拍照光影最漂亮。</p>
        <a href="https://www.google.com/maps/dir/?api=1&destination=谷中銀座商店街&travelmode=driving" target="_blank" class="nav-btn">🚗 導航前往</a>
    </div>

    <div class="app-card card-food">
        <h3>🍱 名代 宇奈とと 上野店</h3>
        <p><span class="tag tag-food">必點菜單：雙倍鰻魚飯 (うな丼ダブル)</span></p>
        <p>超高 CP 值的現烤鰻魚飯！自駕請注意上野車站周邊的單行道與停車場位置。</p>
        <a href="https://www.google.com/maps/dir/?api=1&destination=名代+宇奈とと+上野店&travelmode=driving" target="_blank" class="nav-btn">🚗 導航前往</a>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.info("🌤️ 今日天氣：20°C 晴朗 | 適合登塔")
    
    st.markdown("""
    <div class="app-card card-spot">
        <h3>🗼 18:00 晴空塔 (Tokyo Skytree)</h3>
        <p><span class="tag tag-alert">重要預約代號：請準備電子票券 QR Code</span></p>
        <p><span class="tag tag-buy">必買伴手禮：Tokyo Banana 晴空塔限定版</span></p>
        <p>建議提前抵達，可以在底層的 Solamachi 商場先逛街吃東西。</p>
        <a href="https://www.google.com/maps/dir/?api=1&destination=東京晴空塔&travelmode=driving" target="_blank" class="nav-btn">🚗 導航前往</a>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.info("🗻 今日天氣：12°C 晴朗 | 降雨機率 0% (富士山露臉機率高！)")
    
    st.markdown("""
    <div class="app-card card-spot">
        <h3>🚠 天上山公園 & 子神社</h3>
        <p><span class="tag tag-story">故事：日本童話「喀嚓喀嚓山」兔子與狸貓的故事發源地</span></p>
        <p><span class="tag tag-buy">必買伴手禮：兔子御守</span></p>
        <p>搭乘纜車上山，天氣好時可以拍到毫無遮蔽的富士山全景。</p>
        <a href="https://www.google.com/maps/dir/?api=1&destination=天上山公園&travelmode=driving" target="_blank" class="nav-btn">🚗 導航前往</a>
    </div>

    <div class="app-card card-food">
        <h3>🍜 ほうとう (不動烏龍麵)</h3>
        <p><span class="tag tag-food">必點菜單：招牌不動烏龍麵 (名物不動ほうとう)</span></p>
        <p>山梨縣鄉土料理，超大鐵鍋裝著滿滿蔬菜與粗麵條，非常燙口請小心！河口湖周邊有多家分店 (如東戀路店為雲朵造型建築，極好拍)。</p>
        <a href="https://www.google.com/maps/dir/?api=1&destination=ほうとう不動&travelmode=driving" target="_blank" class="nav-btn">🚗 導航前往</a>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.info("☁️ 今日天氣：19°C 多雲")
    
    st.markdown("""
    <div class="app-card card-spot">
        <h3>✨ teamLab Planets (豐洲)</h3>
        <p><span class="tag tag-alert">重要預約代號：嚴格控管入場時間，請出示憑證</span></p>
        <p><span class="tag tag-story">攻略：這是一個會「涉水」的展覽，建議穿著容易捲起褲管的衣物，現場可免費寄放鞋襪。</span></p>
        <a href="https://www.google.com/maps/dir/?api=1&destination=teamLab+Planets+Tokyo&travelmode=driving" target="_blank" class="nav-btn">🚗 導航前往</a>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. 實用工具分頁
# ==========================================
with tab_tools:
    st.header("🧰 實用工具與記帳")
    
    with st.expander("✈️ 航班與住宿資訊", expanded=True):
        st.markdown("**去程航班**：亞航 FD: 234 (08:15 - 13:05 成田機場第二航廈)")
        st.markdown("**住宿飯店**：WING HOTEL AKABANE")
        st.markdown("*地址：1 Chome-17 Akabanenishi, Kita City, Tokyo*")
        
    with st.expander("🚨 緊急聯絡電話"):
        st.markdown("""
        - **報警**：110
        - **救護車 / 火警**：119
        - **旅外國人急難救助全球免付費專線**：001-010-800-0885-0885
        - **駐日經濟文化代表處**：+81-3-3280-7811
        """)
        
    st.subheader("💰 記帳 / 預算表")
    st.caption("直接在表格內點擊修改，系統會自動加總花費。")
    
    # 建立動態記帳表
    if 'budget_df' not in st.session_state:
        st.session_state.budget_df = pd.DataFrame([
            {"日期": "Day 1", "項目": "租車費用", "金額(JPY)": 0, "分類": "交通"},
            {"日期": "Day 1", "項目": "宇奈とと", "金額(JPY)": 0, "分類": "飲食"},
            {"日期": "Day 2", "項目": "晴空塔門票", "金額(JPY)": 0, "分類": "票券"},
            {"日期": "", "項目": "", "金額(JPY)": 0, "分類": ""}
        ])
    
    # 使用 Streamlit 的 data_editor 達成互動式表格
    edited_df = st.data_editor(
        st.session_state.budget_df, 
        num_rows="dynamic", 
        use_container_width=True,
        column_config={
            "金額(JPY)": st.column_config.NumberColumn("金額(JPY)", min_value=0, format="¥ %d")
        }
    )
    
    # 自動計算總花費
    total_spent = edited_df["金額(JPY)"].sum()
    st.metric(label="📊 目前累積總花費", value=f"¥ {total_spent:,}")
