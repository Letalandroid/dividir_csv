import pandas as pd

archivo_original = "datos.csv"

try:
    # Intentar detectar el separador automáticamente y saltar errores
    df = pd.read_csv(
        archivo_original,
        encoding="latin1",
        sep=None,           # autodetecta el separador (coma, punto y coma, tab, etc.)
        engine="python",    # motor más flexible
        on_bad_lines="skip" # ignora filas con columnas de más/menos
    )

    print(f"✅ Archivo leído correctamente con {len(df)} filas y {len(df.columns)} columnas")

    # Dividir exactamente en 23455, 23455, 23454
    parte1 = 23455
    parte2 = 23455

    df1 = df.iloc[:parte1]
    df2 = df.iloc[parte1:parte1+parte2]
    df3 = df.iloc[parte1+parte2:]

    # Guardar en 3 archivos CSV
    df1.to_csv("parte1.csv", index=False, encoding="latin1")
    df2.to_csv("parte2.csv", index=False, encoding="latin1")
    df3.to_csv("parte3.csv", index=False, encoding="latin1")

    print(f"✅ Dividido en: {len(df1)} / {len(df2)} / {len(df3)} registros")

except Exception as e:
    print(f"❌ Error: {e}")
