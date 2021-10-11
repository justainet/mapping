from sklearn import preprocessing
import pandas as pd
import numpy as np
import warnings
from IPython.display import clear_output
warnings.filterwarnings("ignore")

def chunch(lis):
    bag=[]
    pp=lis.copy()
    try:
        for i in range(len(lis)-1):
            for j in range(1,len(pp)):
                bag.append([pp[0],pp[j]])
            pp.pop(0)
    except:
        pass
    return bag
def swapPositions(listts):
    for listt in listts:
        listt[0], listt[1] = listt[1], listt[0]
    return listts
def simi(lists,refers):
    Reff=[]
    pef=lists.copy()
    for i,j in enumerate(lists):
        try:
            pef.pop(0)
            if j in pef:
                chk=pef.index(j)
                Reff.append([refers[chk+i+1],refers[i]])
            dd=swapPositions(pef)
            if j in dd:
                chk=pef.index(j)
                Reff.append([refers[chk+i+1],refers[i]])
        except:
            pass
    return Reff
def fac(n):
    return sum([i for i in range(n)])
def chunches(lis):
    bag=[]
    for i in range(1,len(lis)):
        bag.append([lis[0],lis[i]])
    return bag
def similar(lists,refers):
    Reff=[]
    pef=lists.copy()
    for i,j in enumerate(lists):
        try:
            pef.pop(0)
            if j in pef:
                chk=pef.index(j)
                Reff.append([refers[chk+i+1],refers[i]])
            dd=swapPositions(pef)
            if j in dd:
                chk=pef.index(j)
                Reff.append([refers[chk+i+1],refers[i]])
        except:
            pass
    return Reff
def bib_large(file):
    file_1=file.groupby("reference").filter(lambda x: len(x) >2)
    file_2=file.groupby("reference").filter(lambda x: len(x) ==2)
    nodelist_1=[i for i in  file_1.groupby('reference').groups.values()]
    nodelist_2=[i for i in  file_2.groupby('reference').groups.values()]
    edgelist=pd.DataFrame(nodelist_2)
    bbb=[]
    for i in nodelist_1:
        bbb+=chunches(i)
    edgelist_2=pd.DataFrame(bbb)
    all_edgelist=pd.concat([edgelist,edgelist_2])
    all_edgelist.columns=['Source','Target']
    all_edgelist['Weight']=1
    edgelistDF =all_edgelist[all_edgelist.duplicated(keep=False)]
    wbag=[]
    for i,j in edgelistDF.iterrows():
        weight1=len(edgelistDF[(edgelistDF.Source==j.Source)&(edgelistDF.Target==j.Target)].dropna())
        wbag.append(weight1)
    edgelistDF['Weight']=wbag
    edgelistDF1=all_edgelist.drop_duplicates(keep=False)
    all_edgelist=pd.concat([edgelistDF,edgelistDF1])
    nodelist=pd.DataFrame()
    nodelist['Label']=list(set([i for i in all_edgelist.Source.unique()]+[i for i in all_edgelist.Target.unique()]))
    le = preprocessing.LabelEncoder()
    le.fit(nodelist['Label'])
    nodelist['Id']=le.transform(nodelist['Label'])
    nodelist.set_index('Id',inplace=True)
    all_edgelist['Source']=le.transform(all_edgelist['Source'])
    all_edgelist['Target']=le.transform(all_edgelist['Target'])
    all_edgelist.set_index('Source',inplace=True)
    all_edgelist['Type']='Undirected'
    all_edgelist.to_csv('bib_edgelist.csv')
    nodelist.to_csv('bib_nodelist.csv')
def bib(file):
    file_1=file.groupby("reference").filter(lambda x: len(x) >2)
    file_2=file.groupby("reference").filter(lambda x: len(x) ==2)
    nodelist_1=[list(i) for i in  file_1.groupby('reference').groups.values()]
    nodelist_2=[i for i in  file_2.groupby('reference').groups.values()]
    edgelist=pd.DataFrame(nodelist_2)
    bbb=[]
    for i in nodelist_1:
        bbb+=chunch(i)
    edgelist_2=pd.DataFrame(bbb)
    print('20%')
    all_edgelist=pd.concat([edgelist,edgelist_2])
    all_edgelist.columns=['Source','Target']
    all_edgelist['Weight']=1
    edgelistDF =all_edgelist[all_edgelist.duplicated(keep=False)]
    wbag=[]
    for i,j in edgelistDF.iterrows():     
        weight1=len(edgelistDF[(edgelistDF.Source==j.Source)&(edgelistDF.Target==j.Target)].dropna())
        wbag.append(weight1)
    edgelistDF['Weight']=wbag
    print('80%')
    edgelistDF1=all_edgelist.drop_duplicates(keep=False)
    all_edgelist=pd.concat([edgelistDF,edgelistDF1])
    nodelist=pd.DataFrame()
    nodelist['Label']=list(set([i for i in all_edgelist.Source.unique()]+[i for i in all_edgelist.Target.unique()]))
    le = preprocessing.LabelEncoder()
    le.fit(nodelist['Label'])
    nodelist['Id']=le.transform(nodelist['Label'])
    nodelist.set_index('Id',inplace=True)
    all_edgelist['Source']=le.transform(all_edgelist['Source'])
    all_edgelist['Target']=le.transform(all_edgelist['Target'])
    all_edgelist.set_index('Source',inplace=True)
    all_edgelist['Type']='Undirected'
    all_edgelist.to_csv('bib_edgelist.csv')
    nodelist.to_csv('bib_nodelist.csv')
def cc(file):
    trim=file.groupby("reference").filter(lambda x: len(x) >2)
    trim_1= file.groupby("reference").filter(lambda x: len(x) ==2)
    trim_all=file.groupby("reference").filter(lambda x: len(x) >1)
    nodelist_1=[list(i) for i in  trim_1.groupby('reference').groups.values()]
    nodelist_2=[i for i in  trim_1.groupby('reference').groups.keys()]
    el1=simi(nodelist_1,nodelist_2)
    edgelist1=pd.DataFrame(el1)
    nodelist_3=[list(i) for i in  trim_all.groupby('reference').groups.values()]
    nodelist_4=[]
    for i,k in  zip(trim_all.groupby('reference').groups.keys(),trim_all.groupby('reference').groups.values()):
        lenght=fac(len(k))
        for j in range(lenght):
            nodelist_4.append(i)
    el2=[]
    for i in nodelist_3:
        el2+=chunch(i)
    ell=simi(el2,nodelist_4)
    edgelist2=pd.DataFrame(ell)
    all_edgelist=pd.concat([edgelist1,edgelist2])
    all_edgelist.columns=['Source','Target']
    nodelist=pd.DataFrame()
    nodelist['Label']=[i for i in trim_all.reference.unique()]
    le = preprocessing.LabelEncoder()
    le.fit(nodelist['Label'])
    nodelist['Id']=le.transform(nodelist['Label'])
    nodelist.set_index('Id',inplace=True)
    all_edgelist['Source']=le.transform(all_edgelist['Source'])
    all_edgelist['Target']=le.transform(all_edgelist['Target'])
    all_edgelist.set_index('Source',inplace=True)
    all_edgelist['Type']='Undirected'
    all_edgelist.to_csv('cc_edgelist.csv')
    nodelist.to_csv('cc_nodelist.csv')
    
def cc_large(file):
    trim=file.groupby("reference").filter(lambda x: len(x) >2)
    trim_1= file.groupby("reference").filter(lambda x: len(x) ==2)
    trim_all=file.groupby("reference").filter(lambda x: len(x) >1)
    nodelist_1=[list(i) for i in  trim_1.groupby('reference').groups.values()]
    nodelist_2=[i for i in  trim_1.groupby('reference').groups.keys()]
    el1=similar(nodelist_1,nodelist_2)
    edgelist1=pd.DataFrame(el1)
    nodelist_3=[list(i) for i in  trim.groupby('reference').groups.values()]
    nodelist_4=[]
    for i in  trim.groupby('reference').groups.keys():
        for j in range(len(nodelist_3)):
            nodelist_4.append(i)
    el2=[]
    for i in nodelist_3:
        el2+=chunches(i)
    ell=similar(el2,nodelist_4)
    edgelist2=pd.DataFrame(ell)
    all_edgelist=pd.concat([edgelist1,edgelist2])
    all_edgelist.columns=['Source','Target']
    nodelist=pd.DataFrame()
    nodelist['Label']=[i for i in  trim_all.groupby('reference').groups.keys()]
    le = preprocessing.LabelEncoder()
    le.fit(nodelist['Label'])
    nodelist['Id']=le.transform(nodelist['Label'])
    nodelist.set_index('Id',inplace=True)
    all_edgelist['Source']=le.transform(all_edgelist['Source'])
    all_edgelist['Target']=le.transform(all_edgelist['Target'])
    all_edgelist.set_index('Source',inplace=True)
    all_edgelist['Type']='Undirected'
    all_edgelist.to_csv('cc_edgelist.csv')
    nodelist.to_csv('cc_nodelist.csv')
    
def main():
    filename = str(input("Enter your filename. Add the extension. Filename:  "))
    file=pd.read_csv(filename, sep=';')
    file.set_index('title',inplace=True)
    if len(file)>100:
        print('Biblographic Coupling start')
        bib_large(file)
        print('Co-citation Coupling start')
        cc_large(file)
        print('done. Files have been saved as bib or cc. edgelist or nodelist')
    else:
        print('Biblographic Coupling start')
        bib(file)
        print('Co-citation Coupling start')
        cc(file)
        print('done. Files have been saved as bib or cc. edgelist or nodelist')        
if __name__ == '__main__':
    main()