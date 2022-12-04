#!/bin/sh
python3 demineur.py 0
python3 demineur.py 0 0
python3 demineur.py 0 0 0
python3 demineur.py 'a'
python3 demineur.py 'a' 'a'
python3 demineur.py 'a' 'a' 'a'
python3 demineur.py 'a' 0 0
python3 demineur.py 0 'a' 0
python3 demineur.py 0 0 'a'
python3 demineur.py 0 0 0 0
python3 demineur.py 0 0 0 0 0
python3 demineur.py -1 0 0
python3 demineur.py 0 -1 0
python3 demineur.py 0 0 -1
python3 demineur.py 0 0 0 -1
python3 demineur.py 0 0 0 0 -1
python3 demineur.py 1 0 0
python3 demineur.py 0 1 0
python3 demineur.py 0 0 1
python3 demineur.py 2 0 0
python3 demineur.py 0 2 0
python3 demineur.py 0 0 2
python3 demineur.py 3 0 0
python3 demineur.py 0 3 0
python3 demineur.py 0 0 3
python3 demineur.py 4 0 0
python3 demineur.py 0 4 0
python3 demineur.py 0 0 4
python3 demineur.py 5 0 0
python3 demineur.py 0 5 0
python3 demineur.py 0 0 5
python3 demineur.py 3 3 3
python3 demineur.py 3 3 0
python3 demineur.py 3 0 3
python3 demineur.py 0 3 3
python3 demineur.py 4 4 0
python3 demineur.py 4 0 4
python3 demineur.py 0 4 4
python3 demineur.py 5 5 0
python3 demineur.py 5 0 5
python3 demineur.py 0 5 5
python3 demineur.py 6 2 6
python3 demineur.py 2 6 6
python3 demineur.py 6 6 6 6


for i in 0 1 10 20 100 200 1000 2000 10000 20000 1000000 2000000; do
    python3 demineur.py $i $i $i
done


