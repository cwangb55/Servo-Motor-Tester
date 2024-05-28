# Servo-Motor-Tester

First of all, I am experienced in software programming, but new to almost everything (robotics, mechanical design, 3D printing, motors, Arduino). As a result, the design and implementation are far from satisfactory. Please feel free to use, improve, or comment.

This project is test simple Servo Motor such as MG90S and MG996R, which provides no feedback. My objective is to test the angle accuracy using a potentiometer. I am using a B10K (linear resistenance distribution, 10K Ohm) potentiometer with 300 degree rotation range.

## 3-D print tester rig
Hold a servo motor and a potentiometer in sync. The model is created using FreeCAD 0.21.2. It contains 4 parts:
* MotorBase to secure MG90S servo motor, it also contains a measuring (half) circle with repeated polar lines 10 degrees apart for measurement. The ciricle is centered at the servo motor shaft center. 
* MotorMount to connect the shaft of the servo motor with a small arm and downward needle pointing to the measuring circle.
* PotentiometerBase to secure the B10K potentiometer and connect with the MotorBase via a screw. It is separated from the MotorBase so that Potentiometer can be installed.
* PotentiometerKnob to sync the rotation of the potentiometer knob and the servo motor shaft. It is separated from the MotorMount since the MotorMount has a hole from top to secure it to the shaft.

STL files are included (export from FreeCAD), and gcode files are included for my Creality Ender 3 S1 Pro printer, using CrealityPrint with 0.4mm nozzle and CR-PLA High Quality settings. 

## Arduino test code
I would like to set random angles, and read potentiometer values back. 

I followed https://docs.arduino.cc/learn/electronics/servo-motors/, to initially have challenges to actuate the motor (I searched pin 9, found D6 mapping to pin 9). Eventually, I purchased a new Arduino Nano (my old one needs to use Old Bootloader) and tried D9, instead of D6, on my Arduino Nano, which works.  

In the end, I used the following:
* Breadboard with power module to provide 5V power for motor
* Arduino Nano
    * Arduino NEG to breadboard power module GND
* MG90S servo 
    * Brown to Arduino GND
    * Red to breadboard power module +5V
    * Yellow to Arduino Nano D9
* Potentiometer 
    * Left (assume knob on top) to Arduino +5
    * Right to Arduino GND
    * Middle to Arduino A5 (you can change this along with the Sketch code, I used other Analog pins for other purposes)

## Result analysis

I used scikit-learn LinearRegression, and got a slope of -3.4791. The expected slope is -1024/300 = -3.4133 (since 300 degree is represented by a number between 0 and 1023). The error is 2%. The linear regression fit is reasonable (0.998 R-squared score), and rooted mean squared error is 7.836 (the range is 0 to 1023). 

The MG90S servo is purchased from [AliExpress](https://www.aliexpress.us/item/3256806367285184.html?src=google&src=google&albch=shopping&acnt=708-803-3821&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&src=google&albch=shopping&acnt=708-803-3821&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=en3256806367285184&ds_e_product_merchant_id=107793278&ds_e_product_country=US&ds_e_product_language=en&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=19108282527&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=EAIaIQobChMIr5-phfewhgMVohCtBh3wmgHOEAQYASABEgKoWfD_BwE&aff_fcid=29174c1d50f943769efa8012031d57cc-1716919365627-05534-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=29174c1d50f943769efa8012031d57cc-1716919365627-05534-UneMJZVf&terminal_id=737d9ac3691746ff8ef5a6a48b8417fd&afSmartRedirect=y&gatewayAdapt=glo2usa). The B10K potentiometer is also bought from [AliExpress](https://www.aliexpress.us/item/2251832615097149.html?spm=a2g0o.productlist.main.1.18932f0bm6LZTu&algo_pvid=0a63f5f6-c752-4cde-8f51-b22f4c4bc927&algo_exp_id=0a63f5f6-c752-4cde-8f51-b22f4c4bc927-0&pdp_npi=4%40dis%21USD%211.75%211.75%21%21%211.75%211.75%21%40210324f117169197356962988eef38%2166432637308%21sea%21US%210%21AB&curPageLogUid=x8oTYf4QWT1x&utparam-url=scene%3Asearch%7Cquery_from%3A), which comes with nuts and washers to secure it to a base.





