import { spawnSync } from 'node:child_process';

for (const file of ['assets/site.js', 'assets/practice.js']) {
  const result = spawnSync(process.execPath, ['--check', file], { encoding: 'utf8' });
  if (result.status !== 0) {
    process.stderr.write(result.stderr || result.stdout);
    process.exit(result.status || 1);
  }
}
console.log('OK: generoidut JavaScript-tiedostot');
