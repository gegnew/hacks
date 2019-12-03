# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

Forecast.delete_all

Forecast.create! (
  [
    {
      source: 'https://www.mtavalanche.com/forecast',
      forecast: "This is a test forecast"
    }
  ]
)
puts "Forecasts seeded!"
