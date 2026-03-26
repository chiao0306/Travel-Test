import streamlit as st
import pandas as pd

# ==========================================
# 1. 頁面基本設定
# ==========================================
st.set_page_config(page_title="🗼 2025 東京自由行攻略", page_icon="✈️", layout="wide")

# 自訂 CSS 讓字體跟排版更好看
st.markdown("""
    <style>
    .big-font { font-size:20px !important; font-weight: bold; color: #1E90FF; }
    .stCheckbox > label { font-size: 16px; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 標題與動態小工具 (模擬即時資訊)
# ==========================================
st.title("🎒 2025 東京互動專屬行程表")
st.write("你的隨身數位導遊，點擊側邊欄切換每日行程！")

# 頂部儀表板 (可玩性：未來可以串接真實 API)
col1, col2, col3 = st.columns(3)
col1.metric("今日日幣匯率 (參考)", "0.212", "-0.001")
col2.metric("東京天氣", "18°C 🌤️", "適合穿薄外套")
col3.metric("河口湖降雨機率", "10%", "-5%")
st.divider()

# ==========================================
# 3. 側邊欄：導覽選單
# ==========================================
st.sidebar.image("https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Tokyo Vibes")
st.sidebar.header("📅 行程天數")
days = ["Day 1: 抵達與上野", "Day 2: 晴空塔", "Day 3: 富士山河口湖", "Day 4: 澀谷與豐洲"]
selected_day = st.sidebar.radio("請選擇：", days)

# ==========================================
# 4. 每日行程內容
# ==========================================
if selected_day == days[0]:
    st.header("Day 1: 降落東京，前往赤羽與上野 🛫")
    
    # 使用 Tabs 讓資訊更分類
    tab1, tab2 = st.tabs(["📝 行程清單", "🗺️ 景點地圖"])
    
    with tab1:
        st.subheader("上午：航班與交通")
        st.checkbox("08:15 搭乘亞航 FD: 234 航班")
        st.checkbox("13:05 抵達成田機場第二航廈")
        st.checkbox("搭乘 Skyliner (約45分鐘至日暮里)")
        
        st.subheader("下午：飯店 Check-in")
        st.checkbox("抵達北區赤羽 WING HOTEL AKABANE Check-in")
        st.checkbox("前往谷中銀座商店街看夕陽")
        
        st.subheader("晚上：上野美食大挑戰 🍱")
        st.info("💡 晚餐口袋名單：名代 宇奈とと 上野店 (鰻魚飯) 或 肉之大山可樂餅")
        st.checkbox("逛阿美橫町")
        st.checkbox("吃晚餐！")

    with tab2:
        st.write("📌 **本日移動熱點**")
        # 簡易地圖：赤羽、上野、谷中銀座
        map_data = pd.DataFrame({
            'lat': [35.7781, 35.7115, 35.7275],
            'lon': [139.7208, 139.7745, 139.7667]
        })
        st.map(map_data, zoom=11)

elif selected_day == days[1]:
    st.header("Day 2: 晴空塔周邊漫步 🗼")
    st.info("💡 交通提示：搭乘京濱東北線至上野，轉乘東武晴空塔線至押上 (約20分)")
    st.checkbox("前往押上站")
    st.checkbox("18:00 登上晴空塔 (記得準備門票)")

elif selected_day == days[2]:
    st.header("Day 3: 富士山河口湖一日遊 🗻")
    st.image("https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", caption="祈禱今天能看到完整的富士山！")
    
    colA, colB = st.columns(2)
    with colA:
        st.subheader("景點與美食")
        st.checkbox("搭乘天上山公園纜車")
        st.checkbox("參拜子神社")
        st.checkbox("品嚐 ほうとう (不動烏龍麵)")
    with colB:
        st.subheader("回程注意")
        st.warning("🚌 務必趕上 **18:15** 從河口湖站回新宿的巴士！")

elif selected_day == days[3]:
    st.header("Day 4: 澀谷流行與光影藝術 ✨")
    st.checkbox("逛澀谷 Sakura Stage 與 PARCO")
    st.checkbox("參觀 teamLab Planets (豐洲)")
    st.success("好好享受東京之旅！")