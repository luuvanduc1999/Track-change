from colorama import Fore,Back,init
import numpy as np
import sys
from halo import Halo
import os

def split_string(source):
    splitlist = ",!.;? "
    output = [" "]
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
            output[-1] = output[-1]+char
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1] + char
    return output

def Optimize(BEGIN,END):
    X= split_string(BEGIN)
    Y= split_string(END)
    m=len(X)
    n=len(Y)

#   KHỞI TẠO GTRI
    F=np.zeros((m+1,n+1))
    for i in range(m+1):
        F[i][-1]=sys.maxsize

    for j in range(n+1):
        F[-1][j]=sys.maxsize

    for j in range(n+1):
        F[0][j]=j
    for i in range(1,m+1):
        F[i,0]=i

#   QHĐ
    for i in range(1,m):
        for j in range(1,n):
            if (X[i]==Y[j]):
                F[i][j]=F[i-1][j-1]
            else:
                F[i][j]=min(F[i][j-1],F[i-1][j]) +1

#   TRUY VẾT
    i=m-1
    j=n-1
    while (i!=0)|(j!=0):
        if X[i]==Y[j]:
            i-=1
            j-=1
        elif F[i,j]==F[i,j-1]+1:
            Y[j]=Back.GREEN+Y[j][0:-1]+Back.RESET+Y[j][-1]
            j-=1
        elif F[i,j]==F[i-1][j]+1:
            X[i]=Back.RED+X[i][0:-1]+Back.RESET+X[i][-1]
            i-=1

#
    print("\n\n","".join(X))
    print("\n\n","".join(Y),"\n\n")



init(autoreset=True)
os.system('cls')
BEGIN="Khoảng cách giữa cực bắc nam Việt Nam theo đường chim bay là 1650km. Vị trí chiều ngang hẹp nhất ở Quảng Bình chưa đầy 50 km. Đường biên giới đất liền dài 4.550 km."
END = "K/c giữa hai cực bắc nam Việt Nam tính theo đường chim bay là 1650km. Chiều ngang hẹp nhất ở Quảng Bình chưa tới 50 km. Đường biên giới đất liền dài 4.550 (km)."
Optimize(BEGIN,END)


