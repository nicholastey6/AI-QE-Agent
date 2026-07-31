import sqlite3


conn = sqlite3.connect(
    "failures.db"
)


cursor = conn.cursor()



cursor.execute(
"""
CREATE TABLE IF NOT EXISTS failures(

id INTEGER PRIMARY KEY,

defect TEXT,

root_cause TEXT,

solution TEXT

)
"""
)



data = [

(
"Leakage current increase",

"Oxide thickness variation",

"Check oxidation temperature and recipe drift"
),


(
"Yield drop",

"Particle contamination",

"Inspect chamber cleanliness"
)

]



cursor.executemany(

"""
INSERT INTO failures
(
defect,
root_cause,
solution
)

VALUES

(?,?,?)

""",

data

)



conn.commit()


conn.close()


print(
"Database created"
)
