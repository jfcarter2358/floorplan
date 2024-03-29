```py
require jfcarter2358.page_darken
import jfcarter2358.theme
import jfcarter2358.status
```

```yaml
title: floorplan Test
color: '#A3BE8C'
links:
    swagger: /swagger/index.html
themes:
    name: light
    base: theme-light
    border: theme-border-light
    table: theme-table-light
version: 0.1.0
items: |
    <a href="/ui/home" class="w3-bar-item w3-button light sidebar-hover w3-border-bottom theme-border-light">
        <i class="fa-solid fa-house"></i> Home
    </a>
```

```js
function toggleSidebar() {
    var sidebar = document.getElementById("sidebar")
    var page_darken = document.getElementById("page-darken")
    if (sidebar.className.indexOf("show") == -1) {
        sidebar.classList.add("show");
        sidebar.classList.remove("left-slide-out-300");
        void sidebar.offsetWidth;
        sidebar.classList.add("left-slide-in-300")
        $("#sidebar").css("left", "0px")

        page_darken.classList.remove("fade-out");
        void page_darken.offsetWidth;
        page_darken.classList.add("fade-in");
        $("#page-darken").css("opacity", "1")
    } else {
        sidebar.classList.remove("show");
        sidebar.classList.remove("left-slide-in-300");
        void sidebar.offsetWidth;
        sidebar.classList.add("left-slide-out-300")
        $("#sidebar").css("left", "-300px")

        page_darken.classList.remove("fade-in");
        void page_darken.offsetWidth;
        page_darken.classList.add("fade-out");
        $("#page-darken").css("opacity", "0")
    }
}
```

```html
<div class="w3-sidebar w3-bar-block w3-card w3-border ${{ themes.name }} ${{ themes.border }} ${{ themes.base }} sidebar" id="sidebar" style="z-index:996;left:-300px;">
    <div class="w3-container w3-border-bottom sidebar-color w3-container sidebar-header">
        <div class="w3-large w3-container w3-cell w3-cell-middle w3-left-align default-cursor sidebar-item">
            <i class="fa-solid fa-bars w3-large" onclick="toggleSidebar()"></i>
        </div>
        <div class="w3-large w3-container w3-cell w3-cell-middle w3-left-align sidebar-item">
            <h3>${{ title }}</h3>
        </div>
    </div>
    ${{ items }}
    <div class="w3-border-top ${{ themes.border }} w3-container sidebar-copyright" style="position:absolute;bottom:0px;">
        &copy; 2023 John Carter ${{ version }}
        <i class="fa-solid fa-palette w3-right sidebar-theme sidebar-text-green" onclick="toggleTheme()" id="theme-button"></i>
        <i class="fa-solid fa-circle-question w3-right sidebar-theme sidebar-text-green" onclick="showStatus()" id="status-icon" style="margin-right:8px;"></i>
        <a class="fa-solid fa-book w3-right sidebar-theme sidebar-text-green" href="${{ links.swagger }}" id="docs-icon" style="margin-right:8px;"></a>
    </div>
</div>
<jfcarter2358.status>
color: "${{ color }}"
themes:
    name: ${{ themes.name }}
    base: ${{ themes.base }}
    border: ${{ themes.border }}
    table: ${{ themes.table }}
</jfcarter2358.status>
```

```css
.sidebar-color,.sidebar-hover:hover{color:#fff!important;background-color:${{ color }}!important}
.sidebar-text,.sidebar-hover-text:hover{color:${{ color }}!important}
.sidebar-border,.sidebar-hover-border:hover{border-color:${{ color }}!important}

.sidebar-item {
    margin-left: 4px;
    padding-left: 0px;
}

.sidebar-end {
    height: 5px;
    width: 100%;
}

.sidebar {
    width:300px;
    display:block;
    left:-300px;
    z-index: 999;
}

.sidebar-header {
    border:4px;
}

.sidebar-copyright {
    position:absolute;
    bottom:0px;
    width:100%;
    border:4px;
}

.sidebar-theme {
    cursor:pointer;
    margin-top:4px;
}

.left-slide-in-300 {
    animation-duration: 0.5s;
    animation-name: slide-in-left-300;
}

.left-slide-out-300 {
    animation-duration: 0.5s;
    animation-name: slide-out-left-300;
}

@keyframes slide-in-left-300 {
    from {
        left: -300px;
    }

    to {
        left: 0px;
    }
}

@keyframes slide-out-left-300 {
    from {
        left: 0px;
    }

    to {
        left: -300px;
    }
}

.right-slide-in-500 {
    animation-duration: 0.5s;
    animation-name: slide-in-right-500;
}

.right-slide-out-500 {
    animation-duration: 0.5s;
    animation-name: slide-out-right-500;
}

@keyframes slide-out-right-500 {
    from {
        left: calc(100% - 500px);
    }

    to {
        left: calc(100%);
    }
}

@keyframes slide-in-right-500 {
    from {
        left: calc(100%);
    }

    to {
        left: calc(100% - 500px);
    }
}

.right-slide-in-1000 {
    animation-duration: 0.5s;
    animation-name: slide-in-right-1000;
}

.right-slide-out-1000 {
    animation-duration: 0.5s;
    animation-name: slide-out-right-1000;
}

@keyframes slide-out-right-1000 {
    from {
        left: calc(100% - 1000px);
    }

    to {
        left: calc(100%);
    }
}

@keyframes slide-in-right-1000 {
    from {
        left: calc(100%);
    }

    to {
        left: calc(100% - 1000px);
    }
}

.fade-in {
    animation: fadeIn 0.5s;
    -webkit-animation: fadeIn 0.5s;
    -moz-animation: fadeIn 0.5s;
    -o-animation: fadeIn 0.5s;
    -ms-animation: fadeIn 0.5s;
}

.fade-out {
    animation: fadeOut 0.5s;
    -webkit-animation: fadeOut 0.5s;
    -moz-animation: fadeOut 0.5s;
    -o-animation: fadeOut 0.5s;
    -ms-animation: fadeOut 0.5s;
}

@keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}

@-moz-keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}

@-webkit-keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}

@-o-keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}

@-ms-keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}

@keyframes fadeOut {
    0% {opacity:1;}
    100% {opacity:0;}
}

@-moz-keyframes fadeOut {
    0% {opacity:1;}
    100% {opacity:0;}
}

@-webkit-keyframes fadeOut {
    0% {opacity:1;}
    100% {opacity:0;}
}

@-o-keyframes fadeOut {
    0% {opacity:1;}
    100% {opacity:0;}
}

@-ms-keyframes fadeOut {
    0% {opacity:1;}
    100% {opacity:0;}
}
```
