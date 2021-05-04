# TimSort

Timsort é um algoritmo de ordenação híbrido derivado do merge sort e do insertion sort, projetado para ter 
boa performance em vários tipos de dados do mundo real. Foi inventado por Tim Peters em 2002 para ser usado 
na linguagem de programação Python, e tem sido o algoritmo de ordenação padrão de Python desde a versão 2.3.
Ele atualmente é usado para ordenar arrays em Java SE 7, talvez, você esteja usando um celular nesse momento que não sabe que os celulares usam esse grande metodo para ordenação de dados em tempo real. 

De acordo que descobrimos o TimSort é um algoritmo de classificação baseado em Insertion Sort e Merge Sort. 
Mas segue uma linha de caracteristicas que são:

        I - Um algoritmo de classificação estável funciona em tempo O (n Log n).   
        II - Usado em Arrays.sort () de Java, bem como em Sort () e Sort () do Python. 
        III - Primeiro, classifique as pequenas peças usando a classificação por inserção e, a seguir, 
             mescle as peças usando a fusão da classificação por fusão.

podendo dividir o Array em blocos conhecidos como Run. Classificamos essas execuções usando a classificação por inserção uma por uma e, em seguida, mesclamos essas execuções usando a função de combinação usada na classificação por mesclagem. Se o tamanho do Array for menor do que run, o Array será classificado apenas usando Insertion Sort. O tamanho da execução pode variar de 32 a 64, dependendo do tamanho da matriz. 
Observe que a função de mesclagem tem um bom desempenho quando os subarrays de tamanho têm potências de 2. 
A ideia é baseada no fato de que a classificação por inserção tem um bom desempenho para pequenos arrays.



Para mais informações acesse https://www.infopulse.com/blog/timsort-sorting-algorithm/