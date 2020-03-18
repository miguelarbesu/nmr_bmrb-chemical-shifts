#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from bokeh.transform import factor_cmap
from bokeh.palettes import viridis
from bokeh.plotting import figure, save, output_file

ppm_ranges = {
              'C': [220, -20],
              'H': [20, -5],
              'N': [220, -20],
              }

massnumbers = {
              'C': '13',
              'H': '1',
              'N': '15',
              }


def makechart(infile, outfile, chart_size=(900, 900)):

    df = pd.read_csv(filepath_or_buffer=infile)
    unique_atoms = sorted(df['atom_id'].unique())
    atomtype = unique_atoms[0].split()[0]
    ppm_range = ppm_ranges[atomtype]
    aminoacids = sorted(df.comp_id.unique(), reverse=True)

    title = '{massnumber}{atom} chemical shift mean \
± one standard deviation'.format(
                                 massnumber=massnumbers[atomtype],
                                 atom=atomtype
                                 )

    fcmap = factor_cmap('atom_id',
                        palette=viridis(len(unique_atoms)),
                        factors=unique_atoms)
    tools = ['pan', 'wheel_zoom', 'reset', 'crosshair, hover']
    tooltips = [
        ('current position', '$x'),
        ('amino acid', '@comp_id'),
        ('atom type', '@atom_id'),
        ('avg', '@avg'),
        ('std', '@std'),
        ('max', '@max'),
        ('min', '@min'),
    ]

    p = figure(title=title,
               y_range=aminoacids,
               x_range=ppm_range,
               tools=tools,
               active_scroll='wheel_zoom',
               tooltips=tooltips,
               plot_width=chart_size[0], plot_height=chart_size[1])

    p.hbar(y='comp_id', left='avg-std', right='avg+std', height=0.75,
           alpha=0.75, fill_color=fcmap, source=df,
           legend_group='atom_id')

    p.hbar(y='comp_id', left='avg', right='avg', height=0.75,
           alpha=0.75, source=df, line_color='black', line_width=2.5)

    p.legend.location = "center_right"

    output_file(outfile)
    save(p, title=title)


for csv, html in zip(snakemake.input, snakemake.output):
    makechart(csv, html)
