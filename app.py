import streamlit as st

# ==========================================
# 1. 頁面基本設定與自訂時間軸 CSS
# ==========================================
st.set_page_config(page_title="🗼 2025 東京自由行攻略", page_icon="✈️", layout="wide")

# 利用 CSS 畫出時間軸的視覺效果
st.markdown("""
    <style>
    .time { font-size: 1.2em; font-weight: bold; color: #FF4B4B; margin-right: 15px; }
    .location { font-size: 1.2em; font-weight: bold; color: #1E90FF; }
    .transit { 
        color: #888888; 
        font-size: 0.95em; 
        margin-left: 25px; 
        border-left: 2px dashed #cccccc; 
        padding-left: 20px; 
        padding-top: 10px; 
        padding-bottom: 10px; 
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎒 2025 東京互動專屬行程表")
st.write("你的隨身數位導遊，點擊上方分頁切換每日行程！")

# ==========================================
# 2. 側邊欄：小工具 (天氣、匯率)
# ==========================================
st.sidebar.header("📊 即時旅遊資訊")
st.sidebar.metric("今日日幣匯率 (參考)", "0.212", "-0.001")
st.sidebar.metric("東京天氣", "18°C 🌤️", "適合穿薄外套")
st.sidebar.metric("河口湖降雨機率", "10%", "-5%")

# ==========================================
# 3. 頂部導覽：每日行程分頁
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📍 Day 1: 抵達與上野", 
    "🗼 Day 2: 晴空塔", 
    "🗻 Day 3: 富士山河口湖", 
    "✨ Day 4: 澀谷與豐洲"
])

# ==========================================
# 4. 每日行程內容 (時間、地點與交通)
# ==========================================
with tab1:
    st.header("Day 1: 降落東京，前往赤羽與上野 🛫")
    
    st.markdown("<span class='time'>08:15 - 13:05</span><span class='location'>📍 成田機場第二航廈 (亞航 FD: 234)</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚆 搭乘 Skyliner 前往日暮里 (約 45 分鐘)，站內轉乘京濱東北線至赤羽 (約 20 分鐘)</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>15:00</span><span class='location'>🏨 WING HOTEL AKABANE (飯店 Check-in)</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚆 搭乘京濱東北線返回日暮里 (約 20 分鐘)，步行前往</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>16:30</span><span class='location'>🌇 谷中銀座商店街 (看夕陽)</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚆 步行回日暮里站，轉乘山手線或京濱東北線至上野站 (約 6 分鐘)</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>18:00</span><span class='location'>🛍️ 阿美橫町</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚶 步行前往餐廳</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>19:00</span><span class='location'>🍱 晚餐：名代 宇奈とと 上野店 或 肉之大山</span>", unsafe_allow_html=True)

with tab2:
    st.header("Day 2: 晴空塔周邊漫步 🗼")
    
    st.markdown("<span class='time'>09:00</span><span class='location'>📍 赤羽出發</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚆 搭乘京濱東北線/高崎線至上野 (約 15 分)，轉乘東武晴空塔線至押上 (約 20 分)</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>10:00</span><span class='location'>🛍️ 押上站 / 晴空塔周邊逛街</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚶 自由活動 / 午餐</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>18:00</span><span class='location'>🗼 晴空塔觀景 (已預約門票)</span>", unsafe_allow_html=True)

with tab3:
    st.header("Day 3: 富士山河口湖一日遊 🗻")
    
    st.markdown("<span class='time'>06:00</span><span class='location'>📍 起床 / 出發前往新宿</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚆 搭乘埼京線或湘南新宿線至新宿 (約 20 分鐘)，轉乘特急富士回遊或高速巴士 (約 2 小時)</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>09:00</span><span class='location'>🚉 富士山河口湖站</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚌 購買周遊巴士券，搭乘紅線巴士或步行</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>10:00</span><span class='location'>🚠 天上山公園纜車 & ⛩️ 子神社</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚶 步行或搭乘短程巴士</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>12:30</span><span class='location'>🍜 午餐：ほうとう (不動烏龍麵)</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚌 搭乘周遊巴士返回河口湖車站</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>18:15</span><span class='location'>🚌 河口湖站 (搭乘巴士回新宿)</span>", unsafe_allow_html=True)

with tab4:
    st.header("Day 4: 澀谷流行與光影藝術 ✨")
    
    st.markdown("<span class='time'>10:00</span><span class='location'>🛍️ 澀谷 Sakura Stage & PARCO</span>", unsafe_allow_html=True)
    st.markdown("<div class='transit'>⬇️ 🚆 搭乘銀座線/半藏門線等路線轉乘至豐洲站 (約 40 分鐘)</div>", unsafe_allow_html=True)
    
    st.markdown("<span class='time'>14:00</span><span class='location'>🎨 teamLab Planets (豐洲)</span>", unsafe_allow_html=True)
