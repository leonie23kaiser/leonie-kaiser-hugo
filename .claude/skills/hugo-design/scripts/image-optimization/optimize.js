const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const targetDir = path.resolve(
  __dirname,
  '../../../../../src/integrations.at/static/images',
);

// Folders to focus on based on prompt
const targetFolders = ['areas', 'cards', 'class-pictures', 'services', 'og'];

async function getFiles(dir) {
  const dirents = await fs.promises.readdir(dir, { withFileTypes: true });
  const files = await Promise.all(
    dirents.map((dirent) => {
      const res = path.resolve(dir, dirent.name);
      return dirent.isDirectory() ? getFiles(res) : res;
    }),
  );
  return Array.prototype.concat(...files);
}

function formatBytes(bytes) {
  return (bytes / 1024).toFixed(2) + ' KB';
}

async function run() {
  console.log('Starting optimization pass...');
  const allFiles = await getFiles(targetDir);

  // Filter for PNG and JPG
  const candidates = allFiles
    .filter((f) => {
      const ext = path.extname(f).toLowerCase();
      return ext === '.png' || ext === '.jpg' || ext === '.jpeg';
    })
    .filter((f) => {
      // Only focus on specified folders
      return targetFolders.some(
        (folder) => f.includes(`\\${folder}\\`) || f.includes(`/${folder}/`),
      );
    });

  const results = [];
  const skipped = [];

  for (const file of candidates) {
    try {
      const stats = fs.statSync(file);
      // Skip small files that probably don't need aggressive optimization
      if (stats.size < 100 * 1024) {
        skipped.push({
          file: path.relative(targetDir, file),
          reason:
            'Size is small (< 100KB), skipped to preserve absolute quality.',
        });
        continue;
      }

      const parsedPath = path.parse(file);
      const webpPath = path.join(parsedPath.dir, `${parsedPath.name}.webp`);
      const avifPath = path.join(parsedPath.dir, `${parsedPath.name}.avif`);

      let convertedWebp = false;
      let convertedAvif = false;
      let webpSize = 0;
      let avifSize = 0;

      // Ensure we haven't already optimized correctly or it's a huge bad generated file
      await sharp(file)
        .webp({ quality: 80, effort: 6 }) // Removed nearLossless for JPEGs
        .toFile(webpPath);

      webpSize = fs.statSync(webpPath).size;
      convertedWebp = true;

      await sharp(file).avif({ quality: 75, effort: 5 }).toFile(avifPath);

      avifSize = fs.statSync(avifPath).size;
      convertedAvif = true;

      if (convertedWebp || convertedAvif) {
        results.push({
          file: path.relative(targetDir, file),
          originalSize: stats.size,
          webpCreated: convertedWebp,
          webpSize,
          avifCreated: convertedAvif,
          avifSize,
        });
      }
    } catch (e) {
      skipped.push({
        file: path.relative(targetDir, file),
        reason: `Error: ${e.message}`,
      });
    }
  }

  console.log(`\n=== Optimization Report ===`);
  console.log(`\nConverted Files:`);
  results.forEach((r) => {
    console.log(`- ${r.file} (${formatBytes(r.originalSize)})`);
    if (r.webpCreated)
      console.log(
        `   -> WEBP: ${formatBytes(r.webpSize)} (${Math.round((1 - r.webpSize / r.originalSize) * 100)}% saved)`,
      );
    if (r.avifCreated)
      console.log(
        `   -> AVIF: ${formatBytes(r.avifSize)} (${Math.round((1 - r.avifSize / r.originalSize) * 100)}% saved)`,
      );
  });

  console.log(`\nSkipped Files:`);
  skipped.forEach((s) => {
    console.log(`- ${s.file} (Reason: ${s.reason})`);
  });
}

run().catch(console.error);
