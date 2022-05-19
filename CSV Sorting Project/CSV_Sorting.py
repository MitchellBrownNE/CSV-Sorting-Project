import csv
from typing import Dict, KeysView

### LoadFiles function ###
def LoadFiles():

    ### Lists intialization ###
    States = []
    HeartDiseaseRateList = []
    MotorVehicleList = []
    TeenBirthList = []
    AdultSmokingList = []
    AdultObesityList = []


    ### Opening csv file and creating list ###
    f = open("riskfactors.csv", "r")
    Reader = csv.reader(f)

    ### Titles ###
    for skip in range(5):
        next(Reader)
    Titles = next(Reader)

    ### For loop appending each line in each column ###
    for line in Reader:
        States.append(line[0])
        HeartDiseaseRateList.append(float(line[1]))
        MotorVehicleList.append(float(line[5]))
        TeenBirthList.append(float(line[7]))
        AdultSmokingList.append(float(line[11].strip("%")))
        AdultObesityList.append(float(line[13].strip("%")))

    ### Making dictionaries for each while zipping states to each category ###
    HeartDiseaseDict = dict(zip(States, HeartDiseaseRateList))
    MotorVehicleDict = dict(zip(States, MotorVehicleList))
    TeenBirthDict = dict(zip(States, TeenBirthList))
    AdultSmokingDict = dict(zip(States, AdultSmokingList))
    AdultObesityDict = dict(zip(States, AdultObesityList))
 

    ### Closing file ###
    f.close()

    ### Returning each dictionary to use elsewhere ###
    return (HeartDiseaseDict, MotorVehicleDict, TeenBirthDict, AdultSmokingDict, AdultObesityDict, Titles)
    

def Output():

    Dicts = LoadFiles()

    Titles = Dicts[5]

    ### Heart disease min and max ###
    HeartRate = Dicts[0] 
    MinHeartKey = min(HeartRate, key= HeartRate.get)
    MinHeartVal = HeartRate[MinHeartKey]
    MaxHeartKey = max(HeartRate, key= HeartRate.get)
    MaxHeartVal = HeartRate[MaxHeartKey]

    ### Motor vehicle min and max ###
    MotorVehicle = Dicts[1]
    MinMotorKey = min(MotorVehicle, key= MotorVehicle.get)
    MinMotorVal = MotorVehicle[MinMotorKey]
    MaxMotorKey = max(MotorVehicle, key= MotorVehicle.get)
    MaxMotorVal = MotorVehicle[MaxMotorKey]

    ### Teen birth min and max ###
    TeenBirth = Dicts[2]
    MinTeenKey = min(TeenBirth, key= TeenBirth.get)
    MinTeenVal = TeenBirth[MinTeenKey]
    MaxTeenKey = max(TeenBirth, key= TeenBirth.get)
    MaxTeenVal = TeenBirth[MaxTeenKey]

    ### Adult smoking min and max ###
    AdultSmoking = Dicts[3]
    MinSmokingKey = min(AdultSmoking, key= AdultSmoking.get)
    MinSmokingVal = AdultSmoking[MinSmokingKey]
    MaxSmokingKey = max(AdultSmoking, key= AdultSmoking.get)
    MaxSmokingVal = AdultSmoking[MaxSmokingKey]

    ### Adult obesity min and max ###
    AdultObesity = Dicts[4]
    MinObesityKey = min(AdultObesity, key= AdultObesity.get)
    MinObesityVal = AdultObesity[MinObesityKey]
    MaxObesityKey = max(AdultObesity, key= AdultObesity.get)
    MaxObesityVal = AdultObesity[MaxObesityKey]

    file = open("Best_And_Worst.txt", "w")

    file.write("{0:48}{1:50}{2:50}".format("Category", ": Min", "Max"))
    file.write("\n")
    file.write("-" * 124)
    file.write("\n{0:<50}{1:<30}{2:5}{3:>24}{4:>15}".format(Titles[1], MinHeartKey, MinHeartVal, MaxHeartKey, MaxHeartVal))
    file.write("\n{0:<50}{1:<30}{2:5.1f}{3:>20}{4:>19.1f}".format(Titles[5], MinMotorKey, MinMotorVal, MaxMotorKey, MaxMotorVal))
    file.write("\n{0:<50}{1:<30}{2:5}{3:>24}{4:>15}".format(Titles[7], MinTeenKey, MinTeenVal, MaxTeenKey, MaxTeenVal))
    file.write("\n{0:50}{1:<30}{2:>5}{3:>26}{4:>13}".format(Titles[11], MinSmokingKey, MinSmokingVal, MaxSmokingKey, MaxSmokingVal))
    file.write("\n{0:50}{1:<30}{2:>5}{3:>24}{4:>15}".format(Titles[13], MinObesityKey, MinObesityVal, MaxObesityKey, MaxObesityVal))

    
    file.close()


Output()
