/* J@M — solo home: titolo di particelle sopra l'opera di Escher, sipario di Vettriano, isola che emerge */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isMobile = window.matchMedia("(max-width: 700px)").matches;
  var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
  var ease = function (t) { return t < 0 ? 0 : t > 1 ? 1 : 1 - Math.pow(1 - t, 3); };

  /* ---------- Titolo di particelle ---------- */
  var LINES = ["TESTA, CUORE", "E SPIRITO", "D'INIZIATIVA"];
  var PALETTE = ["#FF2D4A", "#D82E00", "#FF6A00", "#FFB300", "#FFF1E0"];
  var WEIGHTS = [0.30, 0.26, 0.24, 0.13, 0.07];
  var hero = document.getElementById("home"), canvas = document.getElementById("heroCanvas"), slot = document.getElementById("wordSlot");
  if (!hero || !canvas || !slot) return;
  var ctx = canvas.getContext("2d");
  var off = document.createElement("canvas"), octx = off.getContext("2d", { willReadFrequently: true });
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, N = isMobile ? 2200 : 4200, STEP = isMobile ? 3 : 5, SIZE = isMobile ? 1.7 : 2.2;
  var parts = [], mouse = { x: -9999, y: -9999 };
  var state = "form", stateT = 0, running = true, raf = 0, ready = false;
  var HOLD = 4200, FORM = 1400, EXPLODE = 850;

  function pickColor() { var r = Math.random(), acc = 0; for (var i = 0; i < WEIGHTS.length; i++) { acc += WEIGHTS[i]; if (r <= acc) return i; } return 0; }
  function resize() {
    var r = hero.getBoundingClientRect(); W = Math.max(1, Math.round(r.width)); H = Math.max(1, Math.round(r.height));
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
  }
  function sample() {
    var s = slot.getBoundingClientRect(), hr = hero.getBoundingClientRect();
    var maxW = Math.max(40, s.width), maxH = Math.max(60, s.height), lineH = maxH / LINES.length, fs = lineH * 0.9;
    off.width = Math.ceil(maxW); off.height = Math.ceil(maxH);
    var font = function (px) { return "800 " + px + "px Geist, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"; };
    octx.font = font(fs);
    var widest = 0; LINES.forEach(function (l) { widest = Math.max(widest, octx.measureText(l).width); });
    if (widest > maxW * 0.96) { fs = fs * (maxW * 0.96 / widest); octx.font = font(fs); }
    octx.clearRect(0, 0, off.width, off.height); octx.fillStyle = "#fff"; octx.textBaseline = "alphabetic";
    LINES.forEach(function (l, i) { var w = octx.measureText(l).width; octx.fillText(l, Math.round((maxW - w) / 2), Math.round(lineH * i + lineH * 0.82)); });
    var d = octx.getImageData(0, 0, off.width, off.height).data, pts = [];
    var ox = s.left - hr.left, oy = s.top - hr.top;
    for (var y = 0; y < off.height; y += STEP) for (var x = 0; x < off.width; x += STEP) if (d[(y * off.width + x) * 4 + 3] > 120) pts.push(x + ox, y + oy);
    return pts;
  }
  function makeParts() { parts = []; for (var i = 0; i < N; i++) parts.push({ x: Math.random() * W, y: Math.random() * H, vx: 0, vy: 0, tx: 0, ty: 0, c: pickColor(), s: SIZE, a: 1, dust: false }); }
  function assign() {
    var pts = sample(), n = pts.length / 2, k = Math.max(1, Math.ceil(n / N));
    for (var i = 0; i < N; i++) {
      var p = parts[i], idx = (i * k) % n;
      if (i * k < n) { p.tx = pts[idx * 2] + (Math.random() - .5); p.ty = pts[idx * 2 + 1] + (Math.random() - .5); p.dust = false; p.s = SIZE; p.a = 1; }
      else { p.tx = Math.random() * W; p.ty = Math.random() * H; p.dust = true; p.s = SIZE * 0.55; p.a = 0.22; }
    }
  }
  function explode() {
    var cx = 0, cy = 0, n = 0, i, p;
    for (i = 0; i < N; i++) if (!parts[i].dust) { cx += parts[i].x; cy += parts[i].y; n++; }
    cx /= (n || 1); cy /= (n || 1);
    for (i = 0; i < N; i++) {
      p = parts[i]; var dx = p.x - cx, dy = p.y - cy, d = Math.sqrt(dx * dx + dy * dy) || 1, f = p.dust ? 1.5 : (6 + Math.random() * 15);
      p.vx = (dx / d) * f + (Math.random() - .5) * 7; p.vy = (dy / d) * f + (Math.random() - .5) * 7;
    }
    state = "explode"; stateT = performance.now();
  }
  function step(now) {
    if (!running) return; raf = requestAnimationFrame(step);
    if (state === "form" && now - stateT > FORM) { state = "hold"; stateT = now; }
    else if (state === "hold" && now - stateT > HOLD && !reduce) explode();
    else if (state === "explode" && now - stateT > EXPLODE) { assign(); state = "form"; stateT = now; }
    ctx.globalCompositeOperation = "destination-out";
    ctx.fillStyle = state === "explode" ? "rgba(0,0,0,0.22)" : "rgba(0,0,0,0.45)"; ctx.fillRect(0, 0, W, H);
    ctx.globalCompositeOperation = "lighter";
    var mx = mouse.x, my = mouse.y, R = 120, R2 = R * R, i, p;
    for (i = 0; i < N; i++) {
      p = parts[i];
      if (state === "explode") { p.vx *= 0.955; p.vy *= 0.955; p.x += p.vx; p.y += p.vy; }
      else {
        var k = p.dust ? 0.02 : 0.08;
        p.vx = (p.vx + (p.tx - p.x) * k) * 0.76; p.vy = (p.vy + (p.ty - p.y) * k) * 0.76;
        if (state === "hold" && !p.dust) { p.vx += (Math.random() - .5) * 0.45; p.vy += (Math.random() - .5) * 0.45; }
        var dx = p.x - mx, dy = p.y - my, d2 = dx * dx + dy * dy;
        if (d2 < R2) { var d = Math.sqrt(d2) || 1, f = (R - d) / R * 4.5; p.vx += (dx / d) * f; p.vy += (dy / d) * f; }
        p.x += p.vx; p.y += p.vy;
      }
    }
    for (var c = 0; c < PALETTE.length; c++) { ctx.fillStyle = PALETTE[c]; for (i = 0; i < N; i++) { p = parts[i]; if (p.c !== c) continue; ctx.globalAlpha = p.a; ctx.fillRect(p.x, p.y, p.s, p.s); } }
    ctx.globalAlpha = 1;
  }
  function start() { resize(); makeParts(); assign(); state = "form"; stateT = performance.now(); ready = true; if (!raf) raf = requestAnimationFrame(step); }
  hero.addEventListener("pointermove", function (e) { var r = hero.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
  hero.addEventListener("pointerleave", function () { mouse.x = -9999; mouse.y = -9999; });
  hero.addEventListener("click", function (e) { if (e.target.closest("a, button")) return; if (ready && state !== "explode") explode(); });
  var rT; window.addEventListener("resize", function () { clearTimeout(rT); rT = setTimeout(function () { if (ready) { resize(); assign(); } }, 150); });
  function setRun(on) { running = on; if (on && ready && !raf) raf = requestAnimationFrame(step); if (!on) { cancelAnimationFrame(raf); raf = 0; } }
  new IntersectionObserver(function (en) { setRun(en[0].isIntersecting && !document.hidden); }).observe(hero);
  document.addEventListener("visibilitychange", function () { setRun(!document.hidden); });
  var fontsReady = (document.fonts && document.fonts.load) ? document.fonts.load("800 100px Geist") : Promise.resolve();
  var started = false; function once() { if (!started) { started = true; start(); } }
  fontsReady.then(once, once); setTimeout(once, 1800);

  /* ---------- Scene guidate dallo scroll ---------- */
  var curtain = document.getElementById("curtain"), isolaSec = document.getElementById("isola"), isolaArt = document.getElementById("isolaArt");
  function progress(sec) { var r = sec.getBoundingClientRect(), vh = window.innerHeight; return clamp(-r.top / (r.height - vh), 0, 1); }
  var t0 = performance.now();
  function scene(now) {
    requestAnimationFrame(scene);
    var vh = window.innerHeight;
    if (curtain) {
      var r = curtain.getBoundingClientRect();
      var o = ease(clamp((vh * 0.9 - r.top) / (vh * 0.7), 0, 1));
      curtain.style.setProperty("--open", o);
    }
    if (isolaSec && isolaArt) {
      var p = progress(isolaSec), e = ease(clamp(p / 0.6, 0, 1));
      var bob = Math.sin((now - t0) / 900) * 6 * e;
      isolaArt.style.transform = "translateY(" + ((1 - e) * vh * 0.75 + bob) + "px) scale(" + (0.85 + e * 0.15) + ")";
    }
  }
  if (reduce) {
    if (curtain) curtain.style.setProperty("--open", 1);
    if (isolaArt) isolaArt.style.transform = "none";
    document.querySelectorAll(".pin").forEach(function (s) { s.style.height = "auto"; }); document.querySelectorAll(".pin .stage").forEach(function (s) { s.style.position = "relative"; s.style.height = "auto"; s.style.paddingBlock = "120px"; });
  } else requestAnimationFrame(scene);
})();
