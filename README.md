# online_sales_analysis
Tema 3 curs Github
Sarcină
Etapa 1: Pregătirea mediului de lucru
Creați un director local online_sales_analysis.
Pe GitHub, creați un repozitoriu nou cu același nume (online_sales_analysis).
Clonați repozitoriul local din GitHub.
Setați-vă numele și adresa de e-mail cu comanda git config.
Etapa 2: Analiza datelor – Funcționalitatea Python
Creați fișierul Python product.py și implementați următoarelor cerințe:
Clasa Product:
Conține atributele: name, price și quantity.
Metoda pentru afișarea informațiilor despre produs.
Metoda pentru actualizarea cantității de produse.
Creați fișierul Python product_manager.py și implementați următoarele cerințe:
Clasa ProductManager:
Conține ca atribut o listă cu toate produsele disponibile.
Adăugarea de produse.
Afișarea tuturor produselor.
Afișarea valorii totale a tuturor produselor.
Creați fișierul Python main.py și în el:
creați instanța ProductManager.
adăugați câteva produse arbitrare.
afișați produsele și valoarea totală a inventarului.
Etapa 3: Gestionarea versiunilor
Faceți primul commit cu un mesaj semnificativ.
Etapa 4: Adăugarea de funcționalități
Creați o ramură nouă add-product-removal.
Adăugați metoda în ProductManager pentru a elimina produsele după nume.
Faceți commit cu un mesaj semnificativ.
Etapa 5: Conflictele și îmbinarea

Reveniți la ramura principală
Îmbinați ramurile și rezolvați conflictele în cod, dacă există.
Etapa 6: Adăugarea clasei Cart

Creați și treceți la o ramură nouă cu add-cart-functionality.
Extindeți proiectul Python adăugând o clasă nouă cart.py care gestionează coșul clientului:
Clasa Cart:
Atribut: cart_items – lista de produse din coș.
Metode:
Adăugarea produselor în coș.
Calcularea valorii totale a coșului, adică a sumei de plată.
Afișarea conţinutul coşului.
Adăugați următoarele modificări în fișierul main.py:
Creați o instanță a clasei Cart.
Adăugați în coș 3 produse selectate aleatoriu din lista de produse disponibile a instanței ProductManager.
Afișați valoarea totală de plată a conținutului coșului, precum și produsele care se află în acesta.
Faceți un commit cu un mesaj semnificativ.
Etapa 7: Ramura principală – Conflict și îmbinare:

Reveniți la ramura principală.
Adăugați următoarele modificări în fișierul main.py:
Schimbați denumirile produselor care au fost adăugate sau cantitatea lor.
Ștergeți liniile de cod legate de afișarea produsului și valoarea totală a inventarului.
Îmbinați ramura principală cu funcționalitatea add-cart-functionality și rezolvați conflictele din cod, dacă există.
Etapa 8: Adăugarea fișierului .gitignore
Creați un fișier de testare config.json în directorul proiectului și adăugați următorul conținut:
{
    "api_key": "12345",
    "database_url": "localhost"
}
Fișierul config.json care conține chei API sau date confidențiale ar trebui ignorat în proiect. Adăugați la fișierul .gitignore o linie de cod care asigură acest lucru.
Pe lângă cele menționate, sistemul pentru versionare ar trebui să ignore și toate capturile de ecran pe care le facem, pentru a prezenta pașii intermediari instructorului cursului.
Rezultatul așteptat: config.json, precum și capturile de ecran, nu ar trebui să apară în lista fișierelor pregătite pentru urmărire și nici pe platforma GitHub.

Etapa 9: Pașii finali
Adăugați fișierul README.md:
Descrierea proiectului, clasele și funcționalitățile.
Folosiți Push pentru modificările de pe contul vostru GitHub.
