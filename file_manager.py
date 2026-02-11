#liam stuff
#file format
#NULL,username,score,score type
#<game name>,<username>,<score>,<score type>
class score:
    def __init__(self, path_to_csv):
        self.path_to_csv=path_to_csv
        try:
            with open(path_to_csv,mode="r") as high_scores:
                content=csv.reader(high_scores)
                hedders = next(content)
                rows=[]
                for line in content:
                    rows.append({line[0]:{hedders[1]:line[1],hedders[2]:line[2],hedders[3]:line[3]}})
        except FileNotFoundError:
            print("there is no file")
            return "0"
        except Exception as e:
            print(f'an error orrured: {e}')
            return "0"
        else:
            self.rows=rows
            high_scores.close()
            return rows
    def read(self,game):
        for x in self.rows():
            if game in x:
                return x
    def write(self,game,score,username):
        self.rows[game]["username"]=username
        self.rows[game]["score"]=score
        try:
            with open(self.path_to_csv,mode="w") as high_scores:
                
        except FileNotFoundError:
            print("there is no file")
            return "0"
        except Exception as e:
            print(f'an error orrured: {e}')
            return "0"
    def better_score(self,score,game):
        if self.read(game)["score type"]=="time":
            if self.read(game)["score"]>score:
                s
        else:


        
        
        