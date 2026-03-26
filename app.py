import streamlit as st
import pandas as pd

# ==========================================
# 1. 頁面與全域設定 (修復 UI 問題)
# ==========================================
st.set_page_config(page_title="2025 東京自由行", page_icon="📱", layout="centered")

# 重新設計 CSS，解決上方空白、標題過大，並保留原生的控制台
st.markdown("""
    <style>
    /* 大幅減少頂部預設空白 */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* 自訂精緻小標題，取代原本巨大的 st.title */
    .app-header {
        text-align: center;
        font-size: 1.5em;
        font-weight: 800;
        color: #1C1C1E;
        margin-bottom: 20px;
    }
    
    /* 卡片基礎設計 (更緊湊) */
    .app-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        border: 1px solid #f0f0f0;
    }
    
    /* 分類卡片左側識別色 */
    .card-spot { border-left: 5px solid #5E5CE6; }     /* 景點：紫色 */
    .card-food { border-left: 5px solid #FF9F0A; }     /* 餐廳：橘色 */
    .card-transit { border-left: 5px solid #32ADE6; background: #F8F9FA; } /* 交通：淺灰藍 */

    /* 導遊攻略標籤設計 */
    .tag {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 8px;
        font-size: 0.75em;
        font-weight: 700;
        margin-right: 5px;
        margin-bottom: 6px;
    }
    .tag-food { background: #FFF0E6; color: #FF9F0A; }
    .tag-buy { background: #EAEBFE; color: #5E5CE6; }
    .tag-alert { background: #FFEBEE; color: #FF3B30; }
    .tag-story { background: #E8F5E9; color: #34C759; }

    /* 次級導航按鈕 (縮小一點才不會太突兀) */
    .nav-btn {
        display: block;
        background: #F2F2F7;
        color: #007AFF !important;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9em;
        margin-top: 10px;
    }
    .nav-btn:active { background: #E5E5EA; }
    
    .time-badge { color: #8E8E93; font-weight: bold; font-family: monospace; font-size: 1.1em; margin-right: 8px; }
    h3 { margin-top: 0; color: #1C1C1E; font-size: 1.15em; font-weight: 700; margin-bottom: 6px; }
    p { color: #3A3A3C; font-size: 0.9em; line-height: 1.5; margin-bottom: 4px; }
    </style>
""", unsafe_allow_html=True)

# 使用 HTML 標籤代替 st.title 以縮小字體
st.markdown('<div class="app-header">📱 2025 東京專屬行程</div>', unsafe_allow_html=True)

# ==========================================
# 2. 底部導覽列設計
# ==========================================
tab1, tab2, tab3, tab4, tab_tools = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "🧰 工具"])

# ==========================================
# 3. 每日行程內容 (補齊 Excel 遺漏內容)
# ==========================================
with tab1:
    st.info("🌤️ 天氣：18°C 晴時多雲 | 降雨機率 10%")
    
    st.markdown("""
    <div class="app-card card-transit">
        <h3><span class="time-badge">08:15</span> ✈️ 航班抵達與機場交通</h3>
        <p>亞航 FD: 234，預計 13:05 抵達成田機場第二航廈。</p>
        <p>搭乘 Skyliner (約45分) 至日暮里，轉京濱東北線至赤羽。</p>
        <a href="https://maps.app.goo.gl/YourHotelLink" target="_blank" class="nav-btn">📍 導航至 WING HOTEL AKABANE</a>
    </div>

    <div class="app-card card-spot">
        <h3><span class="time-badge">傍晚</span> 🌇 谷中銀座商店街</h3>
        <p><span class="tag tag-story">著名夕陽階梯</span> <span class="tag tag-buy">必買：貓尾巴雞蛋糕</span></p>
        <p>由赤羽搭京濱東北線至日暮里。充滿昭和風情，傍晚光影最美。</p>
        <a href="https://maps.app.goo.gl/YanakaGinzaLink" target="_blank" class="nav-btn">📍 導航前往</a>
    </div>

    <div class="app-card card-food">
        <h3><span class="time-badge">晚上</span> 🍱 上野 / 阿美橫町晚餐</h3>
        <p><span class="tag tag-food">名代 宇奈とと (鰻魚飯)</span> <span class="tag tag-food">肉之大山 (可樂餅)</span></p>
        <p>逛完街後吃高 CP 值的現烤鰻魚飯！</p>
        <a href="https://maps.app.goo.gl/UnatotoLink" target="_blank" class="nav-btn">📍 導航至宇奈とと</a>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.info("🌤️ 天氣：20°C 晴朗 | 適合登塔")
    
    st.markdown("""
    <div class="app-card card-spot">
        <h3><span class="time-badge">18:00</span> 🗼 晴空塔 (預約門票)</h3>
        <p><span class="tag tag-alert">請準備電子 QR Code</span> <span class="tag tag-buy">伴手禮：Tokyo Banana 晴空塔限定版</span></p>
        <p>交通：搭乘京濱東北線/高崎線至上野，轉乘東武晴空塔線至押上 (約20分)。</p>
        <a href="https://maps.app.goo.gl/SkytreeLink" target="_blank" class="nav-btn">📍 導航前往</a>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.info("🗻 天氣：12°C 晴朗 | 降雨機率 0%")
    
    st.markdown("""
    <div class="app-card card-transit">
        <h3><span class="time-badge">06:00</span> 🚆 出發前往河口湖</h3>
        <p>第一班車前往新宿，轉乘前往富士山河口湖。</p>
    </div>

    <div class="app-card card-spot">
        <h3><span class="time-badge">上午</span> 🚠 天上山公園 & 子神社</h3>
        <p><span class="tag tag-story">「喀嚓喀嚓山」童話發源地</span></p>
        <p>搭乘纜車上山，眺望無遮蔽富士山全景。</p>
        <a href="https://maps.app.goo.gl/KachiKachiLink" target="_blank" class="nav-btn">📍 導航前往</a>
    </div>

    <div class="app-card card-food">
        <h3><span class="time-badge">中午</span> 🍜 河口湖美食巡禮</h3>
        <p><span class="tag tag-food">ほうとう (不動烏龍麵)</span> <span class="tag tag-food">Giraffa (咖哩麵包)</span></p>
        <p>吃完粗麵條後，可以去 Gateway Fujiyama 逛逛，並品嚐當地知名的 Giraffa 咖哩麵包或甜甜圈！</p>
        <a href="https://maps.app.goo.gl/HoutouLink" target="_blank" class="nav-btn">📍 導航至不動烏龍麵</a>
    </div>
    
    <div class="app-card card-transit">
        <h3><span class="time-badge">18:15</span> 🚌 賦歸</h3>
        <p>從河口湖站搭車回新宿，請注意發車時間。</p>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.info("☁️ 天氣：19°C 多雲")
    
    st.markdown("""
    <div class="app-card card-spot">
        <h3><span class="time-badge">上午</span> 🛍️ 澀谷 Sakura Stage & PARCO</h3>
        <p><span class="tag tag-buy">必逛：任天堂旗艦店、寶可夢中心 (PARCO內)</span></p>
        <p>體驗澀谷最新落成的複合式商場與潮流文化。</p>
        <a href="https://maps.app.goo.gl/ParcoLink" target="_blank" class="nav-btn">📍 導航前往</a>
    </div>
    
    <div class="app-card card-spot">
        <h3><span class="time-badge">下午</span> ✨ teamLab Planets & LaLaport 豐洲</h3>
        <p><span class="tag tag-alert">展覽需涉水，請穿輕便褲子</span> <span class="tag tag-buy">LaLaport (海景商場)</span></p>
        <p>看完展覽後，可以直接到旁邊的 LaLaport 豐洲吃飯看東京灣海景。</p>
        <a href="https://maps.app.goo.gl/TeamLabLink" target="_blank" class="nav-btn">📍 導航至 teamLab</a>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. 實用工具與記帳
# ==========================================
with tab_tools:
    with st.expander("✈️ 航班與住宿資訊", expanded=True):
        st.markdown("**去程航班**：亞航 FD: 234 (08:15 - 13:05 成田機場第二航廈)")
        st.markdown("**住宿飯店**：WING HOTEL AKABANE")
        
    with st.expander("🚨 緊急聯絡電話"):
        st.markdown("""
        - **報警**：110
        - **救護車/火警**：119
        - **旅外國人急難救助**：001-010-800-0885-0885
        - **駐日代表處**：+81-3-3280-7811
        """)
        
    st.subheader("💰 記帳 / 預算表")
    if 'budget_df' not in st.session_state:
        st.session_state.budget_df = pd.DataFrame([
            {"日期": "Day 1", "項目": "Skyliner車票", "金額(JPY)": 0},
            {"日期": "Day 1", "項目": "宇奈とと鰻魚飯", "金額(JPY)": 0},
            {"日期": "Day 2", "項目": "晴空塔門票", "金額(JPY)": 0},
            {"日期": "", "項目": "", "金額(JPY)": 0}
        ])
    
    edited_df = st.data_editor(
        st.session_state.budget_df, 
        num_rows="dynamic", 
        use_container_width=True,
        column_config={"金額(JPY)": st.column_config.NumberColumn("金額(JPY)", format="¥ %d")}
    )
    
    st.metric(label="📊 總花費", value=f"¥ {edited_df['金額(JPY)'].sum():,}")
