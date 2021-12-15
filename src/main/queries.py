#The top 10 games for all consoles
all_top_10 = """SELECT * FROM results_ ORDER BY avg_score DESC LIMIT 10"""
#The worst 10 games for all consoles
all_bottom_10 = """SELECT * FROM results_  ORDER BY avg_score  LIMIT 10"""

#The top 10 games for each console-company
top_10_by_console_cmp = """SELECT * FROM (SELECT A.avg_score, UPPER(A.console) as console, \
UPPER(B.company) as company, A.name, \
ROW_NUMBER() OVER (PARTITION BY A.console, B.company ORDER BY A.avg_score DESC) RANKING_AVG \
FROM results_ A \
LEFT JOIN consoles_ B ON A.console = B.console) \
WHERE RANKING_AVG <= 10"""

#The worst 10 games for each console-company
worst_10_by_console_cmp = """SELECT * FROM (SELECT A.avg_score, UPPER(A.console) as console, \
UPPER(B.company) as company, A.name, \
ROW_NUMBER() OVER (PARTITION BY A.console, B.company ORDER BY A.avg_score) RANKING_AVG \
FROM results_ A \
LEFT JOIN consoles_ B ON A.console = B.console) \
WHERE RANKING_AVG <= 10"""