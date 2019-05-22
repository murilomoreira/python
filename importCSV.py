import psycopg2
conn = psycopg2.connect("host=127.0.0.1 dbname=big_geo user=postgres password=postgres")
try:
    cur = conn.cursor()
    with open('C:\BRANCOS_BR.csv', 'r') as f:
        next(f) #pula a linha do cabeçalho
        cur.copy_from(f, 'latlon', sep=';')

    conn.commit()
    print("#sucesso!")
except:
    print("erro")