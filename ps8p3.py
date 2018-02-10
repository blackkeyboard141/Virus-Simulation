
from ps8 import *
from pyhisty import *

def simulationDelayedTreatment(numTrials, delay):
    """Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed
    treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of
    300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
    """

    # TODO


    #random.seed()


    # Virus Characteristics.
    maxPop = 1000
    numViruses = 100
    maxBirthProb = 0.1
    clearProb = 0.05
    mutProb = .005
    resistances={}
    resistances["guttagonol"]=False
    numTimeSteps=delay+150
    count=0



    triallist=[]
    for trial in range(numTrials):
           # print "this"
            # Model a random patient with the given virus charateristics.
            viruses = virusCollection(numViruses, maxBirthProb, clearProb,resistances,mutProb)
            randPatientX = Patient(viruses, maxPop)

            dataMatrix = []
            for time in range(1,numTimeSteps):
                    if(time<delay):
                        dataMatrix.append(randPatientX.update())
                    else:
                        randPatientX.addPrescription("guttagonol")
                        dataMatrix.append(randPatientX.update())
            x=dataMatrix.pop()
            triallist.append(x)
            if x>=0 and x<=50:
                count+=1

    percentage = (count*1.0/numTrials*1.0)*100

    return triallist,percentage

listss , perce = simulationDelayedTreatment(1000,300)
streeng = "total virus population values, Cured =",perce
plothisty(listss,streeng,"patients","Delayed simulation with delay = 300")

listss , perce = simulationDelayedTreatment(1000,150)
streeng = "total virus population values, Cured =",perce
plothisty(listss,streeng,"patients","Delayed simulation with delay = 150")

listss , perce = simulationDelayedTreatment(1000,75)
streeng = "total virus population values, Cured =",perce
plothisty(listss,streeng,"patients","Delayed simulation with delay = 75")

listss , perce = simulationDelayedTreatment(1000,0)
streeng = "total virus population values, Cured =",perce
plothisty(listss,streeng,"patients","Delayed simulation with delay = 0")

