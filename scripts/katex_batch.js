// Render a JSON list of {tex, display} with KaTeX. stdin: JSON array. stdout: JSON array of HTML strings.
const katex = require("katex");
let input = "";
process.stdin.on("data", (d) => (input += d));
process.stdin.on("end", () => {
  const items = JSON.parse(input);
  const out = items.map((it) =>
    katex.renderToString(it.tex, { displayMode: !!it.display, throwOnError: false, output: "htmlAndMathml", strict: "ignore" })
  );
  process.stdout.write(JSON.stringify(out));
});
