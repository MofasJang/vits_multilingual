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

f1=open("./filelists/baker_ljs_train1.txt","rb")
f2=open("./filelists/baker_ljs_val1.txt","rb")

train=open("./filelists/baker_ljs_ms_train1.txt","ab+")
val=open("./filelists/baker_ljs_ms_val1.txt","ab+")

for i,line in enumerate(f1.readlines()):
    line=line.split(b"|")
    if line[0].split(b'/')[0]==b"BAKER":
        train.write(line[0]+b"|0|"+line[1])
    else:
        train.write(line[0]+b"|1|"+line[1])
for i,line in enumerate(f2.readlines()):
    line=line.split(b"|")
    if line[0].split(b'/')[0]==b"BAKER":
        val.write(line[0]+b"|0|"+line[1])
    else:
        val.write(line[0]+b"|1|"+line[1])
f1.close()
f2.close()
train.close()
val.close()