# J@M — proposta di nuovo sito

Rifacimento della home di [jam-srl.it](https://www.jam-srl.it/) con gli stessi contenuti e le grafiche originali di J@M (logo, mascotte, isola, TV, pattern Mood, opera del Museo), ripulite e alleggerite.

- Un solo file `index.html` + cartella `assets/` (immagini WebP). Nessuna dipendenza oltre ai font Google e al player Vimeo dentro la TV.
- Titolo "Testa, cuore e spirito d'iniziativa" fatto di particelle (Canvas): esplode e si ricompone; un clic lo fa esplodere.
- L'isola emerge dal mare mentre scorri; il Museo si accende avvicinandosi.
- Per aggiornare il sito: modifica `index.html`, commit e push su `main`. GitHub Pages lo pubblica da solo (workflow in `.github/workflows/pages.yml`).
- L'indirizzo a cui arrivano le richieste del modulo è la costante `CONTACT_EMAIL` in fondo a `index.html`.
