# Webscrape of tech stacks from remote companies with job listings

The source are companies listed on https://himalayas.app/companies

Install Python 3

* Run `python scrap.py` to save all the languages and frameworks in data.txt

* Afterwards, run `python stat.py` to get a count of each stack

Results from 5 June 2022 are listed in `languages and frameworks.csv`

You can change `data-category` in `scrap.py` (line 26), so something other than "Languages & Frameworks", e.g. "Data Stores" or whatever tech stsack statistics interest you.