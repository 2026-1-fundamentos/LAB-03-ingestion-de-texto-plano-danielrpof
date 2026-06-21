"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    rowz = []
    fh = open("files/input/clusters_report.txt", encoding="utf-8")
    lns = fh.readlines()
    fh.close()

    datapart = lns[4:]
    clust_n = None
    cnt_kw  = None
    pct_kw  = None
    kw_txt = ""

    for ln in datapart:
        ln = ln.rstrip('\n')
        if not ln.strip():
            if clust_n is not None:
                cln = re.sub(r'\s+', ' ', kw_txt).strip().rstrip('.')
                pz = [p.strip() for p in cln.split(',') if p.strip()]
                rowz.append({
                    'cluster': clust_n,
                    'cantidad_de_palabras_clave': cnt_kw,
                    'porcentaje_de_palabras_clave': pct_kw,
                    'principales_palabras_clave': ', '.join(pz)
                })
                clust_n = None
                kw_txt = ""
            continue

        hd = ln[:9].strip()
        if hd.isdigit():
            clust_n = int(hd)
            cnt_kw  = int(ln[9:25].strip())
            praw = ln[25:41].strip().replace(' %', '').replace(',', '.')
            pct_kw = float(praw)
            kw_txt = ln[41:] if len(ln) > 41 else ""
        elif clust_n is not None:
            kw_txt += " " + (ln[41:] if len(ln) > 41 else "")

    if clust_n is not None:
        cln = re.sub(r'\s+', ' ', kw_txt).strip().rstrip('.')
        pz = [p.strip() for p in cln.split(',') if p.strip()]
        rowz.append({
            'cluster': clust_n,
            'cantidad_de_palabras_clave': cnt_kw,
            'porcentaje_de_palabras_clave': pct_kw,
            'principales_palabras_clave': ', '.join(pz)
        })

    return pd.DataFrame(rowz)
