#!/bin/sh
python SpeechSampling.py
python Menu.py
python Apriori.py -f menu_hist.csv -c 0.4 -s 0.4

