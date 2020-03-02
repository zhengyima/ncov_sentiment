#coding=utf-8
import json
import csv
label_list = ["0","1","-1"]
puncs = ['【','】',')','(','、','，','“','”',
		'。','《','》',' ','-','！','？','.',
		'\'','[',']','：','/','.','"','\u3000',
		'’','．',',','…','?',';','·','%','（',
		'#','）','；','>','<','$', ' ', ' ','\ufeff'] 
					 
train_f = open("/home/zhengyi_ma/ncov_sentiment/dataset/nCoV_100k_train.labled.csv",'r')
train_list = []
for line in train_f:
	# print(len(line.strip().split(",")))
	weiboId, weiboTime, userid, text, img, video, label = next(csv.reader(line.splitlines(), skipinitialspace=True))
	# if len(line_cols) != 7:
	#     print(line_cols)
	if label not in label_list:
		continue
	train_list.append([text, label])
	# weiboId, weiboTime, userid, text, img, video, label =  line.strip().split(",")
train_f.close()

train_end = int(len(train_list) * 1)
dev_end = int(len(train_list) * 0.9)

f_w_train = open("/home/zhengyi_ma/ncov_sentiment/dataset_bert/train.tsv","w")
for i in range(0, train_end):
	f_w_train.write(train_list[i][0] + "\t" + train_list[i][1] + "\n")
f_w_train.close()

f_w_train = open("/home/zhengyi_ma/ncov_sentiment/dataset_bert/dev.tsv","w")
for i in range(train_end+ 1, dev_end):
	f_w_train.write(train_list[i][0] + "\t" + train_list[i][1] + "\n")
f_w_train.close()


test_f = open("/home/zhengyi_ma/ncov_sentiment/dataset/nCov_10k_test.csv",'r')
test_list = []
for line in test_f:
	# print(len(line.strip().split(",")))
	weiboId, weiboTime, userid, text, img, video = next(csv.reader(line.splitlines(), skipinitialspace=True))
	# if len(line_cols) != 7:
	#     print(line_cols)
	test_list.append([text, "0"])
	# weiboId, weiboTime, userid, text, img, video, label =  line.strip().split(",")
test_f.close()

f_w_train = open("/home/zhengyi_ma/ncov_sentiment/dataset_bert/test.tsv","w")
for i in range(len(test_list)):
	f_w_train.write(test_list[i][0] + "\t" + test_list[i][1] + "\n")
f_w_train.close()