// E2E Tests for PressWire API
const { test, expect } = require('@playwright/test');

test.describe('PressWire API', () => {
  test('should return API information', async ({ request }) => {
    const response = await request.get('/api');
    expect(response.status()).toBe(200);

    const data = await response.json();
    expect(data.name).toBe('PressWire.ie API v2');
    expect(data.status).toBe('operational');
    expect(data.version).toBe('2.0.0');
  });

  test('should generate a press release', async ({ request }) => {
    const response = await request.post('/api/v1/press-releases/generate', {
      data: {
        company_name: 'Test Company Ltd',
        announcement: 'We are launching a new product',
        company_info: 'Leading tech company in Ireland',
        contact_email: 'test@example.com'
      }
    });

    expect(response.status()).toBe(200);

    const data = await response.json();
    expect(data).toHaveProperty('headline');
    expect(data).toHaveProperty('body');
    expect(data).toHaveProperty('seo_title');
  });

  test('should enhance a press release', async ({ request }) => {
    const response = await request.post('/api/v1/press-releases/enhance', {
      data: {
        content: 'Test Company announces new product launch. The product is innovative.'
      }
    });

    expect(response.status()).toBe(200);

    const data = await response.json();
    expect(data).toHaveProperty('overall_score');
    expect(data.overall_score).toBeGreaterThan(0);
  });

  test('should list press releases', async ({ request }) => {
    const response = await request.get('/api/v1/press-releases/');
    expect(response.status()).toBe(200);

    const data = await response.json();
    expect(data).toHaveProperty('items');
    expect(Array.isArray(data.items)).toBe(true);
  });

  test('API documentation should be accessible', async ({ page }) => {
    await page.goto('/api/docs');

    // Check if Swagger UI loads
    await expect(page.locator('.swagger-ui')).toBeVisible({ timeout: 10000 });
    await expect(page).toHaveTitle(/API/i);
  });
});