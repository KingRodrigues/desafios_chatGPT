#Cores no Terminal
#Códigos de escape sequence ANSI para configurar cores para os seus programas em Pytho
# \033["codigos"m || Nenhum códigos, um código, dois códigos ou três códigos
#[style];0[text];[back] | Comportamento [Normal, negrito, etc], Texto [cor do texto] e Background [cor do fundo].
#ex: \033[0;33/44m
from tkinter import mainloop

#style que são melhores para Python: 0 [sem estilo / none], 1 [Negrito / bold], 4 [Sublinhar / Underline] e 7 [Inverter / Negative]
#text: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 margenta, 36 ciano, 37 cinza. Pra mais é com biblioteca
#back: 40 ao 47

\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[0;30;42m
\033[m
\033[7;30;m

