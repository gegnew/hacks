class Api::ForecastsController < ApplicationController
  def show
    @forecast = Forecast.find(params[:id])
  end
end
