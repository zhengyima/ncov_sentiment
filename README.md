
# NCOV_Sentiment

NCOV_Sentiment Source Code 

[疫情期间网民情绪识别比赛](https://www.datafountain.cn/competitions/423)baseline，使用BERT进行端到端的fine-tuning，平台评测F1值0.716。

很基础的基线，只用了labeled数据，没有利用unlabeled数据，没有调参。

# Preinstallation

Before launch the script install these packages in your **Python3** environment:
- tensorflow 1.11

建议使用Conda安装 :) 


```
 conda create -n tf1.11 python=3.6 tensorflow=1.11 tensorflow-gpu=1.11
 conda activate tf1.11
```

下载[Bert中文模型](https://github.com/google-research/bert)至本地，并更改[bert/run.sh](https://github.com/zhengyima/ncov_sentiment/blob/master/bert/run.sh)中的BERT_BASE_DIR路径。

在datafountain平台上下载数据，解压至本地目录。**将数据由gbk转为utf-8编码(vscode或linux shell的iconv命令)**

运行数据预处理脚本[dataprocess/data_process.py](https://github.com/zhengyima/ncov_sentiment/blob/master/dataprocess/data_process.py)，将数据处理成bert的输入格式。（注意更改代码中的输出路径，并保持输出路径与[bert/run.sh](https://github.com/zhengyima/ncov_sentiment/blob/master/bert/run.sh)中的NCOV_DIR路径一致。

```
 python dataprocess/data_process.py
```


更改[bert/run.sh](https://github.com/zhengyima/ncov_sentiment/blob/master/bert/run.sh)中的OUTPUT_DIR路径为模型及结果输出路径。


# Launch the script

环境配好，模型下好之后便可以运行代码了！

```
 bash bert/run.sh
```



## Links
- https://github.com/google-research/bert

