# logAnalysis_Udacity README
Source code for analyzing a real-time web app's log. The web app is a fictional news site
with 8 articles in total. These are all stored in a PostgreSQL database, called 'news'.
The 'news' database has 3 tables in it, "articles", "authors", and "log". You may find
additional information about the database by exploring it yourself, as explained
in the "How to use" section below.
The assignment was to give answers to the following 3 questions.
1) What are the 3 highest ranking articles and their access counts?
2) What is the authors' ranking by access counts?
3) In which day did errors occur more than 1% of the transactions?
I created views to simplify the select statement in the python script, and these
can be recreated by passing the 4 'create view' statements at the bottom to the
news database.
My first approach was to use the psycopg2 module in python to query the news
database. But it gave multiple OperationalErrors such as, "password not provided" 
or "incorrect password". So that is why I used the subprocess module to bypass
the password required by the virtual machine. Next, for the UI, a simple text menu
was created for interactive usage and reporting.

This code may be downloaded from: https://github.com/wonhyeongseo/logAnalysis_Udacity

## Requirements
* Git CMD
* Vagrant
* VirtualBox

## How to use:
(Assuming you have installed the Requirements by their **default** settings...)
1. Donwload analysis.py in this github dipository.
2. Download [Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm), and create_views.sql from this dipository.
3. Download newsdata.sql from [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. Put analysis.py, Vagrantfile, newsdata.sql into a new directory called 'vagrant' inside another directory. (For example, "Downloads/logAnalysis/vagrant")
5. Open Git CMD, and navigate to the directory in step 4.
6. Type "vagrant up". If this doesn't work, check if your computer's [Intel Virtual Technology is enabled in the BIOS](http://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html).
7. If "Done installing your virtual machine!" shows in the conosle, you are ready to type in,
"vagrant ssh".
8. Congradulations! You are inside your virtual machine. Type in, "cd /vagrant".
9. Type in "psql -d news -f newsdata.sql". This will connect to your installed database server.
10. Now type in "psql -d news -f create_views.sql". This will create views needed for the python script.
11. Run the logAnalysis tool by typing "python analysis.py"
12. Check your results with the analysisresults.txt. If different, please message me.

Sources: Udacity's Full Stack Web Developer NanoDegree Program
