<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>2025 東京自駕專屬</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Noto Sans TC', sans-serif;
            background-color: #F2F2F7; /* iOS 系統底色 */
            -webkit-tap-highlight-color: transparent;
        }
        /* 隱藏滾動條但保留滾動功能 */
        ::-webkit-scrollbar { display: none; }
        
        .app-container {
            max-width: 480px; /* 限制在手機寬度 */
            margin: 0 auto;
            background-color: #F9F9FB;
            min-height: 100vh;
            position: relative;
            padding-bottom: 90px; /* 留空間給底部導航列 */
            box-shadow: 0 0 20px rgba(0,0,0,0.05);
        }
        
        /* 標籤樣式 */
        .badge-food { background: #FFF0E6; color: #FF9F0A; }
        .badge-buy { background: #EAEBFE; color: #5E5CE6; }
        .badge-story { background: #E8F5E9; color: #34C759; }
        .badge-alert { background: #FFEBEE; color: #FF3B30; }
    </style>
</head>
<body class="text-gray-800">

<div class="app-container">
    <div class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-100 px-5 py-4">
        <h1 class="text-xl font-black text-gray-900 tracking-wider">✈️ 2025 東京自駕</h1>
    </div>

    <div class="px-5 py-4">
        
        <div id="day1" class="tab-content">
            <div class="bg-blue-50 rounded-2xl p-4 mb-6 flex items-center justify-between border border-blue-100">
                <div>
                    <p class="text-xs text-blue-600 font-bold mb-1">Day 1 • 東京市區</p>
                    <p class="text-sm font-medium text-gray-700">18°C 晴時多雲 | 降雨 10%</p>
                </div>
                <i class="fa-solid fa-cloud-sun text-3xl text-blue-400"></i>
            </div>

            <div class="bg-white rounded-2xl p-5 mb-4 shadow-sm border border-gray-100 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-1.5 h-full bg-blue-400"></div>
                <div class="flex items-center mb-2">
                    <span class="text-gray-400 font-mono font-bold text-sm mr-3">08:15</span>
                    <h3 class="font-bold text-lg text-gray-900">抵達成田機場</h3>
                </div>
                <p class="text-sm text-gray-500 mb-4 ml-11">亞航 FD: 234，轉乘 Skyliner 至日暮里，再轉京濱東北線至赤羽。</p>
                <a href="https://maps.google.com/?q=WING+HOTEL+AKABANE" target="_blank" class="ml-11 block bg-gray-50 text-blue-600 text-center text-sm font-bold py-2.5 rounded-xl border border-gray-200 active:bg-gray-100 transition">
                    <i class="fa-solid fa-car-side mr-1"></i> 導航至 WING HOTEL
                </a>
            </div>

            <div class="bg-white rounded-2xl p-5 mb-4 shadow-sm border border-gray-100 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-1.5 h-full bg-indigo-500"></div>
                <div class="flex items-center mb-2">
                    <span class="text-gray-400 font-mono font-bold text-sm mr-3">傍晚</span>
                    <h3 class="font-bold text-lg text-gray-900">谷中銀座商店街</h3>
                </div>
                <div class="ml-11 mb-3 flex flex-wrap gap-2">
                    <span class="badge-story text-xs font-bold px-2.5 py-1 rounded-lg"><i class="fa-solid fa-book-open mr-1"></i>夕陽階梯</span>
                    <span class="badge-buy text-xs font-bold px-2.5 py-1 rounded-lg"><i class="fa-solid fa-bag-shopping mr-1"></i>貓尾巴雞蛋糕</span>
                </div>
                <p class="text-sm text-gray-500 mb-4 ml-11">充滿昭和風情的貓咪老街，傍晚光影最美。</p>
                <a href="https://maps.google.com/?q=Yanaka+Ginza" target="_blank" class="ml-11 block bg-gray-50 text-indigo-600 text-center text-sm font-bold py-2.5 rounded-xl border border-gray-200 active:bg-gray-100 transition">
                    <i class="fa-solid fa-location-dot mr-1"></i> 導航前往
                </a>
            </div>

            <div class="bg-white rounded-2xl p-5 mb-4 shadow-sm border border-gray-100 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-1.5 h-full bg-orange-400"></div>
                <div class="flex items-center mb-2">
                    <span class="text-gray-400 font-mono font-bold text-sm mr-3">晚上</span>
                    <h3 class="font-bold text-lg text-gray-900">名代 宇奈とと 上野店</h3>
                </div>
                <div class="ml-11 mb-3 flex flex-wrap gap-2">
                    <span class="badge-food text-xs font-bold px-2.5 py-1 rounded-lg"><i class="fa-solid fa-utensils mr-1"></i>雙倍鰻魚飯</span>
                </div>
                <p class="text-sm text-gray-500 mb-4 ml-11">吃完超高 CP 值的現烤鰻魚飯，順便逛阿美橫町！</p>
            </div>
        </div>

        <div id="day2" class="tab-content hidden">
            <div class="bg-white rounded-2xl p-8 text-center shadow-sm border border-gray-100 mt-10">
                <i class="fa-solid fa-tower-broadcast text-4xl text-indigo-300 mb-4"></i>
                <h3 class="font-bold text-gray-700 mb-2">Day 2 晴空塔</h3>
                <p class="text-sm text-gray-400">（套用相同卡片格式即可無限擴充）</p>
            </div>
        </div>

        </div>

    <div class="fixed bottom-0 left-0 w-full bg-white/90 backdrop-blur-lg border-t border-gray-200 pb-safe pt-2 px-6 flex justify-between items-center z-50 shadow-[0_-10px_20px_rgba(0,0,0,0.03)]" style="padding-bottom: env(safe-area-inset-bottom, 20px);">
        <button onclick="switchTab('day1', this)" class="nav-item flex flex-col items-center p-2 text-blue-600 w-16">
            <i class="fa-solid fa-plane-arrival text-xl mb-1"></i>
            <span class="text-[10px] font-bold">Day 1</span>
        </button>
        <button onclick="switchTab('day2', this)" class="nav-item flex flex-col items-center p-2 text-gray-400 hover:text-gray-600 transition w-16">
            <i class="fa-solid fa-tower-broadcast text-xl mb-1"></i>
            <span class="text-[10px] font-bold">Day 2</span>
        </button>
        <button onclick="switchTab('day3', this)" class="nav-item flex flex-col items-center p-2 text-gray-400 hover:text-gray-600 transition w-16">
            <i class="fa-solid fa-mountain-sun text-xl mb-1"></i>
            <span class="text-[10px] font-bold">Day 3</span>
        </button>
        <button onclick="switchTab('day4', this)" class="nav-item flex flex-col items-center p-2 text-gray-400 hover:text-gray-600 transition w-16">
            <i class="fa-solid fa-city text-xl mb-1"></i>
            <span class="text-[10px] font-bold">Day 4</span>
        </button>
    </div>
</div>

<script>
    function switchTab(tabId, element) {
        // 隱藏所有內容
        document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
        // 顯示目標內容
        document.getElementById(tabId).classList.remove('hidden');
        
        // 重置所有按鈕顏色
        document.querySelectorAll('.nav-item').forEach(btn => {
            btn.classList.remove('text-blue-600');
            btn.classList.add('text-gray-400');
        });
        
        // 點亮當前按鈕
        element.classList.remove('text-gray-400');
        element.classList.add('text-blue-600');
        
        // 讓頁面滾動回頂部
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
</script>

</body>
</html>
