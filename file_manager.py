#liam stuff
#file format
#NULL,username,score,score type
#<game name>,<username>,<score>,<score type>

#impoort csv
#make class called score
    #define init func with path to csv as peramater
    #open file as highscores in read mode and set variable rows to a dict of dicts with game name score score type and username than return rows
    #define read with peramater as game and will return that games dict
    #define write with peramaters of game score and username and set the spisific games dict to the new valeu and update the csv file
    #define better scoer with peramaters of score game and username and if the score type is time if the score is lower set it to thta else if it is bigger set it to that



        
        
#impoort csv
import csv
#make class called score
class score:
    #define init func with path to csv as peramater
    #open file as highscores in read mode and set variable rows to a dict of dicts with game name score score type and username than return rows
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
    #define read with peramater as game and will return that games dict
    def read(self,game):
        for x in self.rows:
            if game in x:
                return x
    #define write with peramaters of game score and username and set the spisific games dict to the new valeu and update the csv file
    def write(self,game,score,username):
        self.rows[game]["username"]=username
        self.rows[game]["score"]=score
        feildnames=self.rows.keys()
        try:
            with open(self.path_to_csv,mode="w") as high_scores:
                writer=csv.DictWriter(high_scores,fieldnames=feildnames)
                writer.writeheader()
                writer.writerow()
        except FileNotFoundError:
            print("there is no file")
            return "0"
        except Exception as e:
            print(f'an error orrured: {e}')
            return "0"
    #define better scoer with peramaters of score game and username and if the score sype is time if the scoe is lower set it to thta else if it is bigger set it to that
    def better_score(self,score,game,username):
        if self.read(game)["score type"]=="time":
            if self.read(game)["score"]>score:
                self.write(game,score,username)
                return True
            return False
        else:
            if self.read(game)["score"]<score:
                self.write(game,score,username)
                return True
            return False



