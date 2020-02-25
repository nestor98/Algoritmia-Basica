// Practica1.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <iostream>
#include <vector>
#include <random>
#include <math.h>
#include <string>

// El vector de la cuenta de cada digito se inicializa con -1 en el 0 para que el algoritmo funcione correctamente:
#define CUENTA_INICIAL {-1,0,0,0,0,0,0,0,0,0}

#define N_ELEMENTOS 100000

using namespace std;


// Muestra todos los elementos de v separados por un espacio por salida estandar
void mostrar(vector<string>& v) {
    for (auto e : v) {
        cout << e << " ";
    }
    cout << endl;
}


// Rellena los N_ELEMENTOS primeros elementos de v con strings de longitud n_digs que representan numeros del 0 al 10^n_digs-1
void inicializar(vector<string>& v, const int n_digs) {
  
    for (int i = 0; i < N_ELEMENTOS; i++) {
        long num = rand() % long(pow(10.0, n_digs)); // numero aleatorio entre 0 y 10^n_digs, es decir, un numero con n_digs
        string num_str = to_string(num); // en string
        while (num_str.length() < n_digs) { // si tiene menos de n_digs digitos, se añaden 0s a la izq
            num_str = "0" + num_str;
        }
        v[i] = num_str;
        // TODO: strings aleatorias de long n
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
void radix(vector<string>& v, const int n_dig) {
    // Iterar desde el digito menos significativo
    vector<int> cuenta = CUENTA_INICIAL; // lleva la cuenta del numero de veces que aparece cada digito
    vector<string> aux(v.size()); // auxiliar del mismo tamaño que el original
    for (int i = n_dig - 1; i >= 0; i--) {
        // Si se quieren ver la evolucion con las iteraciones, descomentar estas tres lineas:
            //cout << "------ iter " << n_dig - i << " ------\n";
            //mostrar(v);
            //cout << "--------------------\n";
        // Para cada digito de los numeros en v:
        for (auto e : v) {
            int digito = e[i] - '0'; // i-ésimo digito
            //cout << "digito: " << digito << endl;
            cuenta[digito]++; // Contamos el digito correspondiente
        }
        // Acumulamos las cuentas de los digitos de izquierda a dcha:
        acumular(cuenta);
        // Y recolocamos cada elemento del original en el auxiliar según la cuenta:
        for (int j = N_ELEMENTOS - 1; j >= 0; j--) { // (empezando por la dcha)
            string elemento = v[j]; // Tomamos el j-esimo elemento
            int digito = elemento[i] - '0'; // Y su i-esimo digito
            int indice = cuenta[digito]--; // Posicion en el auxiliar (y reducimos esa cuenta)
            aux[indice] = elemento;
        }
        // Finalmente, actualizamos el vector original:
        v = aux; // Comprobar que esto funcione, tengo mis dudas
        // Y resetear la cuenta:
        cuenta = CUENTA_INICIAL;
    }
}



// v el vector de numeros (formato string), n el numero de digitos
// ordena v con el algoritmo de radix LSF
void radix_rec(vector<string>& v, const int n, const int j) {
    // Iterar desde el digito menos significativo
    vector<int> cuenta = CUENTA_INICIAL; // lleva la cuenta del numero de veces que aparece cada digito
    for (int i = n - 1; i >= 0; i--) {
       
        // Para cada digito de los numeros en v:
        for (auto e : v) {
            int digito = e[i] - '0'; // i-ésimo digito
            cuenta[digito]++; // Contamos el digito correspondiente

        }
        cuenta = CUENTA_INICIAL;
    }

}



int main()
{
    int n_digs;
    cout << "Introduce el numero de digitos: " << flush;
    cin >> n_digs; 
    vector<string> v(N_ELEMENTOS); // Se inicializa con N_ELEMENTOS
    inicializar(v, n_digs); // Valores aleatorios de n_digs cada uno
    cout << "Inicial:" << endl;
    mostrar(v);
    cout << "-----------------------------------------------" << endl;
    // Medir tiempo de aqui
    radix(v,n_digs); // Se ordena
    // a aqui
    cout << "Ordenado:" << endl;
    mostrar(v);

    return 0;
}
