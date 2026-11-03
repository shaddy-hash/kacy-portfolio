(function () {
  "use strict";

  /* ---------- mobile menu (disclosure pattern) ---------- */
  var btn = document.querySelector(".menu-button");
  var list = document.getElementById("main-nav");
  if (btn && list) {
    var label = btn.querySelector(".menu-text");
    function setOpen(open, returnFocus) {
      btn.setAttribute("aria-expanded", String(open));
      list.classList.toggle("is-open", open);
      if (label) label.textContent = open ? "Close" : "Menu";
      if (!open && returnFocus) btn.focus();
    }
    btn.addEventListener("click", function () {
      setOpen(btn.getAttribute("aria-expanded") !== "true");
    });
    list.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && btn.getAttribute("aria-expanded") === "true") setOpen(false, true);
    });
    document.addEventListener("click", function (e) {
      if (btn.getAttribute("aria-expanded") === "true" && !e.target.closest(".site-header")) setOpen(false);
    });
  }

  /* ---------- print button ---------- */
  var pb = document.querySelector("[data-print]");
  if (pb) pb.addEventListener("click", function () { window.print(); });

  /* ---------- table of contents: mark the section in view ---------- */
  var tocLinks = [].slice.call(document.querySelectorAll(".toc a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove("is-current"); a.removeAttribute("aria-current"); });
          var a = map[en.target.id];
          if (a) { a.classList.add("is-current"); a.setAttribute("aria-current", "location"); }
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    Object.keys(map).forEach(function (id) { var s = document.getElementById(id); if (s) io.observe(s); });
  }

  /* ---------- image viewer (native <dialog>) ---------- */
  var dialog = document.querySelector(".viewer");
  var zooms = [].slice.call(document.querySelectorAll(".zoom"));
  if (!dialog || !zooms.length || typeof dialog.showModal !== "function") {
    zooms.forEach(function (z) {
      z.addEventListener("click", function () { window.open(z.getAttribute("data-src"), "_blank"); });
    });
    return;
  }
  var vImg = dialog.querySelector("img");
  var vCap = dialog.querySelector("figcaption");
  var vCount = dialog.querySelector(".viewer-count");
  var idx = 0, opener = null;

  function render() {
    var z = zooms[idx];
    vImg.src = z.getAttribute("data-src");
    vImg.alt = z.getAttribute("data-alt");
    vCap.textContent = z.getAttribute("data-caption");
    vCount.textContent = "Image " + (idx + 1) + " of " + zooms.length;
  }
  function open(i) {
    idx = i; opener = zooms[i]; render();
    dialog.showModal();
    document.body.classList.add("viewer-open");
    dialog.querySelector("[data-close]").focus();
  }
  function step(d) { idx = (idx + d + zooms.length) % zooms.length; render(); }

  zooms.forEach(function (z, i) { z.addEventListener("click", function () { open(i); }); });
  dialog.querySelector("[data-close]").addEventListener("click", function () { dialog.close(); });
  dialog.querySelector("[data-prev]").addEventListener("click", function () { step(-1); });
  dialog.querySelector("[data-next]").addEventListener("click", function () { step(1); });
  dialog.addEventListener("close", function () {
    document.body.classList.remove("viewer-open");
    if (opener) opener.focus();
  });
  dialog.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") { e.preventDefault(); step(-1); }
    if (e.key === "ArrowRight") { e.preventDefault(); step(1); }
  });
  dialog.addEventListener("click", function (e) {
    if (e.target === dialog || e.target.classList.contains("viewer-figure")) dialog.close();
  });
  var sx = null;
  dialog.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
  dialog.addEventListener("touchend", function (e) {
    if (sx === null) return;
    var dx = e.changedTouches[0].clientX - sx;
    if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1);
    sx = null;
  });
})();
