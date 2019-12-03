# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

Rails.application.routes.draw do
  #get 'pages/home'
  root to: "pages#home"
  namespace :api, defaults: {format: :json } do
    resources :forecasts, only: [ :show ]
  end
  get '/gnfac' => 'gnfac#todaysforecast'
  get '/caic' => 'caic#todaysforecast'
end
