```py
import jfcarter2358.sidebar
import jfcarter2358.head
import jfcarter2358.header
import jfcarter2358.theme
import jfcarter2358.page_darken
```

```yaml
title: floorplan Test
color: '#A3BE8C'
content: |
  <div class="card-container w3-container">
    <h2>Hello World!</h2>
  </div>
themes: 
  name: light
  base: theme-light
  border: theme-border-light
  text: theme-text
  table: theme-table-light
  hover: theme-hover-text-dark
```

```html
<!doctype html>
<html style="height:100%;min-height:100%;">
  <head>
    <jfcarter2358.head>
        title: ${{ title }}
    </jfcarter2358.head>
    <!-- add custom css -->
    <link rel="stylesheet" type="text/css" href="../static/css/index.css">
    <!-- add javascript -->
    <script src="../static/js/index.js"></script>
  </head>
  <body class="light theme-base">
    <jfcarter2358.sidebar>
      color: "${{ color }}"
      themes: 
        name: ${{ themes.name }}
        base: ${{ themes.base }}
        border: ${{ themes.border }}
        table: ${{ themes.table }}
    </jfcarter2358.sidebar>
    <div class="main">
        <jfcarter2358.header>
          color: "${{ color }}"
          title: ${{ title }}
          themes: 
            name: ${{ themes.name }}
            base: ${{ themes.base }}
            border: ${{ themes.border }}
            text: ${{ themes.text }}
            hover: ${{ themes.hover }}
        </jfcarter2358.header>
      <div class="contents w3-container">
        <br>
        ${{ content }}
        <br>
      </div>
      <jfcarter2358.page_darken>
      </jfcarter2358.page_darken>
      <jfcarter2358.theme>
      </jfcarter2358.theme>
    </div>
  </body>
</html>
```

```css
.card-container {
    height: 90%;
    min-height: 90%;
}
```
