
Feature: Transfers

    Scenario Outline: Transfer Money
        Given i open the app in [<device>]
        And i click the omit button
        And i write the email [<email>]
        And i write the password [<password>]
        And i click the login button
        And i am redirected to the MyAcount screen
        Given i click the transfers button
        And i select the first frecuent contact
        When i write [<money>] to send
        And i click the send button
        And i write a description [<desc>]
        And i click the send button
        And i write the cvv [<cvv>]
        And i confirm the cvv
        And i check if amount to send showed equals[<money>]
        And i confirm the send
        Then the successful send message is displayed
        And i click the back to my account button

        Examples:
            | device  | email              | password | money  | desc | cvv |
            | android | zuz@mailinator.com | Abc1234! | 200.00 | test | 123 |