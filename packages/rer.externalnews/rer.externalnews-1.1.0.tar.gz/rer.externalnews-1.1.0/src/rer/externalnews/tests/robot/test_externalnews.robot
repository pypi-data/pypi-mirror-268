# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s rer.externalnews -t test_externalnews.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src rer.externalnews.testing.RER_EXTERNALNEWS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_externalnews.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a ExternalNews
  Given a logged-in site administrator
    and an add externalnews form
   When I type 'My ExternalNews' into the title field
    and I submit the form
   Then a externalnews with the title 'My ExternalNews' has been created

Scenario: As a site administrator I can view a ExternalNews
  Given a logged-in site administrator
    and a externalnews 'My ExternalNews'
   When I go to the externalnews view
   Then I can see the externalnews title 'My ExternalNews'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add externalnews form
  Go To  ${PLONE_URL}/++add++ExternalNews

a externalnews 'My ExternalNews'
  Create content  type=ExternalNews  id=my-externalnews  title=My ExternalNews


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the externalnews view
  Go To  ${PLONE_URL}/my-externalnews
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a externalnews with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the externalnews title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
