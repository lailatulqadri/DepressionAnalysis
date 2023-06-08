import json
import contractions

def read_file():
        f = open('depression_lexicon.json','r')
        data = json.load(f)

        signal_1 = []
        for i in data['signal_1']:
                i = i.replace("_", " ")
                i = contractions.fix(i)
                #print(i)
                signal_1.append(i)

        f.close()
        list_symptoms =[signal_1] 
        return list_symptpms
