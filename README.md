# J@M — proposta di nuovo sito

Proposta di home page moderna per [jam-srl.it](https://www.jam-srl.it/): un solo file `index.html`, nessuna dipendenza oltre ai font Google.

- Titolo animato con particelle (Canvas), capitoli guidati dallo scroll, galleria servizi, modulo contatti.
- Per aggiornare il sito: modifica `index.html`, commit e push su `main`. GitHub Pages lo pubblica da solo (workflow in `.github/workflows/pages.yml`).
- L'indirizzo a cui arrivano le richieste del modulo è la costante `CONTACT_EMAIL` in fondo a `index.html`.
