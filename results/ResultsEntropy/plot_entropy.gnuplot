
# Script for plotting entropy results with custom proportions

set datafile separator ","

# Set terminal with transparent background, Helvetica Bold, and desired size
set terminal pngcairo transparent size 1400,800 enhanced font "Helvetica-Bold,20" 

# First plot: Z0, Z2, Z3
set output 'Entropy_Z0_Z2_Z3.png'

set xlabel 'Time'
set ylabel 'Entanglement Entropy (log2)'
set title 'Entanglement Entropy over Time'
set grid
set key top right

plot 'entropy_N16_PBC_Z0.csv' using 1:2 with lines lw 3 lc rgb '#1f77b4' title 'Z0',      'entropy_N16_PBC_Z2.csv' using 1:2 with lines lw 3 lc rgb '#ff7f0e' title 'Z2',      'entropy_N16_PBC_Z3.csv' using 1:2 with lines lw 3 lc rgb '#2ca02c' title 'Z3'


# Second plot: Z2, Z2_flip_up, Z2_flip_down
set output 'Entropy_Z2_Z2up_Z2down.png'

set xlabel 'Time'
set ylabel 'Entanglement Entropy (log2)'
set title 'Entanglement Entropy: Z2 with Flips'
set grid
set key top right

plot 'entropy_N16_PBC_Z2.csv' using 1:2 with lines lw 3 lc rgb '#ff7f0e' title 'Z2',      'entropy_N16_PBC_Z2_flip_up.csv' using 1:2 with lines lw 3 lc rgb '#d62728' title 'Z2 Flip Up',      'entropy_N16_PBC_Z2_flip_down.csv' using 1:2 with lines lw 3 lc rgb '#9467bd' title 'Z2 Flip Down'

set output
