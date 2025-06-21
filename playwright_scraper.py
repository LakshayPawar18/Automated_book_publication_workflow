from playwright.sync_api import sync_playwright

def scrape_chapter(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.text_content("#mw-content-text")
        page.screenshot(path="screenshots/chapter1.png", full_page=True)
        browser.close()
        return content

