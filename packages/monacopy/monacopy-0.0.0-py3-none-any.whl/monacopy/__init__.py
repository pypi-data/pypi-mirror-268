import os,sys,mystring
from jinja2 import Environment, BaseLoader

raw_html_template = content = """

<html>
<body>
    <div id="container" style="width:1280px;height:1020px;"></div>
    <script src="https://requirejs.org/docs/release/2.3.5/minified/require.js"></script>
    <script src="https://unpkg.com/monaco-editor@latest/min/vs/loader.js"></script>
    <script>const source_value=`{{ source_code }}`;</script>
    <div id="svg"></div>
    <!-- You can access to the editor instance via module rocher_editor followed by the container id -->
    <script>
    let patternCount = 0;



let htmlToSvgConfig = {
  downloadSvg: true,
  downloadPng: false,
  filename: "htmlsvg",
  convertDataUrl: false,
};

const toDataURL = (url) =>
  fetch(url)
    .then((response) => response.blob())
    .then(
      (blob) =>
        new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.onloadend = () => resolve(reader.result);
          reader.onerror = reject;
          reader.readAsDataURL(blob);
        })
    );

function addBackground(defs, svgElement, htmlElement, convertDataUrl) {
  let style = window.getComputedStyle(htmlElement);
  let imageProp = getBackgroundProp(style);

  var pattern = document.createElementNS(
    "http://www.w3.org/2000/svg",
    "pattern"
  );
  const svgImage = document.createElementNS(
    "http://www.w3.org/2000/svg",
    "image"
  );
  pattern.id = "pattern" + patternCount;
  patternCount++;
  pattern.setAttribute("patternUnits", "userSpaceOnUse");
  pattern.setAttribute("height", imageProp.height);
  pattern.setAttribute("width", imageProp.width);

  svgImage.setAttribute("height", imageProp.height);
  svgImage.setAttribute("width", imageProp.width);

  if (convertDataUrl) {
    toDataURL(imageProp.src).then((dataUrl) => {
      svgImage.setAttribute("href", dataUrl);
    });
  } else {
    svgImage.setAttribute("href", imageProp.src);
  }
  svgImage.setAttribute("x", svgElement.getAttribute("x"));
  svgImage.setAttribute("y", svgElement.getAttribute("y"));
  pattern.appendChild(svgImage);
  svgElement.setAttribute("fill", "url(#" + pattern.id + ")");
  defs.appendChild(pattern);
}

function htmlToSvg(mainDiv, config = htmlToSvgConfig) {
  var mainStyle = window.getComputedStyle(mainDiv);
  var mainDivPosition = mainDiv.getBoundingClientRect();
  let width = mainDiv.offsetWidth;
  let height = mainDiv.offsetHeight;
  var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  var defs = document.createElementNS("http://www.w3.org/2000/svg", "defs");
  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("xmlns:xlink", "http://www.w3.org/1999/xlink");
  svg.classList = mainDiv.classList;
  svg.style = mainDiv.style;
  svg.id = "svg";
  svg.setAttribute("width", width);
  svg.setAttribute("height", height);

  if (mainStyle.backgroundImage !== "none") {
    const svgRect = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "rect"
    );
    svgRect.setAttribute("x", "0");
    svgRect.setAttribute("y", "0");
    svgRect.setAttribute("width", width);
    svgRect.setAttribute("height", height);

    addBackground(defs, svgRect, mainDiv, config.convertDataUrl);

    svg.appendChild(svgRect);
  }

  const elements = findAllChilds(mainDiv);
  for (var i = 1; i < elements.length; i++) {
    const htmlElement = elements[i];
    var style = window.getComputedStyle(htmlElement);
    var elementPosition = htmlElement.getBoundingClientRect();
    let svgElement = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "rect"
    );
    let svgText;
    if (svgElement.classList) {
      svgElement.classList = htmlElement.classList;
    }
    copyNodeStyle(htmlElement, svgElement);

    var position = htmlElement.getBoundingClientRect();
    var x = parseInt(position.left) - parseInt(mainDivPosition.left);
    var y = parseInt(position.top) - parseInt(mainDivPosition.top);

    let width = parseInt(elementPosition.width);
    let height = parseInt(elementPosition.height);
    svgElement.setAttribute("width", width);
    svgElement.setAttribute("height", height);
    svgElement.setAttribute("x", x);
    svgElement.setAttribute("y", y);
    // if div has a background image then create a image pattern
    if (style.backgroundImage !== "none") {
      addBackground(defs, svgElement, htmlElement, config.convertDataUrl);

      svgElement.style.backgroundImage = style.backgroundImage;
    } else if (style.backgroundColor) {
      svgElement.setAttribute("fill", style.backgroundColor);
    } else if (htmlElement.tagName == "DIV") {
      svgElement.setAttribute("fill-opacity", 0);
    }
    switch (htmlElement.tagName.toUpperCase()) {
      case "IMG":
        let svgImage = document.createElementNS(
          "http://www.w3.org/2000/svg",
          "image"
        );
        if (config.convertDataUrl) {
          toDataURL(htmlElement.src).then((dataUrl) => {
            svgImage.setAttribute("href", dataUrl);
          });
        } else {
          svgImage.setAttribute("href", htmlElement.src);
        }
        svgImage.setAttribute("width", width);
        svgImage.setAttribute("height", height);
        svgImage.setAttribute("x", x);
        svgImage.setAttribute("y", y);
        svgElement = svgImage;
        break;
      case "P":
      case "H3":
      case "H1":
      case "H2":
      case "H4":
      case "H5":
      case "SPAN":
      case "TD":
      case "TH":
      case "BUTTON":
        svgText = document.createElementNS(
          "http://www.w3.org/2000/svg",
          "text"
        );
        svgText.innerHTML = htmlElement.innerHTML;
        svgText.setAttribute("fill", style.color);
        svgText.setAttribute("font-family", style.fontFamily);
        svgText.setAttribute("font-size", style.fontSize);
        svgText.setAttribute("font-stretch", style.fontStretch);
        svgText.setAttribute("font-size-adjust", style.fontSizeAdjust);
        svgText.setAttribute("font-variant", style.fontVariant);
        svgText.setAttribute("font-weight", style.fontWeight);
        x += parseInt(style.paddingLeft.slice(0, -2));
        y +=
          parseInt(style.paddingTop.slice(0, -2)) +
          parseInt(style.fontSize.slice(0, -2)) -
          2;

        svgText.setAttribute("x", x);
        svgText.setAttribute("y", y);

        break;
      default:
        break;
    }
    svg.appendChild(svgElement);

    if (svgText) {
      svg.appendChild(svgText);
    }
  }
  svg.appendChild(defs);
  if (config.downloadSvg) {
    downloadSvg(svg, config.filename);
  }
  if (config.downloadPng) {
    downloadPng(svg, config.filename);
  }
  return svg;
}
function downloadPng(svg, filename) {
  var svgData = new XMLSerializer().serializeToString(svg);
  var canvas = document.createElement("canvas");
  var ctx = canvas.getContext("2d");

  canvas.width = svg.getAttribute("width");
  canvas.height = svg.getAttribute("height");
  var img = document.createElement("img");
  img.setAttribute("src", "data:image/svg+xml;base64," + btoa(svgData));
  var link = document.createElement("a");
  link.download = filename + ".png";
  img.onload = function () {
    ctx.drawImage(img, 0, 0);
    // Now is done
    link.href = canvas.toDataURL("image/png");
    link.click();
  };
}
function findAllChilds(div) {
  const elements = [];
  function _findAllChilds(_div) {
    elements.push(_div);
    if (_div.hasChildNodes()) {
      var searchEles = _div.children;
      for (var i = 0; i < searchEles.length; i++) {
        _findAllChilds(searchEles[i]);
      }
    }
  }
  _findAllChilds(div);
  return elements;
}

function getBackgroundProp(style) {
  let prop;
  var src = style.backgroundImage
    .replace(/url\((['"])?(.*?)\1\)/gi, "$2")
    .split(",")[0];

  // I just broke it up on newlines for readability
  return new Promise((resolve) => {
    var image = new Image();
    image.src = src;
    image.onload = function () {
      var width = image.width,
        height = image.height;
      prop = { width, height, src };
      resolve(prop);
    };
  });
}

function downloadSvg(svg, filename) {
  //get svg source.
  var serializer = new XMLSerializer();
  var source = serializer.serializeToString(svg);

  // for ie
  if (window.navigator.msSaveBlob) {
    var blob = new Blob([source], {
      type: "data:image/svg+xml;charset=utf-8;",
    });
    window.navigator.msSaveOrOpenBlob(blob, filename + ".svg");
  } else {
    if (!source.match(/^<svg[^>]+xmlns="http\:\/\/www\.w3\.org\/2000\/svg"/)) {
      source = source.replace(
        /^<svg/,
        '<svg xmlns="http://www.w3.org/2000/svg"'
      );
    }
    if (!source.match(/^<svg[^>]+"http\:\/\/www\.w3\.org\/1999\/xlink"/)) {
      source = source.replace(
        /^<svg/,
        '<svg xmlns:xlink="http://www.w3.org/1999/xlink"'
      );
    }

    //add xml declaration
    source = '<?xml version="1.0" standalone="no"?>\r\n' + source;

    //convert svg source to URI data scheme.
    var url = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(source);

    var downloadLink = document.createElement("a");
    downloadLink.href = url;
    downloadLink.download = filename + ".svg";
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  }
}

function copyNodeStyle(sourceNode, targetNode) {
  var computedStyle = window.getComputedStyle(sourceNode);
  targetNode.style.opacity = computedStyle.opacity;
  targetNode.style.border = computedStyle.border;
}

        require.config({ paths: { 'vs': 'https://unpkg.com/monaco-editor@latest/min/vs'}});
        require(['vs/editor/editor.main'], function () {
            monaco.editor.defineTheme('myCustomTheme', {
                base: "vs",
                inherit: false,
                colors: {
                  "editor.background": "#ffffff",
                  "editor.foreground": "#0f2611",
                },
                rules: [
                  {
                        "foreground": "#c4908e",
                        "token": "string"
                  },
                  {
                        "foreground": "#f9d585",
                        "token": "type.identifier.js"
                  },
                  {
                        "foreground": "#ee9d5b",
                        "token": "number"
                  },
                  {
                        "foreground": "#cc4940",
                        "token": "keyword"
                  },
                  {
                        "foreground": "#c97f4a",
                        "token": "delimiter"
                  },
                  {
                        "foreground": "#945755",
                        "token": "identifier"
                  }
            ]
            
        });
        monaco.editor.setTheme("myCustomTheme");
        //https://microsoft.github.io/monaco-editor/playground.html?source=v0.47.0#example-customizing-the-appearence-scrollbars
        var editor = monaco.editor.create(document.getElementById('container'), {
        value: source_value,
        language: 'javascript',
        minimap: {
            enabled: false
        },
        lineNumbers: "off",
        scrollBeyondLastLine: false,
    	scrollbar: {
    		// Subtle shadows to the left & top. Defaults to true.
    		useShadows: false,
    
    		// Render vertical arrows. Defaults to false.
    		verticalHasArrows: false,
    		// Render horizontal arrows. Defaults to false.
    		horizontalHasArrows: false,
    
    		// Render vertical scrollbar.
    		// Accepted values: 'auto', 'visible', 'hidden'.
    		// Defaults to 'auto'
    		vertical: "hidden",
    		// Render horizontal scrollbar.
    		// Accepted values: 'auto', 'visible', 'hidden'.
    		// Defaults to 'auto'
    		horizontal: "hidden",
    	},
      });
        var myBinding = editor.addCommand(monaco.KeyCode.F9, function () {
            alert("F9 pressed!");
        });

    });

    window.onload = function(){
       setTimeout(loadAfterTime, 10000)
    };

    function loadAfterTime(){
               const svg= htmlToSvg(document.getElementById("container"), {
              downloadSvg: true,
              filename: "htmltosvg",
            });
           console.log(svg);
           var uriContent = "data:image/svg+xml;base64," + encodeURIComponent(svg);
           window.open(uriContent, '{{ filename }}');
    };
    </script>


</body>
</html>

""".strip()


def template_fron_string(string=raw_html_template):return Environment(loader=BaseLoader()).from_string(raw_html_template)

def render_template(source_code, svg_image_name="image.svg"):return template_fron_string(string=raw_html_template).render(source_code=source_code,filename=svg_image_name)

def render_template_to_file(file_out, source_code, svg_image_name="image.svg"):
    with open(file_out, "w+") as writer:
        writer.write(render_template(source_code=source_code, svg_image_name=svg_image_name))
    return file_out