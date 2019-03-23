var Crawler = require("js-crawler");
var cheerio = require("cheerio");
var newstitle, URL, date;
var newsItem = {newstitle, URL, date};
var newsList = [];
 
new Crawler().configure({depth: 2})
  .crawl("https://www.cnn.com/specials/politics/president-donald-trump-45", function onSuccess(page) {
  if (page.url.includes('trump')) {
//    var updateTime = page.getElementsByClassName("timingText")[0];
    var $ = cheerio.load(page.body);

//    console.log($('title').text());
//    console.log(page.url);
//    console.log(page.error);
    console.log($('.update-time').text());
//    console.log($('.timingText').text());
    newsItem.newstitle = $('title').text(); 
    newsItem.URL = page.url; 
    newsItem.date = $('.update-time').text();
    if (typeof newsItem.date == 'null') {
        newsItem.date = $('.timingText').text();
    }
//    console.log(newsItem.date);
//    console.log(date);
    newsList.push(newsItem);
  }
  }, null, function onAllFinished(crawledUrls) {
    console.log('All crawling finished');
    console.log(newsList);
  });
