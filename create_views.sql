CREATE VIEW articles_ranking AS
SELECT a.title, l.access, a.author
FROM articles a INNER JOIN(
  SELECT path, count(*) AS access
  FROM log
  GROUP BY path
) l
ON l.path = '/article/' || a.slug
ORDER BY access DESC;

CREATE VIEW authors_ranking AS 
SELECT name, access 
FROM authors INNER JOIN (
  SELECT author, SUM(access) AS access 
  FROM articles_ranking GROUP BY author
) AS t
ON t.author = authors.id;

CREATE VIEW daily_error_rates AS
SELECT to_char(a.date, 'Mon DD, YYYY') AS date, (a.errors * 100 / CAST(b.requests AS float)) AS percentage
FROM 
  (
  SELECT time::date AS date, count(*) AS errors
  FROM log 
  WHERE status != '200 OK' 
  GROUP BY date
  ) AS a, 
  (
  SELECT time::date AS date, count(*) AS requests 
  FROM log 
  GROUP BY date
  ) AS b 
WHERE a.date = b.date AND (a.errors * 100 / CAST(b.requests AS float)) >= 1
