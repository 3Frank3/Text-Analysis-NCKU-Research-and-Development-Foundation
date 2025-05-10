import pandas as pd
from fuzzywuzzy import fuzz

# 設定詞彙集合
vocabulary = '''
																																																																																																																																																																																																																																																																								
'''
vocabulary = vocabulary.split()

# 定義類別列表
categories = {
    "機構、產業": ["公司", "股份", "有限公司", "企業", "實業", "電廠","產業"],
    "研究方法": ["分析","設計","工程"," 開發", "工作"," 發展","處理","治理","計算","解析","研擬"," 遙測","管理"],
    "研究資源、類型": ["設施","電源","有機物","研究", "方法","數據", "資安", "資料","設備","材料","課程"],
    "技術": [ "掃瞄","電子","醫療","技術", "掃瞄", "資訊", "工程", "區塊鏈", "光達", "衛星影像", "空載", "ISO", "精密", "金屬加工", "電弧爐粉塵回收製程", "水工模型試驗", "科技", "智慧", "開發", "顧問", "電材", "智慧生產", "智慧路邊停車服務"],
    "服務": ["服務","勞務"],
    "評估": ["評估","評測","觀測","管控"],
    "檢測、審查": ["審查","檢測","測試", "盤查", "監測","查證","查","調查","預測","偵測","試驗"],
    "環境生態": ["環境", "生物" ,"生態","再生", "循環", "生質","環保","變遷"],
    "水文": ["地下水","水庫","水質","水文","水力","水土","廢水","水","水足跡", "環境", "衛生"],
    "地點與區域": ["區", "段", "廠", "路", "台灣", "公園", "水庫集水區", ]
}

# 創建空字典，用於存放每個類別的詞彙
category_words = {category: [] for category in categories}

# 分類詞彙
for word in vocabulary:
    max_ratio = 0
    max_category = None
    for category, keywords in categories.items():
        for keyword in keywords:
            ratio = fuzz.ratio(word, keyword)
            if ratio > max_ratio:
                max_ratio = ratio
                max_category = category

    # 確保每個詞彙都被分類到最相似的類別中
    if max_category is not None:
        category_words[max_category].append(word)

# 將分類結果轉換成 DataFrame
max_length = max(len(words) for words in category_words.values())
filled_category_words = {category: words + [''] * (max_length - len(words)) for category, words in category_words.items()}
df = pd.DataFrame(filled_category_words)

# 將 DataFrame 寫入 Excel 檔案
df.to_excel("category_result_year(103~113).xlsx", index=False)

# Print the DataFrame
print(df)
