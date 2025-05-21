import copy
import xml.etree.ElementTree as ET
import AutomatoFD

def importXml(caminho):

    #pega o arquivo e tranforma em uma arvore de elementos e pega seu no raiz
    raiz = ET.parse(str(caminho)).getroot()

    # Pegando o nó <automaton>
    automaton = raiz.find('automaton')

    alfabeto = set()

    for transicao in automaton.findall('transition'):
        text = transicao.find('read').text
        if text is None:
            raise ("Automato nao e deterministico")
        alfabeto.add(text)

    alfabeto = ''.join(sorted(alfabeto))

    afd = AutomatoFD.AFD(alfabeto)

    for state in automaton.findall('state'):
        id = int(state.attrib['id'])
        afd.criaEstado(id)

        if not state.find('initial') == None:
            afd.mudaEstadoInicial(id)
        if not state.find('final') == None:
            afd.mudaEstadoFinal(id, True)

    for transicao in automaton.findall('transition'):
        afd.criaTransicao(transicao.find('from').text, transicao.find('to').text, transicao.find('read').text)
    return afd

