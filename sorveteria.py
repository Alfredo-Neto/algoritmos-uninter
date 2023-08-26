class Sorveteria:

    def tabulate(self, data, headers):
    # Encontrar a largura ideal para cada coluna
        column_widths = [
            max(len(str(item)) 
                for item in col) 
                  for col in zip(headers, *data)
        ]

        # Imprimir a linha superior
        line = "+"
        for width in column_widths:
            line += "-" * (width + 2) + "+"
        print(line)

        # Imprimir cabeçalhos
        header_line = "| "
        for word, width in zip(headers, column_widths):
            header_line += word.ljust(width) + " | "
        print(header_line)
        print(line)

        # Imprimir os dados da tabela
        for row in data:
            data_line = "| "
            for word, width in zip(row, column_widths):
                data_line += word.ljust(width) + " | "
            print(data_line)
            print(line)

data = [
    ["1", "R$ 6,00", "R$ 7,00", "R$ 8,00"],
    ["2", "R$ 10,00", "R$ 12,00", "R$ 14,00"],
    ["3", "R$ 14,00","R$ 17,00", "R$ 20,00"]
]

headers = [
           "No DE BOLAS", 
           "Sabor Tradicional (tr)", 
           "Sabor Premium (pr)", 
           "Sabor Especial (es)"
          ]

sorveteria = Sorveteria()
sorveteria.tabulate(data, headers)
