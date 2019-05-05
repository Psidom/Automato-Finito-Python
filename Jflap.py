import xml.etree.cElementTree as ET

from pip._vendor.distlib.compat import raw_input


class XML(object):
    def __init__(self):
        pass

    def gerar_xml(self):
        structure = ET.Element("structure")
        type = ET.SubElement(structure, "type").text = 'fa'
        automaton = ET.SubElement(structure, "automaton")
        #ET.SubElement(automaton, "user", name="user").text = 'bla'

        from pip._vendor.distlib.compat import raw_input
        value = raw_input("Adicionar um elemento? (s/n): ")
        self.gerar_automato(automaton,value)
        #ET.SubElement(automaton, "senha", name="senha").text = 'balbala'
        arquivo = ET.ElementTree(structure)
        arquivo.write("meu_xml.xml")

    def gerar_automato(self, automaton, value, estado=None):
         i=0
         x=0
         lista = []
         while value == 's' or value == 'S':
            state = ET.SubElement(automaton, "state", id=str(i),name="q"+str(i))
            name = 'q' + str(i)
            ET.SubElement(state, "x").text = str(x)
            ET.SubElement(state, "y").text = str(136)
            if estado != None:
                ET.SubElement(state, estado)
            if i == 0:
                ET.SubElement(state, "initial")
            i += 1
            x += 100
            value = raw_input("Adicionar um elemento? (s/n): ")
            if value == 'n' or value == 'N':
                ET.SubElement(state, "final")
            lista.append(name)
         print("De acordo com a lista de status abaixo diga quais são as transições que você quer fazer")
         n=0
         for j in lista:
             print('nome: '+ j)
             print(' id: '+str(n))
             n+=1
         opt = 's'
         while opt == 's' or opt == 'S':
             fonte = raw_input('Qual o id status fonte?')
             desti = raw_input ('Qual o id status destino?')
             trans = raw_input ('Qual o nome da transição')
             transition = ET.SubElement(automaton, "transition")
             ET.SubElement(transition, "from").text = str(fonte)
             ET.SubElement(transition, "to").text = str(desti)
             ET.SubElement(transition, "read").text = str(trans)
             opt = raw_input('Deseja adicionar outra transição?')
def main():
    xml = XML()
    xml.gerar_xml()

main()
