Feature: Login

    Feature Description

    Scenario Outline: Login with correct user
        Given i open the app in [<device>]
        And i click the omit button
        And the login button is disabled
        When i write the email [<email>]
        And i write the password [<password>]
        Then the login button is enabled
        And i click the login button
        And i am redirected to the MyAcount screen

        Examples:
            | device  | email              | password |
            | android | zuz@mailinator.com | Abc1234! |