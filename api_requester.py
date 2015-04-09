#!/usr/bin/python  
# -*- coding: utf-8 -*-

import argparse, urllib2, base64, json

DATACENTERS_PATH='datacenters/'
SERVERS_PATH='servers/'

# Gets a protected with basic auth URL with username and password
def get_auth_url(url, username, password):
    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)   
    try:
        return urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        return
   
# Returns the URL parameter of the args
def get_arg_url(parser):
    args = parser.parse_args()
    if not args.url.endswith('/'):
        args.url = args.url + '/'
    return args.url

# Returns the username parameter of the args
def get_arg_username(parser):
    args = parser.parse_args()
    return args.username

# Returns the password parameter of the args
def get_arg_password(parser):
    args = parser.parse_args()
    return args.password

# Returns all the datacenters
def get_datacenters(url, username, password):
    url = url + DATACENTERS_PATH
    result = get_auth_url(url, username, password)
    if result:
        return json.load(result)
    else:
        return None

# Given a server id returns the server info
def get_server(url, server, username, password):
    url = url + SERVERS_PATH + server
    result = get_auth_url(url, username, password)
    if result:
        return json.load(result)
    else:
        return None

# Starts the arg parser
def start_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', dest='url', help='Url of the API - default value http://localhost/', default='http://localhost/')
    parser.add_argument('-p', dest='password', help='Password of the basic auth user - default: test', default='test')
    parser.add_argument('-u', dest='username', help='Username of the basic auth - default: test', default='test')
    return parser


# Main: It gets the variables from the command line and gets all
# the datacenters, for every one it gets all the associated servers    
def main():
    parser = start_parser()
    url = get_arg_url(parser)
    password = get_arg_password(parser)
    username = get_arg_username(parser)

    datacenters = get_datacenters(url, username, password)
    for datacenter in datacenters:
        print "***************************************"
        print '- Datacenter: ' + datacenter['name']
        print '- Servers:'
        for server_text in datacenter['servers'].split(','):
            server = get_server(url, server_text, username, password)
            if server:
                print '- ' + server['name'] + ": " + server['description']
            else:
                print 'The server with the id ' + server_text + ' does not exist'

if __name__ == "__main__":
    main()

