#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

double countCoordinate(double latitudea, double longitudea, double altitudea, double latitudeb, double longitudeb, double altitudeb) {
    // Input format: x1 y1 z1
    //               x2 y2 z2
    return sqrt(pow((latitudea - latitudeb), 2) + pow((longitudea - longitudeb), 2) + pow((altitudea - altitudeb), 2));
}

int main(){
    int lata, longa, alta, latb, longb, altb;
    cin >> lata >> longa >> alta >> latb >> longb >> altb;
    cout << countCoordinate(lata, longa, alta, latb, longb, altb) << endl;
    return 0;
}