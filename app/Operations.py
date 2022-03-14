from datetime import datetime
import json


class Operations():
    
    def bind(self, arrUsers, arrScores): 
        for user in arrUsers:
            score = self.findScore(arrScores, user['matricula'])
            signo = self.caluclarSigno(user['anio'])
            user['score'] = score
            user['signo'] = signo
        
        return arrUsers
    
    def findScore(self, scores, matricula):
        score = -1
        
        for score in scores:
            if score['matricula'] == matricula:
                return score['calificacion']
        
        return score
    
    def calcularEdad(self, ano, mes, dia):
        edad = 0
        now = datetime.now()
        
        edad = now.year - ano
        
        if dia<=now.day and mes<=now.month:
            return edad
        else:
            return (edad-1)
        
    def caluclarSigno(self, anio):
        signo = ''
        
        aux = anio % 12
        
        if aux == 0:
            signo = 'Mono'
        if aux == 1:
            signo = 'Gallo'
        if aux == 2:
            signo = 'Perro'
        if aux == 3:
            signo = 'Cerdo'
        if aux == 4:
            signo = 'Rata'
        if aux == 5:
            signo = 'Buey'
        if aux == 6:
            signo = 'Tigre'
        if aux == 7:
            signo = 'Conejo'
        if aux == 8:
            signo = 'Dragón'
        if aux == 9:
            signo = 'Serpiente'
        if aux == 10:
            signo = 'Caballo'
        if aux == 11:
            signo = 'Cabra'
        
        return signo


class Filer():
    
    def save(self, element):
        # guardar elemento en archivo 
        # appends to file
        jsonString = json.dumps(element)
        f = open("data_db.txt", "a")
        f.write(jsonString + "\n")
        f.close()
        
    def read(self):
        # reads element lines in file
        # returns array of elements
        f = open("data_db.txt", "r")

        dataArr = []

        raw_data = f.readlines()
        for line in raw_data:
            lineData = json.loads(line.strip())
            dataArr.append(lineData)
        f.close()
        
        return dataArr

    def readCriteria(self, criteria):
        # reads element lines in file
        # returns array of elements
        f = open("data_db.txt", "r")

        dataArr = []

        raw_data = f.readlines()
        for line in raw_data:
            lineData = json.loads(line.strip())
            dataArr.append(lineData)
        f.close()
        
        dataArr = self.filterTheDict(dataArr, criteria)
        
        
        return dataArr
    
    def saveScore(self, element):
        # guardar elemento en archivo 
        # appends to file
        jsonString = json.dumps(element)
        f = open("calificaciones.txt", "a")
        f.write(jsonString + "\n")
        f.close()
        
    def readScore(self, criteria):
        # reads element lines in file
        # returns array of elements
        f = open("calificaciones.txt", "r")

        dataArr = []

        raw_data = f.readlines()
        for line in raw_data:
            lineData = json.loads(line.strip())
            dataArr.append(lineData)
        f.close()
        
        dataArr = self.filterTheDict(dataArr, criteria)
        
        return dataArr
    
    def filterTheDict(self, arr, criteria):
        newDict = []
        # Iterate over all the items in dictionary
        for elem in arr:
            # Check if item satisfies the given condition then add to new dict
            if elem['matricula'] == criteria or elem['grupo'] == criteria:
                newDict.append(elem)
        return newDict