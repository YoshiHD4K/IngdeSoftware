#include <iostream>
#include <vector>

using namespace std;

// Función Quicksort sencilla
vector<int> quicksort(vector<int> arr) {
    if (arr.size() <= 1)
        return arr;

    int pivot = arr[0]; // Elegimos el primer elemento como pivote
    vector<int> menores;
    vector<int> mayores;

    // Recorremos desde el segundo elemento
    for (size_t i = 1; i < arr.size(); ++i) {
        if (arr[i] < pivot)
            menores.push_back(arr[i]);
        else
            mayores.push_back(arr[i]);
    }

    // Ordenamos recursivamente y combinamos
    vector<int> resultado;

    vector<int> ordenados_menores = quicksort(menores);
    vector<int> ordenados_mayores = quicksort(mayores);

    // Agregamos los menores
    for (int num : ordenados_menores)
        resultado.push_back(num);

    // Agregamos el pivote
    resultado.push_back(pivot);

    // Agregamos los mayores
    for (int num : ordenados_mayores)
        resultado.push_back(num);

    return resultado;
}

int main() {
    vector<int> lista = {8, 3, 1, 7, 0, 10, 2};
    vector<int> ordenada = quicksort(lista);

    cout << "Lista ordenada: ";
    for (int num : ordenada)
        cout << num << " ";
    cout << endl;

    return 0;
}