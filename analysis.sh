#!/usr/bin/env bash
echo '----Logs Analysis Tool for Udacity Backend Project----'
echo '<any character> + <backspace> + <Enter> to see menu again.'
OPTIONS="Top_Three_Articles Authors_Ranking Days_Of_Many_Errors Quit"
select opt in $OPTIONS; do
    if [ "$opt" = "Quit" ]; then
      echo done
      exit
    elif [ "$opt" = "Top_Three_Articles" ]; then
      psql -d news -c "select title, access from articles_ranking limit 3"
    elif [ "$opt" = "Authors_Ranking" ]; then
      psql -d news -c "select * from authors_ranking"
    elif [ "$opt" = "Days_Of_Many_Errors" ]; then
      psql -d news -c "select * from daily_error_rates where percentage >= 1.0;"
    else
      clear
      echo bad option
    fi
done