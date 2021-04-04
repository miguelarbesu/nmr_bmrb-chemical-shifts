#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


ATOMS = ['C', 'H', 'N']

def process(csv_file):
    df = pd.read_csv(filepath_or_buffer=csv_file)
    # Rename Methyl Hs (MX#) as H's
    df["atom_id"] = df["atom_id"].str.replace('M', 'H')
    # Calculate limits
    df['avg-std'] = df['avg'] - df['std']
    df['avg+std'] = df['avg'] + df['std']
    # Split and save    
    for atom in ATOMS:
        print(atom)
        out_file = f'data/processed/{atom}_bmrb_cs_stats_filtered.csv'
        atomdf = df[df['atom_id'].str.startswith(atom)]
        atomdf.to_csv(path_or_buf=out_file)


if __name__=="__main__":
    process(snakemake.input)
