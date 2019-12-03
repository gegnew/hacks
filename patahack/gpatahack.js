/*jshint esversion: 6 */
var axios = require('axios');
var cheerio = require('cheerio');
var fs = require('fs');

axios.get('https://wornwear.patagonia.com/shop/mens')
.then((response) => {
	if(response.status === 200) {
		const html = response.data;
			const $ = cheerio.load(html);
		console.log($);
	}
}).catch(function(err) {
  console.log("Fricken error");
	console.log(err);
});






















