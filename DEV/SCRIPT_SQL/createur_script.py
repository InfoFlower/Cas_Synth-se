import pandas as pd

def typetext(value):
    if type(value)==str:
        ret='VARCHAR'
    elif type(value)==int:
        ret='INTEGER'
    else:
        ret='FLOAT'
    return ret

def all_stats(df):
    ret={}
    for i in df.columns:
        ret[i]=[typetext(df[i][0])]
        if ret[i][0]=='VARCHAR':
            ret[i].append(max([len(z) for z in df[i] if type(z)==str]))
    return ret

def crea_script(df,nom,pk=None,write=False):
    dico=all_stats(df)
    script=f'CREATE TABLE {nom} ('+'\n'
    for k,v in dico.items():
        param=''
        if len(v)==1:
            param=v[0]
        else:
            param=v[0]+'('+str(v[1])+')'
        script+=' '*4+' '+k+' '+param+','+'\n'
    if pk is not None:
        pkk=''
        for i in pk:
            pkk+=i +','
        script+=f'CONSTRAINT pk_{nom} PRIMARY KEY ({pkk})'
    script+=');'
    if write:
        with open(f'CREATE_TABLE_{nom}.sql','w') as f:
            f.write(script)
    return script

