#Conecta ao banco oracle SIE

import cx_Oracle
import time
import pandas as pd

con = cx_Oracle.connect('iam/c0nsulta@ORCL_SIE')

cur = con.cursor()
cur.prepare('select * from sie.rf_cpf where num_cpf = :id')
cur.execute(None,{'id':'03169726145'})
res = cur.fetchmany(numRows=1)

print(res)

cur.close()
con.close()