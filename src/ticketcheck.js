var page = require('webpage').create();

var siteUrl = "http://prime.paxsite.com/";

page.open(siteUrl, function(status) {
    if (status !== 'success') {
      console.log('FAIL to load the address');
    }
    else {
      var soldOutElement = document.querySelectorAll('li.soldOut');
      if(soldOutElement) {
          console.log("PAX Tickets still sold out :(");
      }
    }
    phantom.exit();
});