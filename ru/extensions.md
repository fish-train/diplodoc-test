# Внедрение расширений Sphinx

Экспериментировал со следующими расширениями:

- [sphinx-reredirects](https://github.com/documatt/sphinx-reredirects). Позволяет настроить редиректы внутрипроекта. У меня расширенение не заработало;
- [redirects](https://github.com/sphinx-contrib/redirects). Позволяет настроить редиректы внутрипроекта. Расширение не работает с билдером dirhtml, который я использую;
- [sphinx_selective_exclude](https://github.com/pfalcon/sphinx_selective_exclude). Позволяет настроить условия сборки. Текущая реализация директивы only меня устраивает;
- [sphinx_cli_recorder](https://kai-tub.github.io/sphinx_cli_recorder/intro.html). Генерирует вывод команд в терминале. Не работает на Windows;
- [icon](https://github.com/sphinx-contrib/icon). Вставляет иконки из fontawesome, требует включения в проекте большой css-файл от fontawesome. Решил не использовать ради одной иконки для AI-отчетов. Также иконки можно добавить в sphinx-design, который я уже использую;
- [sphinx-lint](https://github.com/sphinx-contrib/sphinx-lint). Проверяет синтаксис в RST-файлах. Добавил скрипт для запуска првоерки.
- [spelling](https://github.com/sphinx-contrib/spelling). Проверяет орфографию, но использовать в терминале неудобно. Проверяю орфографию средствами Sublime, VS Code и CSpell.
