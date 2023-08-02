import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


def execute_query(curs, query):
    curs.execute(query)
    conn.commit()
    return curs.fetchall()


demo = '''
CREATE TABLE IF NOT EXISTS demo (
  "s" TEXT NOT NULL,
  "x" INT NOT NULL,
  "y" INT NOT NULL
);
'''

INSERT_DEMO = '''
  INSERT INTO demo (s, x, y)
  VALUES
  ('g', 3, 9),
  ('v', 5, 7),
  ('f', 8, 7);
'''
queries = (demo, INSERT_DEMO)

row_count = '''
    SELECT COUNT(*)
    FROM demo
'''
xy_at_least_5 = '''
    SELECT COUNT(*)
    FROM demo
    WHERE x>=5 AND y>=5
'''

unique_y = '''
    SELECT COUNT(DISTINCT y)
    FROM demo
'''
if __name__ == "__main__":
    print(execute_query(curs, queries))
