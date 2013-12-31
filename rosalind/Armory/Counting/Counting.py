from Bio.Seq import Seq

if __name__ == '__main__':
    f = open("data.txt")
    data = f.readline()
    mySeq = Seq(data)
    print str(mySeq.count("A")) + " " + str(mySeq.count("C")) + " " + str(mySeq.count("G")) + " " + str(mySeq.count("T"))