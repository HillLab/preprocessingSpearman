# SpearmansRank
Sequence.py script used for pre-processing groups of *fasta files so they can be used as an input for SRCC R script (Spearman's Rank Correlation Coefficient). 
 - Sequence.py is a little messy and suboptimal, so you can decide to remake the functions if you want, or I would recommend just calling them in
   the new Python script being developed for SRCC. 
Steps to run the script: 
- Run the script 
- Set fastagroup to be the name of your folder with all your sequence in it. 
- You can now call chop.Sequence() to chop all fasta files within the set directory to 20kb chunks.
	- This raises a small issue, since all the outputs are in their seperate folders, 
	  you might want to write a script that then also moves all the chunks into a single folder to make work easier.
- You can also use spearman.prep(). This will prepare your sequences for the R script. 
	- It takes every fasta file in the trajectory, and it extracts the proportions of k-mers for each. An example is provided below. The outputs need to be in .xlsx
	 and labeld as shown in the sample folder (NameofGroup_k=n where n is the kmer value of this folder)

-This output is then entered into the R script.

Random move is another script you might want to implement into your script. It randomly moves  set percentage or number 
of folders from one directory to another. Good if you want to randomly sample your data. 

Updatedfilesplitting is also necessary. It is a necessary script that you use to split multi-fastas (a single fasta file with 
multiple sequneces inside. This should be implemented in before Sequence.py (but it should be optional, so students could toggle it)


***All things included in the folder are numbered by the order they go before they go into the r script for SRCC
