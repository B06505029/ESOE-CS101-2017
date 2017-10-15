﻿#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。




if __name__== "__main__":
	#inputSTR=input("input something")
	def charFreqLister(inputSTR):
		resultLIST =[]
		freq = {}
    
		for x in inputSTR:
			freq[x] = inputSTR.count(x) 
			freq[x]=  freq[x]/len(inputSTR)   
		for y in freq:
			resultLIST.append((freq[y], y))
    
		resultLIST.sort(key=lambda input:input[0], reverse=False)
		#i=0
		#while i<len(resultLIST):
			#print (resultLIST[i])
			#i=i+1

		
		return resultLIST


	#charFreqLister(inputSTR)
	

# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
	def huffmanTranslater(inputSTR):
	
	
		resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]
    
    
    
    
		return resultLIST
	
# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
	def condNOT(inputSTR_X):
		outputSTR = ""
		for i in inputSTR_X:
			if i == "0":
				outputSTR = outputSTR + "1"
			else:
				outputSTR = outputSTR + "0"
		return outputSTR

#condition00 and condition02
	def condAND(inputSTR_X, inputSTR_Y):
		output= ""    
		for (x,y) in zip(inputSTR_X,inputSTR_Y):
			if x=="1" and y =="1":
				output = output + "1"
			else: 
				output = output + "0"
        
    
		return output

#condition00 or condition03
	def condOR(inputSTR_X, inputSTR_Y):
		output = ""
		for (x,y) in zip(inputSTR_X,inputSTR_Y):
			if x=="0" and y=="0":
				output = output + "0"
			else:
				output = output + "1"
        
    
    
    
		return output

#condition00 xor condition04
	def conXOR(inputSTR_X, inputSTR_Y):
		output = ""
		for (x,y) in zip(inputSTR_X,inputSTR_Y):
			if x == "0" and y =="0":
				output = output + "0"
			elif x == "1" and y == "1":
				output = output + "0"
			else: 
				output = output + "1"
            
		return output







	#condition00X = ""
    #condition00Y = ""

    #condition01 = condNOT(condition00X)
    #print(condition01)

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    # Ch3 表示為第三章
    # P3_20a 表示為該章最後 Problem 處的 P3-20 題的第 a 小題。
    
	print("Ans:")
	Ch3P3_20a = "0 10000001 000 0000 0000 0000 0011 0011"
	Ch3P3_20b = "1 10000010 000 0000 0000 0001 0010 1001"
	Ch3P3_20c = "0 10000010 000 0000 0000 0000 0110 1101"
	Ch3P3_20d = "1 01111101 000 0000 0000 0000 0000 0001"
	print("========")
	Ch3P3_28a = "234"
	Ch3P3_28b = "overflow"
	Ch3P3_28c = "874"
	Ch3P3_28d = "888"
	print("========")
	Ch3P3_30a = "235"
	Ch3P3_30b = "overflow"
	Ch3P3_30c = "875"
	Ch3P3_30d = "889"
	print("========")
	Ch4P4_3a = "0x99"
	Ch4P4_3b = "0x99"
	Ch4P4_3c = "0xFF"
	Ch4P4_3d = "0xFF"
	print("========")
	Ch4P4_4a = "0x66"
	Ch4P4_4b = "0xFF"
	Ch4P4_4c = "0x11"
	Ch4P4_4d = "0xBB"
	print("========")
	Ch4P4_13a = "1184"
	Ch4P4_13b = "-862"
	Ch4P4_13c = "862"
	Ch4P4_13d = "-1184"
	print("========")
	Ch4P4_15a = "X"
	Ch4P4_15b = "X"
	Ch4P4_15c = "X"
	Ch4P4_15d = "O"
	print("========")
	Ch4P4_16a = "0xF51"
	Ch4P4_16b = "overflow"
	Ch4P4_16c = "0x8012"
	Ch4P4_16d = "overflow"