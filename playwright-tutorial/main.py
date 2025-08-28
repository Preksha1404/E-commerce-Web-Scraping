from playwright.async_api import async_playwright
import asyncio

# main function to fetch the page
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Initialize the browser instance (headless mode-->see browser in action)
        page = await browser.new_page() # Open a new page
        await page.goto('https://books.toscrape.com/') # Navigate to the URL
        await page.wait_for_timeout(1000) # Wait for 1 second to ensure the page loads completely
        title_element=await page.query_selector("title")
        title_text=await title_element.inner_text()
        # print(title_text)
        product_names=await page.locator("h3 a").all_inner_texts()
        product_prices=await page.locator(".product_price .price_color").all_inner_texts()
        for i in range(len(product_names)):
            print(f"Product Name: {product_names[i]}, Price: {product_prices[i]}")
        await page.wait_for_timeout(2000)
        await browser.close()

# Run the main function --> asynchronous function so run using asyncio module
if __name__ == '__main__':
    asyncio.run(main())