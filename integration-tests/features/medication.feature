Feature: Medication management
    As a system administrator
    I want to manage medications
    So that patients' treatment can be recorded accurately

    Scenario: New medication is created
        When a new medication is created
        Then the medication can be seen in the medication list
        And the medication can be retrieved by its uuid
        And the medication matches that previously created

    Scenario: Medication update
        Given a new medication is created
        When the medication is updated
        Then the updated medication is persisted

    Scenario: Medication delete
        Given a new medication is created
        When the medication is deleted
        Then the medication can not be seen in the medication list
        And the medication can not be retrieved by its uuid

    Scenario: Medication tagging
        When a new medication is created
        Then the medication can be retrieved by its tags

    Scenario: Static medications
        Then there are the expected UK-DEFAULT medications for GDM
        And there are the expected UK-DEFAULT medications for DBM
        And there are the expected US-DEFAULT medications for GDM
        And there are the expected US-DEFAULT medications for DBM
        And there are the expected JFH medications for GDM
        And there are the expected JFH medications for DBM
        And there are the expected USTRAINING medications for GDM
        And there are the expected USTRAINING medications for DBM
