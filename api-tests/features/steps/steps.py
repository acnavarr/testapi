import json

import requests
from behave import given, when, then
from hamcrest import assert_that, greater_than, is_in, equal_to


@given(u'The user sets REST API url "{service_name}"')
def step_set_url(context, service_name):
    context.api_url = context.api_host + "/" + service_name


@when(u'The user Sets HEADER param request with content type as "{header_content_type}"')
def step_headers(context, header_content_type):
    request_headers = {}
    request_headers['x-api-key'] = context.api_key
    request_headers['Content-Type'] = header_content_type
    context.headers = request_headers


@given(u'The user sets the API resource "{resource}"')
def step_resource(context, resource):
    context.api_resource = '{}/{}'.format(context.api_url, resource)


@when(u'Send HTTP method "{method}" with body "{body}"')
def step_get_request(context, method, body):
    if body!="{}":
        data = json.loads(body)
    else:data=None
    response = requests.request(method=method, url=context.api_resource,
                                json=data,params=context.params, headers=context.headers, verify=True)

    context.response = response


@then(u'The user receives a valid HTTP Response')
def step_validate_response_code(context):
    response_code = context.response.status_code
    assert_that(response_code, equal_to(200))


@then(u'The user receives a "{response_code}" HTTP Response')
def step_validate_response_code_parameter(context, response_code):
    response_code_out = context.response.status_code
    assert_that(response_code_out, equal_to(int(response_code)))



@when(u'execution time of "{resource}"')
def step_validate_field_first(context,resource):
    value = context.response.elapsed.total_seconds()

    value_milliseconds = int(round(value * 1000))

    print('execution time of '+ resource + ' :%i' % value_milliseconds)



@then(u'The field "{value}" is present in response')
def step_validate_field_referral(context, value):
    result_list = json.loads(context.response.text)
    assert_that(value, is_in(result_list["message"]))




@then('The user checks service with {jsonName}')
def check_(context,jsonName):
    json_response_value=""
    url_json ='schemas/' + jsonName +'.json'
    file1 = open('log/contract_fail_'+jsonName+'.txt', 'w')
    cont=0
    with open(url_json) as file:
        json_data = json.load(file)
    json_response=json.loads(context.response.text)
    if len(json_response) > 0:
        if type(json_response)==list:
          json_response_value=json_response[0]
        elif type(json_response)==dict:
            json_response_value=json_response
        for k in json_data.keys():
            if type(json_data[k])!=type(json_response_value[k]):
                file1.write("field = " + k + " Expected:"+ str(type(json_data[k])) + " but: was" + str(type(json_response_value[k])) + "\n")
                cont += 1
            if type(json_data[k]) == dict and len(json_data[k]) > 0:
                for l in json_data[k].keys():
                    if type(json_data[k][l]) != type(json_response_value[k][l]):
                        file1.write("field = " + k + " Expected:" + str(type(json_data[k][l])) + " but: was" + str(
                            type(json_response_value[k][l])) + "\n")
                        cont += 1
    file1.close()
    assert_that(cont, equal_to(0))



@when("The user sets path {page} and {limit}")
def step_impl(context, page, limit):
    request_params = {}
    request_params['limit'] = limit
    request_params['page'] = page
    context.params = request_params

@then('The user checks limit {limit}')
def check_limit(context,limit):
    json_response = json.loads(context.response.text)
    assert_that(len(json_response),equal_to(int(limit)))

@then('The user checks page {page}')
def check_limit(context,page):
    url = context.response.url
    assert_that('page='+page,is_in(url))