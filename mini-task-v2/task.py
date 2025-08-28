from playwright.async_api import async_playwright
import asyncio
import os

# main function to fetch the page
async def main():
    os.makedirs("productData", exist_ok=True)  

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # Initialize the browser instance (headless mode-->see browser in action)
        page = await browser.new_page() # Open a new page
        query="laptop"
        file=0
        for i in range(1,10):
            await page.goto(f'https://www.ebay.com/sch/i.html?_nkw={query}&_sacat=0&_from=R40&_pgn={i}') # Navigate to the URL
            
            elems = await page.locator(".su-card-container").all()
            print(f"Total elements found: {len(elems)}")
            for elem in elems:
                d=await elem.inner_html()
                with open(f"productData/{query}_{file}.html","w",encoding="utf-8") as f:
                    f.write(d)
                    file+=1
            # product_names=await page.locator("div .s-card__title").all_inner_texts()
            # product_prices=await page.locator("span.s-card__price").all_inner_texts()
            
            # print(product_names,product_prices)
            await page.wait_for_timeout(2000)
        await browser.close()

# Run the main function --> asynchronous function so run using asyncio module
if __name__ == '__main__':
    asyncio.run(main())