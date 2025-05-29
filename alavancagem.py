
def alavancagem_banca(banca_inicial, odd=2.0):
    porcentagem_aposta = banca_inicial * 0.10
    aposta_atual = porcentagem_aposta
    resultados = []
    lucro_total = 0

    for rodada in range(1, 11):
        ganho = aposta_atual * (odd - 1)
        lucro_total += ganho
        resultados.append({
            'rodada': rodada,
            'apostado': aposta_atual,
            'ganho': ganho,
            'lucro acumulado': lucro_total
        })

        # Próxima aposta: 10% da banca inicial + lucro acumulado
        aposta_atual = porcentagem_aposta + lucro_total

    return resultados
