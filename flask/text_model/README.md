# 模型使用说明

这是一个多文本分类模型，包含两个文件夹及一个model.py文件

data文件夹下存放包含所有数据的文本文件(Alldata.txt)和 用于预处理的两个文本文件(stopwords.txt与userdict.txt)

在后端使用如下语句可导入并使用模型：



```python
from model import model
# 导入语句
label = model(text)
'''
使用语句如上：
其中text代表需要判断的申请理由
label代表模型返回的标签
'''
```

**请注意返回的label会有四个：pass、fail、undetermined和error**

其中：

* pass代表审核通过
* fail代表审核失败
* undetermined代表出国待定
* error代表模型判断时出错了

有任何问题及时沟通奥～