

def find_related_terms(text, target_term, window_size):
    words = text.split()  # 假設文本已經斷好詞，用空格分隔
    related_terms = []

    for i in range(len(words)):
        if words[i] == target_term:
            # 提取窗口內的詞
            start = max(0, i - (window_size // 2))
            end = min(len(words), i + (window_size // 2) + 1)
            related_terms.append(words[start:end])

    return related_terms

# 示例文本
text = "這 是 一個 包含 技術 和 其他 詞語 的 示例 文本 ， 我們 要 找到 技術 前後 的 相關 詞 。"

# 找到“技術”的相關詞
related_terms = find_related_terms(text, "技術",4)
for terms in related_terms:
    print("相關詞:", terms)
print("finish")
