import asyncio
from typing import Any

from playwright.async_api import Page, TimeoutError

from harambe import SDK


async def scrape(
    sdk: SDK, url: str, context: Any, *args: Any, **kwargs: Any
) -> None:
    page: Page = sdk.page
    await page.wait_for_selector('div.table-responsive')
    rows = await page.query_selector_all('div.table-responsive tbody tr td:first-child a')
    for i in range(len(rows)):
        await page.wait_for_selector('div.table-responsive')
        rows = await page.query_selector_all('div.table-responsive tbody tr td:first-child a')
        await rows[i].click()
        await page.wait_for_selector("//td[strong[text()='Solicitation Number: ']]/following-sibling::td")
        notice_id = await page.locator(
            "//td[strong[text()='Solicitation Number: ']]/following-sibling::td").inner_text()
        notice_title = await page.locator("//td[strong[text()='Title: ']]/following-sibling::td").inner_text()
        try:
            await page.wait_for_selector("//td[strong[text()='Description:']]/following-sibling::td", timeout=1000)
            desc = await page.locator("//td[strong[text()='Description:']]/following-sibling::td").inner_text()
            desc = desc.strip()
        except TimeoutError:
            desc = None

        try:
            buyer_name = await page.wait_for_selector("//td[strong[text()='Contact Name: ']]/following-sibling::td[1]",
                                                      timeout=2000)
            buyer_name = await page.locator(
                "//td[strong[text()='Contact Name: ']]/following-sibling::td[1]").first.inner_text()
            buyer_name = buyer_name.strip()
        except TimeoutError:
            buyer_name = None
        try:
            buyer_email = await page.wait_for_selector(
                "//td[strong[text()='Contact Email: ']]/following-sibling::td[1]", timeout=2000)
            buyer_email = await page.locator(
                "//td[strong[text()='Contact Email: ']]/following-sibling::td[1]").first.inner_text()
            buyer_email = buyer_email.strip()
        except TimeoutError:
            buyer_email = None
        try:
            buyer_phone = await page.wait_for_selector("//td[strong[text()='Contact Phone:']]/following-sibling::td[1]",
                                                       timeout=2000)
            buyer_phone = await page.locator(
                "//td[strong[text()='Contact Phone:']]/following-sibling::td[1]").first.inner_text()
            buyer_phone = buyer_phone.strip()
        except TimeoutError:
            buyer_phone = None
        try:
            await page.wait_for_selector("//td[strong[text()='Close Date:']]/following-sibling::td[1]", timeout=1000)
            close_date = await page.locator(
                "//td[strong[text()='Close Date:']]/following-sibling::td[1]").first.inner_text()
        except TimeoutError:
            close_date = None
        try:
            await page.wait_for_selector("//td[strong[text()='Open Day: ']]/following-sibling::td[1]", timeout=1000)
            issue_dat = await page.locator(
                "//td[strong[text()='Open Day: ']]/following-sibling::td[1]").first.inner_text()
        except TimeoutError:
            issue_dat = None
        try:
            await page.wait_for_selector("//td[strong[text()='Bid Type:']]/following-sibling::td[1]", timeout=1000)
            typ1 = await page.locator("//td[strong[text()='Bid Type:']]/following-sibling::td[1]").first.inner_text()
            typ = typ1
        except TimeoutError:
            typ = None
        files = []
        try:
            await page.click("#BidAttachPanel")
        except:
            pass
        try:
            await page.click("#BidAmendPanel", timeout=2000)
            while True:
                await page.wait_for_selector('#collapseBidAmend table tbody tr')
                rows = await page.query_selector_all('#collapseBidAmend table tbody tr ')
                for row in rows:
                    title = await row.query_selector('td:first-child')
                    title = await title.inner_text()
                    link = await row.query_selector('td:last-child button')
                    if link:
                        meta = await sdk.capture_download(link)
                        files.append(
                            {'title': title.strip(), 'url': meta['url']}
                        )
                try:

                    chk = await page.locator(
                        "(//*[@id='collapseBidAmend']//a[@aria-label='Next'])[2]/..").get_attribute('class')
                    if 'disabled' in chk: break
                    next = await page.query_selector("(//*[@id='collapseBidAmend']//a[@aria-label='Next'])[2]")
                    await next.click(timeout=2000)
                    await page.wait_for_timeout(1000)
                except TimeoutError:
                    break
        except:
            pass
        try:
            while True:
                await page.wait_for_selector('#collapseBidAttach table tbody tr')
                rows = await page.query_selector_all('#collapseBidAttach table tbody tr')
                for row in rows:
                    title = await row.query_selector('td:first-child')
                    title = await title.inner_text()
                    link = await row.query_selector('td:last-child button')
                    if link:
                        meta = await sdk.capture_download(link)
                        files.append(
                            {'title': title.strip(), 'url': meta['url']}
                        )
                try:

                    chk = await page.locator(
                        "(//*[@id='collapseBidAttach']//a[@aria-label='Next'])[2]/..").get_attribute('class')
                    if 'disabled' in chk: break
                    next = await page.query_selector("(//*[@id='collapseBidAttach']//a[@aria-label='Next'])[2]")
                    await next.click(timeout=2000)
                    await page.wait_for_timeout(1000)
                except TimeoutError:
                    break
        except TimeoutError:
            pass
        await sdk.save_data(
            {
                "id": notice_id,
                "title": notice_title,
                "description": desc,
                "location": None,
                "type": typ,
                "category": None,
                "posted_date": issue_dat,
                "due_date": close_date,
                "buyer_name": None,
                "buyer_contact_name": buyer_name,
                "buyer_contact_number": buyer_phone,
                "buyer_contact_email": buyer_email,
                'attachments': files,
                'procurement_items': [],
            }
        )
        await page.go_back()


if __name__ == "__main__":
    asyncio.run(SDK.run(scrape,
                        "https://camisvr.co.la.ca.us/LACoBids/BidLookUp/OpenBidList?page=4&TextSearch=%7C%7C%7C&FieldSort=BidTitle&DirectionSort=Asc"))
