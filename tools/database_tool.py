import sqlite3


def search_failure(keyword):

    conn = sqlite3.connect(
        "database/failures.db"
    )

    cursor = conn.cursor()

    query = """
    SELECT *
    FROM failures
    WHERE defect LIKE ?
    """

    cursor.execute(
        query,
        ('%' + keyword + '%',)
    )

    result = cursor.fetchall()

    conn.close()

    return result
