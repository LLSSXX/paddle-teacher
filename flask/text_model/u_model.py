# -*- coding: utf-8 -*-
"""
Created on Mon April 22 2019

@author: kim
"""
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import jieba
import numpy as np
import os

# 取绝对路径
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# 模型路径
model_path = os.path.join(THIS_FOLDER, 'model', 'model.h5')

# 所有数据文件路径
all_data_path = os.path.join(THIS_FOLDER, 'data', 'Alldata.txt')

# 加载自定义分词词典
userdict_path = os.path.join(THIS_FOLDER, 'data', 'userdict.txt')
jieba.load_userdict(userdict_path)

#创建停用词列表
stopwords_path = os.path.join(THIS_FOLDER, 'data', 'stopwords.txt')
stopwordslist = [line.strip() for line in open(stopwords_path, 'r', encoding='utf-8', errors='ignore').readlines()]


def seg_sentence(sentence):
    # 定义去掉停用词的函数
    outstr = ''
    for word in sentence:
        if word not in stopwordslist:
            if word != ' ':
                outstr += word
                outstr += " "
    # 通过循环去掉停用词
    return outstr


def jieba_cut(sentence):
    # 定义分词函数
    sentence_cut = " ".join(jieba.lcut(sentence, cut_all=False))
    # 分词并以空格分隔
    cut_str = seg_sentence(sentence_cut.split(" "))
    # 调用去停用词函数
    return cut_str


def seqs_text(cut_str):
    # 定义序列化函数
    text = [cut_str]
    # 加载所有数据词组
    train_data = list(open(all_data_path, "r", encoding='utf-8').readlines())
    train_data = [s.strip() for s in train_data]
    # 形成词库
    tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=" ")
    tokenizer.fit_on_texts(train_data)
    # 序列化
    text_ids = tokenizer.texts_to_sequences(text)
    # 统一序列长度
    text_seqs = pad_sequences(text_ids, maxlen=64)
    return text_seqs


def chose_label(num):
    # 定义显示文本标签函数
    if num == 0:
        return 'pass'
    elif num == 1:
        return 'fail'
    elif num == 2:
        return 'undetermined'
    else:
        return 'error'


def use_model(text_str):
    # 定义模型函数
    cut_str = jieba_cut(text_str)
    # 分词
    text_seqs = seqs_text(cut_str)
    # 序列化
    text_model = load_model(model_path)
    # 加载模型
    predict_out = text_model.predict(text_seqs)
    # 用模型预测
    result_max = np.argmax(predict_out, axis=1)
    # 得出最大概率结果
    label = chose_label(result_max)
    # 将概率转换为实际标签
    return label


def test(text_str):
    # 测试函数
    cut_str = jieba_cut(text_str)
    print(cut_str)

    text_seqs = seqs_text(cut_str)
    print(text_seqs)

    text_model = load_model(model_path)

    predict_out = text_model.predict(text_seqs[:])
    print(predict_out)

    result_max = np.argmax(predict_out, axis=1)
    print(result_max)

    label = chose_label(result_max)
    print(label)


if __name__ == '__main__':
    test_text = '我要出国留学'
    test(test_text)
