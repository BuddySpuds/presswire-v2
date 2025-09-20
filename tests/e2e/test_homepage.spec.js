// E2E Tests for PressWire Homepage
const { test, expect } = require('@playwright/test');

test.describe('PressWire Homepage', () => {
  test('should load the homepage', async ({ page }) => {
    await page.goto('/');

    // Check if page loads
    await expect(page).toHaveTitle(/PressWire/i);

    // Check for key elements
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

  test('should have working navigation links', async ({ page }) => {
    await page.goto('/');

    // Check for generate link
    const generateLink = page.locator('a[href="/generate"]');
    if (await generateLink.isVisible()) {
      await generateLink.click();
      await expect(page).toHaveURL('/generate');
    }
  });

  test('should display API health status', async ({ page }) => {
    const response = await page.request.get('/health');
    expect(response.status()).toBe(200);

    const data = await response.json();
    expect(data.status).toBe('healthy');
  });
});