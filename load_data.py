import psycopg2

conn = psycopg2.connect(
    dbname="H1-DB",
    user="postgres",
    password="Mori1234",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

medalvextir_file = r"C:\Users\dagur\OneDrive\Documents\HaskoliReykjavikur\Hugbunadarverkfraedi_Bs\Viðskiptagreind\H1\Comparison-of-WageIndex-and-PolicyInterestRate\vextir.csv"
folskfjoldi_file = r"C:\Users\dagur\OneDrive\Documents\HaskoliReykjavikur\Hugbunadarverkfraedi_Bs\Viðskiptagreind\H1\Comparison-of-WageIndex-and-PolicyInterestRate\brottfarir_kef.csv"

# Load nidarstada.csv into Medalvextir
with open(medalvextir_file, "r", encoding="utf-8") as file:
    next(file)  
    cursor.copy_expert("COPY Medalvextir FROM STDIN WITH CSV HEADER DELIMITER ';'", file)

# Load brottfarir_kef.csv into Laun
with open(folskfjoldi_file, "r", encoding="utf-8") as file:
    next(file) 
    cursor.copy_expert("COPY Brottfarir FROM STDIN WITH CSV HEADER DELIMITER ';'", file)

conn.commit()
cursor.close()
conn.close()
    
print("Successfully loaded Data into PostgreSQL tables!")



