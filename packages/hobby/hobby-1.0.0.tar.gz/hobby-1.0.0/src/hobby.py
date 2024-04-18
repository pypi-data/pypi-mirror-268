#
#    Copyright 2024 José Falero <jzfalero@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Desenvolvimento fácil e rápido de jogos 2D simples.

Este módulo provê objetos e classes de altíssimo nível projetados para o
desenvolvimento fácil e rápido de jogos 2D simples. É baseado em Pygame, porém
muito mais pythônico e fácil de entender e usar.

Aqui estão todos os recursos disponíveis descritos brevemente:

hobby.ticker ---- objeto representando o relógio interno.
hobby.window ---- objeto representando a janela.
hobby.screen ---- objeto representando a tela.
hobby.camera ---- objeto representando a câmera.
hobby.keyboard -- objeto representando o teclado.
hobby.mouse ----- objeto representando o mouse.
hobby.joysticks - tupla de objetos representando joysticks.
hobby.Sound ----- classe de objetos para representar sons.
hobby.Image ----- classe de objetos para representar imagens.
hobby.Animation - classe de objetos para representar animações.
hobby.TileMap --- classe de objetos para representar mapas de ladrilhos.
hobby.Error ----- classe de erros específicos do Hobby.

Consute as docstrings dos objetos e das classes para mais detalhes.
"""

__version__ = '1.0.0'
__author__ = 'José Falero <jzfalero@gmail.com>'

__all__ = ('ticker', 'window', 'screen', 'camera', 'keyboard', 'mouse',
           'joysticks', 'Sound', 'Image', 'Animation', 'TileMap', 'Error')

#===============================================================================
import os
import sys
import types
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'
os.environ['SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS'] = '1'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
os.environ['PYGAME_BLEND_ALPHA_SDL2'] = '1'
os.environ['PYGAME_FREETYPE'] = '1'

import pygame



#===============================================================================
if ((pygame.version.vernum[0] < 2) or
    (pygame.version.vernum[1] < 5) or
    (pygame.version.vernum[2] < 2)):

    raise RuntimeError(f'a versão do Pygame disponível é {pygame.version.ver}, '
                        'mas o Hobby exige a versão 2.5.2 ou superior')

pygame.display.init()
pygame.joystick.init()
pygame.font.init()
pygame.mixer.init(buffer = 1)

pygame.mixer.set_num_channels(0)
pygame.event.set_blocked(None)
pygame.event.set_allowed((pygame.QUIT, pygame.WINDOWRESIZED, pygame.MOUSEWHEEL))



#===============================================================================
def _assert_str(name, candidate):
    """
    Propaga TypeError se "candidate" não for uma string.
    """

    if not isinstance(candidate, str):
        raise TypeError(f'"{name}" precisa ser uma string')



#===============================================================================
def _assert_str_none(name, candidate):
    """
    Propaga TypeError se "candidate" não for uma string ou None.
    """

    if (candidate is not None) and (not isinstance(candidate, str)):
        raise TypeError(f'"{name}" precisa ser uma string ou None')



#===============================================================================
def _assert_int(name, candidate):
    """
    Propaga TypeError se "candidate" não for um inteiro.
    """

    if not isinstance(candidate, int):
        raise TypeError(f'"{name}" precisa ser um inteiro')



#===============================================================================
def _assert_callable(name, candidate):
    """
    Propaga TypeError se "candidate" não for um objeto chamável.
    """

    if not callable(candidate):
        raise TypeError(f'"{name}" precisa ser um objeto chamável')



#===============================================================================
def _assert_callable_none(name, candidate):
    """
    Propaga TypeError se "candidate" não for um objeto chamável ou None.
    """

    if (candidate is not None) and (not callable(candidate)):
        raise TypeError(f'"{name}" precisa ser um objeto chamável ou None')



#===============================================================================
def _assert_float(name, candidate):
    """
    Propaga TypeError se "candidate" não for um float.
    """

    if not isinstance(candidate, float):
        raise TypeError(f'"{name}" precisa ser um float')



#===============================================================================
def _assert_float_bool(name, candidate):
    """
    Propaga TypeError se "candidate" não for um float ou um bool.
    """

    if not isinstance(candidate, (float, bool)):
        raise TypeError(f'"{name}" precisa ser True, False ou um float')



#===============================================================================
def _assert_tuple(name, candidate):
    """
    Propaga TypeError se "candidate" não for uma tupla.
    """

    if not isinstance(candidate, tuple):
        raise TypeError(f'"{name}" precisa ser uma tupla')



#===============================================================================
def _assert_bool(name, candidate):
    """
    Propaga TypeError se "candidate" não for True ou False.
    """

    if not isinstance(candidate, bool):
        raise TypeError(f'"{name}" precisa ser True ou False')



#===============================================================================
def _assert_image(name, candidate):
    """
    Propaga TypeError se "candidate" não for um objeto Image.
    """

    if not isinstance(candidate, Image):
        raise TypeError(f'"{name}" precisa ser um objeto Image')



#===============================================================================
def _assert_image_none(name, candidate):
    """
    Propaga TypeError se "candidate" não for um objeto Image ou None.
    """

    if (candidate is not None) and (not isinstance(candidate, Image)):
        raise TypeError(f'"{name}" precisa ser um objeto Image ou None')



#===============================================================================
def _assert_graphic(name, candidate):
    """
    Propaga TypeError se "candidate" não for um objeto _Graphic.
    """

    if not isinstance(candidate, _Graphic):
        raise TypeError(f'"{name}" precisa ser um objeto gráfico')



#===============================================================================
def _assert_graphic_none(name, candidate):
    """
    Propaga TypeError se "candidate" não for um objeto _Graphic ou None.
    """

    if (candidate is not None) and not isinstance(candidate, _Graphic):
        raise TypeError(f'"{name}" precisa ser um objeto gráfico ou None')



#===============================================================================
def _assert_positional(name, candidate):
    """
    Propaga TypeError se "candidate" não for um objeto _Positional.
    """

    if not isinstance(candidate, _Positional):
        raise TypeError(f'"{name}" precisa ser um objeto posicional')



#===============================================================================
def _assert_gr_0(name, candidate):
    """
    Propaga ValueError se "candidate" não for maior que 0.
    """

    if candidate <= 0:
        raise ValueError(f'"{name}" precisa ser maior que 0')



#===============================================================================
def _assert_gr_eq_0(name, candidate):
    """
    Propaga ValueError se "candidate" não for maior ou igual a 0.
    """

    if candidate < 0:
        raise ValueError(f'"{name}" precisa ser maior ou igual a 0')



#===============================================================================
def _assert_gr_eq_1(name, candidate):
    """
    Propaga ValueError se "candidate" não for maior ou igual a 1.
    """

    if candidate < 1:
        raise ValueError(f'"{name}" precisa ser maior ou igual a 1')



#===============================================================================
def _assert_len_2(name, candidate):
    """
    Propaga ValueError se "candidate" tiver um número de itens diferente de 2.
    """

    if len(candidate) != 2:
        raise ValueError(f'"{name}" precisa ter 2 itens')



#===============================================================================
def _assert_len_4(name, candidate):
    """
    Propaga ValueError se "candidate" tiver um número de itens diferente de 4.
    """

    if len(candidate) != 4:
        raise ValueError(f'"{name}" precisa ter 4 itens')



#===============================================================================
def _assert_all_same_len(name, candidate):
    """
    Propaga ValueError se os itens de "candidate" tiverem comprimentos
    diferentes.
    """

    length = len(candidate[0])

    if any([len(item) != length for item in candidate[1:]]):
        raise ValueError(f'todos os itens de "{name}" precisam ter o mesmo '
                          'comprimento')



#===============================================================================
def _assert_ne_str(name, candidate):
    """
    Propaga ValueError se "candidate" for uma string vazia.
    """

    if not candidate:
        raise ValueError(f'"{name}" não pode ser uma string vazia')



#===============================================================================
def _assert_ne_tuple(name, candidate):
    """
    Propaga ValueError se "candidate" for uma tupla vazia.
    """

    if not candidate:
        raise ValueError(f'"{name}" não pode ser uma tupla vazia')



#===============================================================================
def _assert_ns_str(name, candidate):
    """
    Propaga ValueError se "candidate" for uma string de espaços em branco.
    """

    if candidate.isspace():
        raise ValueError(f'"{name}" não pode ser uma string de espaços em '
                          'branco')



#===============================================================================
def _assert_ns_str_none(name, candidate):
    """
    Propaga ValueError se "candidate" não for None e for uma string de espaços
    em branco.
    """

    if (candidate is not None) and candidate.isspace():
        raise ValueError(f'"{name}" não pode ser uma string de espaços em '
                          'branco')



#===============================================================================
def _assert_ne_str_none(name, candidate):
    """
    Propaga ValueError se "candidate" não for None e for uma string vazia.
    """

    if (candidate is not None) and (not candidate):
        raise ValueError(f'"{name}" não pode ser uma string vazia')



#===============================================================================
def _assert_vld_algn(candidate):
    """
    Propaga ValueError se "candidate" for um alinhamento inválido.
    """

    if candidate not in _TEXT_ALIGNMENTS:
        raise ValueError(f'"{candidate}" não é um alinhamento válido')



#===============================================================================
def _assert_vld_sym(device, candidate):
    """
    Propaga ValueError se "candidate" não for um símbolo válido para "device".
    """

    if candidate not in device._symbols:
        if device is keyboard:
            raise ValueError(f'"{candidate}" não é um símbolo válido para o '
                              'teclado')

        if device is mouse:
            raise ValueError(f'"{candidate}" não é um símbolo válido para o '
                              'mouse')

        raise ValueError(f'"{candidate}" não é um símbolo válido para o '
                         f'joystick "{device._name}"')



#===============================================================================
def _assert_vld_timer_id(candidate):
    """
    Propaga ValueError se "candidate" for um identificador de temporizador
    inválido.
    """

    if candidate not in ticker._timers:
        raise ValueError(f'nenhum temporizador com a identificação {candidate}')



#===============================================================================
def _assert_vld_anchor(candidate):
    """
    Propaga ValueError se "candidate" for uma âncora inválida.
    """

    if candidate not in _ANIMATION_ANCHORS:
        raise ValueError(f'"{candidate}" não é uma âncora válida')



#===============================================================================
def _assert_vld_blend(candidate):
    """
    Propaga ValueError se "candidate" for um método de mistura inválido.
    """

    if candidate not in _GRAPHIC_BLENDS:
        raise ValueError(f'"{candidate}" não é um método de mistura válido')



#===============================================================================
def _assert_le_anim_len(anim_len, candidate):
    """
    Propaga ValueError se "candidate" for um índice maior ou igual ao
    comprimento da animação.
    """

    if candidate >= anim_len:
        raise ValueError('índice fora da faixa de quadros da animação: '
                         f'{candidate}')



#===============================================================================
def _assert_le_graphics_len(graphics_len, candidate):
    """
    Propaga ValueError se "candidate" for um índice maior ou igual ao
    comprimento da tupla de gráficos.
    """

    if candidate >= graphics_len:
        raise ValueError('índice fora da faixa da tupla de objetos gráficos: '
                         f'{candidate}')



#===============================================================================
def _assert_exists(candidate):
    """
    Propaga FileNotFoundError se "candidate" for um caminho de arquivo ou
    diretório inexistente.
    """

    if not os.path.exists(candidate):
        raise FileNotFoundError(f'o arquivo ou diretório "{candidate}" não '
                                 'existe')



#===============================================================================
def _assert_exists_none(candidate):
    """
    Propaga FileNotFoundError se "candidate" não for None e for um caminho de
    arquivo ou diretório inexistente.
    """

    if (candidate is not None) and (not os.path.exists(candidate)):
        raise FileNotFoundError(f'o arquivo ou diretório "{candidate}" não '
                                 'existe')



#===============================================================================
def _assert_file(candidate):
    """
    Propaga IsADirectoryError se "candidate" for um caminho de diretório.
    """

    if os.path.isdir(candidate):
        raise IsADirectoryError(f'"{candidate}" é um diretório')



#===============================================================================
def _assert_file_none(candidate):
    """
    Propaga IsADirectoryError se "candidate" não for None e for um caminho de
    diretório.
    """

    if (candidate is not None) and os.path.isdir(candidate):
        raise IsADirectoryError(f'"{candidate}" é um diretório')



#===============================================================================
def _assert_dir(candidate):
    """
    Propaga NotADirectoryError se "candidate" não for um caminho de diretório.
    """

    if not os.path.isdir(candidate):
        raise NotADirectoryError(f'"{candidate}" não é um diretório')



#===============================================================================
def _load_surf(path):
    """
    Carrega um arquivo de imagem como um objeto Surface.
    """

    try:
        surface = pygame.image.load(path)

    except Exception as exc:
        raise Error(f'impossível carregar o arquivo "{path}"') from exc

    # Surfaces criadas diretamente na memória já têm o formato de pixel mais
    # rápido para blitting. O código abaixo tem o mesmo efeito de chamar o
    # método Surface.convert_alpha(), com a vantagem de não precisarmos esperar
    # a tela ser criada.
    size = surface.get_size()
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.blit(surface, (0, 0))

    return surf



#===============================================================================
def _load_surfs(path):
    """
    Carrega vários arquivos de imagem como objetos Surface.
    """

    names = os.listdir(path)
    if not names:
        raise Error(f'o diretório "{path}" está vazio')

    names.sort()

    surfs = []
    for name in names:
        full_path = os.path.join(path, name)

        surf = _load_surf(full_path)

        surfs.append(surf)

    return tuple(surfs)



#===============================================================================
def _make_surf(width, height):
    """
    Cria um novo objeto Surface preenchido com branco sólido (o padrão para
    novas imagens).
    """

    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    surf.fill((255, 255, 255, 255))

    return surf



#===============================================================================
def _render_text(text, font, size, alignment):
    """
    Cria um novo objeto Surface a partir de texto.
    """

    lines = text.split('\n')
    lines = [font.render(line, True, (255, 255, 255)) for line in lines]
    lines = [line.subsurface(line.get_bounding_rect()) for line in lines]

    linesize = font.get_linesize()
    height = len(lines) * linesize
    width = max([line.get_width() for line in lines])

    surf = pygame.Surface((width, height), pygame.SRCALPHA)
    kwargs = {'top': 0}

    if alignment == 'left':
        kwargs['left'] = 0

    elif alignment == 'center':
        kwargs['centerx'] = width // 2

    else:
        kwargs['right'] = width

    for line in lines:
        rect = line.get_rect(**kwargs)
        surf.blit(line, rect)
        kwargs['top'] += linesize

    surf = surf.subsurface(surf.get_bounding_rect())

    # Não podemos permitir Surfaces com largura == 0 ou altura == 0.
    if (not surf.get_width()) or (not surf.get_height()):
        surf = _make_surf(1, 1)

    return surf



#===============================================================================
def _load_font(path, size):
    """
    Carrega um arquivo de fonte.
    """

    key = (path, size)
    font = _FONTS.get(key, None)

    if font is None:

        try:
            font = pygame.font.Font(path, size)

        except Exception as exc:
            raise Error(f'impossível carregar o arquivo "{path}"') from exc

        _FONTS[key] = font

    return font



#===============================================================================
def _load_matrix(path):
    """
    Carrega um arquivo de matriz de inteiros.
    """

    try:

        with open(path, 'r') as file:
            lines = file.readlines()

        lines = [line.split(' ') for line in lines]

        matrix = []
        for line in lines:

            row = []
            for index in line:
                index = int(index)
                row.append(index)

            row = tuple(row)
            matrix.append(row)

        matrix = tuple(matrix)

        return matrix

    except Exception as exc:
        raise Error(f'impossível carregar o arquivo "{path}"') from exc



#===============================================================================
def _load_sound(path):
    """
    Carrega um arquivo de som.
    """

    try:
        sound = pygame.mixer.Sound(path)

    except Exception as exc:
        raise Error(f'impossível carregar o arquivo "{path}"') from exc

    if _SOUND_CHANNELS:
        channel = _SOUND_CHANNELS.pop()

    else:
        index = pygame.mixer.get_num_channels()
        pygame.mixer.set_num_channels(index + 1)
        channel = pygame.mixer.Channel(index)

    return (sound, channel)



#===============================================================================
def _round_float_0_1(value):
    """
    Arredonda um float para 0.0, se for menor que 0.0, ou para 1.0, se for maior
    que 1.0.
    """

    if value < 0.0:
        value = 0.0

    elif value > 1.0:
        value = 1.0

    return value



#===============================================================================
def _round_float_ep(value):
    """
    Arredonda um float para "sys.float_info.epsilon", se for menor que
    "sys.float_info.epsilon".
    """

    if value < sys.float_info.epsilon:
        value = sys.float_info.epsilon

    return value



#===============================================================================
def _make_sub_color(red, green, blue, alpha):
    """
    Cria e retorna uma cor de subtração adequada para os níveis de cor
    fornecidos.
    """

    red   = int(255 * (1.0 - red))
    green = int(255 * (1.0 - green))
    blue  = int(255 * (1.0 - blue))
    alpha = int(255 * (1.0 - alpha))

    color = pygame.Color(red, green, blue, alpha)

    return color



#===============================================================================
def _s2ms(seconds):
    """
    Converte segundos em milissegundos.
    """

    return int(seconds * 1000)



#===============================================================================
def _ms2s(ms):
    """
    Converte milissegundos em segundos.
    """

    return ms / 1000



#===============================================================================
def _normalize_angle(angle):
    """
    Normaliza um ângulo de rotação.
    """

    if (angle < 0.0) or (angle >= 360.0):
        angle %= 360.0

    return angle



#===============================================================================
class _Ticker(object):
    """
    Objeto representando o relógio interno.
    """

    __slots__ = ('_fps', '_resolution', '_clock', '_timers', '_time')



    def __init__(self):
        self._fps = 60.0
        self._resolution = 1.0 / self._fps
        self._timers = {}
        self._time = 0.0
        self._clock = pygame.time.Clock()



    def _update_timers(self):
        """
        Atualiza os temporizadores.
        """

        to_remove = []

        for (timer_id, timer) in self._timers.items():
            timer.time += self._resolution

            if timer.time >= timer.limit:
                timer.time = 0.0
                keep = timer.callback()

                if not keep:
                    to_remove.append(timer_id)

        for timer_id in to_remove:
            del self._timers[timer_id]



    @property
    def fps(self):
        """
        Float maior ou igual a 1.0 representando a taxa de quadros por segundo.
        """

        return self._fps



    @fps.setter
    def fps(self, fps):
        _assert_float('fps', fps)
        _assert_gr_eq_1('fps', fps)

        self._fps = fps
        self._resolution = 1.0 / self._fps



    def update(self):
        """
        update() -> float

        Atualiza o relógio interno.

        O retorno é um float representando a taxa de quadros por segundo que o
        jogo de fato está conseguindo renderizar.

        Note que este método deve ser chamado 1 vez a cada quadro do jogo.
        """

        self._time += self._resolution
        self._update_timers()

        keyboard._update()
        mouse._update()
        for joystick in joysticks:
            joystick._update()

        window._update()
        screen._update()
        camera._update()

        mouse._draw()

        if window._visible:
            pygame.display.flip()

        for animation in _ANIMATIONS_TO_UPDATE:
            animation._update()
        _ANIMATIONS_TO_UPDATE.clear()

        ms = self._clock.tick_busy_loop(self._fps)

        return 1.0 / _ms2s(ms)



    def time(self):
        """
        time() -> float

        Retorna um float maior ou igual a 0.0 representando o tempo decorrido
        desde a última chamada para este método em segundos.
        """

        time = self._time

        self._time = 0.0

        return time



    def add_timer(self, callback, seconds):
        """
        add_timer(callback, seconds) -> int

        Registra um objeto chamável para que seja chamado a intervalos
        regulares.

        O argumento "callback" é o objeto chamável a ser chamado. As chamadas
        são feitas sem argumentos. Note que o objeto chamável precisa sempre
        retornar um objeto com valor booleano verdadeiro se quiser continuar a
        ser chamado a intervalos regulares; do contrário, isto é, se o objeto
        chamável retornar um objeto com valor booleano falso (inclusive um None
        implícito, fique atento), isso será considerado um sinal para que o
        objeto chamável não seja mais chamado a partir de então.

        O argumento "seconds" é um float maior ou igual a 0.0 representando o
        intervalo entre as chamadas em segundos. Se for 0.0, o objeto chamável
        será chamado 1 vez a cada quadro do jogo.

        O retorno é um inteiro representando a identificação do temporizador.
        Guarde isso se quiser remover o temporizador manualmente em algum
        momento.
        """

        _assert_callable('callback', callback)

        _assert_float('seconds', seconds)
        _assert_gr_eq_0('seconds', seconds)

        timer = types.SimpleNamespace()
        timer_id = id(timer)

        timer.time = 0.0
        timer.limit = seconds
        timer.callback = callback

        self._timers[timer_id] = timer

        return timer_id



    def remove_timer(self, timer_id):
        """
        remove_timer(timer_id) -> None

        Remove um temporizador, isto é, faz com que um objeto chamável deixe de
        ser chamado a intervalos regulares.

        O argumento "timer_id" é um inteiro representando a identificação do
        temporizador a ser removido.
        """

        _assert_int('timer_id', timer_id)
        _assert_vld_timer_id(timer_id)

        del self._timers[timer_id]



    def iteration(self, seconds):
        """
        iteration(seconds) -> range

        Retorna um iterável cuja interação completa tem a mesma duração
        fornecida em segundos.

        O argumento "seconds" é um float maior que 0.0, representando a duração
        da iteração em segundos.
        """

        _assert_float('seconds', seconds)
        _assert_gr_0('seconds', seconds)

        return range(int(seconds * self._fps) or 1)



#===============================================================================
class _Input(object):
    """
    Classe de base dos dispositivos de entrada.
    """

    __slots__ = ()



    def _handle(self):
        """
        Chama o manipulador do dispositivo (se houver).
        """

        if self._handler is None:
            return

        keep = self._handler()

        if not keep:
            self._handler = None



    def _update_symbol(self, symbol):
        """
        Atualiza um símbolo do dispositivo.
        """

        before = self._before[symbol]
        now = self._now[symbol]

        if now and (not before):
            self._last = symbol
            self._busy[symbol] = True
            self._handle()

        elif now and before:
            self._held[symbol] = True
            self._time[symbol] += ticker._resolution

        elif (not now) and before:
            self._free[symbol] = True
            self._time[symbol] = 0.0
            self._handle()



    def _finish_update(self):
        """
        Termina a atualização do dispositivo, iniciada na subclasse.
        """

        self._busy = {symbol: False for symbol in self._symbols}
        self._free = {symbol: False for symbol in self._symbols}
        self._held = {symbol: False for symbol in self._symbols}
        self._last = None

        for symbol in self._symbols:
            self._update_symbol(symbol)



    @property
    def symbols(self):
        """
        Tupla de strings representando os símbolos deste dispositivo.
        """

        return self._symbols



    @property
    def last(self):
        """
        None ou uma string representando o símbolo deste dispositivo que se
        tornou ocpuado por último durante a renderização do último quadro.
        """

        return self._last



    @property
    def handler(self):
        """
        None ou objeto chamável a ser chamado sempre que um símbolo deste
        dispositivo se torna ocupado ou se torna livre. As chamadas são feitas
        sem argumentos. Note que, se você atribuir um objeto chamável a esta
        propriedade, o objeto chamável precisa sempre retornar um objeto com
        valor booleano verdadeiro se quiser ser chamado novamente quando o
        um símbolo deste dispositivo se tornar ocupado ou se tornar livre; do
        contrário, isto é, se o objeto chamável retornar um objeto com valor
        booleano falso (inclusive um None implícito, fique atento), isso será
        considerado um sinal para que o objeto chamável não seja mais chamado a
        partir de então.
        """

        return self._handler



    @handler.setter
    def handler(self, handler):

        _assert_callable_none('handler', handler)

        self._handler = handler



    def busy(self, symbol):
        """
        busy(symbol) -> bool

        Retorna True se o símbolo fornecido se tornou ocupado durante a
        renderização do último quadro. Caso contrário, retorna False.

        O argumento "symbol" é uma string não-vazia representando um símbolo
        deste dispositivo. Veja a propriedade "symbols" para conhecer todos os
        símbolos válidos.
        """

        _assert_str('symbol', symbol)
        _assert_ne_str('symbol', symbol)
        _assert_vld_sym(self, symbol)

        return self._busy[symbol]



    def free(self, symbol):
        """
        free(symbol) -> bool

        Retorna True se o símbolo fornecido se tornou livre durante a
        renderização do último quadro. Caso contrário, retorna False.

        O argumento "symbol" é uma string não-vazia representando um símbolo
        deste dispositivo. Veja a propriedade "symbols" para conhecer todos os
        símbolos válidos.
        """

        _assert_str('symbol', symbol)
        _assert_ne_str('symbol', symbol)
        _assert_vld_sym(self, symbol)

        return self._free[symbol]



    def held(self, symbol):
        """
        held(symbol) -> bool

        Retorna True se o símbolo fornecido é mantido ocupado, independentemente
        de quando tenha se tornado ocupado. Caso contrário, retorna False.

        O argumento "symbol" é uma string não-vazia representando um símbolo
        deste dispositivo. Veja a propriedade "symbols" para conhecer todos os
        símbolos válidos.
        """

        _assert_str('symbol', symbol)
        _assert_ne_str('symbol', symbol)
        _assert_vld_sym(self, symbol)

        return self._held[symbol]



    def time(self, symbol):
        """
        time(symbol) -> float

        Retorna um float maior ou igual a 0.0 indicando há quantos segundos o
        símbolo fornecido é mantido ocupado.

        O argumento "symbol" é uma string não-vazia representando um símbolo
        deste dispositivo. Veja a propriedade "symbols" para conhecer todos os
        símbolos válidos.
        """

        _assert_str('symbol', symbol)
        _assert_ne_str('symbol', symbol)
        _assert_vld_sym(self, symbol)

        return self._time[symbol]



#===============================================================================
class _Keyboard(_Input):
    """
    Objeto representando o teclado.
    """

    __slots__ = ('_table', '_symbols', '_now', '_before', '_busy', '_free',
                 '_held', '_time', '_handler', '_last')



    def __init__(self):

        self._table = {}

        for attr in dir(pygame):

            if not attr.startswith('K_'):
                continue

            index = getattr(pygame, attr)
            symbol = attr[2:].lower().replace('_', '-')

            self._table[symbol] = index

        self._symbols = tuple(self._table.keys())

        self._now    = {symbol: False for symbol in self._symbols}
        self._before = {symbol: False for symbol in self._symbols}
        self._busy   = {symbol: False for symbol in self._symbols}
        self._free   = {symbol: False for symbol in self._symbols}
        self._held   = {symbol: False for symbol in self._symbols}
        self._time   = {symbol: 0.0   for symbol in self._symbols}

        self._handler = None
        self._last = None



    def _update(self):
        """
        Atualiza o teclado.
        """

        self._before = self._now
        self._now = {}

        pressed = pygame.key.get_pressed()
        for (symbol, index) in self._table.items():
            self._now[symbol] = pressed[index]

        self._finish_update()



#===============================================================================
class _Mouse(_Input):
    """
    Objeto representando o mouse.
    """

    __slots__ = ('_symbols', '_now', '_before', '_busy', '_free', '_held',
                 '_time', '_handler', '_last', '_position', '_rel_position',
                 '_visible', '_cursor')



    def __init__(self):

        self._symbols = ('button-left', 'button-middle', 'button-right',
                         'wheel-left', 'wheel-right', 'wheel-up', 'wheel-down',
                         'motion-left', 'motion-right', 'motion-up',
                         'motion-down')

        self._now    = {symbol: False for symbol in self._symbols}
        self._before = {symbol: False for symbol in self._symbols}
        self._busy   = {symbol: False for symbol in self._symbols}
        self._free   = {symbol: False for symbol in self._symbols}
        self._held   = {symbol: False for symbol in self._symbols}
        self._time   = {symbol: 0.0   for symbol in self._symbols}

        self._handler = None
        self._last = None
        
        self._position = pygame.mouse.get_pos()
        self._rel_position = ()
        self._update_rel_position()

        self._visible = True
        self._cursor = None



    def _draw(self):
        """
        Desenha o cursor do mouse na janela (se necessário).
        """

        if not self._visible:
            return

        if self._cursor is None:
            return

        window._surf.blit(self._cursor._surf, self._position)



    def _update_rel_position(self):
        """
        Atualiza a posição do cursor do mouse em relação à tela (quando a
        posição real é alterada pelo movimento do mouse).
        """

        (x, y) = self._position

        if screen._fitness:
            x -= window._fitness_rect.left
            x *= (screen._rect.width / (window._fitness_rect.width or 1))
            y -= window._fitness_rect.top
            y *= (screen._rect.height / (window._fitness_rect.height or 1))

        else:
            x *= (screen._rect.width / window._rect.width)
            y *= (screen._rect.height / window._rect.height)

        self._rel_position = (int(x), int(y))



    def _update_position(self):
        """
        Atualiza a posição real do cursor do mouse (quando a posição em relação
        à tela é alterada por atribuição).
        """

        (x, y) = self._rel_position

        if screen._fitness:
            x *= (window._fitness_rect.width / screen._rect.width)
            x += window._fitness_rect.left
            y *= (window._fitness_rect.height / screen._rect.height)
            y += window._fitness_rect.top

        else:
            x *= (window._rect.width / screen._rect.width)
            y *= (window._rect.height / screen._rect.height)

        self._position = (int(x), int(y))
        pygame.mouse.set_pos(self._position)



    def _update(self):
        """
        Atualiza o mouse.
        """

        self._before = self._now
        self._now = {}

        pressed = pygame.mouse.get_pressed()
        self._now['button-left'] = pressed[0]
        self._now['button-middle'] = pressed[1]
        self._now['button-right'] = pressed[2]

        wleft = False
        wright = False
        wup = False
        wdown = False

        for event in pygame.event.get(pygame.MOUSEWHEEL):
            wleft = event.x > 0
            wright = event.x < 0
            wup = event.y > 0
            wdown = event.y < 0

        self._now['wheel-left'] = wleft
        self._now['wheel-right'] = wright
        self._now['wheel-up'] = wup
        self._now['wheel-down'] = wdown

        (x1, y1) = self._position
        (x2, y2) = pygame.mouse.get_pos()

        self._now['motion-left'] = (x2 < x1)
        self._now['motion-right'] = (x2 > x1)
        self._now['motion-up'] = (y2 < y1)
        self._now['motion-down'] = (y2 > y1)

        self._position = (x2, y2)
        if (x1, y1) != (x2, y2):
            self._update_rel_position()

        self._finish_update()



    @property
    def position(self):
        """
        Tupla de 2 inteiros (x, y) representando a posição do cursor do mouse em
        relação à tela.
        """

        return self._rel_position



    @position.setter
    def position(self, position):

        _assert_tuple('position', position)
        _assert_len_2('position', position)
        _assert_int('position[0]', position[0])
        _assert_int('position[1]', position[1])

        self._rel_position = position
        self._update_position()



    @property
    def cursor(self):
        """
        None ou objeto Image representando o cursor do mouse. Se for None, o
        cursor do sistema será usado.
        """

        return self._cursor



    @cursor.setter
    def cursor(self, cursor):

        _assert_image_none('cursor', cursor)

        self._cursor = cursor

        if (cursor is None) and self._visible:
            pygame.mouse.set_visible(True)

        else:
            pygame.mouse.set_visible(False)



    @property
    def visible(self):
        """
        Bool indicando se o cursor do mouse é visível.
        """

        return self._visible



    @visible.setter
    def visible(self, visible):

        _assert_bool('visible', visible)

        self._visible = visible

        if (self._cursor is None) and visible:
            pygame.mouse.set_visible(True)

        else:
            pygame.mouse.set_visible(False)



#===============================================================================
class _Joystick(_Input):
    """
    Objeto representando um joystick.
    """

    __slots__ = ('_joy', '_num_buttons', '_num_axes', '_num_hats', '_symbols',
                 '_now', '_before', '_busy', '_free', '_held', '_time',
                 '_handler', '_last', '_name', '_rumble')



    def __init__(self, joy_id):
        self._joy = pygame.joystick.Joystick(joy_id)
        self._joy.init()

        self._num_buttons = self._joy.get_numbuttons()
        self._num_axes = self._joy.get_numaxes()
        self._num_hats = self._joy.get_numhats()

        symbols = []

        for button in range(self._num_buttons):
            symbols.append(f'button-{button}')

        for axis in range(self._num_axes):
            symbols.append(f'axis-{axis}-minus')
            symbols.append(f'axis-{axis}-plus')

        for hat in range(self._num_hats):
            symbols.append(f'hat-{hat}-left')
            symbols.append(f'hat-{hat}-right')
            symbols.append(f'hat-{hat}-up')
            symbols.append(f'hat-{hat}-down')

        self._symbols = tuple(symbols)

        self._now    = {symbol: False for symbol in self._symbols}
        self._before = {symbol: False for symbol in self._symbols}
        self._busy   = {symbol: False for symbol in self._symbols}
        self._free   = {symbol: False for symbol in self._symbols}
        self._held   = {symbol: False for symbol in self._symbols}
        self._time   = {symbol: 0.0   for symbol in self._symbols}

        self._handler = None
        self._last = None

        self._name = self._joy.get_name()
        self._rumble = 0.0



    def _update(self):
        """
        Atualiza o joystick.
        """

        self._before = self._now
        self._now = {}

        for button in range(self._num_buttons):
            self._now[f'button-{button}'] = self._joy.get_button(button)

        for axis in range(self._num_axes):
            value = self._joy.get_axis(axis)
            self._now[f'axis-{axis}-minus'] = (value < -0.5)
            self._now[f'axis-{axis}-plus']  = (value > 0.5)

        for hat in range(self._num_hats):
            (x, y) = self._joy.get_hat(hat)
            self._now[f'hat-{hat}-left']   = (x < 0)
            self._now[f'hat-{hat}-right'] = (x > 0)
            self._now[f'hat-{hat}-up']     = (y > 0)
            self._now[f'hat-{hat}-down']  = (y < 0)

        self._finish_update()

        if isinstance(self._rumble, float):
            self._rumble -= ticker._resolution

            if self._rumble <= 0.0:
                self._rumble = False
                self._joy.stop_rumble()



    @property
    def name(self):
        """
        String representando o nome do joystick.
        """

        return self._name



    @property
    def rumble(self):
        """
        Bool ou float maior que 0.0. Se for False, então o joystick não está
        vibrando; se for True, então o joystick está vibrando por tempo
        indeterminado; se for um float, então o joystick está vibrando e o valor
        representa quantos segundos faltam para que o joystick pare de vibrar.
        """

        return self._rumble



    @rumble.setter
    def rumble(self, rumble):

        _assert_float_bool('rumble', rumble)
        if isinstance(rumble, float):
            _assert_gr_0('rumble', rumble)

        self._rumble = rumble

        if not rumble:
            self._joy.stop_rumble()

        else:
            self._joy.rumble(1.0, 1.0, 0)



#===============================================================================
class _2D(object):
    """
    Classe de base dos objetos que têm 2 dimensões.
    """

    __slots__ = ()



    @property
    def width(self):
        """
        Inteiro maior que 0 representando a largura deste objeto em pixels.
        """

        return self._rect.width



    @property
    def height(self):
        """
        Inteiro maior que 0 representando a altura deste objeto em pixels.
        """

        return self._rect.height



    @property
    def size(self):
        """
        Tupla de 2 inteiros (w, h) maiores que 0 representando a largura e a
        altura deste objeto em pixels.
        """

        return self._rect.size



#===============================================================================
class _Resizable(_2D):
    """
    Classe de base dos objetos que podem ser redimensionados arbitrariamente.
    """

    __slots__ = ()



    def _size_changed(self):
        """
        Chamado automaticamente quando o tamanho do objeto muda. Não faz nada.
        As subclasses podem sobrescrever este método caso precisem realizar
        trabalho em resposta às mudanças de tamanho.
        """

        pass



    @_2D.width.setter
    def width(self, width):

        _assert_int('width', width)
        _assert_gr_0('width', width)

        self._rect.width = width
        self._size_changed()



    @_2D.height.setter
    def height(self, height):

        _assert_int('height', height)
        _assert_gr_0('height', height)

        self._rect.height = height
        self._size_changed()



    @_2D.size.setter
    def size(self, size):

        _assert_tuple('size', size)
        _assert_len_2('size', size)
        _assert_int('size[0]', size[0])
        _assert_gr_0('size[0]', size[0])
        _assert_int('size[1]', size[1])
        _assert_gr_0('size[1]', size[1])

        self._rect.size = size
        self._size_changed()



#===============================================================================
class _Rescalable(_2D):
    """
    Classe de base dos objetos que podem ser redimensionados por fatores.
    """

    __slots__ = ()



    def _scale_changed(self):
        """
        Chamado automaticamente quando os fatores de redimensionamento do objeto
        mudam. Não faz nada. As subclasses podem sobrescrever este método caso
        precisem realizar trabalho em resposta às mudanças de fator.
        """

        pass



    @property
    def scalex(self):
        """
        Float maior ou igual a "sys.float_info.epsilon" representando o quanto
        este objeto está redimensionado no eixo x em relção à sua largura
        original. Valores menores que "sys.float_info.epsilon" são arredondados
        para "sys.float_info.epsilon".
        """

        return self._scalex



    @scalex.setter
    def scalex(self, scalex):

        _assert_float('scalex', scalex)

        self._scalex = _round_float_ep(scalex)

        self._scale_changed()



    @property
    def scaley(self):
        """
        Float maior ou igual a "sys.float_info.epsilon" representando o quanto
        este objeto está redimensionado no eixo y em relção à sua altura
        original. Valores menores que "sys.float_info.epsilon" são arredondados
        para "sys.float_info.epsilon".
        """

        return self._scaley



    @scaley.setter
    def scaley(self, scaley):

        _assert_float('scaley', scaley)

        self._scaley = _round_float_ep(scaley)

        self._scale_changed()



    @property
    def scale(self):
        """
        Tupla de 2 floats (x, y) maiores ou iguais a "sys.float_info.epsilon"
        representando o quanto este objeto está redimensionado nos eixos x e y
        em relção à sua largura e à sua altura originais. Valores menores que
        "sys.float_info.epsilon" são arredondados para "sys.float_info.epsilon".
        """

        return (self._scalex, self._scaley)



    @scale.setter
    def scale(self, scale):

        _assert_tuple('scale', scale)
        _assert_len_2('scale', scale)
        _assert_float('scale[0]', scale[0])
        _assert_float('scale[1]', scale[1])

        self._scalex = _round_float_ep(scale[0])
        self._scaley = _round_float_ep(scale[1])

        self._scale_changed()



#===============================================================================
class _Positional(object):
    """
    Classe de base dos objetos que têm propriedades de posionamento.
    """

    __slots__ = ()



    @property
    def top(self):
        """
        Inteiro representando a coordenada y do lado superior deste objeto.
        """

        return self._rect.top



    @property
    def left(self):
        """
        Inteiro representando a coordenada x do lado esquerdo deste objeto.
        """

        return self._rect.left



    @property
    def bottom(self):
        """
        Inteiro representando a coordenada y do lado inferior deste objeto.
        """

        return self._rect.bottom



    @property
    def right(self):
        """
        Inteiro representando a coordenada x do lado direito deste objeto.
        """

        return self._rect.right



    @property
    def centerx(self):
        """
        Inteiro representando a coordenada x do centro deste objeto.
        """

        return self._rect.centerx



    @property
    def centery(self):
        """
        Inteiro representando a coordenada y do centro deste objeto.
        """

        return self._rect.centery



    @property
    def topleft(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do canto
        superior esquerdo deste objeto.
        """

        return self._rect.topleft



    @property
    def bottomleft(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do canto
        inferior esquerdo deste objeto.
        """

        return self._rect.bottomleft



    @property
    def topright(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do canto
        superior direito deste objeto.
        """

        return self._rect.topright



    @property
    def bottomright(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do canto
        inferior direito deste objeto.
        """

        return self._rect.bottomright



    @property
    def midtop(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do centro
        do lado superior deste objeto.
        """

        return self._rect.midtop



    @property
    def midleft(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do centro
        do lado esquerdo deste objeto.
        """

        return self._rect.midleft



    @property
    def midbottom(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do centro
        do lado inferior deste objeto.
        """

        return self._rect.midbottom



    @property
    def midright(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do centro
        do lado direito deste objeto.
        """

        return self._rect.midright



    @property
    def center(self):
        """
        Tupla de 2 inteiros (x, y) representando as coordenadas x e y do centro
        deste objeto.
        """

        return self._rect.center



    def contains_point(self, point):
        """
        contains_point(point) -> bool

        Retorna True se o ponto fornecido estiver dentro da área deste objeto.
        Caso contrário, retorna False.

        O argumento "point" é uma tupla de 2 inteiros (x, y) representando as
        coordenadas x e y de um ponto.
        """

        _assert_tuple('point', point)
        _assert_len_2('point', point)
        _assert_int('point[0]', point[0])
        _assert_int('point[1]', point[1])

        return self._rect.collidepoint(point)



    def contains(self, positional):
        """
        contains(positional) -> bool

        Retorna True se o objeto posicional fornecido estiver totalmente dentro
        da área deste objeto. Caso contrário, retorna False.

        O argumento "positional" é qualquer tipo de objeto posicional. São
        considerados posicionais os objetos Image, os objetos Animation, os
        objetos _Tile, os objetos TileMap, o objeto hobby.camera e o objeto
        hobby.screen.
        """

        _assert_positional('positional', positional)

        return self._rect.contains(positional._rect)



    def collides(self, positional):
        """
        collides(positional) -> bool

        Retorna True se pelo menos uma parte do objeto posicional fornecido
        estiver dentro da área deste objeto. Caso contrário, retorna False.

        O argumento "positional" é qualquer tipo de objeto posicional. São
        considerados posicionais os objetos Image, os objetos Animation, os
        objetos _Tile, os objetos TileMap, o objeto hobby.camera e o objeto
        hobby.screen.
        """

        _assert_positional('positional', positional)

        return self._rect.colliderect(positional._rect)



#===============================================================================
class _Mobile(_Positional):
    """
    Classe de base dos objetos que podem ser movidos.
    """

    __slots__ = ()




    def _position_changed(self):
        """
        Chamado automaticamente quando a posição do objeto muda. Não faz nada.
        As subclasses podem sobrescrever este método caso precisem realizar
        trabalho em resposta às mudanças de posição.
        """

        pass



    @_Positional.top.setter
    def top(self, top):

        _assert_int('top', top)

        self._rect.top = top
        self._position_changed()



    @_Positional.left.setter
    def left(self, left):

        _assert_int('left', left)

        self._rect.left = left
        self._position_changed()



    @_Positional.bottom.setter
    def bottom(self, bottom):

        _assert_int('bottom', bottom)

        self._rect.bottom = bottom
        self._position_changed()



    @_Positional.right.setter
    def right(self, right):

        _assert_int('right', right)

        self._rect.right = right
        self._position_changed()



    @_Positional.centerx.setter
    def centerx(self, centerx):

        _assert_int('centerx', centerx)

        self._rect.centerx = centerx
        self._position_changed()



    @_Positional.centery.setter
    def centery(self, centery):

        _assert_int('centery', centery)

        self._rect.centery = centery
        self._position_changed()



    @_Positional.topleft.setter
    def topleft(self, topleft):

        _assert_tuple('topleft', topleft)
        _assert_len_2('topleft', topleft)
        _assert_int('topleft[0]', topleft[0])
        _assert_int('topleft[1]', topleft[1])

        self._rect.topleft = topleft
        self._position_changed()



    @_Positional.bottomleft.setter
    def bottomleft(self, bottomleft):

        _assert_tuple('bottomleft', bottomleft)
        _assert_len_2('bottomleft', bottomleft)
        _assert_int('bottomleft[0]', bottomleft[0])
        _assert_int('bottomleft[1]', bottomleft[1])

        self._rect.bottomleft = bottomleft
        self._position_changed()



    @_Positional.topright.setter
    def topright(self, topright):

        _assert_tuple('topright', topright)
        _assert_len_2('topright', topright)
        _assert_int('topright[0]', topright[0])
        _assert_int('topright[1]', topright[1])

        self._rect.topright = topright
        self._position_changed()



    @_Positional.bottomright.setter
    def bottomright(self, bottomright):

        _assert_tuple('bottomright', bottomright)
        _assert_len_2('bottomright', bottomright)
        _assert_int('bottomright[0]', bottomright[0])
        _assert_int('bottomright[1]', bottomright[1])

        self._rect.bottomright = bottomright
        self._position_changed()



    @_Positional.midtop.setter
    def midtop(self, midtop):

        _assert_tuple('midtop', midtop)
        _assert_len_2('midtop', midtop)
        _assert_int('midtop[0]', midtop[0])
        _assert_int('midtop[1]', midtop[1])

        self._rect.midtop = midtop
        self._position_changed()



    @_Positional.midleft.setter
    def midleft(self, midleft):

        _assert_tuple('midleft', midleft)
        _assert_len_2('midleft', midleft)
        _assert_int('midleft[0]', midleft[0])
        _assert_int('midleft[1]', midleft[1])

        self._rect.midleft = midleft
        self._position_changed()



    @_Positional.midbottom.setter
    def midbottom(self, midbottom):

        _assert_tuple('midbottom', midbottom)
        _assert_len_2('midbottom', midbottom)
        _assert_int('midbottom[0]', midbottom[0])
        _assert_int('midbottom[1]', midbottom[1])

        self._rect.midbottom = midbottom
        self._position_changed()



    @_Positional.midright.setter
    def midright(self, midright):

        _assert_tuple('midright', midright)
        _assert_len_2('midright', midright)
        _assert_int('midright[0]', midright[0])
        _assert_int('midright[1]', midright[1])

        self._rect.midright = midright
        self._position_changed()



    @_Positional.center.setter
    def center(self, center):

        _assert_tuple('center', center)
        _assert_len_2('center', center)
        _assert_int('center[0]', center[0])
        _assert_int('center[1]', center[1])

        self._rect.center = center
        self._position_changed()



    def move(self, x, y):
        """
        move(x, y) -> None

        Move este objeto.

        O argumento "x" é um inteiro representando quantos pixels este objeto
        deve ser movido no eixo x.

        O argumento "y" é um inteiro representando quantos pixels este objeto
        deve ser movido no eixo y.
        """

        _assert_int('x', x)
        _assert_int('y', y)

        self._rect.move_ip(x, y)
        self._position_changed()



    def clamp(self, positional):
        """
        clamp(positional) -> tuple

        Move este objeto (se necessário) para que fique totalmente dentro da
        área do objeto posicional fornecido. Se este objeto for maior do que o
        objeto posicional fornecido, então será centralizado nele.

        O argumento "positional" é qualquer tipo de objeto posicional. São
        considerados posicionais os objetos Image, os objetos Animation, os
        objetos _Tile, os objetos TileMap, o objeto hobby.camera e o objeto
        hobby.screen.

        O retorno é uma tupla de 2 inteiros (x, y) representando quantos pixels
        este objeto foi movido nos eixos x e y.
        """

        _assert_positional('positional', positional)

        centerx = self._rect.centerx
        centery = self._rect.centery

        self._rect.clamp_ip(positional._rect)
        self._position_changed()

        x = self._rect.centerx - centerx
        y = self._rect.centery - centery

        return (x, y)



#===============================================================================
class _Transformable(object):
    """
    Classe de base dos objetos que podem ser transformados.
    """

    __slots__ = ()



    def _aspect_changed(self):
        """
        Chamado automaticamente quando o aspecto do objeto muda. Não faz nada.
        As subclasses podem sobrescrever este método caso precisem realizar
        trabalho em resposta às mudanças de aspecto.
        """

        pass



    @property
    def red(self):
        """
        Float entre 0.0 e 1.0 representando o nível de vermelho deste objeto.
        Valores menores que 0.0 são arredondados para 0.0 e valores maiores que
        1.0 são arredondados para 1.0.
        """

        return self._red



    @red.setter
    def red(self, red):

        _assert_float('red', red)

        self._red = _round_float_0_1(red)

        self._sub_color = _make_sub_color(
            self._red, self._green, self._blue, self._alpha)

        self._aspect_changed()



    @property
    def green(self):
        """
        Float entre 0.0 e 1.0 representando o nível de verde deste objeto.
        Valores menores que 0.0 são arredondados para 0.0 e valores maiores que
        1.0 são arredondados para 1.0.
        """

        return self._green



    @green.setter
    def green(self, green):

        _assert_float('green', green)

        self._green = _round_float_0_1(green)

        self._sub_color = _make_sub_color(
            self._red, self._green, self._blue, self._alpha)

        self._aspect_changed()



    @property
    def blue(self):
        """
        Float entre 0.0 e 1.0 representando o nível de azul deste objeto.
        Valores menores que 0.0 são arredondados para 0.0 e valores maiores que
        1.0 são arredondados para 1.0.
        """

        return self._blue



    @blue.setter
    def blue(self, blue):

        _assert_float('blue', blue)

        self._blue = _round_float_0_1(blue)

        self._sub_color = _make_sub_color(
            self._red, self._green, self._blue, self._alpha)

        self._aspect_changed()



    @property
    def alpha(self):
        """
        Float entre 0.0 e 1.0 representando o nível de opacidade deste objeto.
        Valores menores que 0.0 são arredondados para 0.0 e valores maiores que
        1.0 são arredondados para 1.0.
        """

        return self._alpha



    @alpha.setter
    def alpha(self, alpha):

        _assert_float('alpha', alpha)

        self._alpha = _round_float_0_1(alpha)

        self._sub_color = _make_sub_color(
            self._red, self._green, self._blue, self._alpha)

        self._aspect_changed()



    @property
    def rgba(self):
        """
        Tupla de 4 floats (r, g, b, a) entre 0.0 e 1.0 representando os níveis
        de vermelho, verde, azul e opacidade deste objeto. Valores menores que
        0.0 são arredondados para 0.0 e valores maiores que 1.0 são arredondados
        para 1.0.
        """

        return (self._red, self._green, self._blue, self._alpha)



    @rgba.setter
    def rgba(self, rgba):

        _assert_tuple('rgba', rgba)
        _assert_len_4('rgba', rgba)
        _assert_float('rgba[0]', rgba[0])
        _assert_float('rgba[1]', rgba[1])
        _assert_float('rgba[2]', rgba[2])
        _assert_float('rgba[3]', rgba[3])

        self._red = _round_float_0_1(rgba[0])
        self._green = _round_float_0_1(rgba[1])
        self._blue = _round_float_0_1(rgba[2])
        self._alpha = _round_float_0_1(rgba[3])

        self._sub_color = _make_sub_color(
            self._red, self._green, self._blue, self._alpha)

        self._aspect_changed()



    @property
    def flipx(self):
        """
        Bool indicando se este objeto está espelhado no eixo x.
        """

        return self._flipx



    @flipx.setter
    def flipx(self, flipx):

        _assert_bool('flipx', flipx)

        self._flipx = flipx
        self._aspect_changed()



    @property
    def flipy(self):
        """
        Bool indicando se este objeto está espelhado no eixo y.
        """

        return self._flipy



    @flipy.setter
    def flipy(self, flipy):

        _assert_bool('flipy', flipy)

        self._flipy = flipy
        self._aspect_changed()



    @property
    def flip(self):
        """
        Tupla de 2 bools (x, y) indicando se este objeto está espelhado nos
        eixos x e y.
        """

        return (self._flipx, self._flipy)



    @flip.setter
    def flip(self, flip):

        _assert_tuple('flip', flip)
        _assert_len_2('flip', flip)
        _assert_bool('flip[0]', flip[0])
        _assert_bool('flip[1]', flip[1])

        self._flipx = flip[0]
        self._flipy = flip[1]
        self._aspect_changed()



    @property
    def angle(self):
        """
        Float entre 0.0 e 360.0 representando o ângulo de rotação deste objeto.
        Valores fora da faixa são convertidos automaticamente em valores
        adequados dentro da faixa.
        """

        return self._angle



    @angle.setter
    def angle(self, angle):

        _assert_float('angle', angle)

        self._angle = _normalize_angle(angle)
        self._aspect_changed()



#===============================================================================
class _Graphic(object):
    """
    Classe de base dos objetos gráficos.
    """

    __slots__ = ()



    def _data_buffered(self):
        """
        Chamado automaticamente quando os dados do objeto são armazenados no
        buffer da tela para que o objeto seja desenhado. Não faz nada. As
        subclasses podem sobrescrever este método caso precisem realizar
        trabalho em resposta aos armazenamentos.
        """

        pass



    @property
    def blends(self):
        """
        Tupla de strings representando os métodos de mistura válidos.
        """

        return _GRAPHIC_BLENDS



    @property
    def osd(self):
        """
        Bool indicando se este objeto é on-screen display.
        """

        return self._osd



    @osd.setter
    def osd(self, osd):

        _assert_bool('osd', osd)

        self._osd = osd



    @property
    def blend(self):
        """
        String não-vazia representando o método de mistura deste objeto. Veja
        a propriedade "blends" para conhecer os métodos de mistura válidos.
        """

        return self._blend



    @blend.setter
    def blend(self, blend):

        _assert_str('blend', blend)
        _assert_ne_str('blend', blend)
        _assert_vld_blend(blend)

        self._blend = blend
        self._blend_flag = _GRAPHIC_BLENDS_TABLE[blend]



    @property
    def info(self):
        """
        Qualquer tipo de objeto representando informações. Esta propriedade é
        útil caso este objeto esteja associado a um ou mais ladrilhos em um mapa
        de ladrilhos. Você pode, por exemplo, atribuir um dicionário a esta
        propriedade, com informações a respeito dos ladrilhos a que este objeto
        está associado: se são ou não transponíveis, se reduzem a velocidade do
        personagem quando o personagem passa por eles, se causam danos etc. Esta
        propriedade é refletida na propriedade "info" de cada ladrilho a que
        este objeto está associado.
        """

        return self._info



    @info.setter
    def info(self, info):

        self._info = info



    def draw(self):
        """
        draw() -> None

        Desenha este objeto na tela.
        """

        data = (self._surf, self._rect.topleft, None, self._blend_flag)

        if self._osd:
            screen._to_draw_osd.append(data)

        else:
            screen._to_draw.append(data)

        self._data_buffered()



#===============================================================================
class _Window(_Resizable):
    """
    Objeto representando a janela.
    """

    __slots__ = ('_fullscreen_size', '_last_windowed_size', '_rect',
                 '_fitness_rect', '_surf', '_fitness_surf', '_visible',
                 '_resizable', '_fullscreen', '_closing', '_title', '_icon',
                 '_closer')

    def __init__(self):
        info = pygame.display.Info()

        self._fullscreen_size = (info.current_w, info.current_h)
        self._last_windowed_size = (info.current_w // 2, info.current_h // 2)

        self._rect = pygame.Rect(0, 0, *self._last_windowed_size)
        self._fitness_rect = self._rect.copy()

        self._surf = None
        self._fitness_surf = None

        self._visible = False
        self._resizable = False
        self._fullscreen = False
        self._closing = False

        self._title = None
        self._set_caption()

        self._icon = None
        self._set_icon()

        self._closer = None



    def _set_caption(self):
        """
        Chama "pygame.display.set_caption" com o argumento adequado.
        """

        if self._title is None:
            pygame.display.set_caption(_DEFAULT_TITLE)

        else:
            pygame.display.set_caption(self._title)



    def _set_icon(self):
        """
        Chama "pygame.display.set_icon" com o argumento adequado.
        """

        if self._icon is None:
            pygame.display.set_icon(_DEFAULT_ICON)

        else:
            pygame.display.set_icon(self._icon._surf)



    def _destroy(self):
        """
        Destrói a janela.
        """

        pygame.display.quit()
        pygame.display.init()

        self._set_caption()
        self._set_icon()

        if (mouse._cursor is None) and mouse._visible:
            pygame.mouse.set_visible(True)

        else:
            pygame.mouse.set_visible(False)

        self._surf = None
        self._fitness_surf = None



    def _create(self):
        """
        Cria a janela.
        """

        if self._surf is not None:
            self._destroy()

        if self._fullscreen:
            self._surf = pygame.display.set_mode(
                self._rect.size, pygame.FULLSCREEN)

        elif self._resizable:
             self._surf = pygame.display.set_mode(
                 self._rect.size, pygame.RESIZABLE)

        else:
             self._surf = pygame.display.set_mode(self._rect.size)

        # Às vezes o Pygame não consigue criar uma Surface de fato com o tamanho
        # solicitado. Precisamos garantir que self._rect.size corresponda ao
        # tamanho da Surface que o Pygame conseguiu criar.
        self._rect.size = self._surf.get_size()

        self._fitness_rect = screen._rect.fit(self._rect)
        self._fitness_surf = self._surf.subsurface(self._fitness_rect)



    def _update(self):
        """
        Atualiza a janela.
        """

        if not self._visible:
            return

        if pygame.event.get(pygame.WINDOWRESIZED):
            self._surf = pygame.display.get_surface()
            self._rect = self._surf.get_rect()
            self._fitness_rect = screen._rect.fit(self._rect)
            self._fitness_surf = self._surf.subsurface(self._fitness_rect)

        self._closing = False
        if pygame.event.get(pygame.QUIT):
            self._closing = True

            if self._closer is not None:
                keep = self._closer()

                if not keep:
                    self._closer = None

        self._surf.fill((0, 0, 0))



    def _size_changed(self):
        """
        Chamado automaticamente quando o tamanho da janela muda.
        """

        # Quando a janela está em modo tela-cheia, o seu tamanho é fixo e
        # equivale ao tamanho do monitor. Mas guardamos o tamanho do retângulo
        # para usar depois, quando a janela sair do modo tela-cheia.
        if self._fullscreen:
            self._last_windowed_size = self._rect.size
            self._rect.size = self._fullscreen_size

            return

        self._fitness_rect = screen._rect.fit(self._rect)

        if not self._visible:
            return

        self._create()



    @property
    def closing(self):
        """
        Bool indicando se o usuário tentou fechar a janela durante a
        renderização do último quadro.
        """

        return self._closing



    @property
    def visible(self):
        """
        Bool indicando se a janela é visível.
        """

        return self._visible



    @visible.setter
    def visible(self, visible):

        _assert_bool('visible', visible)

        if visible is self._visible:
            return

        self._visible = visible

        if not visible:
            self._destroy()

            return

        self._create()



    @property
    def resizable(self):
        """
        Bool indicando se a janela é redimensionável para o usuário.
        """

        return self._resizable

        

    @resizable.setter
    def resizable(self, resizable):

        _assert_bool('resizable', resizable)

        if resizable is self._resizable:
            return

        self._resizable = resizable

        if not self._visible:
            return

        if self._fullscreen:
            return

        self._create()



    @property
    def fullscreen(self):
        """
        Bool indicando se a janela está em modo tela-cheia.
        """

        return self._fullscreen



    @fullscreen.setter
    def fullscreen(self, fullscreen):

        _assert_bool('fullscreen', fullscreen)

        if fullscreen is self._fullscreen:
            return

        self._fullscreen = fullscreen

        if fullscreen:
            self._last_windowed_size = self._rect.size
            self._rect.size = self._fullscreen_size

        else:
            self._rect.size = self._last_windowed_size

        self._fitness_rect = screen._rect.fit(self._rect)

        if not self._visible:
            return

        self._create()



    @property
    def title(self):
        """
        None ou string com pelo menos 1 caractere visível representando o título
        da janela. Se for None, um título padrão será usado.
        """

        return self._title



    @title.setter
    def title(self, title):

        _assert_str_none('title', title)
        _assert_ne_str_none('title', title)
        _assert_ns_str_none('title', title)

        self._title = title
        self._set_caption()



    @property
    def icon(self):
        """
        None ou objeto Image representando o ícone da janela. Se for None, um
        ícone padrão será usado. Note que as transformações aplicadas em um
        objeto Image usado como ícone são refletidas no ícone real da janela. Se
        esse não é o comportamento desejado, crie uma cópia do objeto Image para
        usar exclusivamente como ícone.
        """

        return self._icon



    @icon.setter
    def icon(self, icon):

        _assert_image_none('icon', icon)

        if self._icon is not None:
            self._icon._is_icon = False

        if icon is not None:
            icon._is_icon = True

        self._icon = icon
        self._set_icon()



    @property
    def closer(self):
        """
        None ou objeto chamável a ser chamado sempre que o usuário tenta fechar
        a janela. As chamadas são feitas sem argumentos. Note que, se você
        atribuir um objeto chamável a esta propriedade, o objeto chamável
        precisa sempre retornar um objeto com valor booleano verdadeiro se
        quiser ser chamado novamente quando o usuário tornar a tentar fechar a
        janela; do contrário, isto é, se o objeto chamável retornar um objeto
        com valor booleano falso (inclusive um None implícito, fique atento),
        isso será considerado um sinal para que o objeto chamável não seja mais
        chamado a partir de então.
        """

        return self._closer



    @closer.setter
    def closer(self, closer):

        _assert_callable_none('closer', closer)

        self._closer = closer



#===============================================================================
class _Screen(_Resizable, _Positional):
    """
    Objeto representando a tela.
    """

    __slots__ = ('_rect', '_surf', '_fitness', '_to_draw', '_to_draw_osd')



    def __init__(self):
        self._rect = window._rect.copy()

        self._surf = pygame.Surface(self._rect.size, pygame.SRCALPHA)
        self._fitness = False

        self._to_draw = []
        self._to_draw_osd = []



    def _update(self):
        """
        Atualiza a tela.
        """

        self._surf.fill((0, 0, 0, 0))
        self._surf.blits(self._to_draw, False)
        self._to_draw.clear()

        if ((camera._red < 1.0) or
            (camera._green < 1.0) or
            (camera._blue < 1.0) or
            (camera._alpha < 1.0)):

            self._surf.fill(camera._sub_color, None, pygame.BLEND_RGBA_SUB)

        if camera._flipx or camera._flipy:

            self._surf = pygame.transform.flip(
                self._surf, camera._flipx, camera._flipy)

        if camera._zoom > 0.0:
            surf = self._surf.subsurface(camera._rect)
            pygame.transform.smoothscale(surf, self._rect.size, self._surf)

        if camera._angle != 0.0:

            surf = pygame.transform.rotozoom(
                self._surf, -camera._angle, 1.0)

            rect = surf.get_rect(center = self._rect.center)
            self._surf.fill((0, 0, 0, 0))
            self._surf.blit(surf, rect)

        if camera._rumble:
            left = int(0.01 * self._rect.width)
            left = random.randint(-left, left)
            top = int(0.01 * self._rect.height)
            top = random.randint(-top, top)
            surf = self._surf.copy()
            self._surf.blit(surf, (left, top))

        self._surf.blits(self._to_draw_osd, False)
        self._to_draw_osd.clear()

        if not window._visible:
            return

        if self._fitness:
            size = window._fitness_rect.size
            surface = window._fitness_surf
        else:
            size = window._rect.size
            surface = window._surf

        # O ideal seria redimensionar a Surface de origem direto na Surface de
        # destino, como feito acima no bloco "if camera._zoom > 0.0:", mas não
        # podemos fazer assim aqui, porque o alpha per pixel da Surface de
        # origem é ignorado no processo. Não está muito claro se isso é um BUG
        # do Pygame ou se é o comportamento esperado, já que, neste caso, a
        # Surface de destino é a Surface de exibição e não tem, ela mesma, alpha
        # per pixel.
        surf = pygame.transform.smoothscale(self._surf, size)
        surface.blit(surf, (0, 0))



    def _size_changed(self):
        """
        Chamado automaticamente quando o tamanho da tela muda.
        """

        self._surf = pygame.Surface(self._rect.size, pygame.SRCALPHA)
        window._fitness_rect = self._rect.fit(window._rect)
        camera._update_rect_size()



    @property
    def fitness(self):
        """
        Bool indicando se a tela preserva a relação de aspecto original ao
        renderizar os quadros.
        """

        return self._fitness



    @fitness.setter
    def fitness(self, fitness):

        _assert_bool('fitness', fitness)

        self._fitness = fitness



#===============================================================================
class _Camera(_2D, _Mobile, _Transformable):
    """
    Objeto representando a câmera.
    """

    __slots__ = ('_rect', '_zoom', '_red', '_green', '_blue', '_alpha',
                 '_sub_color', '_flipx', '_flipy', '_angle', '_rumble')



    def __init__(self):
        self._rect = screen._rect.copy()
        self._zoom = 0.0

        self._red = 1.0
        self._green = 1.0
        self._blue = 1.0
        self._alpha = 1.0
        self._sub_color = _make_sub_color(
            self._red, self._green, self._blue, self._alpha)

        self._flipx = False
        self._flipy = False

        self._angle = 0.0

        self._rumble = False



    def _update(self):
        """
        Atualiza a câmera.
        """

        if isinstance(self._rumble, float):
            self._rumble -= ticker._resolution

            if self._rumble <= 0.0:
                self._rumble = False



    def _update_rect_size(self):
        """
        Atualiza o tamanho do retângulo da câmera.
        """

        factor = 1.0 - self._zoom
        width = int(factor * screen._rect.width) or 1
        height = int(factor * screen._rect.height) or 1
        center = self._rect.center

        self._rect.width = width
        self._rect.height = height
        self._rect.center = center

        self._rect.clamp_ip(screen._rect)



    def _position_changed(self):
        """
        Chamado automaticamente quando a posição da câmera muda.
        """

        self._rect.clamp_ip(screen._rect)



    @property
    def zoom(self):
        """
        Float entre 0.0 e 1.0 representando o nível de zoom da câmera. Valores
        menores que 0.0 são arredondados para 0.0 e valores maiores que 1.0 são
        arredondados para 1.0.
        """

        return self._zoom



    @zoom.setter
    def zoom(self, zoom):

        _assert_float('zoom', zoom)

        self._zoom = _round_float_0_1(zoom)
        self._update_rect_size()



    @property
    def rumble(self):
        """
        Bool ou float maior que 0.0. Se for False, então a câmera não está
        vibrando; se for True, então o a câmera está vibrando por tempo
        indeterminado; se for um float, então a câmera está vibrando e o valor
        representa quantos segundos faltam para que a câmera pare de vibrar.
        """

        return self._rumble



    @rumble.setter
    def rumble(self, rumble):

        _assert_float_bool('rumble', rumble)
        if isinstance(rumble, float):
            _assert_gr_0('rumble', rumble)

        self._rumble = rumble



#===============================================================================
class Image(_Rescalable, _Mobile, _Transformable, _Graphic):
    """
    Image(path) -> Image

    Classe de objetos para representar imagens.

    O argumento "path" é uma string não-vazia representando o caminho do arquivo
    de imagem a ser carregado.
    """

    __slots__ = ('_original_surf', '_scalex', '_scaley', '_surf', '_rect',
                 '_osd', '_flipx', '_flipy', '_angle', '_red', '_green',
                 '_blue', '_alpha', '_sub_color', '_blend', '_blend_flag',
                 '_info', '_is_icon')



    def __init__(self, path):

        _assert_str('path', path)
        _assert_ne_str('path', path)
        _assert_exists(path)
        _assert_file(path)

        surf = _load_surf(path)

        self._init(surf)



    def _init(self, surf):
        """
        Inicializa a imagem.
        """

        self._original_surf = surf

        self._scalex = 1.0
        self._scaley = 1.0

        self._surf = surf
        self._rect = surf.get_rect()

        self._osd = False
        self._flipx = False
        self._flipy = False
        self._angle = 0.0

        self._red = 1.0
        self._green = 1.0
        self._blue  = 1.0
        self._alpha = 1.0
        self._sub_color = pygame.Color(0, 0, 0, 0)

        self._blend = 'normal'
        self._blend_flag = 0

        self._info = None
        self._is_icon = False



    def _transform(self):
        """
        Aplica todas as transformações necessárias na imagem.
        """

        surf = self._original_surf

        if ((self._red < 1.0) or (self._green < 1.0) or
            (self._blue < 1.0) or (self._alpha < 1.0)):

            surf = surf.copy()

            surf.fill(self._sub_color, None, pygame.BLEND_RGBA_SUB)

        if self._flipx or self._flipy:
            surf = pygame.transform.flip(surf, self._flipx, self._flipy)

        if (self._scalex != 1.0) or (self._scaley != 1.0):
            width = int(self._scalex * surf.get_width()) or 1
            height = int(self._scaley * surf.get_height()) or 1
            surf = pygame.transform.smoothscale(surf, (width, height))

        if self._angle > 0.0:
            surf = pygame.transform.rotozoom(surf, -self._angle, 1.0)

        self._surf = surf
        self._rect = surf.get_rect(center = self._rect.center)

        if self._is_icon:
            window._set_icon()



    def _scale_changed(self):
        """
        Chamado automaticamente quando os fatores de redimensionamento da imagem
        mudam.
        """

        self._transform()



    def _aspect_changed(self):
        """
        Chamado automaticamente quando o aspecto da imagem muda.
        """

        self._transform()



    def copy(self):
        """
        copy() -> Image

        Cria e retorna uma cópia da imagem.
        """

        image = object.__new__(self.__class__)

        image._original_surf = self._original_surf

        image._scalex = self._scalex
        image._scaley = self._scaley

        image._surf = self._surf
        image._rect = self._rect.copy()

        image._osd = self._osd
        image._flipx = self._flipx
        image._flipy = self._flipy
        image._angle = self._angle

        image._red = self._red
        image._green = self._green
        image._blue  = self._blue
        image._alpha = self._alpha
        image._sub_color = self._sub_color

        image._blend = self._blend
        image._blend_flag = self._blend_flag

        image._info = self._info
        image._is_icon = False

        return image



    @classmethod
    def from_screen(cls):
        """
        from_screen() -> Image

        Cria e retorna uma nova imagem a partir do último quadro renderizado.
        """

        surf = screen._surf.copy()
        image = object.__new__(cls)
        image._init(surf)

        return image



    @classmethod
    def from_size(cls, width, height):
        """
        from_size(width, height) -> Image

        Cria e retorna uma nova imagem com o tamanho fornecido.

        O argumento "width" é um inteiro maior que 0 representando a largura da
        imagem em pixels.

        O argumento "height" é um inteiro maior que 0 representando a altura da
        imagem em pixels.
        """

        _assert_int('width', width)
        _assert_gr_0('width', width)

        _assert_int('height', height)
        _assert_gr_0('height', height)

        surf = _make_surf(width, height)
        image = object.__new__(cls)
        image._init(surf)

        return image



    @classmethod
    def from_text(cls, text, font = None, size = 48, alignment = 'center'):
        """
        from_text(text, font = None, size = 48, alignment = "center") -> Image

        Cria e retorna uma imagem textual.

        O argumento "text" é uma string com pelo menos 1 caractere visível
        representando o texto a ser renderizado.

        O argumento "font" é None ou uma string não-vazia representando o
        caminho do arquivo de fonte a ser utilizado na renderização. Se for
        None, uma fonte padrão será utilizada.

        O argumento "size" é um inteiro maior que 0 representando o tamanho de
        fonte a ser utilizado na renderização.

        O argumento "alignment" é "left", "center" ou "right" indicando como a
        renderização deve alinhar o texto.
        """

        _assert_str('text', text)
        _assert_ne_str('text', text)
        _assert_ns_str('text', text)

        _assert_str_none('font', font)
        _assert_ne_str_none('font', font)
        _assert_exists_none(font)
        _assert_file_none(font)

        _assert_int('size', size)
        _assert_gr_0('size', size)

        _assert_str('alignment', alignment)
        _assert_ne_str('alignment', alignment)
        _assert_vld_algn(alignment)

        font = _load_font(font, size)
        surf = _render_text(text, font, size, alignment)

        image = object.__new__(cls)
        image._init(surf)

        return image



#===============================================================================
class Animation(_Rescalable, _Mobile, _Transformable, _Graphic):
    """
    Animation(path) -> Animation

    Classe de objetos para representar animações.

    O argumento "path" é uma string não-vazia representando o caminho do
    diretório contendo os arquivos de imagem a serem carregados.
    """

    __slots__ = ('_original_surfs', '_scalex', '_scaley', '_surfs', '_rects',
                 '_surf', '_rect', '_red', '_green', '_blue', '_alpha',
                 '_sub_color', '_flipx', '_flipy', '_angle', '_osd', '_blend',
                 '_blend_flag', '_redraw', '_redraw_count', '_length',
                 '_anchor', '_index', '_loop', '_playing', '_backward', '_info')



    def __init__(self, path):

        _assert_str('path', path)
        _assert_ne_str('path', path)
        _assert_exists(path)
        _assert_dir(path)

        surfs = _load_surfs(path)
        self._init(surfs)



    def _init(self, surfs):
        """
        Inicializa a animação.
        """

        self._original_surfs = surfs

        self._scalex = 1.0
        self._scaley = 1.0

        self._surfs = self._original_surfs
        self._rects = tuple([surf.get_rect() for surf in self._surfs])

        self._surf = self._surfs[0]
        self._rect = self._rects[0]

        self._red = 1.0
        self._green = 1.0
        self._blue = 1.0
        self._alpha = 1.0
        self._sub_color = pygame.Color(0, 0, 0, 0)

        self._flipx = False
        self._flipy = False

        self._angle = 0.0
        self._osd = False

        self._blend = 'normal'
        self._blend_flag = 0

        self._redraw = 1
        self._redraw_count = 0
        self._length = len(self._surfs)
        self._anchor = 'midbottom'
        self._index = 0
        self._loop = True
        self._playing = True
        self._backward = False

        self._info = None



    def _transform(self):
        """
        Aplica todas as transformações necessárias na animação.
        """

        surfs = self._original_surfs

        if ((self._red < 1.0) or (self._green < 1.0) or
            (self._blue < 1.0) or (self._alpha < 1.0)):

            surfs = [surf.copy() for surf in surfs]

            for surf in surfs:
                surf.fill(self._sub_color, None, pygame.BLEND_RGBA_SUB)

        if self._flipx or self._flipy:

            surfs = [pygame.transform.flip(surf, self._flipx, self._flipy)
                     for surf in surfs]

        if (self._scalex != 1.0) or (self._scaley != 1.0):

            surfaces = []
            for surf in surfs:
                width = int(self._scalex * surf.get_width()) or 1
                height = int(self._scaley * surf.get_height()) or 1
                surf = pygame.transform.smoothscale(surf, (width, height))
                surfaces.append(surf)

            surfs = surfaces

        if self._angle > 0.0:

            surfs = [pygame.transform.rotozoom(surf, -self._angle, 1.0)
                     for surf in surfs]

        self._surfs = tuple(surfs)
        self._surf = self._surfs[self._index]

        self._rects = tuple([surf.get_rect() for surf in self._surfs])

        center = self._rect.center
        self._rect = self._rects[self._index]
        self._rect.center = center



    def _update_index(self):
        """
        Atualiza o índice da animação.
        """

        self._index += 1

        if self._index == self._length:

            if not self._loop:
                self._index -= 1
                self._playing = False

            else:
                self._index = 0



    def _update_index_backward(self):
        """
        Atualiza o índice da animação reproduzindo de trás para frente.
        """

        self._index -= 1

        if self._index < 0:

            if not self._loop:
                self._index = 0
                self._playing = False

            else:
                self._index = self._length - 1



    def _update(self):
        """
        Atualiza a animação.
        """

        if not self._playing:
            return

        self._redraw_count += 1

        if self._redraw_count < self._redraw:
            return

        self._redraw_count = 0

        if self._backward:
            self._update_index_backward()

        else:
            self._update_index()

        anchor_value = getattr(self._rect, self._anchor)

        self._surf = self._surfs[self._index]
        self._rect = self._rects[self._index]

        setattr(self._rect, self._anchor, anchor_value)



    def _scale_changed(self):
        """
        Chamado automaticamente quando os fatores de redimensionamento da
        animação mudam.
        """

        self._transform()



    def _aspect_changed(self):
        """
        Chamado automaticamente quando o aspecto da animação muda.
        """

        self._transform()



    def _data_buffered(self):
        """
        Chamado automaticamente quando os dados da animação são armazenados no
        buffer da tela para que a animação seja desenhada.
        """

        _ANIMATIONS_TO_UPDATE.add(self)



    @property
    def anchors(self):
        """
        Tupla de strings representando as âncoras válidas.
        """

        return _ANIMATION_ANCHORS



    @property
    def length(self):
        """
        Inteiro maior que 0 representando o número de quadros da animação.
        """

        return self._length



    @property
    def anchor(self):
        """
        String não-vazia representando o atributo de posicionamento cujo valor
        se mantém inalterado nas mudanças entre quadros de tamanhos diferentes.
        Veja a propriedade "anchors" para conhecer as âncoras válidas.
        """

        return self._anchor



    @anchor.setter
    def anchor(self, anchor):

        _assert_str('anchor', anchor)
        _assert_ne_str('anchor', anchor)
        _assert_vld_anchor(anchor)

        self._anchor = anchor



    @property
    def redraw(self):
        """
        Inteiro maior que 0 representando o número de vezes que cada quadro da
        animação é desenhado antes de ser substituído pelo quadro seguinte.
        """

        return self._redraw



    @redraw.setter
    def redraw(self, redraw):

        _assert_int('redraw', redraw)
        _assert_gr_0('redraw', redraw)

        self._redraw = redraw



    @property
    def loop(self):
        """
        Bool indicando se a animação é reproduzida automaticamente desde o
        começo após chegar ao fim.
        """

        return self._loop



    @loop.setter
    def loop(self, loop):

        _assert_bool('loop', loop)

        self._loop = loop



    @property
    def playing(self):
        """
        Bool indicando se a animação está sendo reproduzida.
        """

        return self._playing



    @playing.setter
    def playing(self, playing):

        _assert_bool('playing', playing)

        self._playing = playing



    @property
    def backward(self):
        """
        Bool indicando se a animação é reproduzida de trás para frente.
        """

        return self._backward



    @backward.setter
    def backward(self, backward):

        _assert_bool('backward', backward)

        self._backward = backward



    @property
    def index(self):
        """
        Inteiro maior ou igual a 0 e menor que a propriedade "length"
        representando o índice do quadro atual da animação.
        """

        return self._index



    @index.setter
    def index(self, index):

        _assert_int('index', index)
        _assert_gr_eq_0('index', index)
        _assert_le_anim_len(self._length, index)

        self._index = index

        anchor_value = getattr(self._rect, self._anchor)

        self._surf = self._surfs[self._index]
        self._rect = self._rects[self._index]

        setattr(self._rect, self._anchor, anchor_value)



    def copy(self):
        """
        copy() -> Animation

        Cria e retorna uma cópia da animação.
        """

        animation = object.__new__(self.__class__)

        animation._original_surfs   = self._original_surfs

        animation._scalex = self._scalex
        animation._scaley = self._scaley

        animation._surfs = tuple([surf.copy() for surf in self._surfs])
        animation._rects = tuple([rect.copy() for rect in self._rects])

        animation._surf = animation._surfs[self._index]
        animation._rect = animation._rects[self._index]

        animation._red   = self._red
        animation._green = self._green
        animation._blue  = self._blue
        animation._alpha = self._alpha
        animation._sub_color = self._sub_color

        animation._flipx = self._flipx
        animation._flipy = self._flipy

        animation._angle = self._angle
        animation._osd   = self._osd

        animation._blend = self._blend
        animation._blend_flag = self._blend_flag

        animation._redraw  = self._redraw
        animation._redraw_count = self._redraw_count
        animation._length = self._length
        animation._anchor = self._anchor
        animation._index = self._index
        animation._loop = self._loop
        animation._playing = self._playing
        animation._backward = self._backward

        animation._info = self._info

        return animation



    @classmethod
    def from_images(cls, images):
        """
        from_images(images) -> Animation

        Cria e retorna uma nova animação a partir das imagens fornecidas.

        O argumento "images" é uma tupla com 1 ou mais objetos Image
        representando os quadros da animação.
        """

        _assert_tuple('images', images)
        _assert_ne_tuple('images', images)

        for (index, image) in enumerate(images):
            _assert_image(f'images[{index}]', image)

        surfs = tuple([image._surf.copy() for image in images])

        animation = object.__new__(cls)
        animation._init(surfs)

        return animation



#===============================================================================
class _Tile(_2D, _Positional):
    """
    Objeto representando um ladrilho.
    """

    __slots__ = ('_tmap', '_rect', '_index', '_indexes', '_graphic')



    def __init__(self, tmap, left, top, width, height, index, indexes):
        self._tmap = tmap
        self._rect = pygame.Rect(left, top, width, height)
        self._index = index
        self._indexes = indexes
        self._graphic = None



    @property
    def index(self):
        """
        Inteiro maior ou igual a 0 representando o índice para encontrar o
        ladrilho no vetor do mapa.
        """

        return self._index



    @property
    def indexes(self):
        """
        Tupla de 2 inteiros (r, c) maiores ou iguais a 0 representando os
        índices para encontrar o ladrilho na matriz do mapa.
        """

        return self._indexes



    @property
    def info(self):
        """
        Qualquer tipo de objeto representando informações. Esta propriedade
        reflete o valor da propriedade "info" do objeto gráfico associado ao
        ladrilho.
        """

        if self._graphic is not None:
            return self._graphic._info



    @property
    def graphic(self):
        """
        None ou qualquer tipo de objeto gráfico associado ao ladrilho. São
        considerados gráficos os objetos Image e os objetos Animation.
        """

        return self._graphic



    @graphic.setter
    def graphic(self, graphic):

        _assert_graphic_none('graphic', graphic)

        self._graphic = graphic



#===============================================================================
class TileMap(_2D, _Mobile):
    """
    TileMap(rows, columns, tile_width, tile_height) -> TileMap

    Classe de objetos para representar mapas de ladrilhos.

    O argumento "rows" é um inteiro maior que 0 representando o número de linhas
    do mapa.

    O argumento "columns" é um inteiro maior que 0 representando o número de
    colunas do mapa.

    O argumento "tile_width" é um inteiro maior que 0 representando a largura de
    cada ladrilho do mapa em pixels.

    O argumento "tile_height" é um inteiro maior que 0 representando a altura de
    cada ladrilho do mapa em pixels.
    """

    __slots__ = ('_matrix', '_vector', '_rect', '_focused')



    def __init__(self, rows, columns, tile_width, tile_height):

        _assert_int('rows', rows)
        _assert_gr_0('rows', rows)

        _assert_int('columns', columns)
        _assert_gr_0('columns', columns)

        _assert_int('tile_width', tile_width)
        _assert_gr_0('tile_width', tile_width)

        _assert_int('tile_height', tile_height)
        _assert_gr_0('tile_height', tile_height)

        self._init(rows, columns, tile_width, tile_height)



    def _init(self, rows, columns, tile_width, tile_height):
        """
        Inicializa o mapa.
        """

        matrix = []
        vector = []
        index = 0

        for y in range(rows):

            row = []
            for x in range(columns):

                tile = _Tile(self, x * tile_width, y * tile_height,
                    tile_width, tile_height, index, (y, x))

                index += 1

                row.append(tile)
                vector.append(tile)

            row = tuple(row)
            matrix.append(row)

        self._matrix = tuple(matrix)
        self._vector = tuple(vector)

        self._rect = pygame.Rect(
            0, 0, columns * tile_width, rows * tile_height)

        self._focused = ()
        self._update_focused()



    def _position_changed(self):
        """
        Chamado automaticamente quando a posição do mapa muda.
        """

        x = self._rect.left - self._vector[0]._rect.left
        y = self._rect.top - self._vector[0]._rect.top

        if (not x) and (not y):
            return

        for tile in self._vector:
            tile._rect.move_ip(x, y)

        self._update_focused()



    def _update_focused(self):
        """
        Atualiza o vetor de ladrilhos que estão na tela.
        """

        if not self._rect.colliderect(screen._rect):
            self._focused = ()

            return

        start_row = 0
        for row in self._matrix:
            tile = row[0]
            if tile.bottom > screen.top:
                start_row = self._matrix.index(row)
                break

        end_row = len(self._matrix)
        for row in self._matrix[start_row:]:
            tile = row[0]
            if tile.top > screen.bottom:
                end_row = self._matrix.index(row)
                break

        row = self._matrix[start_row]

        start_column = 0
        for tile in row:
            if tile.right > screen.left:
                start_column = row.index(tile)
                break

        end_column = len(row)
        for tile in row:
            if tile.left > screen.right:
                end_column = row.index(tile)
                break

        focused = []
        for row in self._matrix[start_row:end_row]:
            for tile in row[start_column:end_column]:
                focused.append(tile)

        self._focused = tuple(focused)



    @property
    def focused(self):
        """
        Tupla de objetos _Tile: vetor contendo os ladrilhos do mapa que estão na
        tela.
        """

        return self._focused



    @property
    def vector(self):
        """
        Tupla de objetos _Tile: vetor contendo todos os ladrilhos do mapa.
        """

        return self._vector



    @property
    def matrix(self):
        """
        Tupla de tuplas de objetos _Tile: matriz contendo todos os ladrilhos do
        mapa. O primeiro índice corresponde à linha e o segundo à coluna.
        """

        return self._matrix



    @classmethod
    def from_matrix(cls, matrix, graphics):
        """
        from_matrix(matrix, graphics) -> TileMap

        Cria e retorna um novo mapa a partir de uma matriz de índices.

        O argumento "matrix" é uma tupla de tuplas de inteiros maiores ou iguais
        a 0 e menores que "len(graphics)". Todas tuplas aninhadas (as linhas da
        matriz) precisam ter o mesmo número de itens. Os inteiros das tuplas
        aninhadas serão usados para indexar a tupla "graphics", associando os
        objetos gráficos aos ladrilhos do mapa resultante.

        O argumento "graphics" é uma tupla de objetos gráficos. São considerados
        gráficos os objetos Image e os objetos Animation.

        Note que todos os ladrilhos do mapa resultante terão o mesmo tamanho do
        primeiro objeto gráfico encontrado em "graphics".
        """

         # Precisamos testar a tupla de gráficos primeiro, porque alguns testes
         # de matriz assumem que a tupla de gráficos é válida.
        _assert_tuple('graphics', graphics)
        _assert_ne_tuple('graphics', graphics)
        for (index, graphic) in enumerate(graphics):
            _assert_graphic(f'graphics[{index}]', graphic)

        _assert_tuple('matrix', matrix)
        _assert_ne_tuple('matrix', matrix)

        for (row_index, row) in enumerate(matrix):
            _assert_tuple(f'matrix[{row_index}]', row)
            _assert_ne_tuple(f'matrix[{row_index}]', row)
            _assert_all_same_len('matrix', matrix)

            for (item_index, item) in enumerate(row):
                _assert_int(f'matrix[{row_index}][{item_index}]', item)
                _assert_gr_eq_0(f'matrix[{row_index}][{item_index}]', item)
                _assert_le_graphics_len(len(graphics), item)

        rows = len(matrix)
        columns = len(matrix[0])
        tile_width = graphics[0].width
        tile_height = graphics[0].height

        tmap = object.__new__(cls)
        tmap._init(rows, columns, tile_width, tile_height)

        for tile in tmap._vector:
            (row, column) = tile._indexes
            index = matrix[row][column]
            tile._graphic = graphics[index]

        return tmap



    @classmethod
    def from_file(cls, path, graphics):
        """
        from_file(path, graphics) -> TileMap

        Cria e retorna um novo mapa a partir de um arquivo representando uma
        matriz de índices.

        O argumento "path" é uma string não-vazia representando o caminho do
        arquivo a ser carregado. O arquivo precisa ter pelo menos 1 linha, e
        cada linha do arquivo precisa ter pelo menos 1 número. Todas as linhas
        do arquivo precisam ter a mesma quantidade de números, separados por
        espaço. Aqui está um exemplo de arquivo formatado corretamente:

            31 27 01 99
            02 01 11 32

        Como você pode ver, é possível escrever 02 em vez de 2 para que todos os
        números tenham a mesma quantidade de dígitos e o arquivo fique mais
        legível. Os números do arquivo serão convertidos em inteiros e usados
        para indexar a tupla "graphics", associando os objetos gráficos aos
        ladrilhos do mapa resultante.

        O argumento "graphics" é uma tupla de objetos gráficos. São considerados
        gráficos os objetos Image e os objetos Animation.

        Note que todos os ladrilhos do mapa resultante terão o mesmo tamanho do
        primeiro objeto gráfico encontrado em "graphics".
        """

        _assert_str('path', path)
        _assert_ne_str('path', path)
        _assert_exists(path)
        _assert_file(path)

        matrix = _load_matrix(path)

        return cls.from_matrix(matrix, graphics)



    def draw(self):
        """
        draw() -> None

        Desenha o mapa na tela.
        """

        for tile in self._focused:
            graphic = tile._graphic

            if graphic is None:
                continue

            data = (graphic._surf, tile._rect.topleft,
                    None, graphic._blend_flag)

            screen._to_draw.append(data)

            graphic._data_buffered()



#===============================================================================
class Sound(object):
    """
    Sound(path) -> Sound

    Classe de objetos para representar sons.

    O argumento "path" é uma string não-vazia representando o caminho do arquivo
    de som a ser carregado.
    """

    __slots__ = ('_sound', '_channel', '_volumel', '_volumer')



    def __init__(self, path):
        _assert_str('path', path)
        _assert_ne_str('path', path)
        _assert_exists(path)
        _assert_file(path)

        (self._sound, self._channel) = _load_sound(path)

        self._volumel = 1.0
        self._volumer = 1.0



    def __del__(self):
        try:
            _SOUND_CHANNELS.append(self._channel)

        except:
            pass



    @property
    def length(self):
        """
        Float maior que 0.0 representando a duração do som em segundos.
        """

        return self._sound.get_length()



    @property
    def volumel(self):
        """
        Float entre 0.0 e 1.0 representando o volume do som no alto-falante da
        esquerda. Valores menores que 0.0 são arredondados para 0.0 e valores
        maiores que 1.0 são arredondados para 1.0.
        """

        return self._volumel



    @volumel.setter
    def volumel(self, volumel):

        _assert_float('volumel', volumel)

        self._volumel = _round_float_0_1(volumel)

        self._channel.set_volume(self._volumel, self._volumer)



    @property
    def volumer(self):
        """
        Float entre 0.0 e 1.0 representando o volume do som no alto-falante da
        direita. Valores menores que 0.0 são arredondados para 0.0 e valores
        maiores que 1.0 são arredondados para 1.0.
        """

        return self._volumer



    @volumer.setter
    def volumer(self, volumer):

        _assert_float('volumer', volumer)

        self._volumer = _round_float_0_1(volumer)

        self._channel.set_volume(self._volumel, self._volumer)



    @property
    def volume(self):
        """
        Tupla de 2 floats (l, r) entre 0.0 e 1.0 representando os volumes do som
        nos alto-falantes da esquerda e da direita. Valores menores que 0.0 são
        arredondados para 0.0 e valores maiores que 1.0 são arredondados para
        1.0.
        """

        return (self._volumel, self._volumer)



    @volume.setter
    def volume(self, volume):

        _assert_tuple('volume', volume)
        _assert_len_2('volume', volume)
        _assert_float('volume[0]', volume[0])
        _assert_float('volume[1]', volume[1])

        self._volumel = _round_float_0_1(volume[0])
        self._volumer = _round_float_0_1(volume[1])

        self._channel.set_volume(self._volumel, self._volumer)



    def play(self, times = 1, max_time = 0.0, fade_in = 0.0):
        """
        play(times = 1, max_time = 0.0, fade_in = 0.0) -> None

        Reproduz o som.

        O argumento "times" é um inteiro maior ou igual a 0 representando
        quantas vezes o som deve ser reproduzido. Se for 0, o som será
        reproduzido repetidas vezes, indefinidamente.

        O argumento "max_time" é um float maior ou igual a 0.0 representando o
        tempo máximo da reprodução em segundos. Se for 0.0, o som será
        reproduzido integralmente.

        O argumento "fade_in" é um float maior ou igual a 0.0 representando a
        duração do "fade in" em segundos. Se for 0.0, a reprodução iniciará sem
        "fade in".
        """

        _assert_int('times', times)
        _assert_gr_eq_0('times', times)

        _assert_float('max_time', max_time)
        _assert_gr_eq_0('max_time', max_time)

        _assert_float('fade_in', fade_in)
        _assert_gr_eq_0('fade_in', fade_in)

        times -= 1
        max_time = _s2ms(max_time)
        fade_in = _s2ms(fade_in)

        self._channel.play(self._sound, times, max_time, fade_in)



    def stop(self, fade_out = 0.0):
        """
        stop(fade_out = 0.0) -> None

        Interrompe a reprodução do som.

        O argumento "fade_out" é um float maior ou igual a 0.0 representando a
        duração do "fade out" em segundos. Se for 0.0, a reprodução será
        interrompida sem "fade out".
        """

        _assert_float('fade_out', fade_out)
        _assert_gr_eq_0('fade_out', fade_out)

        fade_out = _s2ms(fade_out)

        if fade_out:
            self._channel.fadeout(fade_out)

        else:
            self._channel.stop()



    def pause(self):
        """
        pause() -> None

        Pausa a reprodução do som.
        """

        self._channel.pause()




    def unpause(self):
        """
        unpause() -> None

        Retoma a reprodução do som no ponto onde foi pausada.
        """

        self._channel.unpause()



#===============================================================================
class Error(Exception):
    """
    Classe de erros específicos do Hobby.
    """

    pass



#===============================================================================
_TEXT_ALIGNMENTS = ('left', 'center', 'right')

_ANIMATION_ANCHORS = ('top', 'left', 'bottom', 'right', 'topleft', 'bottomleft',
                      'topright', 'bottomright', 'midtop', 'midleft',
                      'midbottom', 'midright', 'center', 'centerx', 'centery')

_GRAPHIC_BLENDS_TABLE = {
    'normal' : 0,
    'add'    : pygame.BLEND_RGBA_ADD,
    'sub'    : pygame.BLEND_RGBA_SUB,
    'min'    : pygame.BLEND_RGBA_MIN,
    'max'    : pygame.BLEND_RGBA_MAX,
    'mult'   : pygame.BLEND_RGBA_MULT,
    'premult': pygame.BLEND_PREMULTIPLIED
}

_GRAPHIC_BLENDS = tuple(_GRAPHIC_BLENDS_TABLE.keys())

_FONTS = {}
_SOUND_CHANNELS = []
_ANIMATIONS_TO_UPDATE = set()

_DEFAULT_TITLE = sys.argv[0] or '<stdin>'

_DEFAULT_ICON = pygame.Surface((32, 32))
_DEFAULT_ICON.fill((255, 255, 255))
_DEFAULT_ICON.fill((0, 0, 255), (0, 0, 32, 8))



#===============================================================================
ticker = _Ticker()

window = _Window()
screen = _Screen()
camera = _Camera()

mouse = _Mouse()
keyboard = _Keyboard()

joysticks = []
for joy_id in range(pygame.joystick.get_count()):
    joystick = _Joystick(joy_id)
    joysticks.append(joystick)
joysticks = tuple(joysticks)

try:
    del joy_id

except NameError:
    pass



