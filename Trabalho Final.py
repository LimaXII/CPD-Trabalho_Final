#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Trabalho final de CPD - FIFA 21 - Players.
#Abre e le o arquivo de nomes.
#Funcao que cria a tabela hash.    

#Classe que ira armazenar a funções do nodo da árvore trie.
from types import NoneType

class TrieNode: 
    def __init__(self, char): 
        self.char = char 
        self.is_end = False 
        self.children = {}

#Classe que ira armazenar a funções da árvore trie. 
class Trie(object): 
    def __init__(self): 
        self.root = TrieNode("")
    
    #Função para inserir elementos na árvore.
    def insert(self, word): 
        node = self.root 
        for char in word:
            if char in node.children:
                node = node.children[char]
            else: 
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node         
        node.is_end = True
         
    def dfs(self, node, pre): 
        if node.is_end:
            self.output.append((pre + node.char))         
        for child in node.children.values():
            self.dfs(child, pre + node.char)

    #Função para procurar elementos na árvore.     
    def search(self, x):        
        node = self.root         
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:               
                return []
        self.output = []
        self.dfs(node, x[:-1]) 
        return self.output

#Função que inserte todos os nomes na árvore trie.
def insert_trie(contents):
    for x in range (0, len(contents)):          #Percorre o vetor inteiro.
        test = 0                                #Variável que irá guardar se vai foi passada uma ',' ou não. 
        string = ''                             #Uma string vazia.
        for i in contents[x]:                   #Percorre o nodo do vetor.
            if (i == ','):                      #Caso ache uma ','
                test += 1                       #Test recebe +1.
            if (test == 1) and ((i != '\n') and (i != ',')):    #Caso esteja lendo o nome do jogador.        
                string = string + (i)           #Cria uma string com o nome completo do jogador.                         
        tr.insert(string)                       #Insere ela na trie.

def hash_table(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                  #Percorre todas os nomes da lista.                
        hash_value = horner_method(contents[x], M)      #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash_value, vet,contents[x])        #Chama a funcao que ira inserir os nomes na tabela hash.

def hash_table_players(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                      #Percorre todas os nomes da lista.                
        hash_value = horner_method_players(contents[x], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash_value, vet,contents[x])            #Chama a funcao que ira inserir os nomes na tabela hash.

#Calcula o polinomio de horner para a tabela hash dos JOGADORES.
def horner_method_players(word, M):
    p = 31
    hash_value = 0
    test = 0
    for i in word:
        if (i == ','):
            test += 1
        if (test == 1) and ((i != '\n') and (i != ',')):
            num = ord(i)
            hash_value = (p * hash_value + num) % M
    return(hash_value)      #Retorna a posição do vetor a ser colocado o jogador.

#Mesma função que a de cima, mas simplificada.
#Apenas calcula o hash e retorna ele.
def horner_method_players_smp(word, M):
    p = 31
    hash_value = 0   
    for i in word:        
            num = ord(i)
            hash_value = (p * hash_value + num) % M
    return(hash_value)
    
#Funcao que calcula o valor do polinomio especifico, dado um nome.
def horner_method(word, M):
    test = 0
    p = 11                                              #Primeiro numero primo maior que 10.
    hash_value = 0                                      #Hash comeca valendo 0.
    sigN = 7
    for i in word:                                      #Percorre a palavra.
        if (i == ','):
            test += 1                                           #Marca que passou pela primeira virgula.
        if (test == 1) and ((i != '\n') and (i != ',')):        #Testa se o char eh diferente de "\n" e ",".            
            num = ord(i)                                        #Caso seja diferente, transforma o char para int e acumula em uma soma.
            hash_value = ((sigN * hash_value) + num) % M        #Cria um polinomio correspondente a palavra.
            sigN -= 1            
    return(hash_value)

#Insere o nome em uma determinada posicao da tabela.
def hash_insert(pos, vet, name):     
    vet[pos].append(name)
    return

#Realiza a consulta na tabela hash dos jogadores.
def realizar_consulta_players(vet,name):    
    aux = horner_method_players_smp(name,len(vet))   #Calcula a posição em que está o nome solicitado na tabela hash.
    for i in range(0,len(vet[aux])):
        test = 0
        string = ''                         #Declara uma string vazia, para guardar o nome do jogador.
        for j in vet[aux][i]:
            if (j == ','):                  #Caso ache uma ','.
                test += 1                   #test recebe +1.
            if (test == 1) and ((j != '\n') and (j != ',')):        #Testa se o char eh diferente de "\n" e ",".
                string = string + (j)       #Cria uma string da posição atual do nodo no vetor.
        if(name == string):                 #Caso o nome procurado exista na tabela:         
            return (vet[aux][i])            #Retorna todas as informações sobre o jogador solicitado.
    return('Not found.')                    #Caso o jogador não exista.

#------------------------------------------------------------------
#Leitura dos arquivos do trabalho.
with open('players_clean2.csv') as f:   #Usei o arquivo clean2. O arquivo original não tava lendo por conta da acentuação em alguns nomes.
    players = f.readlines()             #Armazena cada campo em uma posição do vetor players.
                      
#with open('rating.csv') as f:          #Lê o arquivo rating. Arquivo ENORME que consome muito do programa. Precisamos rever isso.
#    rating = f.readlines()             #Armazena cada campo em uma posição do vetor rating.

with open('minirating.csv') as f:       #Arquivo minirating. To usando ele só pra não travar o programa inteiro.
    rating = f.readlines()              #Armazena cada campo em uma posição do vetor rating.   

with open('tags.csv') as f:             #Lê o arquivo tags.csv. 
    tags = f.readlines()                #Armazena cada campo em um posição do vetor tags.
  
del rating[0]                          #Elimina a primeira posição do vetor.
del tags[0]                            #Elimina a primeira posição do vetor.
del players[0]                         #Elimina a primeira posição do vetor.
#------------------------------------------------------------------

#------------------------------------------------------------------
#N/M = 1/3
M = int(len(rating)/4)                  #M será o tamanho da tabela Hash a ser criada para armazenar as médias das avaliações e o total de avaliações para cada jogador.
#Rating_vet é uma tabela Hash que vai armazenar em cada nodo, todas as notas de um mesmo jogador.
#Atualmente anda dando alguns problemas nela, ta armazendo as vezes 2 ou 3 jogadores diferentes no mesmo nodo.
rating_vet = [[] for _ in range(0,M)]   #Vetor que ira armazenar a tabela hash com as notas de cada jogador.   
hash_table(rating, M, rating_vet)       #Chama a funcao para criar a tabela hash.
#------------------------------------------------------------------

#------------------------------------------------------------------
#print(rating_vet)                      #Teste da tabela hash das ratings.
#------------------------------------------------------------------

#------------------------------------------------------------------
#Criação da tabela Hash com as informações complementares dos jogadores.
M = int(len(players)/5)                           #M = len(players), já que não pode ocorrer colisões.
players_vet = [[] for _ in range(0,M)]            #Vetor que ira armazenar a tabela hash com as informações adicionais de cada jogador.
hash_table_players(players, M, players_vet)       #Chama a funcao para criar a tabela hash.
#------------------------------------------------------------------

#------------------------------------------------------------------
#Árvore trie com os nomes dos jogadores.
tr = Trie()
#Chama a função que vai inserir na árvore trie todos os nomes dos jogadores.
insert_trie(players)
#Apenas testando a funcionalidade da árvore trie.
name = input("Please insert a name to search.")
consult = (tr.search(name))         #Pega todos os nomes, dado o prefixo dado
print("sofifa_id   name   player_positions   rating   count")
for x in consult:                   #Para cada nome encontrado.
    info = realizar_consulta_players(players_vet,x)      #Recebe o resto das informações pela tabela hash dos jogadores.    
    print(info)                     #Printa as informações adicionais.
#------------------------------------------------------------------