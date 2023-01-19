# **WOJTEK**

## Table

- [] grid zamiast tabeli
  > <!-- TODO rozwiaznie obrazkow i propertisow w tabeli -->
  >
  > [link](https://stackoverflow.com/questions/9961046/django-template-displaying-images-in-table)

---

# **FILIP**

## select django

w zależności od tego jaki jest model wyswietlanny (all/crypto/stock) to tylko takie opcje select

## podać odpowiednia zmienna do modelu kalkulatora dla przedmiotu typu 'stock'

## django routing

- [] django forbidden route / 404 / _any_
  > (może przekierowywać na poprawną stronę w zależności od (USER_STATE), jak wejdziesz na złą podstrone to przekierowuje na 404)

enum USER_STATE {
LOGGED_OUT
LOGGED_IN
}

<!-- TODO: Change route names -->

enum LOGGED*OUT_PAGES {
/log_in
/about
/\_any* (redirect -> /log_in)
}

enum LOGGED*IN_PAGES {
/logout
/about (/authors)
/\_any* (redirect -> /crypto)
/crypto
/stock
/crypto/:id
/stock/:id
}

> USER_STATE = LOGGED_IN
> fn log_in (redirect -> crypto)
