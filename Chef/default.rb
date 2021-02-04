#
# Cookbook Name:: learn_chef_httpd
# Recipe:: default
#
# Copyright (c) 2016 The Authors, All Rights Reserved.
 
# references:  
#   how to apply recipies - https://learn.chef.io/modules/local-development/rhel/virtualbox/apply-a-cookbook#/
#   how to create recipies - https://learn.chef.io/modules/learn-the-basics/rhel/virtualbox/configure-a-package-and-service#/
#   chef marketplace (where to get recipies) - https://supermarket.chef.io/
#   about recipies - https://docs.chef.io/recipes.html
 
# install apache
package 'httpd'
 
# run apache web server when instance starts
service 'httpd' do
  action [:enable, :start]
end
 
# creates a default homepage with "hello world"
file '/var/www/html/index.html' do
  content '<html>
  <body>
    <h1>hello world</h1>
  </body>
</html>'
end
