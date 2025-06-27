# Кликабельная иконка поиска

В проекте документации PFLB Platform реализовал кнопку поиска как input. Ранее она была добавлена как псевдоэлемент before:

```html
<div class="sidebar-tree">
  <form class="sidebar-search-container" method="get" action="{{ pathto('search') }}" role="search">
    <input class="sidebar-search" placeholder="{{ _("Find a solution") }}" name="q" aria-label="{{ _("Search" ) }}">
    <input type="hidden" name="check_keywords" value="yes">
    <input type="hidden" name="area" value="default">
    <input type="submit" class="search-icon">
  </form>
  <div id="searchbox"></div>
  {{ furo_navigation_tree }}
</div>
```
И добавил настройки кнопки в CSS-файл:

```css
.search-icon{
    z-index: 20;
    right: 15px;
    background-color: var(--color-sidebar-search-icon);
    height: var(--sidebar-search-icon-size);
    -webkit-mask-image: var(--icon-search);
    mask-image: var(--icon-search);
    position: absolute;
    width: var(--sidebar-search-icon-size);
    cursor: pointer;
}
```
