# f=open("./baker_all.txt.cleaned1","rb")
# train=open("./baker_ljs_train1.txt","ab+")
# val=open("./baker_ljs_val1.txt","ab+")
# for i,line in enumerate(f.readlines()):
#     if i<9900:
#         train.write(line)
#     else:
#         val.write(line)

# f1=open("./ljs_audio_text_train_filelist.txt.cleaned","rb")
# f2=open("./ljs_audio_text_val_filelist.txt.cleaned","rb")
# train=open("./baker_ljs_train1.txt","ab+")
# val=open("./baker_ljs_val1.txt","ab+")
# for i,line in enumerate(f1.readlines()):
#     train.write(line)
# for i,line in enumerate(f2.readlines()):
#     val.write(line)
# f1.close()
# f2.close()
# train.close()
# val.close()

# f1=open("./filelists/baker_ljs_train1.txt","rb")
# f2=open("./filelists/baker_ljs_val1.txt","rb")

# train=open("./filelists/baker_ljs_ms_train1.txt","ab+")
# val=open("./filelists/baker_ljs_ms_val1.txt","ab+")

# for i,line in enumerate(f1.readlines()):
#     line=line.split(b"|")
#     if line[0].split(b'/')[0]==b"BAKER":
#         train.write(line[0]+b"|0|"+line[1])
#     else:
#         train.write(line[0]+b"|1|"+line[1])
# for i,line in enumerate(f2.readlines()):
#     line=line.split(b"|")
#     if line[0].split(b'/')[0]==b"BAKER":
#         val.write(line[0]+b"|0|"+line[1])
#     else:
#         val.write(line[0]+b"|1|"+line[1])
# f1.close()
# f2.close()
# train.close()
# val.close()

def aishell3():
    import json
    aishell3_dict_json = json.load(open("filelists/aishell3.json"))
    lines = []
    f1=open("filelists/aishell3.txt","r",encoding="UTF-8")
    f2=open("filelists/aishell3_train.txt","w",encoding="UTF-8")
    f3=open("filelists/aishell3_val.txt","w",encoding="UTF-8")
    f4=open("filelists/aishell3_test.txt","w",encoding="UTF-8")
    for i,line in enumerate(f1.readlines()):
        line=line.split("|")
        line[1] = str(aishell3_dict_json[line[1]])
        lines.append("|".join(line))
        print("|".join(line))
    for i,line in enumerate(lines):
        if i%100 == 1:
            f3.write(line)
        elif i%100 == 2:
            f4.write(line)
        else:
            f2.write(line)
        
        
    


def aishell3_dict():
    import os
    import json

    people = os.listdir("../dataset/aishell3/")
    people_dict = {}
    people_num = []
    for person in people:
        people_num.append(int(person[-4:]))
    people_num.sort()  
    for i,person in enumerate(people_num):
        people_dict["SSB"+str(person).zfill(4)] = i
    aishell3_dict_json = open("filelists/aishell3.json","w")
    json.dump(people_dict,aishell3_dict_json)
    
    
if __name__ == '__main__':
    aishell3()
    # aishell3_dict()
    