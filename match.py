import pandas as pd

# 讀取Excel文件
df = pd.read_excel('Keywords.xlsx')

# 將數據轉換為字典
projects = {}
for index, row in df.iterrows():
    project_name = row['ProjectName']
    keywords = row[1:].dropna().tolist()  # 取出所有關鍵詞並去除NaN值
    projects[project_name] = keywords

# 打印生成的字典
print(projects)

# 定義一個函數來查找對應的專案名稱
def find_projects_by_keywords(keywords):
    keyword_to_projects = {}
    for keyword in keywords:
        keyword_to_projects[keyword] = []
        for project, project_keywords in projects.items():
            if keyword in project_keywords:
                keyword_to_projects[keyword].append(project)
    return keyword_to_projects

# 使用多行字符串來定義keywords_to_search
keywords_to_search = """
1 煉鋼業	創業	專業	電源	用電	工業	股份	有限公司	電業	產品	實驗	七股	作業	產業	公民營	事業	公車	車公里	實驗室	電場	畜牧業	產	精實	節電	真實	國產	企業	製造業	量產	電磁	電工	電網	電廠	產線	農業	公司	作業案	農產	阿公店	中小企業節	電能	實現	工業局	電夥伴節	發電機	電池	實業	光電	實務	風電	公共	電極	事業部	電壓	發電	糖業	公尺	業務	職業	作業化	學院	中華民國	醫療																						
2 處理	 設立	 變更	 管理	 研析	 分析	 研究	 調查	 設置	 處理	 試驗	 變遷	 研討	 合理	 掃	 瞄	 設備	 測	 研習	 有	 研磨	 變	 分身	 設計	 治理	 設定	 應變	 試燒	 劃分	 測驗	 直升	 量測	 預測	 觀測	 統計	 研	 投資	 分選	 測試	 投	 監調	 變化	 轄	 管	 管制	 感測	 計算	 調配	 建設	 解析	 探究	 查案	 調	 適	 試用																														
3 分散式	燃料	研究院	海運	方向	辦理	處分	資源	資料	方案	材料	研討會	合法	納管	機構	流量	護理	計劃	無機	安全帽	管道	異點	部分	設施	新設	機場	分包	機會	數值	數據	安平港	文測站	機制	參數	數位	品管	幹管	機器	手	機物	案	計量	感測器	地理	分局	有效性	成分	飼料	機械	方法	管理局	演算法	研提	情資	料	庫																													
4 編	 開發	 影響	 生產	 加工	 造	 轉爐	 發泡	 編	 影像	 光合	 模擬	 停車	 組織	 發酵	 備	 加速	 供應	 焚化	 回訓	 發生	 回彈	 承載	 育達	 回應	 合																																																											
5 電弧	 爐	 落塵	 南科	 技術	 人員	 美利	 盛達	 雷達	 轉型	 收益	 高科技	 電子	 圖	 金屬	 智慧	 模型	 模式	 醫院	 學術	 化	 精準	 醫療	 器材	 石	 材熱	 資訊	 衛星	 菌	 海科	 車橋	 雛型	 建材	 光學	 觀光	 銅粉	 科技	 科學	 智能	 訊	 區塊	 鏈	 邊坡	 路	 農科	 顧問	 顧問班	 藝術	 空間	 邊緣	 粉體	 空庫	 模組	 訊息	 空氣	 車流	 生醫	 半導體	 教材	 智晶	 光	 金亞	 竹科	 濾材	 高爐	 爐床	 零星	 碳	 金海岸	 金門	 載台	 金奈米	 問卷	 問題	 收容										
6 服務案	服務	港務	勞務	事務																																																																																
7 評估	評定	估算	推估	評估案																																																																																
8 廢棄物	環境	保護	物質	環保	生態環境	生態	建物	態度	情境	環保署	保育	生物	品質	植生	保溫	瑞環	循環	保維	優質	地質	生活	固態	化合物	前驅物	氨氮化合物	基質	添加物	微生物	再	污染物	氧化物	生命	保持	構造物	物化	藥物	雙生	高校生	物化性																																													
9 濕地	足跡	庫	伏流水	地下水	水	水文	國土	地形	水井	用水	地形圖	衛生	水管	水庫	海水	下	水泥	混凝土	水質	地號	水利	地	水工	廢	下陷	水域	張力	土石流	人力	用水閥	土砂	地表	節水	台水	地下水層	風力	北水處	在地好味	土壤	文	水電	水庫庫區	曾文	水保	水力	崩塌地	地層	水患	競爭力	僑力	抗病力	水泵站	污水	水土	柴山泊地	地下	地熱	碳足跡	淨水廠	水庫量	水堰	水源																						
10 監測	認證	檢視	盤查	查證	監測案	改善	驗證	查核	檢測	監審案	監控	巡查	檢核	檢討	審驗	監造	善化	控制	標檢局	監測站	檢驗	巡檢	盤點	圓盤																																																												
11 改版																																																																																				
12 台灣區	園區	區	桃廠	大林廠	花蓮縣	臺灣	國家	國際	高雄市	政府	煉油廠	機台	嘉義縣	工廠	楠梓區	左營區	鼓山區	旗津區	小港區	嘉義市	專家	集團	沿海路	潛勢區	區域	大鵬灣	風景區	家園	集水區	廠	興中路	平台	台灣	段轄區	路面	市場	澎湖縣	碼頭區	交通	台北市	內湖區	康寧段	段	臺南市	永安廠	路	白河段	轄區	路段	階段	鄉鎮市	科學園區	花蓮處轄	港區	頻段	雲林縣	土砂區	社區	公路	臺東縣	直轄市	縣	市	家	廠商	處理廠	郵政	南區	地區	北中區	新北市	石碇區	保持區	港港區浚	填方區	新營段	集	台積	台南市	灣裡	安順廠	魚塭區	中華民國	工業區

""".strip().split()

matching_projects_dict = find_projects_by_keywords(keywords_to_search)

# 打印每個關鍵詞對應的專案名稱
for keyword, matching_projects in matching_projects_dict.items():
    print(f"Projects matching the keyword '{keyword}': {matching_projects}")

# 將結果轉換為DataFrame
results_list = []
for keyword, matching_projects in matching_projects_dict.items():
    for project in matching_projects:
        results_list.append({"Keyword": keyword, "ProjectName": project})

results_df = pd.DataFrame(results_list)

# 將結果寫入新的Excel文件
results_df.to_excel('matching_projects.xlsx', index=False)

print("Results have been written to 'matching_projects.xlsx'")
