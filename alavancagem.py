
def alavancagem_banca(banca_inicial, odd=2.0):
    aposta_atual = banca_inicial * 0.10
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

        # Próxima aposta: valor anterior + 3% da banca original
        aposta_atual += banca_inicial * 0.03

    return resultados
