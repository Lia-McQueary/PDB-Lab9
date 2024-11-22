class FastaParser:
    
    def __init__(self, file):
        self.file = file

    def fastaparsing(self, class_name):
        with open(self.file) as filehandle:
            for line in filehandle:
                if line.startswith(">"):
                    ID = line #cant do the whole rstrip thingy we usually do 
                    sequence = filehandle.readline() #makes the next line the sequence 
                    #calling the other class we made earlier
                    #if P_and_D== 'D':
                    yield class_name(ID, sequence)
                    #if P_and_D== 'P':
                        #yield ProteinSequence(ID, sequence)
