from playwright.sync_api import Page


def test_first_example(page: Page):
    page.goto("https://abc12309.sg-host.com/")
    title=page.title()
    print("--------------------------->", title)
    print("--------------------------->"+ "title2")
    assert "Iqrashoppingdemo" in title
    page.wait_for_timeout(2000)