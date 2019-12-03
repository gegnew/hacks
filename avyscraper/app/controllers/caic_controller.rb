class CaicController < ApplicationController

  def todaysforecast
    require 'openssl'
    require 'open-uri'
    doc = Nokogiri::HTML(open('https://avalanche.state.co.us/', :ssl_verify_mode => OpenSSL::SSL::VERIFY_NONE))
    # discussion = doc.css('#menu-item-95 > a:nth-child(1)')
    # get_zones = doc.css('#menu-item-67 > ul:nth-child(2)')
  names = []
  hrefs = []
  # get all the avalanche zones and links to their pages
  doc.css('li.menu-item-67 > ul > li').each do |node|
    names = names << node.children.text
    hrefs = hrefs << node.children.attribute('href')
  end
  node = Nokogiri::HTML(open('https://avalanche.state.co.us/forecasts/backcountry-avalanche/steamboat-flat-tops/'))
  # node = forecast.css('div.row:nth-child(3)')
  # node = forecast.css('/html/body/div.site-container/div.site-inner')
  # node = forecast.css('/html')
  iframe_source = node.at_css('div.entry-content > iframe').attribute('src')
  iframe_content = Nokogiri::HTML(open('https://avalanche.state.co.us/' + iframe_source))
  #/html/body/div/div/form/div/div[1]/div[2]/div[2]
  #html body div#wrapper.container div#content form#arc_form div.tabs div#avalanche-forecast div.row div.span4.fx-text-area
  @formatteddiscussion = iframe_content
  # render template: 'caic/home'
  render html: @formatteddiscussion
  end


end
