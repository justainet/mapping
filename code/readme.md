bib_analysis.py is a python script to run co-citation analysis and bibliographic coupling on a dataset provided by the user.
It takes a CSV file where each row represents a unique paper. One column contains the paper’s title and another column contains the list of references cited by that paper, separated by a semi-colon.
The script produces two Gephi network files that can be used to visualise bibliographic coupling and co-citation networks.
The script is useful for analysing bibliometric data that is not indexed in the most commonly used databases, such as Scopus and Web of Science.
