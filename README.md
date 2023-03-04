# Vector-Setup
 
A GUI to help the user create a credential file for Vector.

![Vector cute](/img/vector_gif.gif?raw=true "Vector is cute")

*Tested on Windows only-will test on mac-os soon*

Getting a cert file for Vector can be a real pain, especially for users who dont come from a technical background.
Vector depends on an sdk (anki-vector) that cannot run on modern python versions and you have to downgrade some site packages like proto-buff.

To make this easier on people I made a stand-alone exe file so people dont have to downgrade their python version and mess with other libraries.

It's really simple- just enter your information and a cert file will be generated in your user folder under .anki-vector

https://user-images.githubusercontent.com/91567228/222926517-f109ed2c-6686-43b4-a87a-1cb60c49a594.mp4

In order to use this you must first set up and pair Vector, information can be found here: [How to set up Vector](https://support.digitaldreamlabs.com/article/114-video-vector-and-connection-how-to-set-vector-up)

## Troubleshooting

### Error message - Could not verify login:

The most likely reason is your email and password used to create your vector account through Vector's phone app does not match with the email and password you are providing. Please make sure they match. If they match its probably just something going on with anki/vectors servers.

### Error message - Could not verify Vectors serial number / Could not validate the certificate:

Make sure you entered the correct serial number and the correct name. Vectors serial number should be 8 characters long and is alpha-numeric. Vectors name is 4 digits long and is also alphanumeric. You can find this info by double clicking his back (The black stripe with 3 led boxes and the small circle) while hes on his charger. His name should show up as Vector {name} a key and ###### on the bottom. If you lift his arms up and down you can get his serial number. This is where you can also see the ip address.

### Error message - Could not connect to Vector:

The most common reason is that Vector is not powered on. Turn him on.

Another reason could be is that he was never set up through the phone app. To do this follow these instructions- [How to set up Vector](https://support.digitaldreamlabs.com/article/114-video-vector-and-connection-how-to-set-vector-up) . If you are having trouble connecting him through the app make sure you are on the same network as Vector. He cannot use 5Ghz so connect to your 2.4Ghz network.


