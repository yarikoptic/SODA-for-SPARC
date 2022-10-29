const webdriver = require("selenium-webdriver");
const driver = new webdriver.Builder()
  // The "9515" is the port opened by ChromeDriver.
  .usingServer("http://localhost:9515")
  .withCapabilities({
    "goog:chromeOptions": {
      // Here is the path to your Electron binary.
      binary:
        "/home/cmarroquin/Desktop/SODA-for-SPARC/dist/SODA for SPARC-9.3.1.AppImage/resources/app",
    },
  })
  .forBrowser("chrome") // note: use .forBrowser('electron') for selenium-webdriver <= 3.6.0
  .build();
// driver.get('http://www.google.com')
// driver.findElement(webdriver.By.name('q')).sendKeys('webdriver')
// driver.findElement(webdriver.By.name('btnG')).click()
// driver.wait(() => {
//   return driver.getTitle().then((title) => {
//     return title === 'webdriver - Google Search'
//   })
//}, 1000)
driver.quit();
