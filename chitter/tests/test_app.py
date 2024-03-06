from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===
def test_get_posts(page, test_web_address, db_connection):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/posts")

    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text("Today I am trying something new, April 2022")


# === End Example Code ===