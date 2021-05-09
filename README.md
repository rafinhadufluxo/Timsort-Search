# TimSort

Timsort é um algoritmo de ordenação híbrido derivado do merge sort e do insertion sort, projetado para ter 
boa performance em vários tipos de dados do mundo real. Foi inventado por Tim Peters em 2002 para ser usado 
na linguagem de programação Python, e tem sido o algoritmo de ordenação padrão de Python desde a versão 2 e 3.
Ele atualmente é usado para ordenar arrays em Java SE 7, talvez, você está usando algum um celular nesse momento, saiba que 
está usando esse grande metodo para ordenação de dados em tempo real.  Ao utilizar técnicas clássicas, mas de forma bem engenhosa, 
o TimSort consegue chegar à complexidade de O(n) para certas coleções quase ordenadas e com pouco gasto de memória. Assim, o TimSort
é a prova de que o conhecimento de algoritmos clássicos podem resolver problemas atuais com muita qualidade.

De acordo que descobrimos o TimSort é um algoritmo de classificação baseado em Insertion Sort e Merge Sort. 
Mas segue uma linha de caracteristicas que são:

        I - Um algoritmo de classificação estável funciona em tempo O (n Log n).   
        II - Usado em Arrays.sort () de Java, bem como em Sort () e Sort () do Python. 
        III - Primeiro, classifição com vetor pequeno usando a classificação por inserção e, a seguir, 
             mescle os vetores usando a fusão da classificação por fusão.

Mas podendo dividir o Array(vetor) em blocos conhecidos como Run. Classificamos essas execuções usando a classificação por inserção uma por 
uma e, em seguida, mesclamos essas execuções usando a função de combinação usada na classificação por mesclagem. Se o tamanho do Array for 
menor do que run, o Array será classificado apenas usando Insertion Sort. O tamanho da execução pode variar de 32 a 64, dependendo do tamanho 
da matriz. Observe que a função de mesclagem tem um bom desempenho quando os subarrays de tamanho têm potências de 2. 
A ideia é baseada no fato de que a classificação por inserção tem um bom desempenho para pequenos arrays.



*REFERÊNCIAS*

https://www.infopulse.com/blog/timsort-sorting-algorithm/ <br>
https://hackernoon.com/timsort-the-fastest-sorting-algorithm-youve-never-heard-of-36b28417f399 <br>
https://medium.com/@rscheiwe/the-case-for-timsort-349d5ce1e414