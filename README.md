# nmr_bmrb-chemical-shifts

A visualization tool for the [**Biological Magnetic Resonance Databank (BMRB)**](http://www.bmrb.wisc.edu/) chemical shift statistics.

The [filtered data set](http://www.bmrb.wisc.edu/ref_info/stats.php?set=filt&restype=aa&output=html)<sup>1</sup> for standard amino acids is fetched and 
split, then interactive [Bokeh](https://docs.bokeh.org/en/latest/index.html)
 charts are available for each nucleus:

## [<sup>13</sup>C chemical shift stats](https://miguelarbesu.github.io/nmr_bmrb-chemical-shifts/html/C_bmrb_cs_stats_filtered.html) 

## [<sup>1</sup>H chemical shift stats](https://miguelarbesu.github.io/nmr_bmrb-chemical-shifts/html/H_bmrb_cs_stats_filtered.html)

## [<sup>15</sup>N chemical shift stats](https://miguelarbesu.github.io/nmr_bmrb-chemical-shifts/html/N_bmrb_cs_stats_filtered.html)

Black vertical lines indicate the mean chemical shift for each atom, while
the colored horizontal bars indicate ± one standard deviation range.

All charts can be panned and zoomed (also the individual axes). Hover over each bar to see the corresponding data:
- Amino acid type
- Atom type
- Chemical shift stats
    - Average
    - Standard deviation
    - Minimum
    - Maximum


<sup>1</sup> Only chemical shifts from standard amino acids in diamagnetic samples.