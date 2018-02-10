from ps8 import *

def simulationTwoDrugsVirusPopulations(numTrials):
    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    Histograms of final total virus populations are displayed for lag times
    of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
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
    resistances["grimpex"] = False
    delay=300
    numTimeSteps=150+delay+150




    dataMatrix = numpy.zeros(shape=(numTrials, numTimeSteps))
    dataglutagonol = numpy.zeros(shape=(numTrials, numTimeSteps))
    datagrimpex = numpy.zeros(shape=(numTrials, numTimeSteps))
    databoth = numpy.zeros(shape=(numTrials, numTimeSteps))
    for trial in range(numTrials):
           # print "this"
            # Model a random patient with the given virus charateristics.
            viruses = virusCollection(numViruses, maxBirthProb, clearProb,resistances,mutProb)
            randPatientX = Patient(viruses, maxPop)

            dataMatrix[trial][0] = numViruses
            for time in range(1,numTimeSteps):
                    if(time<=150):
                        dataMatrix[trial][time]=randPatientX.update()
                        numberglutagonol=randPatientX.getResistPop(["guttagonol"])
                        dataglutagonol[trial][time]=numberglutagonol
                        numbergrimpex= randPatientX.getResistPop(["grimpex"])
                        datagrimpex[trial][time] = numbergrimpex
                        databoth[trial][time] = numberglutagonol+numbergrimpex
                    elif time>150 and time<=150+delay :
                        randPatientX.addPrescription("guttagonol")
                        dataMatrix[trial][time] = randPatientX.update()
                        numberglutagonol = randPatientX.getResistPop(["guttagonol"])
                        dataglutagonol[trial][time] = numberglutagonol
                        numbergrimpex = randPatientX.getResistPop(["grimpex"])
                        datagrimpex[trial][time] = numbergrimpex
                        databoth[trial][time] = numberglutagonol + numbergrimpex
                    elif time>150+delay and time <numTimeSteps:
                        randPatientX.addPrescription("grimpex")
                        dataMatrix[trial][time] = randPatientX.update()
                        numberglutagonol = randPatientX.getResistPop(["guttagonol"])
                        dataglutagonol[trial][time] = numberglutagonol
                        numbergrimpex = randPatientX.getResistPop(["grimpex"])
                        datagrimpex[trial][time] = numbergrimpex
                        databoth[trial][time] = numberglutagonol + numbergrimpex

                        # Statistical Analysis.
    meanData = dataMatrix.mean(0)
    time = numpy.arange(numTimeSteps)
    stdData95_CI = dataMatrix.std(0) * 2
    selectedTime = numpy.arange(0, numTimeSteps, 10)

    meanData1 = dataglutagonol.mean(0)
    time1 = numpy.arange(numTimeSteps)
    stdData95_CI1 = dataglutagonol.std(0) * 2
    selectedTime1 = numpy.arange(0, numTimeSteps, 10)

    meanData2 = datagrimpex.mean(0)
    time2 = numpy.arange(numTimeSteps)
    stdData95_CI2 = datagrimpex.std(0) * 2
    selectedTime2 = numpy.arange(0, numTimeSteps, 10)

    meanData3 = databoth.mean(0)
    time3 = numpy.arange(numTimeSteps)
    stdData95_CI3 = databoth.std(0) * 2
    selectedTime3 = numpy.arange(0, numTimeSteps, 10)

    # Ploting.
    pylab.plot(time, meanData, label="Total population")
    pylab.errorbar(time[selectedTime], meanData[selectedTime], stdData95_CI[selectedTime], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    pylab.plot(time1, meanData1, label="Glutagonol resistant")
    pylab.errorbar(time1[selectedTime1], meanData1[selectedTime1], stdData95_CI1[selectedTime1], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    pylab.plot(time2, meanData2, label="Grimpex resistant")
    pylab.errorbar(time2[selectedTime2], meanData2[selectedTime2], stdData95_CI2[selectedTime2], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    pylab.plot(time3, meanData3, label="Total resistant population")
    pylab.errorbar(time3[selectedTime3], meanData3[selectedTime3], stdData95_CI3[selectedTime3], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    numTimeSteps4 = 150 + 150

    dataMatrix4 = numpy.zeros(shape=(numTrials, numTimeSteps4))
    dataglutagonol4 = numpy.zeros(shape=(numTrials, numTimeSteps4))
    datagrimpex4 = numpy.zeros(shape=(numTrials, numTimeSteps4))
    databoth4 = numpy.zeros(shape=(numTrials, numTimeSteps4))
    for trial in range(numTrials):
        # print "this"
        # Model a random patient with the given virus charateristics.
        viruses = virusCollection(numViruses, maxBirthProb, clearProb, resistances, mutProb)
        randPatientX = Patient(viruses, maxPop)

        dataMatrix4[trial][0] = numViruses
        for time in range(1, numTimeSteps4):
            if (time <= 150):
                dataMatrix4[trial][time] = randPatientX.update()
                numberglutagonol4 = randPatientX.getResistPop(["guttagonol"])
                dataglutagonol4[trial][time] = numberglutagonol4
                numbergrimpex4 = randPatientX.getResistPop(["grimpex"])
                datagrimpex4[trial][time] = numbergrimpex4
                databoth4[trial][time] = numberglutagonol4 + numbergrimpex4
            elif time > 150 and time < numTimeSteps4:
                randPatientX.addPrescription("guttagonol")
                randPatientX.addPrescription("grimpex")
                dataMatrix4[trial][time] = randPatientX.update()
                numberglutagonol4 = randPatientX.getResistPop(["guttagonol"])
                dataglutagonol4[trial][time] = numberglutagonol4
                numbergrimpex4 = randPatientX.getResistPop(["grimpex"])
                datagrimpex4[trial][time] = numbergrimpex4
                databoth4[trial][time] = numberglutagonol4 + numbergrimpex4

                # Statistical Analysis.
    meanData5 = dataMatrix4.mean(0)
    time5 = numpy.arange(numTimeSteps4)
    stdData95_CI5 = dataMatrix4.std(0) * 2
    selectedTime5 = numpy.arange(0, numTimeSteps4, 10)

    meanData6 = dataglutagonol4.mean(0)
    time6 = numpy.arange(numTimeSteps4)
    stdData95_CI6 = dataglutagonol4.std(0) * 2
    selectedTime6 = numpy.arange(0, numTimeSteps4, 10)

    meanData7 = datagrimpex4.mean(0)
    time7 = numpy.arange(numTimeSteps4)
    stdData95_CI7 = datagrimpex4.std(0) * 2
    selectedTime7 = numpy.arange(0, numTimeSteps4, 10)

    meanData8 = databoth4.mean(0)
    time8 = numpy.arange(numTimeSteps4)
    stdData95_CI8 = databoth4.std(0) * 2
    selectedTime8 = numpy.arange(0, numTimeSteps4, 10)

    # Ploting.
    pylab.plot(time5, meanData5, label="total population")
    pylab.errorbar(time5[selectedTime5], meanData5[selectedTime5], stdData95_CI5[selectedTime5], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    pylab.plot(time6, meanData6, label="guttagonol resistant")
    pylab.errorbar(time6[selectedTime6], meanData6[selectedTime6], stdData95_CI6[selectedTime6], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    pylab.plot(time7, meanData7, label="grimpex resistant")
    pylab.errorbar(time7[selectedTime7], meanData7[selectedTime7], stdData95_CI7[selectedTime7], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)

    pylab.plot(time8, meanData8, label="total resistant population")
    pylab.errorbar(time8[selectedTime8], meanData8[selectedTime8], stdData95_CI8[selectedTime8], fmt='o')
    pylab.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                 ncol=2, mode="expand", borderaxespad=0.)



    pylab.xlabel("Time steps")
    pylab.ylabel("Virus")
    pylab.show()



simulationTwoDrugsVirusPopulations(100)

