import random
import sys
import math
file_train = sys.argv[1]
file_test = sys.argv[2]


#-----------------------------Read-Data-------------------------------
first_label=[]
test_array = []
with open(file_train) as my_file:
    for line in my_file:
        line = line.split()
        test_array.append(line[1:])
        first_label.append(int(line[0]))
Total_rows=len(test_array)
#-------------------------Store last array element-------------------
labels=[]
for line in test_array:
    labels.append(line[-1])
indexes=[]
for i in labels:

    i=i.split(':')
    index=int(i[0])
    indexes.append(index)
max_index=max(indexes)+1

#---------------------Weight + Data Array----------------------------
weight=[]
weight=random.randint(-2,2)
weight=[weight]*max_index

weight=map(float,weight)
weight1=weight
train_array=[]
weight1=map(float,weight1)
weight2=weight
weight2=map(float,weight2)
data=[[0]*max_index for i in range(Total_rows)]

#CROSS VALIDATION:
#--------------------------------------------------------------------

#print len(train_array)
#print split_value
part1=[]
part2=[]
part3=[]
part4=[]
part5=[]
split1=[]
split2=[]
split3=[]
split4=[]
split5=[]
#print train_array[0]
for i in range(0,1):
    part1.extend(train_array[0:1282])
    part2.extend(train_array[1282:2564])
    part3.extend(train_array[2564:3846])
    part4.extend(train_array[3846:5128])
    part5.extend(train_array[5128:6414])
    split1.extend(train_array[1282:6414])
    split2.extend(train_array[3846:6414]+train_array[0:2564])
    split3.extend(train_array[3846:6414]+train_array[0:3846])
    split4.extend(train_array[5128:6414]+train_array[0:3846])
    split5.extend(train_array[0:5128])

#-------------------Assigning values in data array-------------------
final_result=[]
for h in test_array:
    foobar=[0 for i in range(max_index)]
    for item in h:
        item=item.split(':')
        index=int(item[0])
        value=int(item[1])
        foobar[index]=value
    final_result.append(foobar)

#random.shuffle(final_result)
#print final_result[0:5]
#trrue1=random.randint(12,90)

#------------------TEST TEST TEST-----------------------------------
#-----------------------------TEST-----------------------------------

#-----------------------------Read-Data-------------------------------
first_label_test=[]
test_array_test = []
with open(file_test) as my_file:
    for line in my_file:
        line=line.lower()
        line = line.split()
        test_array_test.append(line[1:])
        first_label_test.append(int(line[0]))
Total_rows_test=len(test_array_test)
#-------------------------Store last array element-------------------
labels_test=[]
for line in test_array_test:
    labels_test.append(line[-1])
indexes_test=[]
for i in labels_test:

    i=i.split(':')
    index=int(i[0])
    indexes_test.append(index)
max_index_test=max(indexes_test)+1

#-------------------Assigning values in data array-------------------
final_result_test=[]
for h in test_array_test:
    foobar_test=[0 for i in range(max_index_test)]
    for item in h:
        item=item.split(':')
        index=int(item[0])
        value=int(item[1])
        foobar_test[index]=value
    final_result_test.append(foobar_test)
#------------------------------Margin P-----------------------------
#u=float(input ("what is margin?, between 0 and 5 \n"))
#print type (u)
lrate=[0.8,15,25,35]
bias_glob=random.randint(-2,2)
bias=bias_glob
#print type (bias)
#print bias
c=[0.20,0.001,10,101]
epoch_hy=[5,10,15,20,25,35]
j=0
C=[101,20,50]
#first_label=map(float,first_label)

for l in lrate:
    for ii in C:
        for epoch in epoch_hy:
            gamma0=0.01
            count=0
            #c=0
            true1=0
            false=0
            weight1=weight
            for k in range(epoch):
                count+=1
                #print len(final_result)
                for j,i in enumerate(final_result):
                    i=map(int,i)
                    A=map(lambda x,y:x*y,weight1,i)
                    B=reduce(lambda x,y:x+y,A)
                    derived=B+bias
                    #TT= map(lambda x:labels_train[j]*B,)
                    G=map(lambda x,y:x*y,i,i)
                    V=reduce(lambda x,y:x+y,G)
                    #a_rate=(u-(derived*first_label[j]))/(V-1)
                    learning_rate=float(gamma0)/(1+gamma0*((j+1)/ii))
                    GG = first_label[j]*B
                    GG1 = 1 + math.exp(GG)
                    Constant = float(-first_label[j])/GG1
                    Constant_final = map(lambda x:Constant*x,i)
                    FF = map (lambda x:x*2,weight1)
                    #print FF
                    FF1 = map(lambda x:x/ii*ii,FF)
                    Totall= map(lambda x,y:x+y,FF1,Constant_final)
                    weight=Totall
                    true1=true1+1
                    #bias=bias+(first_label[j]*a_rate)
                    #c=c+1
            #print "Mistakes committed=",c
            true1=0
            false=0
            #first_label=map(int,first_label)
            for j,i in enumerate(final_result):
                weight=map(float,weight)
                i=map(int,i)
                A=map(lambda x,y:x*y,weight,i)
                B=reduce(lambda x,y:x+y,A)
                derived=B+bias
                prediction=0
                if (-derived<=0):
                    #print "second if"
                    prediction=-1
                else:
                    prediction=1
                if prediction==first_label[j]:
                    true1=true1+1
                else:
                    false = false+1
            print "TRAIN Accuracy"
            accuracy1 = float(true1)/(true1+false)
            print accuracy1, "this is accuracy for"," Learning rate=",l," Epoch=",epoch, "Sigma Square is", ii*ii


#--------------------------------------------------------------------
#------------------------------Margin P-----------------------------
lrate=[1]
bias=bias_glob
epoch_hy=[3,5]
j=0
c=0
#first_label=map(int,first_label)
#print len(weight2)
#weight2=map(int,weight2)
for l in lrate:
    for epoch in epoch_hy:
        count=0
        c=0
        weight2=weight
        for k in range(epoch):
            count+=1
            #j=0
            for j,i in enumerate(final_result):
                #weight2=map(int,weight2)
                i=map(int,i)
                A=map(lambda x,y:x*y,weight2,i)
                B=reduce(lambda x,y:x+y,A)
                derived=B+bias
                G=map(lambda x,y:x*y,i,i)
                V=reduce(lambda x,y:x+y,G)
                #a_rate=(u-(derived*first_label[j]))/(V)
                #print c,"########################"

        weight2=weight2 + [0]
        #print "Mistakes committed=",c
        true1=0
        false=0
       # first_label_test=map(int,first_label_test)
        #print len(final_result_test[0])
        for j,i in enumerate(final_result_test):
            i=map(int,i)
            weight2=map(float,weight2)
            A=map(lambda x,y:x*y,weight2,i)
            B=reduce(lambda x,y:x+y,A)
            derived_test=B+bias
            if (derived_test*first_label_test[j])>0:
                true1=true1+1
            else:
                false=false+1
        print "TEST Accuracy"
        accuracy1 = float(false)/(true1+false)
        print accuracy1, "this is accuracy for", " Learning rate=",l," Epoch=",epoch
