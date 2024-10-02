
def main_menu():
    print("Choose an option: ")
    print("[1] Compute a reverse complement of a k-mer pattern")
    print("[2] Count a k-mer pattern")
    print("[3] Find most frequent k-mer patterns")
    print("[4] Leave the program")

def complement(pattern):
    complement2 = ""

    if action == 1:
        genome = pattern


    start = time.time()

    dna_validity = True
    selesai = False

    while dna_validity == True:
        for i in range (len(genome)):
            if(genome[i] == "T"):
                complement_char = "A"
                complement2 = complement2 + complement_char
            if(genome[i] == "A"):
                complement_char = "T"
                complement2 = complement2 + complement_char
            if(genome[i] == "C"):
                complement_char = "G"
                complement2 = complement2 + complement_char
            if(genome[i] == "G"):
                complement_char = "C"
                complement2 = complement2 + complement_char
            if i == len(genome)-1:
                selesai = True
            if genome[i] != "T" and genome[i] != "A" and genome[i] != "C" and genome[i] != "G":
                print("DNA hanya berisi 'T' 'A' 'C' atau 'G'!")
                genome = input("Masukkan DNA di sini: ")
                break
        if selesai == True:
            break

    complement2 = complement2[::-1]

    print(complement2)

    end = time.time()

    print((end-start) * 10**3, "ms")

    return complement2   

def kmer_occurance(pattern, genome):

    complement2 = ""

    start = time.time()

    dna_validity = True
    selesai = False

    while dna_validity == True:
        for i in range (len(genome)):
            if(genome[i] == "T"):
                complement_char = "A"
                complement2 = complement2 + complement_char
            if(genome[i] == "A"):
                complement_char = "T"
                complement2 = complement2 + complement_char
            if(genome[i] == "C"):
                complement_char = "G"
                complement2 = complement2 + complement_char
            if(genome[i] == "G"):
                complement_char = "C"
                complement2 = complement2 + complement_char
            if i == len(genome)-1:
                selesai = True
            if genome[i] != "T" and genome[i] != "A" and genome[i] != "C" and genome[i] != "G":
                print("DNA hanya berisi 'T' 'A' 'C' atau 'G'!")
                genome = input("Masukkan DNA di sini: ")
                break
        if selesai == True:
            break

    complement2 = complement2[::-1]



    while len(pattern) > len(genome):
        print("Pattern terlalu panjang!")
        pattern = input("Masukkan pattern di sini: ")

    while pattern.isdigit() == True:
        print("Pattern tidak boleh berupa angka!")
        pattern = input("Masukkan Pattern di sini: ")

    sama = False
    count = 0


    for i in range (len(genome)-1):
        if genome[i] == pattern[0]:
            for j in range (len(pattern)):
                if genome[i+j] == pattern[j]:
                    sama = True
                else:
                    sama = False
                    break
        if sama == True:
            count += 1
            sama = False
        

    for i in range (len(complement2)-1):
        if complement2[i] == pattern[0]:
            for j in range (len(pattern)):
                if complement2[i+j] == pattern[j]:
                    sama = True
                else:
                    sama = False
                    break
        if sama == True:
            count += 1
            sama = False

    print(count)

    end = time.time()

    print((end-start) * 10**3, "ms")

    return count

def most_frequent_kmer(genome, n):
    complement2 = ""

    #n = int(input("Masukkan K-MER di sini: "))


    start = time.time()

    timer = 0

    list_most_frequent = []

    for i in range (len(genome)):
        if(genome[i] == "T"):
            complement_char = "A"
            complement2 = complement2 + complement_char
        if(genome[i] == "A"):
            complement_char = "T"
            complement2 = complement2 + complement_char
        if(genome[i] == "C"):
            complement_char = "G"
            complement2 = complement2 + complement_char
        if(genome[i] == "G"):
            complement_char = "C"
            complement2 = complement2 + complement_char

    complement2 = complement2[::-1]

    end = time.time()

    print("Fase 1: ")
    print((end-start) * 10**3, "ms")

    timer = timer + (end-start) * 10**3


    start = time.time()

    count = 0
    sama = False


    repeat = len(genome)//n

    list_sliced = []


    for k in range (n):
        for i in range (repeat):
            list_sliced.append(genome[i*n+k:i*n+n+k])

        if i*n+n+k <= len(genome)-1:
            list_sliced.append(genome[i*n+n+k:])

        if (k+1)*repeat > len(genome):
            break


    list_pop = []

    for j in range (len(list_sliced)):

        if len(list_sliced[j]) != n:
            list_pop.append(j)

    for h in range (len(list_pop)):
        list_sliced.pop(list_pop[h]-h)

    #for g in range (len(list_sliced)):
        #print(list_sliced[g])


    for k in range (n):
        for i in range (repeat):
            list_sliced.append(complement2[i*n+k:i*n+n+k])

        if i*n+n+k <= len(complement2)-1:
            list_sliced.append(complement2[i*n+n+k:])

        if (k+1)*repeat > len(complement2):
            break


    list_pop = []

    for j in range (len(list_sliced)):

        if len(list_sliced[j]) != n:
            list_pop.append(j)

    for h in range (len(list_pop)):
        list_sliced.pop(list_pop[h]-h)

    #for g in range (len(list_sliced)):
        #print(list_sliced[g])

    end = time.time()

    print("Fase 2: ")
    print((end-start) * 10**3, "ms")

    timer = timer + (end-start) * 10**3

    start = time.time()

    list_sliced.sort()

    end = time.time()

    timer = timer + (end-start) * 10**3

    print("Fase 3: ")
    print((end-start) * 10**3, "ms")

    #print("List yang sudah disortir")
    #print(list_sliced)

    #udah disortir

    start = time.time()

    count = 1

    new_length = len(list_sliced)

    list3 = []

    count = 1

    for i in range (len(list_sliced)-1):
        if list_sliced[i] == list_sliced[i+1]:
            count += 1
        else:
            list3.append(count)
            list_most_frequent.append(list_sliced[i])
            count = 1

    #print(list3)
    #print(list_most_frequent)

    end = time.time()

    print("Fase 4: ")
    print((end-start) * 10**3, "ms")

    timer = timer + (end-start) * 10**3


    start = time.time()

    list_gede = [list3[0]]
    index_gede = [0]



    for i in range (1,len(list3)):
        if list3[i] > list_gede[0]:
            index_gede.clear()
            list_gede.clear()
            list_gede.append(list3[i])
            index_gede.append(i)
        elif list3[i] == list_gede[0]:
            list_gede.append(list3[i])
            index_gede.append(i)

    #print("Kemunculan terbesar berjumlah: ")
    #print(list_gede)
    #print("Kemunculan terbesar terletak pada index ke: ")
    #print(index_gede)





    complement2 = []

    for k in range (len(index_gede)):
        print(list_most_frequent[index_gede[k]])

    end = time.time()

    print("Fase 5: ")
    print((end-start) * 10**3, "ms")

    timer = timer + (end-start) * 10**3

    print(timer, "ms")

if __name__ == "__main__":

    import time

    list_most_frequent = []
    list_most_frequent_count = []
    list_sliced = []

    running = True

    input_genome = input("Genome file name: ")
    genome = open(input_genome, "r")
    genome = genome.read()
    #genome = input("Masukkan di sini: ")


    while running:

        __name__ = "__main__"

        

        

        main_menu()
        action = int(input("Select an operation: "))
        print("="*72)

        if action == 1:
            pattern = input("Input your pattern: ")
            complement(pattern)
            

        elif action == 2:

            pattern = input("Masukkan pattern di sini: ")
            kmer_occurance(pattern, genome)


        elif action == 3:

            n = int(input("Masukkan panjang K-MER di sini: "))
            most_frequent_kmer(genome, n)

        elif action == 4:
            running = False

        else:
            print("Input harus 1/2/3/4!")





        complement2 = ""

        

        count = 0
        sama = False



    print("Thank You")



        

        #repeat = len(genome)//n


        

