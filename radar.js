const path = require('path');
const { createRadarJson } = require('tech-radar-markdown-tools');

createRadarJson({
  title: 'My radar',
  rings: ['Adopt', 'Explore', 'Endure', 'Retire'],
  quadrants: [
    path.resolve('./Garden/Tech Radar - Platforms.md'),
//    path.resolve('./data/platforms.md'),
//    path.resolve('./data/techniques.md'),
//    path.resolve('./data/tools.md'),
  ],
}).then(radar => {
  console.log(radar);
});
