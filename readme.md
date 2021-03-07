# Example of Android UI Testing Framework using Python3, Pytest, Pytest-bdd, Appium, Allure, and Selenium Grid.
#### Run locally :
* Install [Python3](https://www.python.org/downloads/)
* Install [Appium- Appium-mac-1.15.1.dmg](https://github.com/appium/appium-desktop/releases/tag/v1.15.1)
* Install [appium-doctor](https://www.npmjs.com/package/appium-doctor)
* Java and Android Studio installed, adb is reachable from the Terminal
* Android studio is installed and ANDROID_HOME and JAVA_HOME in path vim .bash_profile
```
JAVA_HOME=/usr/bin/java
export JAVA_HOME;
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-13.0.1.jdk/Contents/Home;
export ANDROID_HOME=/Users/Name.LastName/Library/Android/sdk;
export PATH=$PATH:$ANDROID_HOME/platform-tools;
export PATH=$PATH:$ANDROID_HOME/build-tools;
export PATH=$PATH:$ANDROID_HOME/tools;
export PATH=$PATH:$ANDROID_HOME/platform-tools/bin;
```
* Install Allure
```
$ brew install allure
```
* Install virtualenv
    ```
    $ cd to project Directory
    $ python3 -m pip install virtualenv
    $ python3 -m virtualenv env
    $ source env/bin/activate
    ```
* Install requirements
```
(env) $ pip install -r requirements.txt
```
* get deviceName using adb
```
$ adb devices
List of devices attached
KYV7N15B14006508        device
```
* Run Appium Server on 4723 port
* Validate that appium Server is reachable
[http://127.0.0.1:4723/wd/hub](http://127.0.0.1:4723/wd/hub)
```
Validate in browser : The URL '/wd/hub' did not map to a valid resource
```
* RUN
```
(env) $ python -m  pytest -p no:randomly  --appium_server_url "http://127.0.0.1:4723/wd/hub"  --video_recorder "True" --step_with_screenshot "True" --path_to_apk "apk/testApp.apk" tests
```

#### Quick Start with an Emulator:
* Instal node
    ```
    $ brew install node  
    ```
* Instal appium
    ```
    $ npm install -g appium
    ```
* Start Emulator from Android Studio

* Run "adb devices" to get emulator name
    ```
    $ adb devices
    * daemon not running; starting now at tcp:5037
    * daemon started successfully
    List of devices attached
    emulator-5554
    ```
* Start Appium server
    ```
    appium -p 4723 -U emulator-5554
    ```
* RUN
    ```
    (env) $ python -m  pytest -p no:randomly  --appium_server_url "http://127.0.0.1:4723/wd/hub" --video_recorder "False" --step_with_screenshot "True" --path_to_apk "/apk/testApp.apk" tests
    ```

### Setting up Android devices for CI/C:

* download selenium grid, or use version in repo :
  [](https://www.selenium.dev/downloads/)

* Install Android Studio

* Make sure adb is working

* Get Id of devices:

    ```
    $ adb devices
    List of devices attached
    57585546381232133	device
    988a16424a4541233	device
    KYV7N15B140011231	device
    ```

* Install node

    ```
    $ brew install node  
    ```

* Install Appium


    ```
    $ npm install -g appium
    ```

* Create copies of nodeconfig-android.json for desired quantity of
  devices, modify  "browserName" and "systemPort" values:


     ```
     nodeconfig-android.json:
     
           "browserName":  "Nexys6P",  
           "systemPort": "8201
           
     nodeconfig-android2.json:
     
           "browserName":  "S8Plus",  
           "systemPort": "8202
           
     nodeconfig-android3.json:
     
           "browserName":  "S9",  
           "systemPort": "8203                      
    ```


*  Start Selenium Grid as a Hub :

    ```
        java -jar selenium-server-standalone-3.141.59.jar -port 4444 -role hub
    ```

* Run Appium on desirable port:

    ```
    $ appium -p 4723 --nodeconfig nodeconfig-android1.json -U KYV7N15B140033334
    $ appium -p 4724 --nodeconfig nodeconfig-android2.json -U 988a16424a4222243
    $ appium -p 4725 --nodeconfig nodeconfig-android3.json -U 57585546385dewe38
    ```

* Validate devices in Selenium grid Console

[](http://localhost:4444/grid/console)

* Run :
  ```
  ( env) $  python -m  pytest -p no:randomly --alluredir=report --appium_server_url "http://localhost:4444/wd/hub"  --video_recorder "True" --step_with_screenshot "True" --path_to_apk "/apk/testApp.apk" tests
  ```
      ***Note:***
  *Tests will be distributed across devices*


##### How to add UI tests
Open "tests/bdd/unordered/*.feature" file or Create new Scenario with
shared given statement "I'm a Tester". Please use predefined Then steps,
see statements below.
```
    Usage: "Given"
        Given I'm a Tester
    Allowed statements: "Then"
        Tap on "LOCATOR", By "BY"
        Validate element is presented "LOCATOR", By "BY"
        In field "LOCATOR" type "STRING", By "BY"
        Validate text "LOCATOR", "STRING", By "BY"
        Click arrow back
        Wait "SEC"
        Open a deep link "URL"
    Allowed type locators : ID, XP = XPATH, AI = Accessibility Identifier
 ```
