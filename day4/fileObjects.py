#File Objects

f=open('text.txt','r')
print(f.mode) #file open
f.close()

with open('text.txt','r') as f:
    f_contents=f.read() #reading the whole file
    for line in f:
        print(line,end="")

with open('text2.txt','w') as f:
    f.write('Test') #create another file and writing it
    f.seek(0)
    f.write('R')

with open('text.txt','r') as rf: #Creating exact copy of text.txt
    with open('text_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)    


with open('scratch.jpg','rb') as rf:
    with open('scratch_copy.jpg','wb') as wf:
        # for line in rf:
        #     wf.write(line)
        # too avoid above loop line
        chunk_size=4096
        rf_chunk=rf.read(chunk_size)

        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)


    
    