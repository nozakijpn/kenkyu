import numpy as np

flame_time = 0.02321995464 #vdetの１フレームの秒数
time_th = 0.5 #インターバルの時間の閾値
newsname = "NHK0826"

f = open("timeline.txt","r")#音声切り出しのテキスト
strings = f.readlines()

st = []
end = []

for line in trings:
	data = line.split(" ")

	st.append(data[2])#発話区間の始まりの配列
	end.append(data[3])#発話区間の終わりの配列

f.close


f = open("","r")#音源識別のテキスト(_02)
strings = f.readlines()
audio_d = [] #音源識別結果の配列
for item in strings:
	audio_d.append(int(item))

interval_list = []#発話の間の種類の配列
flag = 0
sox_cnt = 0
for i,item1 in enumerate(st):
	cnt_speech_interval = 0
	if(i != 0):
		time_div = float(st[i])-float(end[i-1])#一つ前の発話と今の発話と間のインターバルの秒数を計算

		#stとendの小数点大２位以下を切り捨てる必要あり？

		cnt_2,cnt_3,cnt_4 = 0,0,0
		for time in range(float(end[i-1]),float(st[i]),0.01):
			now_time = time * flame_time#正確な秒数を書く必要あり。配列に入れるために100倍とかにする必要あり？
			
			if(time[not_time]==2):
				cnt_2 += 1#BGMの区間数をカウント
			if(time[not_time]==3):
				cnt_3 += 1#ノイズの区間数をカウント
			if(time[not_time]==4):
				cnt_4 += 1#pauseの区間数をカウント

			cnt_speech_interval += 1

		sub_li = [np.array(cnt_2).shape,np.array(cnt_3).shape,np.array(cnt_4).shape] 
		interbal_list.append(argmax(sub_li)+2)#発話の間のインターバルの種類を配列に格納




		"""
		場合分けをする部分が増えた
		前だけではなく、後ろも見る必要がある。
		そのため、ループ中ではなく、ループが終わった後に結合の手順を行う
		"""
	
		if(sub_li + 2 == 4):#インターバルがpauseのとき
			if(cnt_speech_interval * flame_time < time_th):#インターバルが短い時
				#つなげる処理をおこなう
				if(flag == 0):

			else:
				#分ける処理を行う
				if(flag == 0):#結合するファイルが一つもない時
					f.write("cp {}_{:04d}.wav {}_{:04d}.wav".format(newsname,i,newsname,sox_cnt))
				else:#二つ以上、結合するファイルが存在する時
					f.write("{}_{:04d}.wav¥n".format(newsname,i))
					flag += 1
				sox_cnt += 1
				flag = 0
		else:#インターバルがBGMもしくはNoiseのとき
			if(interval_list[i-1] == interval_list[i-2] and nt_speech_interval * flame_time < time_th):
				"""
				つなげる処理をおこなう
				"""
			else:
				"""
				分ける
				"""


