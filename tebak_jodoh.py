import random

cowo = ['akbar','rizal','ibro','guntur','asep']
cewe = ['mirna','ansi','jubaedah','julaeha','juminten','siti']

def laki():
    pasangan_laki = random.choice(cowo)
    return pasangan_laki

def putri():
    pasangan_puteri = random.choice(cewe)
    return pasangan_puteri

def mempelai_wanita():
    jodoh = True
    calon = putri()
    pasangan = laki()
    print("Tolong carikan jodoh untuk anakmu yang bernama %s " % calon)
    print("Daftar yang melamarnya adalah :")
    for i in cowo:
        print i
    while jodoh:
        guest = raw_input("Saya yakin jodohnya adalah ")
        if (guest == pasangan):
            print ("Selamat kamu telah menemukan jodohnya !!!")
            jodoh = False
        else:
            print (":'(( Sayang sekali mereka belum cocok")

def mempelai_pria():
    jodoh = True
    calon = laki()
    pasangan = putri()
    print("Tolong carikan jodoh untuk anakmu yang bernama %s " % calon)
    print("Daftar pacarnya adalah :")
    for i in cewe:
        print i
    while jodoh:
        guest = raw_input("Saya yakin jodohnya adalah ")
        if (guest == pasangan):
            print ("Selamat kamu telah menemukan jodohnya !!!")
            jodoh = False
        else:
            print (":'(( Sayang sekali mereka belum cocok")

def pilih():
    print("Mau berperan sebagai siapa kamu?")
    print("1. Ibu dari mempelai wanita")
    print("2. Ibu dari mempelai pria")
    guest = input("Pilihanmu ==>")
    if(guest == 1):
        mempelai_wanita()
    elif(guest == 2):
        mempelai_pria()
pilih()
    
        