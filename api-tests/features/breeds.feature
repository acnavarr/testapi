Feature: Test resource for the breeds API

  Background:
    Given The user sets REST API url "v1"

  Scenario Outline:1. GET resource to breeds
    Given The user sets the API resource "<resource>"
    When The user sets HEADER param request with content type as "application/json"
    And Send HTTP method "<method>" with body "<body>"
    Then The user receives a valid HTTP Response
    And The user checks service with <service>
    Examples:
      | resource    | method | body |service|
      | breeds      | GET    | {}   |response-breeds|
      | breeds/chau | GET    | {}   |response-breeds-breed_id|

#
  Scenario Outline:1. GET resource to breeds with limit and page
    Given The user sets the API resource "breeds"
    When The user sets HEADER param request with content type as "application/json"
    And The user sets path <page> and <limit>
    And Send HTTP method "<method>" with body "<body>"
    Then The user receives a "<response_code>" HTTP Response
    And The user checks limit <limit>
    And The user checks page <page>
    Examples:
      | method | body |response_code|page|limit|
      | GET    | {}   |     200      | 10   |   5  |
      | GET    | {}   |     200      | 8   |   6 |


  Scenario Outline:1. GET resource to breeds, bad path
    Given The user sets the API resource "<resource>"
    When The user sets HEADER param request with content type as "application/json"
    When Send HTTP method "<method>" with body "<body>"
    Then The user receives a "<response_code>" HTTP Response
    And The field "<value>" is present in response
    Examples:
      | resource    | method | body |response_code|value|
      | breed      | GET    | {}   |404|   404 - please consult the documentation for correct url to call. https://docs.thecatapi.com/             |
