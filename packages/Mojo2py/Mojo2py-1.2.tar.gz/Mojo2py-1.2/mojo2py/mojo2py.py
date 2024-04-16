from sys import argv
import json 

class convert:
    filename:str
    def __init__(self,filename:str):
        self.filename=filename
    def return_json(self):
        file=open("mojo.json")
        jsonify=json.load(file)
        for x in jsonify["mojo"]:
            return x  
    def readfile(self,filename):
        lst = []
        with open(filename, "r+") as f:
            line = f.readline()
            while line:
                lst.append(line) 
                line = f.readline()  
        return lst
    def initial_lex(self):
        lst = self.readfile(self.filename)
        jsonify = self.return_json()
        new = []
        for w in lst:
            for jsons, replacement in jsonify.items():
                w = w.replace(jsons, replacement)
            new.append(w)
        return new

    def modules(self):
        lst=self.initial_lex()
        dict={}
        imports=[x.lstrip() for x in lst if "import_module" in x.lower()]
        variables=[tokens.split("=")[0] for tokens in imports]
        mdls=[keys.split("\"")[1][:] for keys in imports]
        for y in range(len(variables)):
            dict.update({mdls[y]:variables[y]})
        return dict    


    def remove_modules(self):
        lst=self.initial_lex()
        imports=[x for x in lst if "import_module" in x.lower()]
        return imports
    def final(self):
        lst=self.initial_lex()

        name=self.filename
        final_name=name.split(".")[0]
        removing=self.remove_modules()
        for x in removing:
            for lst1 in lst:
                if x==lst1:
                    lst.remove(lst1)
        file=open(f"{final_name}.py","w+")
        dict=self.modules()
        keys=list(dict.keys())
        vals=list(dict.values())
        if dict:
            for i in range(len(dict.keys())):
                file.write(f"import {keys[i]} as {vals[i]} \n")
        for l in lst:
            file.write(l)
        string="""
if __name__=="__main__":
     main()
    """ 
        file.write(string)
        file.close()    
