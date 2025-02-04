import csv
import datetime
from collections import defaultdict

# Nafn á inntaksskrá og útgrunnskrá
INNTAK = "Meginvextir.csv"
UTSKRIFT = "nidarstada.csv"

# Búa til gagnagrind til að safna saman upplýsingum eftir mánuðum:
# monthly_data["YYYY-MM"] = list of (daglan, vidskipti, styrivextir)
monthly_data = defaultdict(list)

def parse_date(s):
    # Tekur streng í sniði "dd.mm.yyyy" og skilar datetime.date
    day, month, year = s.split(".")
    return datetime.date(int(year), int(month), int(day))

def parse_float_icelandic(s):
    # Tekur streng í sniði "x,xx" og skilar float (t.d. "6,25" -> 6.25), ef tómt -> None
    s = s.strip()
    if s == '':
        return None
    return float(s.replace(',', '.'))

# Opnum CSV skrána og lesum hana
with open(INNTAK, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

reader = csv.reader(lines, delimiter=';')

# Fyrsta lína er haus (t.d. "Dagsetning";"Vextir á daglánum";...)
header = next(reader)

# Finna dálka með heitum (ef við viljum vera nákvæm, en hér getum við notað fastar breytur)
idx_dagsetn = 0  # "Dagsetning"
idx_daglan = 1   # "Vextir á daglánum"
idx_vidskipti = 2  # "Vextir á viðskiptareikningum"
idx_styrir = 3   # "Meginvextir SÍ (stýrivextir)"

for row in reader:
    # Stöðvum ef lína er tóm
    if not row or len(row) < 1:
        continue
    
    dag_str = row[idx_dagsetn].strip('"')
    if not dag_str:
        continue  # ef dagsetning er tóm, sleppum

    # Breytum dagsetningu í datetime og finnum mánaðaauðkenni "YYYY-MM"
    dt = parse_date(dag_str)
    year_month = f"{dt.year:04d}-{dt.month:02d}"

    # Lesum tölurnar úr dálkunum (gæti verið tómt -> None)
    daglan_str = row[idx_daglan].strip('"') if len(row) > idx_daglan else ""
    v_reikn_str = row[idx_vidskipti].strip('"') if len(row) > idx_vidskipti else ""
    styrir_str  = row[idx_styrir].strip('"') if len(row) > idx_styrir else ""

    daglan_val = parse_float_icelandic(daglan_str)
    v_reikn_val = parse_float_icelandic(v_reikn_str)
    styrir_val  = parse_float_icelandic(styrir_str)

    monthly_data[year_month].append((daglan_val, v_reikn_val, styrir_val))

# Hjálparfall til að taka meðaltal (hendum None-gildum)
def average(values):
    cleaned = [v for v in values if v is not None]
    if not cleaned:
        return None
    return sum(cleaned) / len(cleaned)

# Reiknum meðaltöl
monthly_avg = {}  # { "YYYY-MM": (mean_daglan, mean_vidsk, mean_styrir) }

for ym, measurements in monthly_data.items():
    daglan_list = [m[0] for m in measurements]
    vidskipti_list = [m[1] for m in measurements]
    styrir_list = [m[2] for m in measurements]

    avg_daglan = average(daglan_list)
    avg_vidskipti = average(vidskipti_list)
    avg_styrir = average(styrir_list)

    monthly_avg[ym] = (avg_daglan, avg_vidskipti, avg_styrir)


# Raða eftir year_month í vaxandi röð
sorted_months = sorted(monthly_avg.keys())

# Skrifum út í "nidarstada.csv"
with open(UTSKRIFT, "w", encoding="utf-8", newline="") as f:
    out = csv.writer(f, delimiter=';')
    out.writerow(["Manudur","Medal daglan","Medal vidskipti","Medal styrivextir"])
    for ym in sorted_months:
        avg_daglan, avg_vidskipti, avg_styrir = monthly_avg[ym]
        # Setjum 2 aukastafi, eða "" ef None
        daglan_str = f"{avg_daglan:.2f}" if avg_daglan is not None else ""
        vidskipti_str = f"{avg_vidskipti:.2f}" if avg_vidskipti is not None else ""
        styrir_str = f"{avg_styrir:.2f}" if avg_styrir is not None else ""
        out.writerow([ym, daglan_str, vidskipti_str, styrir_str])

print(f"Tókst! Skráin '{UTSKRIFT}' inniheldur mánaðarlegt yfirlit úr '{INNTAK}'.")
