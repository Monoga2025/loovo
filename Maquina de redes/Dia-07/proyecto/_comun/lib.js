// ===== lib común Loovo (blanco pastel + dorado suave). Helpers de la composición: tl GSAP pausada, tiempos en s de la línea. =====
const D = __DATA__;
const B = D.B;
const S = (id) => D.edl[id].start, EN = (id) => D.edl[id].end;
const F = 1 / 30, LEAD = 2 * F;
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const $ = (s) => document.querySelector(s);
const show = (s, t) => tl.set(s, { autoAlpha: 1 }, t);
const hide = (s, t) => tl.set(s, { autoAlpha: 0 }, t);
const inBlur = (s, t, d = 4 * F, px = 14) => tl.fromTo(s, { autoAlpha: 0, filter: `blur(${px}px)` }, { autoAlpha: 1, filter: "blur(0px)", duration: d, ease: "power2.out", immediateRender: false }, t);
const outUp = (s, t, d = 4 * F) => tl.to(s, { autoAlpha: 0, y: "-=50", filter: "blur(12px)", duration: d, ease: "power1.in" }, t);
const esc = (x) => x.replace(/&/g, "&amp;").replace(/</g, "&lt;");
const norm = (x) => x.toLowerCase().normalize("NFD").replace(/\p{Mn}/gu, "").replace(/[^a-z0-9]/g, "");
let seed = 7; const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
const R = (a, b) => a + (b - a) * rnd();
function at(id, w, n = 0) { const h = D.words[id].filter((x) => x[0] === norm(w)); if (!h.length) throw new Error("no " + w + " en " + id); return h[Math.min(n, h.length - 1)][1]; }
const ICON = (n) => `mask-image:url(assets/icons/${n}-fill.svg);-webkit-mask-image:url(assets/icons/${n}-fill.svg)`;
// título cinético: palabras en su sitio; entran a su tiempo (voz - 2 cuadros). ~x~ serif dorada, *x* clave, ^ visible en cuadro 0, palabra@t fuerza tiempo
function T(sel, lines, segs, o = {}) {
  const el = $(sel); const seq = [].concat(...[].concat(segs).map((s) => D.words[s])); let cur = Math.max(0, seq.findIndex((x) => x[1] >= (o.min || 0) - 0.3)), last = o.min || 0;
  const toks = []; let mode = "";
  el.innerHTML = lines.map((ln) => '<span class="ln">' + ln.split(" ").map((raw) => {
    let t = raw, open = mode, vis0 = false, forced = null;
    if (t.startsWith("^")) { vis0 = true; t = t.slice(1); }
    if (t.startsWith("~")) { mode = "s"; open = "s"; t = t.slice(1); } else if (t.startsWith("*")) { mode = "k"; open = "k"; t = t.slice(1); }
    let close = false; if (t.endsWith("~") || t.endsWith("*")) { close = true; t = t.slice(0, -1); }
    const m = t.match(/^(.*)@([\d.]+)$/); if (m) { t = m[1]; forced = +m[2]; }
    const cls = open; if (close) mode = "";
    let when = forced;
    if (when === null) { const n = norm(t); for (let j = cur; j < Math.min(seq.length, cur + 8); j++) if (seq[j][0] === n) { when = seq[j][1]; cur = j + 1; break; } }
    if (when === null) when = last + 0.08;
    last = when; toks.push({ when, cls, vis0 });
    return `<span class="w${cls ? " " + cls : ""}">${esc(t)}</span>`;
  }).join(" ") + "</span>").join("");
  el.querySelectorAll(".w").forEach((sp, i) => {
    const k = toks[i]; if (k.vis0) { gsap.set(sp, { autoAlpha: 1 }); return; }
    gsap.set(sp, { autoAlpha: 0 }); const serif = k.cls === "s";
    tl.fromTo(sp, { autoAlpha: 0, y: 26, filter: "blur(10px)", scale: serif ? 0.6 : 1 },
      { autoAlpha: 1, y: 0, filter: "blur(0px)", scale: 1, duration: (serif ? 7 : 5) * F, ease: "power2.out", immediateRender: false }, Math.max(o.min || 0, k.when - LEAD));
  });
  return toks;
}
const rich = (t) => t.split("|").map((ln) => '<span class="ln">' + esc(ln).replace(/~([^~]+)~/g, '<span class="s">$1</span>').replace(/\*([^*]+)\*/g, '<span class="k">$1</span>') + "</span>").join("");
function card(text, t0, t1, cls = "") {
  const el = document.createElement("div"); el.className = "cap " + cls; el.innerHTML = rich(text); $("#caps").appendChild(el);
  gsap.set(el, { autoAlpha: 0 });
  tl.fromTo(el, { autoAlpha: 0, filter: "blur(8px)" }, { autoAlpha: 1, filter: "blur(0px)", duration: 2 * F, ease: "power2.out", immediateRender: false }, t0 - LEAD);
  tl.set(el, { autoAlpha: 0 }, t1 - LEAD);
  return el;
}
function keybox(sel, KT, wpx) {
  const kb = $(sel), bg = kb.querySelector(".bg"), cur = kb.querySelector(".cur"), tx = kb.querySelector(".tx");
  gsap.set(cur, { autoAlpha: 0 }); gsap.set(tx, { clipPath: "inset(0 100% 0 0)" });
  tl.set(cur, { autoAlpha: 1 }, KT - 6 * F);
  tl.fromTo(bg, { width: 0 }, { width: wpx, duration: 5 * F, ease: "power3.out", immediateRender: false }, KT - 4 * F);
  tl.fromTo(cur, { x: 0 }, { x: wpx - 12, duration: 5 * F, ease: "power3.out", immediateRender: false }, KT - 4 * F);
  tl.fromTo(tx, { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 5 * F, ease: "power2.out", immediateRender: false }, KT - 3 * F);
  tl.to(cur, { autoAlpha: 0, duration: 2 * F }, KT + 8 * F);
}
function keyboxOn(sel, wpx) { const kb = $(sel); gsap.set(kb.querySelector(".bg"), { width: wpx }); gsap.set(kb.querySelector(".cur"), { autoAlpha: 0 }); gsap.set(kb.querySelector(".tx"), { clipPath: "inset(0 0% 0 0)" }); }
function shake(sel, t, amp = 14, n = 5) { for (let i = 0; i < n; i++) { const a = amp * (1 - i / n); tl.set(sel, { x: (i % 2 ? -1 : 1) * a, y: (i % 3 - 1) * a * 0.6 }, t + i * F); } tl.set(sel, { x: 0, y: 0 }, t + n * F); }
function enterMG(scene, cam, t, until) {
  show(scene, t);
  tl.fromTo(cam, { scale: 4, filter: "blur(18px)" }, { scale: 1.05, filter: "blur(0px)", duration: 0.5, ease: "expo.out", immediateRender: false }, t);
  tl.to(cam, { scale: 1.0, duration: Math.max(0.3, until - t - 0.5), ease: "sine.inOut" }, t + 0.5);
}
function whip(fromCam, fromScene, toScene, toCam, t, dx, dy, until) {
  tl.to(fromCam, { x: -dx * 0.5, y: -dy * 0.5, filter: "blur(22px)", duration: 4 * F, ease: "power3.in" }, t - 4 * F);
  hide(fromScene, t); show(toScene, t);
  tl.fromTo(toCam, { x: dx * 0.6, y: dy * 0.6, filter: "blur(24px)", scale: 1.04 }, { x: 0, y: 0, filter: "blur(0px)", scale: 1.04, duration: 9 * F, ease: "expo.out", immediateRender: false }, t);
  if (until) tl.to(toCam, { scale: 1.0, duration: Math.max(0.2, until - t - 9 * F), ease: "sine.inOut" }, t + 9 * F);
}
function destello(Tp, hideList) {
  tl.fromTo("#leak", { autoAlpha: 0, x: -260 }, { autoAlpha: 1, x: 120, duration: 3 * F, ease: "power1.in", immediateRender: false }, Tp - 3 * F);
  tl.fromTo("#white", { autoAlpha: 0 }, { autoAlpha: 1, duration: 3 * F, ease: "power1.in", immediateRender: false }, Tp - 3 * F);
  if (hideList) hide(hideList, Tp);
  tl.set("#leak", { autoAlpha: 0 }, Tp + 3 * F);
  tl.to("#white", { autoAlpha: 0, duration: 4 * F, ease: "sine.out" }, Tp + 3 * F);
}
function burst(cont, cx, cy, n, t, spread = 520) {
  const c = $(cont);
  for (let i = 0; i < n; i++) {
    const d = document.createElement("div"); d.className = "prt"; const s = R(10, 26);
    d.style.cssText = `left:${cx}px;top:${cy}px;width:${s}px;height:${s}px;background:${["#C8B07A", "#2A2926", "#A88F57", "#E6D6AE"][i % 4]}`; c.appendChild(d);
    const a = (i / n) * Math.PI * 2 + R(-0.2, 0.2), r = R(0.45, 1) * spread;
    gsap.set(d, { autoAlpha: 0 });
    tl.fromTo(d, { autoAlpha: 1, x: 0, y: 0, rotation: 0, filter: "blur(4px)" }, { x: Math.cos(a) * r, y: Math.sin(a) * r, rotation: R(-180, 180), filter: "blur(0px)", duration: 0.7, ease: "expo.out", immediateRender: false }, t);
    tl.to(d, { autoAlpha: 0, duration: 0.3 }, t + R(0.45, 0.8));
  }
}
function tree(svgSel, nodesSel, x0, y0, ys, icons, t, step = 0.09) {
  const svg = $(svgSel), nodes = $(nodesSel); const n = icons.length, xs = icons.map((_, i) => 110 + 85 + i * ((1080 - 220 - 170) / (n - 1)));
  let s = "", h = "";
  xs.forEach((x, i) => { s += `<polyline id="${svgSel.slice(1)}l${i}" points="${x0},${y0} ${x0},${(y0 + ys) / 2} ${x},${(y0 + ys) / 2} ${x},${ys}" fill="none" stroke="#C8B07A" stroke-width="6" stroke-linejoin="miter"/>`;
    h += `<div class="node" id="${nodesSel.slice(1)}n${i}" style="left:${x - 85}px;top:${ys}px"><div class="ico" style="${ICON(icons[i])}"></div></div>`; });
  svg.innerHTML += s; nodes.insertAdjacentHTML("beforeend", h);
  xs.forEach((x, i) => {
    const pl = $(`#${svgSel.slice(1)}l${i}`), L = pl.getTotalLength();
    gsap.set(pl, { strokeDasharray: L, strokeDashoffset: L });
    tl.to(pl, { strokeDashoffset: 0, duration: 0.4, ease: "power2.inOut" }, t + i * step);
    const nd = `#${nodesSel.slice(1)}n${i}`; gsap.set(nd, { autoAlpha: 0 });
    tl.fromTo(nd, { autoAlpha: 0, scale: 0.3, filter: "blur(8px)" }, { autoAlpha: 1, scale: 1, filter: "blur(0px)", duration: 0.35, ease: "back.out(1.6)", immediateRender: false }, t + 0.28 + i * step);
  });
}
// línea SVG que se dibuja
function drawLine(sel, t, d = 0.5, ease = "power2.inOut") { const el = $(sel), L = el.getTotalLength(); gsap.set(el, { strokeDasharray: L, strokeDashoffset: L }); tl.to(el, { strokeDashoffset: 0, duration: d, ease }, t); }
// tecleo: el texto aparece carácter a carácter entre t0 y t1 (cursor dorado al final)
function typeText(sel, text, t0, t1) {
  const el = $(sel); el.innerHTML = [...text].map((c) => `<span class="ch">${esc(c)}</span>`).join("") + '<i class="tcur"></i>';
  const cs = el.querySelectorAll(".ch"); gsap.set(cs, { autoAlpha: 0 });
  cs.forEach((c, i) => tl.set(c, { autoAlpha: 1 }, t0 + (t1 - t0) * i / cs.length));
}
// contador numérico
function counter(sel, a, b, t, d) { const o = { v: a }; $(sel).textContent = a; tl.to(o, { v: b, duration: d, ease: "power2.out", onUpdate: () => { $(sel).textContent = Math.round(o.v); } }, t); }
// base de video: panel 2.5D (perspectiva + marco dorado + sombra sobre el fondo de puntos) o pantalla completa
function basePanel(t, d, o = {}) {
  tl.to("#base", { scale: o.s || 0.80, rotationY: o.ry ?? -10, rotationX: o.rx ?? 5, x: o.x || 0, y: o.y || 0, transformPerspective: 2200, outlineColor: "rgba(200,176,122,1)",
    boxShadow: "0 60px 120px -30px rgba(60,48,26,.55)", duration: d, ease: o.ease || "expo.out" }, t);
}
function baseFull(t, d = 0.01) { tl.to("#base", { scale: 1, rotationY: 0, rotationX: 0, x: 0, y: 0, outlineColor: "rgba(200,176,122,0)", boxShadow: "0 0 0 0 rgba(0,0,0,0)", filter: "blur(0px)", duration: d, ease: "power3.inOut" }, t); }
// la base entra desde el motion: aterriza desde escala 1,3 con desenfoque (expo.out)
function baseIn(t, d = 0.5) { baseFull(t); tl.fromTo("#base", { scale: 1.3, filter: "blur(20px)" }, { scale: 1, filter: "blur(0px)", duration: d, ease: "expo.out", immediateRender: false }, t); }
// la base se va: empuje power4.in + desenfoque (zoom-through)
function baseOut(t, d = 0.35, s = 1.6) { tl.to("#base", { scale: s, filter: "blur(14px)", duration: d, ease: "power4.in" }, t - d); }
