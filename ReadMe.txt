Pre stiahnutie a rozbalenie FastText je možné využiť nasledujúce príkazy:

!wget https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip
!unzip wiki-news-300d-1M.vec.zip 

Pre stiahnutie a rozbalenie GloVe:

!wget https://nlp.stanford.edu/data/glove.42B.300d.zip
!unzip -q glove.42B.300d.zip 

Pre stiahnutie word2Vec bol použitý odkaz z google disc:

https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/view?resourcekey=0-wjGZdNAUop6WykTtMip30g

Ja som stiahnté súbory umiestnila do zložky Data, preto !unzip príkazy v scriptoch sú s priamou cestou tam.


Inštalácia knižníc: 

pip install matplotlib
pip install pandas
pip install seaborn
pip install numpy
pip install torch
pip install transformers
pip install scikit-learn
pip install tensorflow
pip install tensorflow-text
pip install keras
pip install datasets


V každej zložke Scripts_X sa nachádza script Dataset.ipynb, kde je ukázané rozloženie dát. Ďalej obsahuje zložky so scriptami pre jednotlivé modely.

Zložka Data obahuje všetky datasety, ktoré boli použité v práci. Sú tam pred preprocessingom, pretože tie sa použili pre scripty MachineLearning (ten má vlastný preprocessing priamo v scripte).  Všetky csv subory s prefixom final_ sú už po preprocessingu.

Script preprocessing.py bol použitý na všetky dáta s miernymi úpravami, podľa potrieb experimentu (napr. odstránenie niektorých autorov, ktorí nemali dostatoční počet diel a podobne). 

Scripty prepare_data.py a create_dataset.py je potrebné nahrať do projektu od Ing Vojtecha Prokopa, sú jeho rozšírením na pripravenie dát potrebných pre moju prácu.

Scripts_1 - niektoré modely, ktoré boli vytvárané a testované na začiatku celej práce, aby sa našli vhodné architektúry pre ďalšie experiemnty. 
    - Experiment 2
    
Scripts_2 - vybalancovaný dataset
    - Experiment 1 a 4
    
Scripts_3 - nevybalancovaný dataset
    - Experiment 1 a 6
    
Scripts_4 - testovanie TextVectorization vrstvy pre NN modely
    - Experiment 3 a 4
    
Scripts_5 - veľké nevybalancované dáta, meranie času
    - Experiment 5 a 6
    
Scripts_6 - vybraní autori podľa obodbia v ktorom písali, vytvorené heatmaps
    - Experiemnt 7