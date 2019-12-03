class ApplicationController < ActionController::API

  # respond_to :json

  before_action :authenticate_request
  attr_reader :current_user
  # before_action :ensure_json_request

  def authenticate_request
    @current_user = AuthorizeApiRequest.call(request.headers).result
    render json: { error: 'Not Authorized' }, status: 401 unless @current_user
  end

  # def ensure_json_request
  #   return if request.format == :json
  #   render :nothing => true, :status => 406
  # end

end
