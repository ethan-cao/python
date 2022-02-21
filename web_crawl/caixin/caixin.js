const { chromium } = require('playwright');

const URL = 'https://search.caixin.com/newsearch/search?startDate=2013-01-20&endDate=2020-01-15&keyword=%E4%B8%AD%E5%9B%BD%2B%E8%B4%B8%E6%98%93%2B%E7%BE%8E%E5%9B%BD&channel=0&time=&type=1&sort=1&special=false';
const newsLinks = `.searchtext a`;
const newsIds = '.searchtext li';
const TITLE_SELECTOR = '.article h1';
const TIME_SELECTOR = '.article .artInfo';
const SUBHEAD_SELECTOR = '.article .subhead';
const CONTENT_SELECTOR = '.article #Main_Content_Val';

const data = new Map();

(async () => {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({ acceptDownloads: true });
  const page = await browser.newPage();

  await page.goto(URL, {timeout: 60000});
  
  // await page.waitForSelector(newsLinks);
  // const links = await page.$$(newsLinks);
  // console.log(`news count: ${links.length}`)

  await page.waitForSelector(newsIds)
  const idsEle = await page.$$(newsIds);
  const ids = []
  for await(var value of idsEle.values()) {
    ids.push(await value.getAttribute('id'));
  }
  // console.log(ids)

  const searchPageUrl = page.url()
  
  let count = 0

  for await(const [idx, id] of ids.entries()) {
    const eachNewsLink = await (await page.$(`a[href*="${id}"]`)).getAttribute('href')
    await page.goto(eachNewsLink, { timeout: 60000 });

    const title = await (page.locator(TITLE_SELECTOR)).innerText();
    const time = await (await (page.locator(TIME_SELECTOR)).innerText()).split(' ')[0]
    const subhead = await (page.locator(SUBHEAD_SELECTOR)).innerText();
    const content = await (page.locator(CONTENT_SELECTOR)).innerText();

    data.set(eachNewsLink, {title, time, subhead, content});    

    await page.goto(searchPageUrl, { timeout: 60000 });

    count++
    if (count == 3) break

    // const [newPage] = await Promise.all([
    //   context.waitForEvent('page', { timeout: 30000 }),
    //   page.click(eachLink) // Opens a new tab
    // ])
    // // const path = await newPage.title();
    // // console.log(path)  


    // await newPage.waitForLoadState('domcontentloaded', {timeout: 30000});
    // console.log(await newPage.title());

    // page.close()
  }
  console.log(data)

  await browser.close();
})();
