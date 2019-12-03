require 'nokogiri'
require 'openssl'
require 'open-uri'
doc = Nokogiri::HTML(open('https://avalanche.state.co.us/', :ssl_verify_mode => OpenSSL::SSL::VERIFY_NONE))
# doc.xpath('//li[@id="menu-item-307"]/ul').each do |node|
names = []
hrefs = []
doc.css('li.menu-item-67 > ul > li').each do |node|
  # puts node.children.attribute('href')
  names = names << node.children.text
  hrefs = hrefs << node.children.attribute('href')
end
