from collections import Counter


class ShowStatistics:

    def initial_logs(self, results):
        self.total_timeout(results)
        self.total_played(results)
        self.count_winner(results)

    @staticmethod
    def total_timeout(results):
        total_timeout = sum([1 for result in results if result["time_out"]])

        print(f"Quantas partidas terminam por tempo esgotado(timeout): {total_timeout}")

    @staticmethod
    def total_played(results):
        total_played = sum([result["played"] for result in results])

        print(f"Quantos turnos em média demora uma partida: {total_played / len(results):.1f}")

    @staticmethod
    def count_winner(results):
        count_winner = Counter()
        for result in results:
            strategy = str(result['strategy'])
            count_winner[strategy] += 1

        print(f"Qual o comportamento que mais venceu: \n \
            {count_winner.most_common(1)[0][0]} \n \
            venceu: {count_winner.most_common(1)[0][1]} \n \
        ")

        print("Qual a porcentagem de vitórias por comportamento dos jogadores")
        for strategy, winner in count_winner.most_common():
            print("  *  ", f"{strategy}: {(winner * 100) // len(results)}%")


show_statistics = ShowStatistics()
