const path = require("path");
const { createRadarJson } = require("tech-radar-markdown-tools");

const rings = ["Hold", "Assess", "Trial", "Adopt"];

createRadarJson({
  quadrants: [
    path.resolve("./Garden/Tech Radar - Languages & Frameworks.md"),
    path.resolve("./Garden/Tech Radar - Platforms.md"),
    path.resolve("./Garden/Tech Radar - Techniques.md"),
    path.resolve("./Garden/Tech Radar - Tools.md"),
  ],
}).then((radar) => {
  console.log(
    JSON.stringify(
      radar.blips
        .map((blip) => {
          const blipFixed = { ...blip };
          blipFixed.isNew = blip.isNew.toString().toUpperCase();
          return blipFixed;
        })
        .sort((a, b) => rings.indexOf(a.ring) - rings.indexOf(b.ring))
    )
  );
});
