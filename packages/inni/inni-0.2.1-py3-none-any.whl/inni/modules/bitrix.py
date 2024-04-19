from playwright.sync_api import TimeoutError as PwTimeoutError
from playwright.sync_api import sync_playwright

from inni.modules.base import BaseModule


class Module(BaseModule):
    login_template_keys = ()
    logout_template_keys = ()

    def setUp(self):
        self.headless = self.config.get("headless", False)
        self.url = self.config["url"]
        self.username = self.config["username"]
        self.password = self.config["password"]

    def visit(self, login: bool):
        in_or_out = "in" if login else "out"
        with sync_playwright() as pw, self.out.status(
            f"Clocking {in_or_out}"
        ) as status:
            browser = pw.firefox.launch(headless=self.headless)
            context = browser.new_context(viewport={"width": 1800, "height": 900})
            page = context.new_page()
            status.update("Opening webpage")
            page.goto(self.url, timeout=10000000, wait_until="domcontentloaded")

            # Login
            status.update("Filling in username")
            page.get_by_label("Enter phone number or email").click()
            page.get_by_label("Enter phone number or email").fill(
                self.config["username"]
            )
            # Wait a second for bitrix JS to enable the button
            page.wait_for_timeout(1000)
            page.get_by_label("Enter phone number or email").press("Enter")
            while True:
                page.get_by_role("button", name="Next").click()
                status.update("Filling in password")
                try:
                    page.get_by_label("Enter your password to").click(timeout=1000)
                    break
                except PwTimeoutError:
                    status.update("Could not find password field, retrying username.")
            status.update("Filling in password")
            page.get_by_label("Enter your password to").fill(self.config["password"])
            # Wait a second for bitrix JS to enable the button
            page.wait_for_timeout(1000)
            page.get_by_label("Enter your password to").press("Enter")
            page.get_by_role("button", name="Next").click()

            self.out.print("[green]✅Logged into bitrix")
            # Close the popup
            status.update("Closing popup")
            page.locator(".popup-window-close-icon").click()

            # Login/Logout
            status.update(f"Clocking {in_or_out}")
            page.locator("span#timeman-block").click()
            if login:
                page.get_by_role("button", name="Clock In").click()
            else:
                page.get_by_role("button", name="Clock Out").click()

            # Ensure bitrix registered the event
            status.update(
                f"Clocked {in_or_out}. Waiting for bitrix to register the event."
            )
            if login:
                page.get_by_role("button", name="Clock Out").wait_for()
            else:
                page.get_by_role("button", name="Clock In").wait_for()
            page.wait_for_timeout(1000)

            context.close()
            browser.close()
        self.out.print(f"[green]✅ Clocked {in_or_out}")

    def login(self, responses):
        self.visit(True)

    def logout(self, responses):
        self.visit(False)
