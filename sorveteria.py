class Sorveteria:

    def tabulate(self, data, headers):
        # Encontrar a largura ideal para cada coluna
        column_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]

        # Imprimir a linha superior
        print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")

        # Imprimir cabeçalhos
        print("| " + " | ".join(word.ljust(width) for word, width in zip(headers, column_widths)) + " |")
        print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")

        # Imprimir os dados da tabela
        for row in data:
            print("| " + " | ".join(word.ljust(width) for word, width in zip(row, column_widths)) + " |")
            print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")



data = [
    ["row1 column1", "row1 column2"],
    ["row2 column1", "row2 column2"]
]

headers = ["Heading1", "Heading2"]

sorveteria = Sorveteria()
sorveteria.tabulate(data, headers)
