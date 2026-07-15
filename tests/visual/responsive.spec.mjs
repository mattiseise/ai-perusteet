import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { readFileSync } from 'node:fs';
import inventory from './demo-inventory.json' with { type: 'json' };

const views = inventory.views;
const widths = inventory.widths;
const staticIds = inventory.static;
const interactiveIds = Object.keys(inventory.interactive);

function lessonFromId(id) {
  return id.split('-')[1];
}

async function openLesson(page, view, lesson) {
  await page.goto(`/${view}/tunti-${lesson}/#selfstudy`);
  await page.waitForSelector('.panel.active');
}

async function expectNoHorizontalOverflow(page, context) {
  const overflow = await page.evaluate(() => ({
    root: document.documentElement.scrollWidth - document.documentElement.clientWidth,
    body: document.body.scrollWidth - document.body.clientWidth,
  }));
  expect(overflow.root, `${context}: documentElement overflow`).toBeLessThanOrEqual(1);
  expect(overflow.body, `${context}: body overflow`).toBeLessThanOrEqual(1);
}

test('kaikki 26 demoa säilyvät näkyvinä molemmissa näkymissä', async ({ page }) => {
  for (const view of views) {
    for (const width of widths) {
      await page.setViewportSize({ width, height: 900 });
      for (const id of [...staticIds, ...interactiveIds]) {
        await openLesson(page, view, lessonFromId(id));
        const demo = page.locator(`[data-demo-id="${id}"]`);
        await expect(demo, `${view}/${id}/${width}`).toBeVisible();
        await expect(demo.locator('.ai-demo__stage')).toBeVisible();
        if (staticIds.includes(id)) {
          const mobile = demo.locator('.ai-demo__mobile-model');
          if (width <= 430) {
            await expect(mobile).toBeVisible();
            expect(await mobile.locator('.ai-demo__mobile-node').count()).toBeGreaterThanOrEqual(2);
          } else {
            await expect(mobile).toBeHidden();
          }
        }
        await expectNoHorizontalOverflow(page, `${view}/${id}/${width}`);
      }
    }
  }
});

test('mobiilileveydet 320–768 eivät aiheuta sivutason ylivuotoa', async ({ page }) => {
  for (const view of views) {
    for (const width of widths) {
      await page.setViewportSize({ width, height: 844 });
      await openLesson(page, view, '01');
      await expectNoHorizontalOverflow(page, `${view}/lesson-01/${width}`);
      const capSize = await page.locator('.ai-demo__cap').first().evaluate(el => parseFloat(getComputedStyle(el).fontSize));
      expect(capSize).toBeGreaterThanOrEqual(13);
    }
  }
});

async function useLabel(page, target) {
  const label = page.locator(`label[for="${target}"]`);
  const input = page.locator(`#${target}`);
  await expect(label).toBeVisible();
  const box = await label.boundingBox();
  expect(Math.min(box.width, box.height), `${target}: kosketuskohde`).toBeGreaterThanOrEqual(44);
  await input.focus();
  await expect(label).toHaveClass(/demo-focus/);
  await input.press('Space');
  await expect(input).toBeChecked();
}

async function runInteractiveStates(page, id) {
  if (id === 'lesson-07-01') {
    await expect(page.locator('#l07-s1')).toBeChecked();
    await useLabel(page, 'l07-b1'); // väärä
    await expect(page.locator('.r1 .l07-info')).toBeVisible();
    await useLabel(page, 'l07-a1'); // oikea
    for (const target of ['l07-s2', 'l07-b2', 'l07-s3', 'l07-a3', 'l07-s4', 'l07-b4', 'l07-s5', 'l07-b5', 'l07-s1']) {
      await useLabel(page, target);
    }
    await expect(page.locator('#l07-s1')).toBeChecked();
  } else if (id === 'lesson-20-02') {
    await expect(page.locator('#l20q-s1')).toBeChecked();
    await useLabel(page, 'l20q-1c'); // väärä
    await expect(page.locator('.r1 .l20q-fb.f1c')).toBeVisible();
    for (const target of ['l20q-1a', 'l20q-s2', 'l20q-2b', 'l20q-s3', 'l20q-3c', 'l20q-s1']) {
      await useLabel(page, target);
    }
    await expect(page.locator('#l20q-s1')).toBeChecked();
  } else {
    await useLabel(page, 'l24q-1'); // väärä
    await expect(page.locator('.l24q-fb.fbw')).toBeVisible();
    await useLabel(page, 'l24q-3'); // oikea
    await expect(page.locator('.l24q-fb.fbr')).toBeVisible();
  }
}

test('interaktiivisten demojen kaikki tilat toimivat näppäimistöllä pysty- ja vaakatilassa', async ({ page }) => {
  for (const view of views) {
    for (const id of interactiveIds) {
      for (const viewport of [{ width: 390, height: 844 }, inventory.landscape]) {
        await page.setViewportSize(viewport);
        await openLesson(page, view, lessonFromId(id));
        const demo = page.locator(`[data-demo-id="${id}"]`);
        await runInteractiveStates(page, id);
        await expectNoHorizontalOverflow(page, `${view}/${id}/${viewport.width}x${viewport.height}`);
      }
    }
  }
});

test('200 prosentin zoom ja reduced motion säilyttävät sisällön', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  for (const id of interactiveIds) {
    // 195 CSS-pikseliä vastaa 390 px leveää näkymää selaimen 200 % zoomissa.
    await page.setViewportSize({ width: 195, height: 422 });
    await openLesson(page, 'kurssi', lessonFromId(id));
    const demo = page.locator(`[data-demo-id="${id}"]`);
    await expect(demo).toBeVisible();
    await expect(demo.locator('.ai-demo__stage')).toBeVisible();
    await expectNoHorizontalOverflow(page, `${id}/zoom-200`);
    const motion = await demo.locator('*').evaluateAll(nodes => nodes.filter(el => {
      const cs = getComputedStyle(el);
      const duration = cs.animationDuration.split(',').some(v => parseFloat(v) > 0.01);
      const transition = cs.transitionDuration.split(',').some(v => parseFloat(v) > 0.01);
      return duration || transition;
    }).length);
    expect(motion, `${id}: reduced-motion`).toBe(0);
  }
});

test('axe ei löydä vakavia tai kriittisiä rikkeitä sitemapin kaikilta 96 julkiselta sivulta', async ({ page }) => {
  const sitemap = readFileSync(new URL('../../sitemap.xml', import.meta.url), 'utf8');
  const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(match => new URL(match[1]).pathname);
  expect(urls).toHaveLength(96);
  for (const url of urls) {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(url);
    const results = await new AxeBuilder({ page }).analyze();
    const severe = results.violations.filter(v => ['serious', 'critical'].includes(v.impact));
    expect(severe, `${url}: ${severe.map(v => v.id).join(', ')}`).toEqual([]);
  }
});
