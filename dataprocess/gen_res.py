#coding=utf-8
import csv


result_path = "/home/zhengyi_ma/ncov_sentiment/output/test_results.tsv"
out_path = "/home/zhengyi_ma/ncov_sentiment/output/test_results_out.tsv"


test_f = open("/home/zhengyi_ma/ncov_sentiment/dataset/nCov_10k_test.csv",'r')
test_list = []
for line in test_f:
	# print(len(line.strip().split(",")))
	weiboId, weiboTime, userid, text, img, video = next(csv.reader(line.splitlines(), skipinitialspace=True))
	# if len(line_cols) != 7:
	#     print(line_cols)
	test_list.append(weiboId.strip())
	# weiboId, weiboTime, userid, text, img, video, label =  line.strip().split(",")
test_f.close()


f = open(result_path,'r')
fw = open(out_path,"w")
cnt = 1
for line in f:
    ps = line.strip().split("\t")
    assert len(ps) == 3
    ps[0] = float(ps[0])
    ps[1] = float(ps[1])
    ps[2] = float(ps[2])  
    max_index = ps.index(max(ps))  
    if max_index == 0:
        label = 0
    elif max_index == 1:
        label = 1
    elif max_index == 2:
        label = -1
    fw.write(test_list[cnt] + "," + str(label)+"\n")
    cnt += 1
fw.close()
    