from prefect import Flow, Parameter

from tasks import (
    getTimestamp,
    getCaminhoSaida,
    getData,
    escreveResultado,
    transformaCelulares,
    gravaEstatisticas,
    plotaIdades
)

with Flow("Users report") as flow:

    timestampArquivo = getTimestamp()
    myCaminho = getCaminhoSaida()

    numero_usuarios = Parameter("numero_usuarios", default=10)
    dataframeOriginal = getData(numero_usuarios)

    #formata os numeros de celular e de telefone fixo
    DataframeTratada = transformaCelulares(dataframeOriginal,'cell')
    DataframeTratada = transformaCelulares(dataframeOriginal,'phone')

    #Grava em arquivo CSV
    escreveResultado(DataframeTratada, timestampArquivo)
    plotaIdades(DataframeTratada,timestampArquivo)

    #Imprime os calculos de porcentagem
    print(gravaEstatisticas(DataframeTratada, timestampArquivo))
 