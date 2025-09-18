estoque = {"Pastilhas":[20,200],
"discos de freio":[10,400],
"filtros de óleo":[30,800],
"filtros de ar":[17,89],
"filtros de combustível":[25,500],
 "Faróis":[30,450],
"espelhos retrovisores":[40,350],
"palhetas de limpador de para-brisa":[200,50],
"lâmpadas":[200,5],
"Baterias":[20,250], 
"radiadores":[10,550],
"componentes do sistema de arrefecimento":[12,890]}
sei_la_oque = input("digite o produto:")
venda = [[sei_la_oque,int(input("digite a quantidade:"))]]
               
total = 0
print("Vendas:\n")
if sei_la_oque in estoque:
    for operação in venda:
      produto, quantidade = operação 
      preço = estoque[produto][1] 
      custo = preço * quantidade
      print("%12s: %3d x %6.2f = %6.2f" %
		  (produto, quantidade,preço,custo))
      estoque[produto][0] -= quantidade 
      total+=custo
else:
   print(" Custo total: %21.2f\n" % total)
   print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
