# Cкрипт для увеличения изображений в документации

В проект документации PFLB Platform добавил:

- библиотека [medium-zoom](https://github.com/francoischalifour/medium-zoom);
- скрипт для увеличения изображений:

	```js
	// Add zoom to images.
	(() => {
	  mediumZoom(".main .content img:not(.inline-img, .no-zoom)", {
	    margin: 24,
	    background: '#000000b0',
	  });
	})();
	```

В HTML-документации увеличиваются все изображения, кроме тех, что отмечены классами:

- `.inline-img`. Inline-изображения кнопок;
- `.no-zoom`. Небольшие скриншоты, которые нет смысла увеличивать.

Пример реализации можно посмотреть на [странице документации PFLB Platform](https://pflb.us/docs/en/test-creation/).
