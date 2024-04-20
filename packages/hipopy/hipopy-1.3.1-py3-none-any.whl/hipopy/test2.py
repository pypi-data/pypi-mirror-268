
class hipochainIteratorExperimental:

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
    getAllBanks

    Description
    -----------
    Experimental iterator for hipopy.hipopy.hipochain class
    """

    def __init__(self,chain):
        self.chain   = chain
        self.nnames  = len(self.chain.names) #NOTE: Assumes this will stay constant.
        self.idx     = -1
        self.file    = None
        if self.chain.banks is None: self.getAllBankNames()
        self.has_events = True
        self.hbHipoFileIterator = hipopybind.HipoFileIterator(self.chain.names,self.chain.banks,self.chain.step,self.chain.tags)
        self.banknames = self.hbHipoFileIterator.banknames
        self.items = self.hbHipoFileIterator.items
        self.types = self.hbHipoFileIterator.types
        self.batch_counter = 0

    def getAllBankNames(self):
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

    def __next__(self):
        """
        Description
        -----------
        Loops files reading requested banks if they exist 
        """

        if self.has_events:
            if self.batch_counter==0:
                self.has_events = self.hbHipoFileIterator.__next__()
            self.batch_counter += 1
            datadict = {}
            for idx, bankname in enumerate(self.banknames):
                for idx2, item in enumerate(self.items[idx]):
                    item_type = self.types[idx][idx2]
                    if item_type==5: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getDoubles(bankname,item)
                    elif item_type==4: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getFloats(bankname,item)
                    elif item_type==3: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getInts(bankname,item)
                    elif item_type==8: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getLongs(bankname,item)
                    elif item_type==2: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getShorts(bankname,item)
                    elif item_type==1: datadict[bankname+"_"+item] = self.hbHipoFileIterator.getBytes(bankname,item)
            self.has_events = self.hbHipoFileIterator.__next__() #NOTE: IMPORTANT THIS SHOULD BE FILLING THE DICTIONARY SO self.has_events IS SET CORRECTLY FOR THE NEXT CALL.
            return datadict
        raise StopIteration
