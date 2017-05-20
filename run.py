from generator import Generator
import pprint

pp = pprint.PrettyPrinter()
npc_generator = Generator()

if __name__ == '__main__':
    pp.pprint(npc_generator.generate())