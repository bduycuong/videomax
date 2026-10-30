// Satori: JSX-like tree -> SVG; resvg: SVG -> PNG. Notebook-paper cover with the hook question and Max.
import satori from "satori";
import { Resvg } from "@resvg/resvg-js";
import fs from "node:fs";
const a = JSON.parse(process.argv[2]);
const font = (f) => fs.readFileSync(new URL(f, import.meta.url));
const C = { paper: "#FFFDF6", rule: "#D3E3F1", margin: "#F0A3A0", ink: "#262A3B", hi: "#FFE27A", red: "#E0483C" };
const h = (type, style, children) => ({ type, props: { style, children } });
const maxUri = "data:image/svg+xml;base64," + fs.readFileSync(a.max).toString("base64");
// highlight the chosen phrase of the title
const t = a.title, i = a.hl ? t.toLowerCase().indexOf(a.hl.toLowerCase()) : -1;
const parts = i < 0 ? [t] : [t.slice(0, i), t.slice(i, i + a.hl.length), t.slice(i + a.hl.length)];
const words = parts.flatMap((p, k) => p.split(/(\s+)/).filter((w) => w.trim()).map((w) => ({ w, hl: i >= 0 && k === 1 })));
const lines = Array.from({ length: 30 }, (_, k) => h("div", { position: "absolute", left: 0, top: 30 + k * 64, width: 1080, height: 2, background: C.rule }));
const tree = h("div", { width: 1080, height: 1920, display: "flex", flexDirection: "column", background: C.paper, position: "relative", fontFamily: "Patrick" }, [
  ...lines,
  h("div", { position: "absolute", left: 64, top: 0, width: 3, height: 1920, background: C.margin }),
  h("div", { position: "absolute", left: 96, top: 150, display: "flex", padding: "4px 30px", background: C.hi, border: `5px solid ${C.ink}`, borderRadius: 18, fontFamily: "Gochi", fontSize: 54, color: C.ink, transform: "rotate(-3deg)" }, "MAX WISE"),
  a.tag ? h("div", { position: "absolute", right: 90, top: 166, display: "flex", padding: "2px 22px", border: `4px solid ${C.red}`, borderRadius: 14, fontSize: 40, color: C.red, transform: "rotate(4deg)" }, a.tag) : null,
  h("div", { position: "absolute", left: 90, right: 90, top: 330, display: "flex", flexWrap: "wrap", justifyContent: "center", fontFamily: "Gochi", fontSize: 128, lineHeight: 1.06, color: C.ink },
    words.map(({ w, hl }) => h("span", { margin: "0 14px", padding: hl ? "0 10px" : 0, background: hl ? `linear-gradient(transparent 18%, ${C.hi} 18%, ${C.hi} 88%, transparent 88%)` : "transparent" }, w))),
  h("img", { position: "absolute", left: 40, top: 1060, width: 560, height: 710 }, undefined),
  h("div", { position: "absolute", left: 560, top: 1240, display: "flex", fontFamily: "Gochi", fontSize: 300, color: C.red, transform: "rotate(8deg)" }, "?"),
].filter(Boolean));
tree.props.children.find((c) => c && c.type === "img").props.src = maxUri;
const svg = await satori(tree, { width: 1080, height: 1920, fonts: [
  { name: "Gochi", data: font("./gochi-hand.ttf"), weight: 400, style: "normal" },
  { name: "Patrick", data: font("./patrick-hand.ttf"), weight: 400, style: "normal" } ] });
fs.writeFileSync(a.out, new Resvg(svg, { fitTo: { mode: "width", value: 1080 } }).render().asPng());
