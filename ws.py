from ckiptagger import data_utils,WS
import pandas as pd

data_utils.download_data_gdown("./")

ws = WS("./data")

df = pd.read_csv("1130424.csv")

sentence_list = df["名稱"]

word_sentence_list = ws(sentence_list)

print(word_sentence_list)

result_df = pd.DataFrame(columns=["名稱"])


for idx, word_sentence in enumerate(word_sentence_list):
    if isinstance(word_sentence, list):
        for i, word in enumerate(word_sentence):
            col_name = f"斷詞結果_{i}"  # 動態生成列名
            if col_name not in result_df.columns:  # 如果列名還不存在，則創建這一列
                result_df[col_name] = ""
            result_df.loc[idx, col_name] = word  # 將斷詞結果存入對應的列中
        result_df.loc[idx, "名稱"] = sentence_list[idx]  # 放入原始資料到 "名稱" 欄位

print(result_df)

output_csv_file_path = "ws.csv"

result_df.to_csv(output_csv_file_path, index=False)