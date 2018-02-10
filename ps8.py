from ps7 import *
import numpy
import random
import pylab

class ResistantVirus(SimpleVirus):
    """Representation of a virus which can have drug resistance.
        """
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as
        attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        resistances: A dictionary of drug names (strings) mapping to the
        state
        of this virus particle's resistance (either True or False) to each
        drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.
        mutProb: Mutation probability for this virus particle (a float). This
        is
        the probability of the offspring acquiring or losing resistance to a
        drug.
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances={}
        self.mutProb = mutProb
        """            if resistances[x]==True:
                #print "t2"
                if random.random()<mutProb: #check!
                    self.resistances[x]=False
                else:
                    self.resistances[x] = True"""
        for x in resistances:
            if resistances[x]==True:
                #print "t2"
                self.resistances[x]=True
            elif resistances[x]==False:
                #print "f1"
                if random.random()<mutProb:
                    #print "t1"
                    self.resistances[x]=True
                else:
                    #print "f2"
                    self.resistances[x]=False


        # TODO
    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This
        method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.
        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if self.resistances[drug] == True:
            #print "Y"
            return True
        else:
            #print "x"
            return False
        # TODO

    def Rreproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.
        A virus particle will only reproduce if it is resistant to ALL the
        drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no
        drugs,
        then it will NOT reproduce.
        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:
        self.maxBirthProb * (1 - popDensity).If this virus particle reproduces, then reproduce() creates and
        returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent).
        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.
        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.
        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population
        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        #if resitant will reproduuce
        y=0
        if len(activeDrugs)!=0:
            for x in activeDrugs:
                if self.resistances[x]==True:
                    y+=1 #if its not resistant to any one of the drugs, y will increase
       # print y
        if y==len(activeDrugs) or not activeDrugs:#this means the virus is resistant to all drugs in activeDrugs
            # Does the virus reproduce?
            #print "child created"
            maxReproduceProb = self.maxBirthProb * (1 - popDensity)

            if random.random() < maxReproduceProb:
                childOfVirus = ResistantVirus(self.maxBirthProb, self.clearProb,self.resistances, self.mutProb)
                return childOfVirus

            else:
                raise NoChildException('Child not created!')

        else:#if virus is not resistant to all drugs
            #print "no child created"
            raise NoChildException('Child not created!')



        # TODO

class Patient(SimplePatient):
    """
        Representation of a patient. The patient is able to take drugs and
        his/her
        virus population can acquire resistance to the drugs he/she takes.
        """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered(which should initially include no drugs).
        viruses: The list representing the virus population (a list of
        SimpleVirus instances)
        maxPop: The maximum virus population for this patient (an integer)
        """
        errorMsg1 = 'viruses must be a list containing Resistant virus objects'
        errorMsg2 = 'maxPop, or maximum virus population must be an integer!'

        if type(viruses) != list: raise ValueError(errorMsg1)
        self.viruses = viruses

        if type(maxPop) != int: raise ValueError(errorMsg2)
        self.maxPop = maxPop

        self.listofDrugs = []
        # TODO

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If
        the
        newDrug is already prescribed to this patient, the method has no
        effect.
        newDrug: The name of the drug to administer to the patient (a
        string).
        postcondition: The list of drugs being administered to a patient is
        updated
        """
        if not newDrug in self.listofDrugs:
            self.listofDrugs.append(newDrug)


        # TODO
    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.listofDrugs
        # TODO

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed
        in
        drugResist.
        drugResist: Which drug resistances to include in the population (a
        list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])
        returns: The population of viruses (an integer) with resistances to
        all
        drugs in the drugResist list.
        """
        num = 0

        for drug in drugResist:
            for vir in self.viruses:
                if vir.isResistantTo(drug)==True:
                    num+=1

        return num

        # TODO
    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        - Determine whether each virus particle survives and update the list
        ofvirus particles accordingly
        - The current population density is calculated. This population
        density
        value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
        offspring virus particles to the list of viruses in this patient.
        The listof drugs being administered should be accounted for in the
        determination of whether each virus particle reproduces.
        returns: The total virus population at the end of the update (an
        integer)
        """
        # TODO

        # Determine number of viruses to be cleaned, "stochastically".
        resistantlist = []




        for virus in self.viruses:
                    if virus.doesClear()!=True:
                        resistantlist.append(virus)


        # Remove numRemoveVirus from the patient's body.
        """for virusNum in range(numRemoveVirus):
                    virs=self.viruses.pop()
                    if len(self.listofDrugs)!=0:
                        for drugs in self.listofDrugs:
                            if virs.isResistantTo(drugs):
                                resistantlist.append(virs)

        self.viruses += resistantlist"""

        # Calculate population density. TO DO check (keep self!)
        popDensity = self.getTotalPop() / float(self.maxPop)

        if popDensity >= 1:
            print 'virus population reached maximum!'
            popDensity = 1

            # Reproduce at a single time step.


        for virus in resistantlist:
            try:
                resistantlist.append(virus.Rreproduce(popDensity, self.getPrescriptions()))

            except NoChildException:
                pass

        self.viruses = resistantlist


        return self.getTotalPop()


def virusCollection(numViruses, maxBirthProb, clearProb, resistances,mutprob):


    viruses = []
    for virusNum in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutprob))
    return viruses

