#�@�~ 1.
# �аѦҤW�ҡA�ۤv�g�@�ӱN�G�i���ܼ��ର�Q�i���禡�ѵy�᪺�@�~�ϥΡG

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    number =110001
    print("�G�i��Ʀr{0}���Q�i���ܪk���G{1}".format(number,bin2int(number)))

def bin2int(N):
    L = int(len(str(N)))  
    A = 0                
    K = 0
    while L > K :        
        r = int(N%10)    
        A = A + (2**K)*r 
        N = N/10         
        K = K + 1        
        
    str(A)               
    return str(A)

if __name__ == "__main__":
    main()





class HW02:
    def ch2(self):
        '''
        �бN�A�p��X�Ӫ����׶�J�H�U�ܼơA�U�з|�g�{���۰ʧ��C
        Ch2P2_19a = "xxx"
        �N��O
        Ch2   : �ĤG��
        P2_19a: �ĤG�������B�� PRACTICE SET �q���B�� Problems �� P2-19 �D�� a �p�D
        "xxx" �G �A�n��J�A�����צb xxx �o�̡C
        '''
        #�@�~ 2. �ҥ� Ch2. P2.19
        self.Ch2P2_19a = "10"
        self.Ch2P2_19b = "17"
        self.Ch2P2_19c = "6"
        self.Ch2P2_19d = "8"

        #�@�~ 3. �ҥ� Ch2. P2.20
        self.Ch2P2_20a = "15"
        self.Ch2P2_20b = "9"
        self.Ch2P2_20c = "14"
        self.Ch2P2_20d = "5"

        #�@�~ 4. �ҥ� Ch2. P2.22
        self.Ch2P2_22a = "00010001 11101010 00100010 00001110"
        self.Ch2P2_22b = "00001110 00111000 11101010 00111000"
        self.Ch2P2_22c = "01101110 00001110 00111000 01001110"
        self.Ch2P2_22d = "00011000 00111000 00001101 00001011"


    def ch3(self):
        '''
        �бN�A�p��X�Ӫ����׶�J�H�U�ܼơA�U�з|�g�{���۰ʧ��C
        Ch3P3_28a = "xxx"
        �N��O
        Ch3   : �ĤT��
        P3_28a: �ĤT�������B�� PRACTICE SET �q���B�� Problems �� P3-28 �D�� a �p�D
        "xxx" �G �A�n��J�A�����צb xxx �o�̡C
        '''
        #�@�~ 5. �ҥ� Ch3. P3.28
        self.Ch3P3_28a = "234"
        self.Ch3P3_28b = "overflow"
        self.Ch3P3_28c = "874"
        self.Ch3P3_28d = "888"

        #�@�~ 6. �ҥ� Ch3. P3.30
        self.Ch3P3_30a = "234"
        self.Ch3P3_30b = "overflow"
        self.Ch3P3_30c = "875"
        self.Ch3P3_30d = "889"
