/*jshint esversion: 6 */

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const ajax = require('ajax');
const zerorpc = require('zerorpc')


var server = new zerorpc.Server({
	hello: function(name, reply) {
		reply(null, "Hello, " + name);
	}
});

server.bind("tcp://0.0.0.0:6969");

app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

// first: scrape html with inf_scroll.py

// second: set up server and form:
//app.get('/', function (req, res) {
//	res.render('index');
//});

//app.post('/', function (req, res) {
	//console.log(req.body.gucc);
//	var gucc = req.body.gucc;
//	res.render('index');
//});

//app.listen(6969, function () {
//	console.log('Patahack listening in on your 6969');
//});

//third: send input from form to patahack.py

//ajax({
//	type: "POST",
//	url: "home/g/Desktop/patahack/test.py",
	//contentType: "application/json; charset=utf-8",
//	data: gucc,
//	dataType: "json",
//	success: function (msg) {
//		alert("Success");
//	}
//});

//fourth: post it all back to the server...?

