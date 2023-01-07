const path = require("path");
const { createRadarJson } = require("tech-radar-markdown-tools");

createRadarJson({
  title: "Ross Fenning's Tech Radar",
  rings: ["Hold", "Assess", "Trial", "Adopt"],
  quadrants: [
    path.resolve("./Garden/Tech Radar - Languages & Frameworks.md"),
    path.resolve("./Garden/Tech Radar - Platforms.md"),
    path.resolve("./Garden/Tech Radar - Techniques.md"),
    path.resolve("./Garden/Tech Radar - Tools.md"),
  ],
}).then((radar) => {
  console.log(
    JSON.stringify(
      radar.blips.map((blip) => {
        const blipFixed = { ...blip };
        blipFixed.isNew = blip.isNew.toString().toUpperCase();
        blipFixed.ring = blip.ring.toLowerCase();
        return blipFixed;
      })
    )
  );
});
