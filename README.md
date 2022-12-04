# RoofStacks Test Automation Study Case

[![Python](https://img.shields.io/badge/Python-yellow?style=flat&logo=python)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-orange?style=flat&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Allure](https://img.shields.io/badge/-Allure-green)](https://docs.qameta.io/allure/)

![RoofStacks Logo](/roofstacks-logo.png)

## Project Goal:

This project aims to cover all the possible test scenarios for the given endpoints using Python PyTest.<br />

## Work Plan:

Day 1: Creation of base structure & determination of the tools & frameworks going to be used.<br />
Day 2: Creation of test cases for "Create User" request and building required functions.<br />
Day 3: Creation of test cases for "Get User List" & "Get User By ID" & "Remove User" requests and building required
functions.<br />
Day 4: Creation of test cases for "Switch User Activity" & "Update User Info" requests and building required functions.
Refactoring the code.<br />
Day 5: Continue creation of test cases for "Update User Info" request and building required functions. Adding allure
report for the test suite. Editing README.md<br />
<br />

## Worklog:

Day 1: Creation of base structure & determination of the tools & frameworks going to be used.<br />
Day 2: Creation of test cases for "Create User" request and building required functions.<br />
Day 3: Creation of test cases for "Create User" request has completed. Started working on "Get User List" & "Get User By
ID" & "Remove User" requests<br />
Day 4: Project Structure & code refactored. "Switch User Activity" test cases & automation completed.<br />
Day 5: "Update User Info" test cases & automation completed. README.md file edited.<br />

## Introduction & Project Structure

All the test data sets for test cases are included in ./config/test_datas.py file. For some endpoints, request body has
generated dynamically with given parameters.<br />
Test scripts are located in ./tests/test_api.py<br />
Example test results can be found at ./Test Results folder<br />

## Setup & Run

1. Clone the repository.

~~~
git clone https://github.com/burkisilin/RoofStacks_API_Test_Case.git
~~~

2. Install all dependencies.

~~~
pip install -r requirements.txt
~~~

3. Type the following commands to run the tests.

Run All Tests

~~~
pytest
~~~

Run All Tests On Different Environment or Different Base URI

~~~
pytest --BASE_URI https://yourENVurl.com
~~~

Run All Tests and Save Logs

~~~
pytest --SAVE_LOG yourLogName
~~~

## ALLURE REPORT
![allure_report_example](https://user-images.githubusercontent.com/13181041/205501354-0e735ce3-bf85-478c-842b-1e42d9c2bdc1.gif)


![Allure Report Example](https://giphy.com/6fabcb98-5009-4293-86d8-6c9aa57cfbea)


- https://github.com/allure-framework/allure2/releases allure is downloaded and defined in system variables. In
  addition, the necessary packages for Python are downloaded via pip with the following command

```
pip install allure-pytest
```

- The following command is run on the command prompt to run the tests with allure report

```
pytest --alluredir="pathToAllureReportsFolder"
```

- Finally, the command below is run through the command prompt to view the reports.

```
allure serve pathToAllureReportsFolder
```

## HTML REPORT

Another way we view our test run reports is PyTest HTML reporting. We can easily create an HTML report page for our
tests by running the command below through the command prompt.

```
pytest --html=reportFileName.html --capture=tee-sys
```

# TEST CASES

| Scenario Name                                                     | Scenario Description                                                            | Expected Status Code | Status |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------|----------------------|--------|
| Create user - Register Success                                    | The user is created with default request body                                   | 201                  | Failed |
| Create user - Minimum Values                                      | The user is created by entering the minimum values for the required fields.     | 201                  | Failed |
| Create user - Mid Values                                          | The user is created by entering the mid values for the required fields.         | 201                  | Failed |
| Create user - Max Values                                          | The user is created by entering the maximum values for the required fields.     | 201                  | Failed |
| Create user - Empty Firstname Field                               | The user is created by leaving the Firstname Field Empty.                       | 400                  | Failed |
| Create user - Empty Lastname Field                                | The user is created by leaving the Lastname Field Empty.                        | 400                  | Failed |
| Create user - Empty username Field                                | The user is created by leaving the Username Field Empty.                        | 400                  | Failed |
| Create user - Empty Password Field                                | The user is created by leaving the Password Field Empty.                        | 400                  | Failed |
| Create user - Firstname & Lastname Fields Empty                   | The user is created by leaving the Firstname & Lastname Fields Empty.           | 400                  | Failed |
| Create user - Firstname & Lastname & username Fields Empty        | The user is created by leaving the Firstname & Lastname & Username Fields Empty. | 400                  | Failed |
| Create user - All Fields Empty                                    | The user is created by leaving the All Fields Empty.                            | 400                  | Failed |
| Create user - Empty Lastname & username Field                     | The user is created by leaving the Lastname & Username Fields Empty.            | 400                  | Failed |
| Create user - Empty Lastname & username & Password Field          | The user is created by leaving the Lastname & Username & Password Fields Empty. | 400                  | Failed |
| Create user - Empty username & Password Field                     | The user is created by leaving the Username & Password Fields Empty.            | 400                  | Failed |
| Create user - Empty Password Field                                | The user is created by leaving the Password Field Empty.                        | 201                  | Failed |
| Create user - Firstname Alphanumeric                              | The user is created with Alphanumeric Firstname                                 | 400                  | Failed |
| Create user - Firstname Numeric                                   | The user is created with Numeric Firstname                                      | 400                  | Failed |
| Create user - Firstname Symbolic                                  | The user is created with Symbolic Firstname                                     | 400                  | Failed |
| Create user - Firstname Alphanumeric & Symbolic                   | The user is created with Alphanumeric & Symbolic Firstname                      | 400                  | Failed |
| Create user - Lastname Alphanumeric                               | The user is created with Alphanumeric Lastname                                  | 400                  | Failed |
| Create user - Lastname Numeric                                    | The user is created with Numeric Lastname                                       | 400                  | Failed |
| Create user - Lastname Symbolic                                   | The user is created with Symbolic Lastname                                      | 400                  | Failed |
| Create user - Lastname Alphanumeric & Symbolic                    | The user is created with Alphanumeric & Symbolic Lastname                       | 400                  | Failed |
| Create user - username Alpha                                      | The user is created with Alphanumeric Username                                  | 400                  | Failed |
| Create user - username Numeric                                    | The user is created with Numeric Username                                       | 400                  | Failed |
| Create user - username Symbolic                                   | The user is created with Symbolic Username                                      | 400                  | Failed |
| Create user - username AlphaNumeric & Symbolic                    | The user is created with Alphanumeric & Symbolic Username                       | 400                  | Failed |
| Create user - Password Alpha                                      | The user is created with Alpha Password                                         | 201                  | Failed |
| Create user - Password AlphaNumeric                               | The user is created with Alphanumeric Password                                  | 201                  | Failed |
| Create user - Password Numeric                                    | The user is created with Numeric Password                                       | 201                  | Failed |
| Create user - Password Symbolic                                   | The user is created with Symbolic Password                                      | 201                  | Failed |
| Create user - Password AlphaNumeric & Symbolic                    | The user is created with Alphanumeric & Symbolic Password                       | 201                  | Failed |
| Create user - Firstname Is Below Min Value                        | The user is created with Firstname Field below Min Value                        | 400                  | Failed |
| Create user - Firstname & Lastname Are Below Min Value            | The user is created with Firstname & Lastname Fields below Min Value            | 400                  | Failed |
| Create user - Firstname & username Are Below Min Value            | The user is created with Firstname & Username Fields below Min Value            | 400                  | Failed |
| Create user - Firstname & Lastname & username Are Below Min Value | The user is created with Firstname & Lastname & Username Fields below Min Value | 400                  | Failed |
| Create user - LastName Is Below Min Value                         | The user is created with Lastname Field below Min Value                         | 400                  | Failed |
| Create user - LastName & username Are Below Min Value             | The user is created with Lastname & Username Fields below Min Value             | 400                  | Failed |
| Create user - username Is Below Min Value                         | The user is created with Username Field below Min Value                         | 400                  | Failed |
| Create user - Firstname Is Above Max Value                        | The user is created with Firstname Field above Max Value                        | 400                  | Failed |
| Create user - Firstname & Lastname Are Above Max Value            | The user is created with Firstname & Lastname Fields above Max Value            | 400                  | Failed |
| Create user - Firstname & username Are Above Max Value            | The user is created with Firstname & Username Fields above Max Value            | 400                  | Failed |
| Create user - Firstname & Lastname & username Are Above Max Value | The user is created with Firstname & Lastname & Username Fields above Max Value | 400                  | Failed |
| Create user - LastName Is Above Max Value                         | The user is created with Lastname Field above Max Value                         | 400                  | Failed |
| Create user - LastName & username Are Above Max Value             | The user is created with Lastname & Username Fields above Max Value             | 400                  | Failed |
| Create user - username Is Above Max Value                         | The user is created with Username Field above Max Value                         | 400                  | Failed |
| Create User Integration Test                                      | The user is created succesfully and can be found at "/users" endpoint           | 201                  | Failed |
|                                                                   |                                                                                 |                      |        |
| Get User List - Success                                           | The "/users" endpoint returns users                                             | 200                  | Ok     |
|                                                                   |                                                                                 |                      |        |
| Get User - Valid User ID                                          | The user can be found                                                           | 200                  | Ok     |
| Get User - Valid User ID 2                                        | The user can be found                                                           | 200                  | Failed |
| Get User - Invalid User ID                                        | User could not be found, proper error should be returned                        | 404                  | Ok     |
| Get User - Invalid User ID 2                                      | User could not be found, proper error should be returned                        | 404                  | Ok     |
| Get User - Empty User ID                                          | User could not be found, proper error should be returned                        | 404                  | Failed |
|                                                                   |                                                                                 |                      |        |
| Remove User - Valid User ID                                       | The user should be removed successfully                                         | 204                  | Failed |
| Remove User - Invalid User ID                                     | Deletion should not be done, proper error should be returned                    | 404                  | Ok     |
| Remove User - Empty User ID                                       | Deletion should not be done, proper error should be returned                    | 404                  | Failed |
|                                                                   |                                                                                 |                      |        |
| Switch User Activity - Valid User ID - isActive: True (Boolean)   | User Activity should be set to True                                             | 200                  | Failed |
| Switch User Activity - Valid User ID - isActive: False (Boolean)  | User Activity should be set to False                                            | 200                  | Failed |
| Switch User Activity - Valid User ID - isActive: true (String)    | User Activity should not be set, proper error should be returned                | 400                  | Failed |
| Switch User Activity - Valid User ID - isActive: false (String)   | User Activity should not be set, proper error should be returned                | 400                  | Failed |
| Switch User Activity - Valid User ID - isActive: Empty            | User Activity should not be set, proper error should be returned                | 400                  | Failed |
| Switch User Activity - Invalid User ID                            | User Activity should not be set, proper error should be returned                | 400                  | Failed |
|                                                                   |                                                                                 |                      |        |
| Update User Info - Min Values                                     | The user info is updated by entering the minimum values for the required fields. | 200                  | Failed |
| Update User Info - Mid Values                                     | The user info is updated by entering the mid values for the required fields.    | 200                  | Failed |
| Update User Info - Max Values                                     | The user info is updated by entering the maximum values for the required fields. | 200                  | Failed |
| Update User Info - Empty firstName Field                          | The user info is updated by leaving the Firstname Field Empty.                  | 400                  | Failed |
| Update User Info - Empty lastName Field                           | The user info is updated by leaving the Lastname Field Empty.                   | 400                  | Failed |
| Update User Info - Empty firstName & lastName Fields              | The user info is updated by leaving the Firstname & Lastname Fields Empty.      | 400                  | Failed |
| Update User Info - Firstname & Lastname Alpha                     | The user info is updated with Alpha Firstname & Alpha Lastname fields           | 200                  | Failed |
| Update User Info - Firstname Numeric                              | The user info is updated with Numeric Firstname field                           | 400                  | Failed |
| Update User Info - Firstname AlphaNumeric                         | The user info is updated with Alphanumeric Firstname field                      | 400                  | Failed |
| Update User Info - Firstname Symbolic                             | The user info is updated with Symbolic Firstname field                          | 400                  | Failed |
| Update User Info - Firstname AlphaNumeric & Symbolic              | The user info is updated with AlphaNumeric & Symbolic Firstname field           | 400                  | Failed |
| Update User Info - Lastname Numeric                               | The user info is updated with Numeric Lastname field                            | 400                  | Failed |
| Update User Info - Lastname AlphaNumeric                          | The user info is updated with Alphanumeric Lastname field                       | 400                  | Failed |
| Update User Info - Lastname Symbolic                              | The user info is updated with Symbolic Lastname field                           | 400                  | Failed |
| Update User Info - Lastname AlphaNumeric & Symbolic               | The user info is updated with AlphaNumeric & Symbolic Lastname field            | 400                  | Failed |
| Update User Info - Firstname Below Min Value                      | The user info is updated with Firstname Field below Min Value                   | 400                  | Failed |
| Update User Info - Lastname Below Min Value                       | The user info is updated with Lastname Field below Min Value                    | 400                  | Failed |
| Update User Info - Firstname & Lastname are Below Min Value       | The user info is updated with Firstname & Lastname Fields below Min Value       | 400                  | Failed |
| Update User Info - Firstname Above Max Value                      | The user info is updated with Firstname Field above Max Value                   | 400                  | Failed |
| Update User Info - Lastname Above Max Value                       | The user info is updated with Lastname Field above Max Value                    | 400                  | Failed |
| Update User Info - Firstname & Lastname are Above Max Value       | The user info is updated with Firstname & Lastname Fields above Max Value       | 400                  | Failed |
| Update User Info - Invalid Field                                  | The user info is updated with invalid field                                     | 400                  | Failed |
| Update User Info - Invalid User ID                                | The user info of an invalid user updated                                        | 400                  | Failed |
