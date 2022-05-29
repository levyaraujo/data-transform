import tabula
import os
import pandas as pd
from zipfile import ZipFile


def reading_pdf():  # função que irá extrair as tabelas do pdf e exportar como .csv
    target = os.path.join(os.getcwd(), "Test_levy.zip")
    destination = os.path.join(os.getcwd(), "table.csv")
    check = os.path.exists(target)

    # checa se o arquivo já existe, se sim ele irá pular para a proxima função
    if check:
        return True

    with open("Anexo_I.pdf", "rb") as pdf:
        print("\nExtraindo tabelas. Aguarde...")
        tabula.convert_into(pdf, destination, output_format="csv", pages="all")
        print("Arquivo processado com sucesso!")


# função que irá tratar e remover possíveis erros do arquivo csv
def manipulate_csv():
    output_csv = "Test_levy.csv"
    zipped = "Test_levy.zip"
    check = os.path.exists(os.path.join(os.getcwd(), zipped))

    if check:
        print(f"O arquivo {zipped} já existe no diretório atual.")
        return True

    df = pd.read_csv(
        "table.csv",
        encoding="latin1",
        on_bad_lines="skip",
    )

    df.drop_duplicates(inplace=True, keep=False)  # removendo linhas duplicadas

    # substituindo as siglas pelos seus significados
    df["AMB"] = df["AMB"].map({"AMB": "Seg. Ambulatorial"})
    df["OD"] = df["OD"].map({"OD": "Seg. Odontológica"})

    print("\nCompactando CSV...")
    df.to_csv(output_csv, index=False, encoding="latin1")

    with ZipFile("Test_levy.zip", "w") as f:
        f.write(output_csv)
        f.close()

    os.remove("table.csv")
    os.remove("Test_levy.csv")

    print("Arquivo compactado com sucesso!\n")
    result = os.path.join(os.getcwd(), "Test_levy.zip")


reading_pdf()
manipulate_csv()
