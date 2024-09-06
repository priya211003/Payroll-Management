import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
payroll=pd.read_csv(r"C:\Users\akaak\Downloads\SampleData.csv")
print("1 Displaying employee's details")
print("2 Displaying employee's salary details")
print("3 Add employee")
print("4 Add more information")
print("5 Displaying specific information about the employees")
print("6 Add Special Allowance")
print("7 Add Promotion")
print("8 Add Bonus")
print("9 Add Spot Bonus")
print("10 Display information about specific employee")
print("11 Fire employee")
print("12 Display employee details of specific grade")
print("13 Find the high salaried")
print("14 Low salaried")
print("15 Grade System Visualization")
print("16 Quit")
for x in range(20):
    a=int(input('Enter the option(1-16)'))
    if(a==1):
        print(pd.DataFrame(payroll,columns=['Employee_code','Employee_Name',' Employee_Surname','DOB','Date _of_Joining','Designation','Grade'],index=[1,2,3,4,5,6,7,8,9,10]))
    elif(a==2):
        print(pd.DataFrame(payroll,columns=['Employee_Name',"PF_No","PAN","Bank_Name","Account_No","Basic_Salary","House_Rent_Allowance","Medical_Allowance","Travel_Allowance","Lunch_Allowance","Bus_Deduction","PF","Gross_Earnings","Gross_Deduction","Net_Pay"],index=[1,2,3,4,5,6,7,8,9,10]))
    elif(a==3):
        s=int(input('Employee code:'))
        d=str(input('Employee name(in caps):'))
        f=str(input('Employee surname(in caps):'))
        g=int(input('D.O.B(ddmmyyyy):'))
        h=int(input('Date of Joining(ddmmyyyy):'))
        j=str(input('PF No.:'))
        k=str(input('PAN:'))
        l=str(input('Bank Name:'))
        z=int(input("Account No.:"))
        x=int(input('Basic Salary:'))
        v=int(input('Medical  Allowance:'))
        b=int(input("Travel Allowance:"))
        n=int(input('Lunch Allowance:'))
        m=int(input('Bus Deduction:'))
        c=(x)/2
        q=(x)*0.125
        w=v+b+n+x
        e=m+q
        r=w-e
        y=pd.DataFrame([s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,q,w,e,r],columns=['Employee_code','Employee_Name',' Employee_Surname','DOB','Date _of_Joining','Designation','Grade',"PF_No","PAN","Bank_Name","Account_No","Basic_Salary","House_Rent_Allowance","Medical_Allowance","Travel_Allowance","Lunch_Allowance","Bus_Deduction","PF","Gross_Earnings","Gross_Deduction","Net_Pay"])
        u=pd.Dataframe(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        i=u.append(y)
        print(i)
    elif(a==4):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        cn=str(input('Information needed to be added is:'))
        po=int(input('enter the position of the column(1-22):'))
        e1=str(input('Employee code 966732:'))
        e2=str(input('Employee code 966733:'))
        e3=str(input('Employee code 966734:'))
        e4=str(input('Employee code 966735:'))
        e5=str(input('Employee code 966736:'))
        e6=str(input('Employee code 966737:'))
        e7=str(input('Employee code 966738:'))
        e8=str(input('Employee code 966739:'))
        e9=str(input('Employee code 966740:'))
        e10=str(input('Employee code 966741:'))
        df.insert(loc=(po-1),column=cn,value=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10])
        print(df)
    elif(a==5):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        s=int(input('choose the column to be displayed (1-21):\n1.Employee_code\n2.Employee_Name\n3.Employee_Surname\n4.DOB \n5.Date _of_Joining\n6.Designation\n7.Grade\n8.PF_No\n9.PAN\n10.Bank_Name\n11.Account_No\n12.Basic_Salary\n13.House_Rent_Allowance\n14.Medical_Allowance\n15.Travel_Allowance\n16.Lunch_Allowance\n17.Bus_Deduction\n18.PF\n19.Gross_Earnings\n20.Gross_Deduction\n21.Net_Pay'))
        if(s==1):
            print(df[['Employee_Name','Employee_code']])
        if(s==2):
            print(df['Employee_Name'])
        if(s==3):
            print(df[['Employee_Name','Employee_Surname']])
        if(s==4):
            print(df[['Employee_Name','DOB']])
        if(s==5):
            print(df[['Employee_Name','Date_of_Joining']])
        if(s==6):
            print(df[['Employee_Name','Designation']])
        if(s==7):
            print(df[['Employee_Name','Grade']])
        if(s==8):
            print(df[['Employee_Name','PF_No']])
        if(s==9):
            print(df[['Employee_Name','PAN']])
        if(s==10):
            print(df[['Employee_Name','Bank_Name']])
        if(s==11):
            print(df[['Employee_Name','Account_No.']])
        if(s==12):
            print(df[['Employee_Name','Basic_Salary']])
        if(s==13):
            print(df[['Employee_Name','House_Rent_Allowance']])
        if(s==14):
            print(df[['Employee_Name','Medical _Allowance']])
        if(s==15):
            print(df[['Employee_Name','Travel_Allowance']])
        if(s==16):
            print(df[['Employee_Name','Lunch_Allowance']])
        if(s==17):
            print(df[['Employee_Name','Bus_Deduction']])
        if(s==18):
            print(df[['Employee_Name','PF']])
        if(s==19):
            print(df[['Employee_Name','Gross_Earnings']])
        if(s==20):
            print(df[['Employee_Name','Gross_Deduction']])
        if(s==21):
            print(df[['Employee_Name','Net_Pay']])
        if(s>21):
            print('Check The Number And Run The Program Again!!!')
        if(s<1):
            print('Check The Number And Run The Program Again!!!')
    elif(a==6):
        s=float(input('Amount(in numbers):'))
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        df['Special_Allowance']=s
        df['Gross_Earnings']=df['Gross_Earnings']+s
        df['Net_Pay']=df['Net_Pay']+s
        print(df[['Employee_Name','Special_Allowance','Gross_Earnings','Net_Pay']])
    elif(a==7):
       df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
       s=int(input('Choose the Employee (1-10):\n1.XX\n2.YY\n3.ZZ\n4.AA\n5.GG\n6.HH\n7.TT\n8.JJ\n9.LL\n10.SS'))
       if(s==1):
           df.iat[1,20]=df.iat[1,20]+5000.00
           df.iat[1,6]=df.iat[1,6]+1
           print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==2):
           df.iat[2,20]=df.iat[2,20]+5000.00
           df.iat[2,6]=df.iat[2,6]+1
           print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==3):
           df.iat[3,20]=df.iat[3,20]+5000
           df.iat[3,6]=df.iat[3,6]+1
           print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==4):
           df.iat[4,20]=df.iat[4,20]+5000
           df.iat[4,6]=df.iat[4,6]+1
           print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==5):
          df.iat[5,20]=df.iat[5,20]+5000
          df.iat[5,6]=df.iat[5,6]+1
          print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==6):
          df.iat[6,20]=df.iat[6,20]+5000
          df.iat[6,6]=df.iat[6,6]+1
          print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==7):
          df.iat[7,20]=df.iat[7,20]+5000
          df.iat[7,6]=df.iat[7,6]+1
          print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==8):
          df.iat[8,20]=df.iat[8,20]+5000
          df.iat[8,6]=df.iat[8,6]+1
          print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==9):
          df.iat[9,20]=df.iat[9,20]+5000
          df.iat[9,6]=df.iat[9,6]+1
          print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s==10):
          df.iat[10,20]=df.iat[10,20]+5000
          df.iat[10,6]=df.iat[10,6]+1
          print(df[['Employee_Name','Grade','Net_Pay']].head(1))
       if(s>10):
          print('Check The Number And Run The Program Again!!!')
       if(s<1):
          print('Check The Number And Run The Program Again!!!')
    elif(a==8):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        s=float(input('Bonus Amount:'))
        df['Net_Pay']=df['Net_Pay']+s
        df['Bonus']=s
        df['Gross_Earnings']=df['Gross_Earnings']+s
        print(df[['Employee_Name','Bonus','Gross_Earnings','Net_Pay']])
    elif(a==9):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        s=float(input('Amount:'))
        d=int(input('Choose the Employee (1-10):\n1.XX\n2.YY\n3.ZZ\n4.AA\n5.GG\n6.HH\n7.TT\n8.JJ\n9.LL\n10.SS'))
        if(d==1):
            df['Spot_Bonus']=[s,0,0,0,0,0,0,0,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==2):
            df['Spot_Bonus']=[0,s,0,0,0,0,0,0,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==3):
            df['Spot_Bonus']=[0,0,s,0,0,0,0,0,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==4):
            df['Spot_Bonus']=[0,0,0,s,0,0,0,0,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==5):
            df['Spot_Bonus']=[0,0,0,0,s,0,0,0,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==6):
            df['Spot_Bonus']=[0,0,0,0,0,s,0,0,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==7):
            df['Spot_Bonus']=[0,0,0,0,0,0,s,0,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==8):
            df['Spot_Bonus']=[0,0,0,0,0,0,0,s,0,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==9):
            df['Spot_Bonus']=[0,0,0,0,0,0,0,0,s,0]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d==10):
            df['Spot_Bonus']=[0,0,0,0,0,0,0,0,0,s]
            df['Gross_Earnings']=df['Gross_Earnings']+df['Spot_Bonus']
            df['Net_Pay']=df['Net_Pay']+df['Spot_Bonus']
            print(df[['Employee_Name','Spot_Bonus','Gross_Earnings','Net_Pay']])
        if(d>10):
            print('Check The Number And Run The Program Again!!!')
        if(d<1):
            print('Check The Number And Run The Program Again!!!')
    elif(a==10):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        s=int(input('Choose the Employee (1-10):\n1.XX\n2.YY\n3.ZZ\n4.AA\n5.GG\n6.HH\n7.TT\n8.JJ\n9.LL\n10.SS'))
        if(s==1):
            print(df.loc[1,:])
        if(s==2):
            print(df.loc[2,:])
        if(s==3):
            print(df.loc[3,:])
        if(s==4):
            print(df.loc[4,:])
        if(s==5):
            print(df.loc[5,:])
        if(s==6):
            print(df.loc[6,:])
        if(s==7):
            print(df.loc[7,:])
        if(s==8):
            print(df.loc[8,:])
        if(s==9):
            print(df.loc[9,:])
        if(s==10):
            print(df.loc[10,:])
        if(s>10):
            print('Check The Number And Run The Program Again!!!')
        if(s<1):
            print('Check The Number And Run The Program Again!!!')
    elif(a==11):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        s=int(input('Choose the Employee (1-10):\n1.XX\n2.YY\n3.ZZ\n4.AA\n5.GG\n6.HH\n7.TT\n8.JJ\n9.LL\n10.SS'))
        if(s==1):
            d=df.drop(1)
            f=d.rename(index={2:1,3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9})
            print(f)
        if(s==2):
            d=df.drop(2)
            f=d.rename(index={3:2,4:3,5:4,6:5,7:6,8:7,9:8,10:9})
            print(f)
        if(s==3):
            d=df.drop(3)
            f=d.rename(index={4:3,5:4,6:5,7:6,8:7,9:8})
            print(f)
        if(s==4):
            d=df.drop(4)
            f=d.rename(index={5:4,6:5,7:6,8:7,9:8,10:9})
            print(f)
        if(s==5):
            d=df.drop(5)
            f=d.rename(index={6:5,7:6,8:7,9:8,10:9})
            print(f)
        if(s==6):
            d=df.drop(6)
            f=d.rename(index={7:6,8:7,9:8,10:9})
            print(f)
        if(s==7):
            d=df.drop(7)
            f=d.rename(index={8:7,9:8,10:9})
            print(f)
        if(s==8):
            d=df.drop(8)
            f=d.rename(index={9:8,10:9})
            print(f)
        if(s==9):
            d=df.drop(9)
            f=d.rename(index={10:9})
            print(f)
        if(s==10):
            d=df.drop(10)
            print(d)
        if(s>10):
            print('Check The Number And Run The Program Again!!!')
        if(s<1):
            print('Check The Number And Run The Program Again!!!')
    elif(a==12):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        s=int(input('Enter the Grade(3-7)'))
        if(s==3):
            d=df['Grade']==3
            f=pd.DataFrame(df.where(d))
            print(f.dropna(axis=0))
        if(s==4):
            d=df['Grade']==4
            f=pd.DataFrame(df.where(d))
            print(f.dropna(axis=0))
        if(s==5):
            d=df['Grade']==5
            f=pd.DataFrame(df.where(d))
            print(f.dropna(axis=0))
        if(s==6):
            d=df['Grade']==6
            f=pd.DataFrame(df.where(d))
            print(f.dropna(axis=0))
        if(s==7):
            d=df['Grade']==7
            f=pd.DataFrame(df.where(d))
            print(f.dropna(axis=0))
        if(s>7):
            print('Check The Number And Run The Program Again!!!')
        if(s<3):
            print('Check The Number And Run The Program Again!!!')
    elif(a==13):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        p=df['Basic_Salary'].max(axis=0)
        d=df['Basic_Salary']==p
        f=pd.DataFrame(df.where(d))
        print(f.dropna(axis=0))
    elif(a==14):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        p=df['Basic_Salary'].min(axis=0)
        d=df['Basic_Salary']==p
        f=pd.DataFrame(df.where(d))
        print(f.dropna(axis=0))
    elif(a==15):
        df=pd.DataFrame(payroll,index=[1,2,3,4,5,6,7,8,9,10])
        x=df["Grade"]
        y=df['Basic_Salary']*12
        plt.bar(x,y)
        plt.xlabel('Grade')
        plt.ylabel("Employee Salary per Annum")
        plt.title('Visualizing Company\nGrade System')
        plt.show()
        continue
    else:
        exit()
else:
    exit()
