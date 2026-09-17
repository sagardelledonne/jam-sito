# J@M — nuovo sito

Rifacimento completo di [jam-srl.it](https://www.jam-srl.it/) con gli stessi contenuti, le stesse pagine (stessi indirizzi) e le grafiche originali di J@M: logo, mascotte, illustrazioni della ragazza dai capelli rossi, le sedi, e le opere del Museo J@M (Escher, Vettriano, Magritte, Botticelli, Lichtenstein, Yerka, Amano…).

## Come è fatto
- `build.py` contiene **tutti i testi** delle pagine e genera i file `index.html` (home + 18 pagine interne).
- `assets/site.css` e `assets/site.js` sono lo stile e le animazioni comuni; `assets/home.js` è solo per la home (titolo di particelle).
- `assets/img/` illustrazioni e opere (WebP), `assets/museo/` i 34 quadri, `assets/ig/` le foto Instagram.

## Come si aggiorna
1. Modifica il testo in `build.py` (o un'immagine in `assets/`).
2. Esegui `python build.py` (rigenera tutte le pagine).
3. Commit e push su `main`: GitHub Pages pubblica da solo (workflow `.github/workflows/pages.yml`).

Per usare un dominio proprio (es. jam-srl.it) basta mettere `BASE = ""` in `build.py` e rigenerare.

## Effetti
- Home: titolo "Testa, cuore e spirito d'iniziativa" fatto di particelle sopra *Giorno e notte* di Escher (clic = esplosione), sipario sul Vettriano, isola che emerge sopra *Convesso e concavo*, parete del Museo che scorre, Botticelli e Magritte come sfondi animati.
- Ogni pagina: opera d'arte con "faro" che segue il mouse e parallasse, ragazza dai capelli rossi che accompagna lo scroll e guarda verso il mouse, illustrazioni fluttuanti, frasi che si accendono parola per parola.
- Il modulo contatti apre la posta con la richiesta compilata (indirizzo in `CONTACT_EMAIL` dentro `assets/site.js`).
