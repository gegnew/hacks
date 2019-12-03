const request = require('request');
const argv = require('yargs').argv;

// TODO: unexpose this api key
let apiKey = '4816e05345cf9358a4a93693b4adc048';
let city = argv.c || 'portland';
let url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&units=imperial&appid=${apiKey}`

// console.log(`${apiKey}`)

request(url, function (err, response, body) {
	if(err){
		console.log('error:', error);
		console.log('heckin error');
	} else {
		console.log('body:', body);
		let weather = JSON.parse(body)

		if(weather.main == undefined){
			res.render('index', {weather: null, error: 'that aint a city'});
		} else {
			let weather Text = `It's ${weather.main.temp} degrees in ${weather.name}.`;
			res.render('index', {weather: weatherText, error: null});
			
		let message =	`It's ${weather.main.temp} degrees in ${weather.name}!`;
		console.log(message);
		// console.log(weather);
	}
});


