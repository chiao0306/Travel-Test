import streamlit as st
import pandas as pd

# 設定頁面資訊
st.set_page_config(page_title="2025 東京自由行", page_icon="🗼", layout="wide")

# 自訂 CSS 讓 UI 更炫一點
st.markdown("""
    <style>
    .time-slot { font-weight: bold; color: #FF4B4B; }
    .location { font-size: 1.2em; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("✈️ 2025 東京自由行互動攻略")
st.write("探索路線、美食地圖與每日行程一目了然！")

# 側邊欄：天數導覽
st.sidebar.header("📅 行程導覽")
days = ["Day 1: 抵達與赤羽/上野", "Day 2: 晴空塔周邊", "Day 3: 富士山河口湖", "Day 4: 澀谷與 teamLab"]
selected_day = st.sidebar.radio("選擇日期", days)

if selected_day == days[0]:
    st.header("Day 1: 降落東京，前往赤羽與上野")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 行程時間表")
        # [span_1](start_span)根據 PDF 內容建立的行程[span_1](end_span)
        with st.expander("🛫 08:15 - 13:05 | 航班抵達", expanded=True):
            [span_2](start_span)st.markdown("- 搭乘 **亞航 FD: 234** 抵達成田機場第二航廈[span_2](end_span)")
            [span_3](start_span)st.markdown("- 轉乘 Skyliner (約45分鐘至日暮里)[span_3](end_span)")
            
        with st.expander("🏨 下午 | 飯店 Check-in & 谷中銀座"):
            [span_4](start_span)st.markdown("- **WING HOTEL AKABANE** Check-in (位於北區赤羽)[span_4](end_span)")
            [span_5](start_span)st.markdown("- 轉車前往 **谷中銀座商店街** 看夕陽[span_5](end_span)")
            
        with st.expander("🍱 晚上 | 上野逛街與晚餐"):
            [span_6](start_span)st.markdown("- 逛 **阿美橫町**[span_6](end_span)")
            [span_7](start_span)st.markdown("- 晚餐推薦：**名代 宇奈とと 上野店** (鰻魚飯) 或 肉之大山可樂餅[span_7](end_span)")
            
    with col2:
        st.subheader("🗺️ 景點地圖")
        # 簡單的互動地圖 (赤羽與上野的粗略座標)
        map_data = pd.DataFrame({
            'lat': [35.7781, 35.7115, 35.7275],
            'lon': [139.7208, 139.7745, 139.7667],
            'name': ['WING Hotel Akabane', 'Ueno', 'Yanaka Ginza']
        })
        st.map(map_data, zoom=11)

elif selected_day == days[1]:
    st.header("Day 2: 晴空塔與市區漫步")
    [span_8](start_span)st.info("搭乘京濱東北線/高崎線至上野，轉乘東武晴空塔線至押上 (約20分)[span_8](end_span)")
    [span_9](start_span)st.markdown("- **18:00** | 🗼 晴空塔觀景 (記得先購票)[span_9](end_span)")
    # 這裡可以繼續擴充你的第二天景點

elif selected_day == days[2]:
    st.header("Day 3: 富士山河口湖一日遊")
    st.image("https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", caption="富士山絕景")
    [span_10](start_span)st.markdown("- 🚠 **景點**：天上山公園、子神社[span_10](end_span)")
    [span_11](start_span)st.markdown("- 🍜 **美食**：ほうとう (不動烏龍麵)[span_11](end_span)")
    [span_12](start_span)st.markdown("- 🚌 **回程**：18:15 從河口湖站搭車回新宿[span_12](end_span)")

elif selected_day == days[3]:
    st.header("Day 4: 澀谷流行與光影藝術")
    [span_13](start_span)st.markdown("- 🛍️ **澀谷**：Sakura Stage / PARCO[span_13](end_span)")
    [span_14](start_span)st.markdown("- ✨ **展覽**：teamLab Planets (豐洲)[span_14](end_span)")
