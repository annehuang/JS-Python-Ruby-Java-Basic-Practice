-- select 12 owners who have written at least 1 article from the most recent dates

select owner, max(date_created) from table1 group by owner order by date desc limit 12;
