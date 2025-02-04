import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="H1-DB",
    user="postgres",
    password="....",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# File paths
medalvextir_file = r"C:\Users\dagur\OneDrive\Documents\HaskoliReykjavikur\Hugbunadarverkfraedi_Bs\Viðskiptagreind\H1\Comparison-of-WageIndex-and-PolicyInterestRate\nidarstada.csv"
folskfjoldi_file = r"C:\Users\dagur\OneDrive\Documents\HaskoliReykjavikur\Hugbunadarverkfraedi_Bs\Viðskiptagreind\H1\Comparison-of-WageIndex-and-PolicyInterestRate\brottfarir_kef.csv"

# Load nidarstada.csv into Medalvextir
with open(medalvextir_file, "r", encoding="utf-8") as file:
    # next(file)  # Skip header row
    cur.copy_expert("COPY Medalvextir FROM STDIN WITH CSV HEADER DELIMITER ';'", file)

# Load brottfarir_kef.csv into Laun
with open(folskfjoldi_file, "r", encoding="utf-8") as file:
    next(file)  # Skip header row
    cur.copy_expert("COPY Brottfarir FROM STDIN WITH CSV HEADER DELIMITER ';'", file)

# Commit and close connection
conn.commit()
cur.close()
conn.close()

print("Data successfully loaded into PostgreSQL tables!")
