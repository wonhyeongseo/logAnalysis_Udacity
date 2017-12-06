# logAnalysis_Udacity README
Source code for analyzing real-time web app log.

This code may be downloaded from: https://github.com/wonhyeongseo/logAnalysis_Udacity

How to use:
1. Log into Udacity's Virtual Machine (https://github.com/udacity/fullstack-nanodegree-vm)
2. Download newsdata.sql from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip 
3. Put code & newsdata.sql into a new subdirectory in /vagrant
4. Follow prepartion instructions on udacity, and create views as done in the bottom
5. Run by typing "python analysis.py"
6. Check if correct.

Sources: Udacity's Full Stack Web Developer NanoDegree Program

create view temp as select replace(replace(substring(path from 10), '-', ' '), 'so many', 'a lot of') as sub, count(path) as access from log where path::text like '/article/%' group by path order by access desc limit 8;

create view articles_ranking as select articles.title, temp.access, articles.author from articles inner join temp on lower(replace(articles.title::text, '''', '')) like '%' || temp.sub::text || '%' order by access desc;

create view authors_ranking as select name, access from authors inner join (select author, sum(access) as access from articles_ranking group by author) as t on t.author = authors.id;

create view daily_error_rates as select total.date, (error.count / total.count * 100) as percentage from (select substring(time::text from 0 for 11) as date, count(status) from log group by date) as total inner join (select substring(time::text from 0 for 11) as date, count(status) from log where status like '4%' or status like '5%' group by date) as error on total.date = error.date;
