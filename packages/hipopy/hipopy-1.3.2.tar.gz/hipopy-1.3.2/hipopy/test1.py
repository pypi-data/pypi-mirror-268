class hipochainIterator:

    """
    Attributes
    ----------
    chain : hipopy.hipopy.hipochain
        Hipochain object overwhich to iterate
    idx : int
        Index of current file in hipochain
    counter : int
        Event counter for batching data
    file : hipopy.hipopy.hipoFile
        Current file in hipochain
    items : dict
        Dictionary of bank names to item names to read
    dict : dict
        Dictionary into which Hipo bank data is read

    Methods
    -------
    switchFile

    Description
    -----------
    Iterator for hipopy.hipopy.hipochain class
    """

    def __init__(self,chain):
        self.chain   = chain
        self.nnames  = len(self.chain.names) #NOTE: Assumes this will stay constant.
        self.idx     = -1
        self.counter = 0
        self.file    = None
        self.items   = {}
        self.dict    = None
        # self.experimental = True
        # self.tags = [0,1] #NOTE: EXPERIMENTAL
        # if self.experimental and self.chain.banks is None: self.switchFile()
        # if self.experimental:
        #     self.reached_end = False
        #     self.hbHipoFileIterator = hipopybind.HipoFileIterator(self.chain.names,self.chain.banks,self.chain.step,self.tags) #NOTE: EXPERIMENTAL

    def switchFile(self):
        """
        Description
        -----------
        Checks if next file in chain exists and then opens and reads requested banks if so.
        """
        # Open file
        self.idx += 1 #NOTE: Do this before everything below since we initiate at -1.
        if self.idx>=self.nnames: return #NOTE: Sanity check
        self.file = hipofile(self.chain.names[self.idx],mode=self.chain.mode,tags=self.chain.tags)
        self.file.open()
        
        if self.chain.banks is None: self.chain.banks = self.file.getBanks() #NOTE: This assumes all the files in the chain have the same banks.

        # Read all requested banks
        for b in self.chain.banks:
            self.file.readBank(b,self.chain.verbose)
            helper = self.file.getNamesAndTypes(b)
            self.items[b] = helper

    def __next__(self):
        """
        Description
        -----------
        Loops files reading requested banks if they exist 
        """

        # if self.experimental:

        #     has_events = self.hbHipoFileIterator.__next__()
        #     banknames = self.hbHipoFileIterator.banknames
        #     items = self.hbHipoFileIterator.items
        #     types = self.hbHipoFileIterator.types
        #     datadict = {}
        #     for idx, bankname in enumerate(banknames):
        #         for idx2, item in enumerate(items[idx]):
        #             item_type = types[idx][idx2]
        #             if item_type==5: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getDoubles(bankname,item)
        #             elif item_type==4: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getFloats(bankname,item)
        #             elif item_type==3: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getInts(bankname,item)
        #             elif item_type==8: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getLongs(bankname,item)
        #             elif item_type==2: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getShorts(bankname,item)
        #             elif item_type==1: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getBytes(bankname,item)

        #     self.experimental = has_events
        #     return datadict
        # raise StopIteration
        

        if self.idx == -1: self.switchFile() # Load first file manually

        if self.idx<(self.nnames): #TODO: Check this condition.

            # Check if output array has been initialized
            if self.dict is None:
                self.dict = {}

            # Loop events in current file
            while self.file.nextEvent():

                # Get bank data
                for bank in self.chain.banks:
                    self.file.event.getStructure(self.file.banklist[bank])#NOTE: NECESSARY OR YOU WILL NOT READ ANY DATA!
                    for item in self.items[bank]:
                        data = []
                        item_type = self.items[bank][item]
                        if   item_type=="D": data = self.file.getDoubles(bank,item)
                        elif item_type=="I": data = self.file.getInts(bank,item)
                        elif item_type=="F": data = self.file.getFloats(bank,item)
                        elif item_type=="L": data = self.file.getLongs(bank,item)
                        elif item_type=="S": data = self.file.getShorts(bank,item)
                        elif item_type=="B": data = self.file.getBytes(bank,item)

                        # Add bank data to batch dictionary
                        if not bank+"_"+item in self.dict: self.dict[bank+"_"+item] = [data]
                        else: self.dict[bank+"_"+item].append(data)

                # Check size of output array
                self.counter += 1
                if self.counter % self.chain.step == 0:
                    res       = self.dict
                    self.dict = None
                    return res

            # Switch the file AFTER you get through event loop above
            self.switchFile()

        # Final return for remainder
        if self.dict != None and len(self.dict.keys())>0:
            res       = self.dict
            self.dict = None
            return res #TODO: Will this return last remainder that is not necessarily stepsize?
        
        # Final stop
        raise StopIteration
