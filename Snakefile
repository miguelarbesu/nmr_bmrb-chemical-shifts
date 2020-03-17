ATOMS = ['C', 'H', 'N']

rule fetch:
    input: 
    output: 
        'data/raw/bmrb_cs_stats_filtered.csv' 
    shell: 
        'wget http://www.bmrb.wisc.edu/ftp/pub/bmrb/statistics/chem_shifts/aa_filt.csv -O {output}'


rule split:
    input: 
        'data/raw/bmrb_cs_stats_filtered.csv'
    output: 
        expand('data/processed/{atoms}_bmrb_cs_stats_filtered.csv',
        atoms=ATOMS)
    run:
        import pandas as pd 

        df = pd.read_csv(filepath_or_buffer=input[0])
        df['avg-std'] = df['avg'] - df['std']
        df['avg+std'] = df['avg'] + df['std']
            
        for atom in ATOMS:
            out_file = 'data/processed/{atom}_bmrb_cs_stats_filtered.csv'.format(atom=atom)
            atomdf = df[df['atom_id'].str.startswith(atom)]
            atomdf.to_csv(path_or_buf=out_file)

rule all:
    input:
        expand('data/processed/{atoms}_bmrb_cs_stats_filtered.csv',
        atoms=ATOMS)