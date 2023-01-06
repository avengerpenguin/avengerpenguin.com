const path = require("path");
const { createRadarJson } = require("tech-radar-markdown-tools");

createRadarJson({
  title: "Ross Fenning's Tech Radar",
  rings: ["Adopt", "Trial", "Assess", "Hold"],
  quadrants: [
    path.resolve("./Garden/Tech Radar - Languages & Frameworks.md"),
    path.resolve("./Garden/Tech Radar - Platforms.md"),
    path.resolve("./Garden/Tech Radar - Techniques.md"),
    path.resolve("./Garden/Tech Radar - Tools.md"),
  ],
}).then((radar) => {
  console.log(JSON.stringify(radar.blips));
});
