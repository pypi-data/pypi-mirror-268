# hobby
Desenvolvimento fácil e rápido de jogos 2D simples.

# Instalação
pip install hobby

# Recursos
O Hobby provê objetos e classes de altíssimo nível projetados para o desenvolvimento fácil e rápido de jogos 2D simples. É baseado em Pygame, porém muito mais pythônico e fácil de entender e usar.

Aqui estão todos os recursos disponíveis descritos brevemente:

- hobby.ticker: objeto representando o relógio interno.
- hobby.window: objeto representando a janela.
- hobby.screen: objeto representando a tela.
- hobby.camera: objeto representando a câmera.
- hobby.keyboard: objeto representando o teclado.
- hobby.mouse: objeto representando o mouse.
- hobby.joysticks: tupla de objetos representando joysticks.
- hobby.Sound: classe de objetos para representar sons.
- hobby.Image: classe de objetos para representar imagens.
- hobby.Animation: classe de objetos para representar animações.
- hobby.TileMap: classe de objetos para representar mapas de ladrilhos.
- hobby.Error: classe de erros específicos do Hobby.

# História (por José Falero)
Um dia eu fui desenvolver um jogo em Python e comecei a pesquisar por bibliotecas que pudessem me ajudar. Logo descobri a biblioteca Pygame e, levando em consideração as minhas necessidades, fiquei muito satisfeito. Só não fiquei ainda mais satisfeito porque senti um certo descompasso entre a usabilidade do Pygame e a expressividade do Python.

Python é uma linguagem de altíssimo nível, e não falta quem diga, num misto de brincadeira e elogio, que o código Python é quase como se fosse uma espécie de pseudo-código executável. A biblioteca Pygame, por outro lado, às vezes é bastante burocrática, em parte pelo evidente esforço de ser geral, de servir para tudo, o que de fato exige que ela seja tão crua quanto possível. Mas não é só isso. A verdade é que Pygame me cheira a C. O seu criador, Pete Shinners, a quem devemos muito, infelizmente estava mais familiarizado com a programação em C do que com a programação em Python quando deu à luz a nossa tão amada biblioteca.

Enquanto eu programava o meu jogo, era possível sentir a diferença de produtividade entre os trechos de código que interagiam com o Pygame e os que não interagiam. De certo modo, era como se o Pygame contrabalançasse a expressividade do Python. Então, passado algum tempo, me dei conta de que eu tinha escrito muito código para abstrair as funcionalidades do Pygame, a fim não só de programar o meu jogo de modo mais pythônico, mas também de reusar as abstrações em outros projetos, no futuro.

E aqui está: essas abstrações são o que compõe o módulo Hobby.
