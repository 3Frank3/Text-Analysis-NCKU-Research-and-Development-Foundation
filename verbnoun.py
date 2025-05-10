import jieba
import jieba.posseg as pseg

# 示例文本
text = '''

'''

# 初始化动词和名词的列表
verbs = []
nouns = []

# 使用 jieba 进行词性标注
words = pseg.cut(text)

# 遍历每个词语及其词性
for word, flag in words:
    if flag.startswith('v'):  # 动词以 'v' 开头
        verbs.append(word)
    elif flag.startswith('n'):  # 名词以 'n' 开头
        nouns.append(word)

print("动词:", verbs)
print("名词:", nouns)