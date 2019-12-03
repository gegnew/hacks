# README

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

* Ruby version

* System dependencies

* Configuration

* Database creation

* Database initialization

* How to run the test suite

* Services (job queues, cache servers, search engines, etc.)

* Deployment instructions

* ...



####Blow-by-blow build, for future writeup:

rails new map_me_api --api --database=postgresql

#followed this thru part 1:
https://blog.shakacode.com/isomorphic-react-with-rails-part-i-440754e82a59

and then part 2 up to "Create resource":
https://blog.shakacode.com/isomorphic-react-with-rails-part-ii-614980b65aef

Switched over to this:
https://medium.com/@anaharris/how-to-make-a-simple-map-app-using-ruby-on-rails-react-and-leaflet-part-1-backend-cc4d285d9008

#At the "Preparing data" section, I followed this:
https://cobwwweb.com/how-to-write-a-custom-rake-task
    and made a rake task to build db seeds

#Then I continued on to the "Importing data" section and improvised, based on what I found here:
http://www.bryceholcomb.com/2015/02/10/mapbox-and-rails/
and here:
http://vladigleba.com/blog/2013/11/14/using-mapbox-with-ruby-on-rails/

Basically, I set up a rake task to get the new user authentication token from strava, using
'strava-ruby-client' from dblock

# Setting up token-based authentication, based on:
Shoot. This sets up token-based authentication for my users, but doesn't store the Strava token
https://www.pluralsight.com/guides/token-based-authentication-with-ruby-on-rails-5-api

Noting only differences from tutorial:
added gem 'bcrypt' to Gemfile (tutorial says to do '~> 3.1.7'...we'll do this if something breaks)

# I'm trying to do this, I think, but @anaharris gets her data in a Rake task
It looks like I could make a rake task that loops through every user and pulls in their routes
I think I'll try to use this tutorial instead of the rake task, so that I don't have to loop through every user's data...?
https://revs.runtime-revolution.com/integrating-a-third-party-api-with-rails-5-134f960ddbba
