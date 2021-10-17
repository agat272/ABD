Agata Swatowska
Temat 5:
earthquake_data.csv https://fivethirtyeight.com/features/the-rock-isnt-alone-lots-of-people-are-worried-about-the-big-one/
 (należy zmienić nazwy kolumn i przygotować tabelę łączącą wiek, płeć 
i odpowiedź na pytanie "Do you think the "Big One" will occur in your lifetime?"

Rozwiązanie:
1. Wczytanie pliku .csv z użyciem biblioteki pandas; z wybiorem interseujących nas kolumn (wiek, płeć oraz odpowiedź na podane wyżej pytanie)
2. Zmiana nazw kolumn na ('Age', 'Gender' oraz 'Answer to question')
3. Zmiana kolejności kolumn na: Age, Gender, Answer to question (poprzednio było: Answer, Age, Gender)
4. Zamieniono wszytskie puste odpowiedzi na wartość NaN
5. Aby zwiększyć przejrzystość wyników oraz wyeleminować błedne odpowiedzi( bez podanie wieku, płci lub odpowiedzi na pytanie), usunięto wszytskie rejestry z wartościami NaN
6. Utowrzenie pliku wynikowego .csv w folderze Analysis Data