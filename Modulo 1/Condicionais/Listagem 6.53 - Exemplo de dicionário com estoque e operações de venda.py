estoque={   "tomate": [ 1000, 2.30],
            "alface": [ 500, 0.45],
			"batata": [ 2001, 1.20],
			"feijão": [ 100, 1.50] }

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
