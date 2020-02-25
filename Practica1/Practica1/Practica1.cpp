// Practica1.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
//

#include <iostream>
#include <vector>

#define CUENTA_INICIAL {-1,0,0,0,0,0,0,0,0,0}

const int N_ELEMENTOS = 100;

using namespace std;

void inicializar(vector<string>& v, const int n) {
    for (int i = 0; i < N_ELEMENTOS; i++) {
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
        // Para cada digito de los numeros en v:
        for (auto e : v) {
            int digito = e[i] - '0'; // i-ésimo digito
            cuenta[digito]++; // Contamos el digito correspondiente
        }
        // Acumulamos las cuentas de los digitos de izquierda a dcha:
        acumular(cuenta);
        // Y recolocamos cada elemento del original en el auxiliar según la cuenta:
        for (int j = N_ELEMENTOS - 1; i >= 0; i--) { // (empezando por la dcha)
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


void mostrar(vector<string>& v) {
    for (auto e : v) {
        cout << e << " ";
    }
    cout << endl;
}

int main()
{
    int n;
    cout << "Introduce el numero de digitos: " << flush;
    cin >> n;
    vector<string> v;
    inicializar(v, n);
    mostrar(v);
    // Medir tiempo de aqui
    radix(v);
    // a aqui
    mostrar(v);

    return 0;
}
