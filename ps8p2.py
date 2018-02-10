from ps8 import *

def simulationWithDrug(numTrials, numTimeSteps):
    """
    Runs simulations and plots graphs for problem 4.Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time
    population
    vs. time are plotted
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



    dataMatrix = numpy.zeros(shape=(numTrials, numTimeSteps))
    dataMatri = numpy.zeros(shape=(numTrials, numTimeSteps))
    for trial in range(numTrials):
           # print "this"
            # Model a random patient with the given virus charateristics.
            viruses = virusCollection(numViruses, maxBirthProb, clearProb,resistances,mutProb)
            randPatientX = Patient(viruses, maxPop)


            # Simulate the time-steps.
            dataMatrix[trial][0] = numViruses


            for time in range(1,numTimeSteps):
                    if(time<150):
                        dataMatrix[trial][time] = randPatientX.update()
                        dataMatri[trial][time] = randPatientX.getResistPop(["guttagonol"])
                    else:
                        randPatientX.addPrescription("guttagonol")
                        dataMatrix[trial][time] = randPatientX.update()
                        dataMatri[trial][time] = randPatientX.getResistPop(["guttagonol"])




                # Statistical Analysis.
    meanData = dataMatrix.mean(0)
    time = numpy.arange(numTimeSteps)
    stdData95_CI = dataMatrix.std(0) * 2
    selectedTime = numpy.arange(0, numTimeSteps, 10)

    # Statistical Analysis.
    meanData1 = dataMatri.mean(0)
    time1 = numpy.arange(numTimeSteps)
    stdData95_CI1 = dataMatri.std(0) * 2
    selectedTime1 = numpy.arange(0, numTimeSteps, 10)



    # Ploting.
    pylab.plot(time, meanData, label="total virus population")
    pylab.errorbar(time[selectedTime], meanData[selectedTime], stdData95_CI[selectedTime], fmt='o')
    pylab.plot(time1, meanData1, label="guttagonol resistant")
    pylab.errorbar(time1[selectedTime1], meanData1[selectedTime1], stdData95_CI1[selectedTime1], fmt='o')
    pylab.legend(bbox_to_anchor=(1.05, 1),loc=4, borderaxespad=0.)
    pylab.xlabel("Time steps")
    pylab.ylabel("Mean virus population")
    pylab.title("Graph of virus simulation for applying medication after 150 timesteps", fontsize=14, fontweight='bold', )
    pylab.show()



simulationWithDrug(100,300)
