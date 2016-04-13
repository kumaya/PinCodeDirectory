import csv, sqlite3

def _get_col_datatypes(fin):
    dr = csv.DictReader(fin) # comma is default delimiter
    fieldTypes = {}
    for entry in dr:
        feildslLeft = [f for f in dr.fieldnames if f not in fieldTypes.keys()]
        if not feildslLeft: break # We're done
        for field in feildslLeft:
            data = entry[field]

            # Need data to decide
            if len(data) == 0:
                continue

            if data.isdigit():
                fieldTypes[field] = "INTEGER"
            else:
                fieldTypes[field] = "TEXT"
        # TODO: Currently there's no support for DATE in sqllite

    if len(feildslLeft) > 0:
        raise Exception("Failed to find all the columns data types - Maybe some are empty?")

    return fieldTypes


def escapingGenerator(f):
    for line in f:
        yield line.decode("utf-8").strip()


def csvToDb(csvFile, outputToFile = False):

    with open(csvFile, mode='r') as fin:
        dt = _get_col_datatypes(fin)

        fin.seek(0)

        reader = csv.DictReader(fin)

        # Keep the order of the columns name just as in the CSV
        fields = reader.fieldnames
        cols = []

        # Set field and type
        for f in fields:
            cols.append("%s %s" % (f, dt[f]))

        con = sqlite3.connect("%s" % db_name)
        cur = con.cursor()

        # Generate create table statement:
        fields = ",".join(cols)
        fields = fields + ", PRIMARY KEY (%s)" % cols[1].strip(" INTEGER")
        stmt = "CREATE TABLE %s (%s)" % (table_name, fields)
        print stmt

        cur.execute(stmt)

        fin.seek(0)

        reader = csv.reader(escapingGenerator(fin))

        #reader = csv.reader(fin)
        # Generate insert statement:
        stmt = "INSERT INTO %s VALUES(%s);" % (table_name, ','.join('?' * len(cols)))
        try:
            cur.executemany(stmt, reader)
        except Exception as e:
            print
        con.commit()

    return con

if __name__ == "__main__":
    csv_file = "./all_india_pin_code.csv"
    table_name = "postalinfo"
    db_name = "./inventory.db"
    csvToDb(csv_file)
