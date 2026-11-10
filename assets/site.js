(function () {
  var KW = new Set(("import from as def return for in if else elif not and or is lambda with class " +
    "None True False try except while pass yield raise").split(" "));
  function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function highlight(src) {
    var re = /(#[^\n]*)|(f?"(?:[^"\\]|\\.)*"|f?'(?:[^'\\]|\\.)*')|(\b\d+(?:\.\d+)?\b)|([A-Za-z_][A-Za-z0-9_]*)|([=<>!+\-*\/]=?)|([\s\S])/g;
    var out = "", m;
    while ((m = re.exec(src))) {
      if (m[1]) out += '<span class="tk-com">' + esc(m[1]) + "</span>";
      else if (m[2]) out += '<span class="tk-str">' + esc(m[2]) + "</span>";
      else if (m[3]) out += '<span class="tk-num">' + m[3] + "</span>";
      else if (m[4]) {
        var w = m[4], rest = src.slice(re.lastIndex).match(/^\(/);
        if (KW.has(w)) out += '<span class="tk-kw">' + w + "</span>";
        else if (rest) out += '<span class="tk-fn">' + w + "</span>";
        else out += esc(w);
      }
      else if (m[5]) out += '<span class="tk-op">' + esc(m[5]) + "</span>";
      else out += esc(m[6]);
    }
    return out;
  }
  document.querySelectorAll("pre code.py").forEach(function (el) {
    el.innerHTML = highlight(el.textContent);
  });
  document.querySelectorAll(".copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var code = btn.closest(".code-inner").querySelector("pre");
      var text = code.textContent;
      function selectIt() {
        var r = document.createRange(); r.selectNodeContents(code);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        btn.textContent = "selected";
      }
      try {
        navigator.clipboard.writeText(text).then(function () { btn.textContent = "copied"; }, selectIt);
      } catch (e) { selectIt(); }
      setTimeout(function () { btn.textContent = "copy"; }, 1600);
    });
  });
})();
