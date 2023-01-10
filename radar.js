const path = require("path");
const { createRadarJson } = require("tech-radar-markdown-tools");
const slugify = require("slugify");

const rings = ["Adopt", "Trial", "Assess", "Hold"];

function wikilinkToMarkdown(match, href, foundText) {
  const text = foundText || href;
  const cleanHref = slugify(href, {
    lower: true,
  });
  return `<a href="/${cleanHref}/">${text}</a>`;
}

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
          blipFixed.description = blipFixed.description.replaceAll(
            /\[\[([^|\]]+)\|?(.*?)\]\]/g,
            wikilinkToMarkdown
          );
          return blipFixed;
        })
        .sort((a, b) => rings.indexOf(a.ring) - rings.indexOf(b.ring))
    )
  );
});
