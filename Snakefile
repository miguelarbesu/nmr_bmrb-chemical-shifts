rule fetch:
    input: 
    output: "data/aa_filt.csv" 
    shell: 
        """
        cd data
        wget 'http://www.bmrb.wisc.edu/ftp/pub/bmrb/statistics/chem_shifts/aa_filt.csv'
        cd ..
        """

