import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    webkit = playwright.chromium
    browser = await webkit.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.baidu.com")
    await page.screenshot(path="screenshot.png")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())