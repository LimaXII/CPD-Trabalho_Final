#Nomes: Luccas da Silva Lima e Bruno Longo Farina
#Trabalho final de CPD - FIFA 21 - Players.
#Abre e le o arquivo de nomes.
#Funcao que cria a tabela hash.    

import time  #Usado para cronometrar o tempo para gerar as estruturas utilizadas no trabalho.

#Classe que ira armazenar a funções do nodo da árvore trie.
#from types import NoneType
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
        for i in range (0, len(contents[x])):                               
            tr.insert(contents[x][i][1])        #Insere ela na trie.

def hash_table(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                         #Percorre todas os nomes da lista.                
        hash_value = horner_method_players(contents[x][0], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert_rating(hash_value, vet,contents[x])        #Chama a funcao que ira inserir os nomes na tabela hash.

def hash_table_players(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                             #Percorre todas os nomes da lista.                
        hash_value = horner_method_players_smp(contents[x][1], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert(hash_value, vet,contents[x])                   #Chama a funcao que ira inserir os nomes na tabela hash.

def hash_table_players_in_rating(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                         #Percorre todas os nomes da lista.                
        hash_value = horner_method_players(contents[x][0], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert_names_in_media(hash_value, vet,contents[x][0]) 

def insert_ratings(contents, M, vet):
    #Variavel que ira guardar o numero correspondente a cada nome    
    for x in range (0, len(contents)):                         #Percorre todas os nomes da lista.                
        hash_value = horner_method_players(contents[x][1], M)  #Chama a funcao do metodo de Horner, para achar uma posicao adequada para o nome na tabela hash.                               
        hash_insert_ratings_in_media(hash_value, vet,contents[x]) 

#Calcula o polinomio de horner para a tabela hash dos JOGADORES.
def horner_method_players(word, M):
    p = 31
    hash_value = (p * int(word)) % M
    return(hash_value)       #Retorna a posição do vetor a ser colocado o jogador.

#Mesma função que a de cima, mas simplificada.
#Apenas calcula o hash e retorna ele.
def horner_method_players_smp(word, M):
    p = 31
    hash_value = 0   
    for i in word:        
            num = ord(i)
            hash_value = (p * hash_value + num) % M
    return(hash_value)

#Insere o nome em uma determinada posicao da tabela.
def hash_insert(pos, vet, name):     
    vet[pos].append(name)
    return

def hash_insert_ratings_in_media(pos, vet, name):     
    for i in range(0,len(vet[pos])):
        if(vet[pos][i][0]==name[1]):
            vet[pos][i].append(name[2])
            return
    print('error')
    return

def hash_insert_names_in_media(pos, vet, name):     
    for i in range(0,len(vet[pos])):
        if(vet[pos][i]== [] ):
            vet[pos][i].append(name)
            return
    vet[pos].append([])
    i+=1
    vet[pos][i].append(name)
    return        

def hash_insert_rating(pos, vet, name):     
    for i in range(0,len(vet[pos])):
        if(vet[pos][i][0]==name[0]):      #se o usuário já deu rating para outro jogador
            vet[pos][i].append(name[1])   #apenas dá um append com o ID do jogador e o rating
            vet[pos][i].append(name[2])
            return
    vet[pos].append(name)
    return

#Realiza a consulta na tabela hash dos jogadores.
def realizar_consulta_players(vet,name):    
    aux = horner_method_players_smp(name,len(vet))  #Calcula a posição em que está o nome solicitado na tabela hash.
    for i in range(0,len(vet[aux])):                #Declara uma string vazia, para guardar o nome do jogador.                     
        if(name == vet[aux][i][1]):                 #Caso o nome procurado exista na tabela:  
            player_id = vet[aux][i][0]  
            player_name = vet[aux][i][1]
            string = (player_id + '   ' + player_name + '   ')
            for x in range (2, len(vet[aux][i])):
                player_pos = vet[aux][i][x]                
                string = string + player_pos   
            string = string.replace("\n", "")         
            return (string)                         #Retorna todas as informações sobre o jogador solicitado.    
    return('Not found.')                            #Caso o jogador não exista.

#Função que transforma um vetor de string em uma string normal.
def transform_to_str(text):
    str1 = ""
    for x in text:
        str1 += x
    return (str1)

#------------------------------------------------------------------
start_time = time.time() #Inicia a contagem de tempo.

#Leitura dos arquivos do trabalho.
with open('players_clean2.csv') as f:   #Usei o arquivo clean2. O arquivo original não tava lendo por conta da acentuação em alguns nomes.
    players = f.readlines()             #Armazena cada campo em uma posição do vetor players.
for i in range(0,len(players)):
    a=players[i].split(',')
    players[i]=a

#with open('rating.csv') as f:          #Lê o arquivo rating.
#    rating = f.readlines()             #Armazena cada campo em uma posição do vetor rating.

with open('minirating.csv') as f:       #Arquivo minirating. To usando ele só pra não travar o programa inteiro.
    rating = f.readlines()              #Armazena cada campo em uma posição do vetor rating.   

for i in range(0,len(rating)):
    a=rating[i].split(',')
    rating[i]=a  

with open('tags.csv') as f:             #Lê o arquivo tags.csv. 
    tags = f.readlines()                #Armazena cada campo em um posição do vetor tags.
  
for i in range(0,len(tags)):
    a=tags[i].split(',')
    tags[i]=a 

del rating[0]                          #Elimina a primeira posição do vetor.
del tags[0]                            #Elimina a primeira posição do vetor.
del players[0]                         #Elimina a primeira posição do vetor.
#------------------------------------------------------------------
#N/M = 1/3
M = int(len(rating)/4) #M será o tamanho da tabela Hash a ser criada para armazenar as médias das avaliações e o total de avaliações para cada jogador.
#Rating_vet é uma tabela Hash que vai armazenar em cada nodo, todas as notas de um mesmo jogador.
#Atualmente anda dando alguns problemas nela, ta armazendo as vezes 2 ou 3 jogadores diferentes no mesmo nodo.
rating_vet = [[] for _ in range(0,M)]   #Vetor que ira armazenar a tabela hash com as notas de cada jogador.   
hash_table(rating, M, rating_vet)       #Chama a funcao para criar a tabela hash.
#------------------------------------------------------------------
#caad valor dos ratings na tabela hash é um array com o primeiro elemento representando
#o ID do usuário e os elementos seguintes são o ID do jogador que ele deu review e a nota 
#atribuída, podendo repetir esses elementos mais de uma vez caso o usuário tenha dado review 
#a mais de um jogador EX:

#['20434', '220440', '5.0\n', '200529', '3.0\n']
#ID do usuário: 20434
#review para o jogador de ID 220440: 5.0
#review para o jogador de ID 200529: 3.0

'''
for i in range(0,len(rating_vet)):
    if(len(rating_vet[i])>0):
        for j in range(0,len(rating_vet[i])):
            if(len(rating_vet[i][j])>3):
                print(rating_vet[i][j])
                '''

#------------------------------------------------------------------
#Criação da tabela Hash com as informações complementares dos jogadores.
M = int(len(players)/5)                           
players_vet = [[] for _ in range(0,M)]            #Vetor que ira armazenar a tabela hash com as informações adicionais de cada jogador.
hash_table_players(players, M, players_vet)       #Chama a funcao para criar a tabela hash.
#------------------------------------------------------------------
players_media =[[[]] for _ in range(0,M)]
hash_table_players_in_rating(players,M,players_media)

insert_ratings(rating,M,players_media)
#------------------------------------------------------------------
#Árvore trie com os nomes dos jogadores.
tr = Trie()
#Chama a função que vai inserir na árvore trie todos os nomes dos jogadores.
insert_trie(players_vet)

#Finaliza a criação de estruturas para o programa.
end_time = time.time()
print("Time to create the structures " + '{:.2f}'.format(end_time - start_time) + " seconds.")

running = 1                         #Variável que vai controlar quando o programa irá terminar.
while (running == 1):               #Loop para deixar o programa rodando.
    text = input("Please insert a name to search. ")
    text = text.split(' ')          #Separa o texto em diferentes partes.
    if (text[0] == 'Exit'):         #Exit para terminar o programa.
        print("Ending program.")
        running = 0             
    elif (text[0] == 'player'):     #Caso digite player, procura o jogador solicitado.                                           
        if (len(text) >= 2):
            del text[0]             #Deleta a parte "player", da string.
            text = transform_to_str(text)        #Transforma o vetor de volta em uma string.   
            consult = (tr.search(text))          #Pega todos os nomes, dado o prefixo dado   
            print("\nsofifa_id   name              player_positions   rating   count")
            for x in consult:                                        #Para cada nome encontrado.
                info = realizar_consulta_players(players_vet,x)      #Recebe o resto das informações pela tabela hash dos jogadores.    
                print(info)                                          #Printa as informações adicionais.
        else:
            print("Please, insert a name after player")    #Caso o usuário insira somente "player".            
    else:
        print("Wrong command. Please, try again. ")        #Caso o usuário insira algum comando inválido. 
#--------------------------------------------------------
# 
#   O que a gente tem de lista e array
# 
# 
#   rating_vet = usuário,jogador,rating,jogador,rating...
#
#   players_vet = ID, nome, posição
# 
#   players_media = ID, rating, rating, rating...
# 
# #
#----------