# each request to API should include Accept header with api version:
# application/vnd.map-me.v1+json
require 'api_constraints'



Rails.application.routes.draw do

  
  resources :items
  post 'authenticate', to: 'authentication#authenticate'

  namespace :api, defaults: {format: :json }, constraints: {subdomain: 'api' }, path: '/' do
    scope module: :v1, constraints: ApiConstraints.new(version:1, default: true) do
      resources :comments
    end
  end

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
