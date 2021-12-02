#!/usr/bin/env bash
## Ford Fishman

# Set pathing
sourcepath=/N/slate/ffishman/RhizobiumDefense/CasProfiles

output=/N/slate/ffishman/RhizobiumDefense/output.fasta

# remove output file if it exists
if [ -f $output ]; then rm $output; fi

# run python script on all cas profiles (.sr files)
for file in $sourcepath/*.sr
do
    # python3 make_fasta.py -f "$file" -o $output
    python3 make_fasta.py -f "$file"
done
