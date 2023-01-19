# API data

- [] extend dane z api (niech pobiera wiecej informacji i niech nie łączy stock'a z crypto, niech to beda osobne strony tak jak w figmie)
  > postman?

# Table

1. - [x] tabela, filtry i searchbox (biblioteka!)
2. - [x] buttony do tabeli, <make update> javascript async ajax [interval 10 sec, 1 time call]
     > [link](https://openbase.com/categories/python/best-django-table-packages?vs=django-jinja-knockout%2Cdjango-ajax-datatable%2Cdjango-tables2)
3. - [] grid zamiast tabeli
     > <!-- TODO rozwiaznie obrazkow i propertisow w tabeli -->
     >
     > [link](https://stackoverflow.com/questions/9961046/django-template-displaying-images-in-table)

# Component: Calculator

- [x] Łapać dane z modelu do java'scriptu i stworzyć kontrolowalny komponent
  > https://www.geeksforgeeks.org/how-to-pass-data-to-javascript-in-django-framework/

# Layout

## Alerts

- [] alerts (fixme, wiecej niz jeden na raz javascript!)
- [] alerts (translacja z pl na ang)

## Topappbar

- [] topappbar na '/log_in' gdy użytkownik jest na podstronie /log_in to wygląda inaczej

===WOJTEK===

## Navbar

- [] navbar
  (to nie jest filter, tylko nawigacja routes '/crypto' lub '/stock', defaultowo po zalogowaniu wrzuca w jedno albo drugie. Obie podstrony mają swoją własną przestrzeń na tabele (mają inne pola, dlatego separation of concerns))

===FILIP===

# django routing

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
