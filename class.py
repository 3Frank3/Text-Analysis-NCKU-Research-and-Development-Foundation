# -*- coding: utf-8 -*-import pandas as pd
import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# 下載並載入預訓練的GloVe模型
glove_model = api.load("glove-wiki-gigaword-50")

# 定義詞彙和類別的字典
categories = {
    "企業社會責任CSR報告書輔導": ["企業", "社會", "責任", "CSR", "報告書", "輔導"],
    "能源管理輔導": ["能源", "管理","輔導","資源"],
    "節能減碳、碳足跡": ["碳", "碳標籤", "節能", "碳標籤","減碳","足跡","碳足跡"],
    "AEO制度和供應鏈管理": ["AEO", "制度", "輔導","建置","供應鏈"],
    "循環永續": ["循環", "永續", "環保","溫室","氣體","綠色","環境","盤查"],
    "企業、公司": ["有限公司", "股份", "企業","公司","製造業","產業","組織"],
    "技術": ["系統", "科技", "技術","分析","電子","科學"],
}

# 待分類的詞彙列表
words = ["企業能源管理節能系統試點示範專案","「組織型溫室氣體盤查與產品碳足跡」建置工作"]



# 建立分類結果的字典
classified_words = {category: [] for category in categories}

# 將詞彙分類到對應的類別
for word in words:
    for category, keywords in categories.items():
        if word in keywords:
            classified_words[category].append(word)
            break

# 將分類結果轉換為DataFrame
df = pd.DataFrame(dict([(k, pd.Series(v, dtype='object')) for k, v in classified_words.items()]))
print(df)

'''
# 將 DataFrame 寫入 Excel 檔案
output_file = "classified.xlsx"
df.to_excel(output_file, index=False)

print(f"分類結果已成功輸出到 {output_file}")
'''