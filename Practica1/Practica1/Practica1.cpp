// Practica1.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <iostream>
#include <vector>
#include <random>
#include <math.h>
#include <string>
#include <ctime>
#include <algorithm>
#include <ratio>
#include <chrono>

// El vector de la cuenta de cada digito se inicializa con -1 en el 0 para que el algoritmo funcione correctamente:
#define CUENTA_INICIAL {-1,0,0,0,0,0,0,0,0,0}
// Numero de elementos del vector:
#define N_ELEMENTOS 100000

#define hrc std::chrono::high_resolution_clock

using namespace std;

// Muestra todos los elementos de v separados por un espacio por salida estandar
void mostrar(const vector<string>& v) {
    for (auto e : v) {
        cout << e << " ";
    }
    cout << endl;
}

// Rellena los n_eltos primeros elementos de v con strings de longitud n_digs que representan numeros del 0 al 10^n_digs-1
void inicializar(vector<string>& v, const int n_digs) {
    int n_eltos = v.size();
   /* for (int i = 0; i < n_eltos; i++) {
        long num = rand() % long(pow(10.0, n_digs)); // numero aleatorio entre 0 y 10^n_digs, es decir, un numero con n_digs
        // Nota: parece que para valores de n_digs>7, casi todos tienen menos digitos... Probar otra f que no sea rand?
        // long no lo ha funcionado
        string num_str = to_string(num); // en string
        while (num_str.length() < n_digs) { // si tiene menos de n_digs digitos, se añaden 0s a la izq
            num_str = "0" + num_str;
        }
        v[i] = num_str;
    }*/
    for (int i = 0; i < n_eltos; i++){
        for(int j = 0; j < n_digs; j++){
            char num = (rand() % 10) + '0';
            v[i] += num;
        }
    }
}

// Suma cada elemento i con el i+1, para i=0..9
void acumular(vector<int>& cuenta) {
    for (int i = 1; i < 10; i++) {
        cuenta[i] += cuenta[i - 1];
    }
}

// v el vector de numeros (formato string), n_dig el numero de digitos
// ordena v con el algoritmo de radix LSF
void radix_rec(vector<string>& v, const int n_dig, const int i_dig) {
    vector<int> cuenta = CUENTA_INICIAL; // lleva la cuenta del numero de veces que aparece cada digito
    int n_eltos = v.size();
    vector<string> aux(n_eltos); // auxiliar del mismo tamaño que el original
    for (auto e : v) {
        int digito = e[i_dig] - '0'; // i-ésimo digito
        //cout << "digito: " << digito << endl;
        cuenta[digito]++; // Contamos el digito correspondiente
    }
    // Acumulamos las cuentas de los digitos de izquierda a dcha:
    acumular(cuenta);
    // Y recolocamos cada elemento del original en el auxiliar según la cuenta:
    for (int j = n_eltos - 1; j >= 0; j--) { // (empezando por la dcha)
        string elemento = v[j]; // Tomamos el j-esimo elemento
        int digito = elemento[i_dig] - '0'; // Y su i-esimo digito
        int indice = cuenta[digito]--; // Posicion en el auxiliar (y reducimos esa cuenta)
        aux[indice] = elemento;
    }
    // Finalmente, actualizamos el vector original:
    if(i_dig > 0){
        radix_rec(aux, n_dig, i_dig-1);
    }
}




int main()
{
    int n_digs, n_eltos;
    hrc::time_point t1, t2;

    cout << "Introduce el numero de digitos: " << flush;
    cin >> n_digs; 
    cout << "Y el numero de elementos a ordenar: " << flush;
    cin >> n_eltos;

    vector<string> v(n_eltos); // Se inicializa con n_eltos
    inicializar(v, n_digs); // Valores aleatorios de n_digs cada uno

    //vector<string> v_aux(v);

    vector<unsigned long long> v_aux(n_eltos);
    for(auto e : v){
        v_aux.push_back(stoull(e));
    }


    t1 = hrc::now();
    sort(v_aux.begin(), v_aux.end());
    t2 = hrc::now();
    chrono::duration<double> tiempo_sort = chrono::duration_cast<chrono::duration<double>>(t2 - t1);

    cout << "Inicial:" << endl;
    mostrar(v);
    cout << "-----------------------------------------------" << endl;


    t1 = hrc::now();
    radix_rec(v,n_digs,n_digs-1); // Se ordena
    t2 = hrc::now();
    chrono::duration<double> tiempo_radix = chrono::duration_cast<chrono::duration<double>>(t2 - t1);


    cout << "Ordenado:" << endl;
    //mostrar(v);

    cout << "Ordenado2:" << endl;
    //mostrar(v_aux);

    cout << "Tiempo Radix: " << tiempo_radix.count() << endl;
    cout << "Tiempo Sort: " << tiempo_sort.count() << endl;


    return 0;
}
