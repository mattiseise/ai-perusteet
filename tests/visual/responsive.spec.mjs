import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { readFileSync } from 'node:fs';
import inventory from './demo-inventory.json' with { type: 'json' };

const views = inventory.views;
const widths = process.env.WIDTH_FILTER ? inventory.widths.filter(w => String(w) === process.env.WIDTH_FILTER) : inventory.widths;
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

test(`kaikki ${inventory.expectedDemoCount} demoa säilyvät näkyvinä molemmissa näkymissä`, async ({ page }) => {
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
          if (width <= 680) {
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

test('kurssin ajattelugraafi toimii työpöydällä ja vaihtuu mobiiliesitykseen', async ({ page }) => {
  await page.setViewportSize({ width: 1100, height: 800 });
  await page.goto('/kurssi/');
  await expect(page.locator('.course-thinking-graph')).toBeVisible();
  await expect(page.locator('.course-thinking-mobile')).toBeHidden();

  await page.setViewportSize({ width: 390, height: 844 });
  await expect(page.locator('.course-thinking-graph')).toBeHidden();
  await expect(page.locator('.course-thinking-mobile')).toBeVisible();
  await expect(page.locator('.course-thinking-mobile .ai-demo__mobile-node')).toHaveCount(5);
  await expect(page.locator('body')).not.toHaveCSS('overflow-x', 'scroll');
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
  if (id === 'lesson-20-02') {
    await expect(page.locator('.l20q-round.r1')).toBeVisible();
    await expect(page.locator('.l20q-round.r2')).toBeHidden();
    await useLabel(page, 'l20q-1c'); // väärä
    await expect(page.locator('.r1 .l20q-fb.f1c')).toBeVisible();
    expect(await page.locator('.r1 .l20q-fb:visible').count()).toBe(1);
    await useLabel(page, 'l20q-1a'); // oikea
    await page.locator('.r1 .l20q-next').click();
    await expect(page.locator('.l20q-round.r1')).toBeHidden();
    await expect(page.locator('.l20q-round.r2')).toBeVisible();
    await expect(page.locator('.r2 .l20q-sc')).toBeFocused();
    await useLabel(page, 'l20q-2b');
    await page.locator('.r2 .l20q-next').click();
    await expect(page.locator('.l20q-round.r3')).toBeVisible();
    await useLabel(page, 'l20q-3c');
    await page.locator('.r3 .l20q-restart').click();
    await expect(page.locator('.l20q-round.r1')).toBeVisible();
    await expect(page.locator('.l20q-round.r3')).toBeHidden();
    expect(await page.locator('.l20q-in:checked').count()).toBe(0);
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

test('T20-testin tab-järjestyksessä ei ole piilotettuja radioita ja vain valittu palaute on esillä', async ({ page }) => {
  await page.setViewportSize({ width: 1000, height: 900 });
  await openLesson(page, 'kurssi', '20');
  const hiddenFocusable = await page.evaluate(() => {
    const wrap = document.querySelector('.l20q-wrap');
    return [...wrap.querySelectorAll('input,button')].filter(el => el.closest('[hidden]') && el.tabIndex >= 0 && !el.disabled)
      .filter(el => el.offsetParent !== null).length;
  });
  expect(hiddenFocusable, 'piilotetut fokusoitavat').toBe(0);
  const reachable = await page.evaluate(() => {
    const wrap = document.querySelector('.l20q-wrap');
    return [...wrap.querySelectorAll('input')].filter(el => el.closest('[hidden]') === null).map(el => el.name);
  });
  expect(new Set(reachable).size, 'vain aktiivisen kierroksen radiot').toBe(1);
  expect(await page.locator('.l20q-fb:visible').count()).toBe(0);
  await page.locator('label[for="l20q-1b"]').click();
  expect(await page.locator('.l20q-fb:visible').count()).toBe(1);
});

test('animaatio-ohjaimet vain data-once-kuvioilla, ei interaktiivisissa, piilossa mobiilikortin alla', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'no-preference' });
  await page.setViewportSize({ width: 1000, height: 900 });
  await openLesson(page, 'kurssi', '20');
  await expect(page.locator('.ai-demo[data-demo-kind="static"] .ai-demo__ctrl .ad-restart')).toHaveCount(1);
  await expect(page.locator('.ai-demo[data-demo-kind="interactive"] .ai-demo__ctrl')).toHaveCount(0);
  await openLesson(page, 'kurssi', '05'); // vanha silmukkakuvio ilman data-oncea
  await expect(page.locator('.ai-demo__ctrl')).toHaveCount(0);
  await openLesson(page, 'kurssi', '13');
  await expect(page.locator('.ai-demo__ctrl')).toHaveCount(1);
  await page.setViewportSize({ width: 480, height: 900 });
  await expect(page.locator('.ai-demo[data-demo-kind="static"] .ai-demo__ctrl')).toBeHidden();
  await expect(page.locator('.ai-demo__mobile-model')).toBeVisible();
});

test('axe ei löydä vakavia tai kriittisiä rikkeitä sitemapin kaikilta julkisilta sivuilta', async ({ page }) => {
  const sitemap = readFileSync(new URL('../../sitemap.xml', import.meta.url), 'utf8');
  const allUrls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(match => new URL(match[1]).pathname);
  expect(allUrls).toHaveLength(67);
  const start = Number(process.env.AXE_START || 0);
  const count = Number(process.env.AXE_COUNT || allUrls.length);
  const urls = allUrls.slice(start, start + count);
  for (const url of urls) {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(url);
    const results = await new AxeBuilder({ page }).analyze();
    const severe = results.violations.filter(v => ['serious', 'critical'].includes(v.impact));
    expect(severe, `${url}: ${severe.map(v => v.id).join(', ')}`).toEqual([]);
  }
});
