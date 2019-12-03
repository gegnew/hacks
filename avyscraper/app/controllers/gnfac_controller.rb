class GnfacController < ApplicationController

  def todaysforecast
    require 'openssl'
    require 'open-uri'
    doc = Nokogiri::HTML(open('https://www.mtavalanche.com/forecast/', :ssl_verify_mode => OpenSSL::SSL::VERIFY_NONE))
    discussion = doc.css('.discussion')
    @formatteddiscussion = discussion.text
    render template: 'gnfac/home'

  end
end
