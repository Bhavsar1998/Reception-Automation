import nltk
sentence="I Am Himanshu Singh Bhavsar And I Have An Appointment"
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    #name=""
    tok=dict(sent)
    # print (tok)
    namelis=[]
    purpose=[]
    name_purp=[]
    ke=list(tok.keys())
    val=list(tok.values())
    # print(ke)
    # print(val)
    for i in range(0,len(val)):
        if val[i]=="NNP":
            namelis.append(ke[i])
        if val[i]=='NN':
            purpose.append(ke[i])
    name_purp.append(namelis)
    name_purp.append(purpose)
    visitor_name=""
    for i in namelis:
        visitor_name+=i
        visitor_name+=" "
    return visitor_name

# print(preprocess(sentence))