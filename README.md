# SSMILE (Stroke Screening Made Instant, Live, and Easy)

With fifteen million cases of stroke worldwide every year and many more complications arising from stroke, early detection of stroke is significant to prevent any further brain damage and to possibly decrease both mortality and morbidity. This Python GUI project helps one determine whether one has facial asymmetry, one of the most common symptoms of stroke, with an image of one's face or through web camera.

*This project is an extension of a hacakthon team project described below.*

*This repository contains scripts but not image or video files.* 

### Library/Package Used (Python 3.9.7)

* OpenCV v.
* dlib v.
* SequenceMatcher v.
* Tkinter v.8.6

## Archive : Project Description from [DevPost](https://devpost.com/software/ssmile) and [Git](https://github.com/we437b/SSMILE)

### Inspiration

We believe it is the duty of the more fortunate to protect those most vulnerable. While researching the most prevalent diseases among the elderly, multiple members of the team mentioned that they personally know someone who has suffered from a stroke and have witnessed firsthand their debilitating effects on the survivors’ lifestyles. After realizing the worldwide scope of the issue, our team knew that something had to be done. SSMILE revolves around the F.A.S.T. acronym in order to provide steadfast detection, enhance emergency responsiveness, and potentially save lives.

### SSMILE’s Abilities

Facial Muscle Weakness Detection: facial droops are one of the first signs of a stroke. Through facial recognition algorithms, SSMILE can scan the user’s face for irregularities and signs of muscle weakness.

Arm Motor Control Detection: weakness in the arms is another key warning of a stroke. Through an encoded gyroscope accelerometer, SSMILE can test if there is any drifting in the user’s arms through a quick 10-second test!

Speech Function Failure Detection: the last sign of stroke in the FAST acronym is irregular speech. After establishing a personalized baseline pattern of speech, SSMILE can compare new speech samples to the original baseline and quantify any outliers.

Time To Contact Emergency: through push notifications, family members of the user can obtain recordings of speech, arm movement, and smiles to visually confirm if a stroke is present. If a stroke is confirmed emergency services can be immediately contacted.

### Project Challenges

As many of us were inexperienced coders, a large portion of the programming development was difficult. Developing the facial recognition system, gyroscope accelerometer, and speech reader was irrefutably challenging. Additionally, converting PC implemented algorithms into a user-friendly android app was tricky and certainly took a good amount of debugging and thinking.

### Project Accomplishments

The program can successfully detect facial droops, weaknesses in arms, and speech function failure.

### SSMILE’s Future

Given the time constraint, we were unable to implement many ideas that we conjured up! However, we are excited to see what the future may hold for SSMILE. Here’s a list of things we foresee in SSMILE’s near future…

Train our model to differentiate facial drooping due to strokes, bell’s palsy, post-stroke symptoms, injury, etc.
Develop a personalized baseline status of facial features to account for possible post-stroke and facial injuries
Develop a passive arm motor control sensor once the mobile device is unlocked to account for sudden strokes
Develop an additional arm motor control test using augmented reality (ie. search for an object within the room)
Train our model with databases of stroke patients and their cognitive and behavioral functions
Train the language model on an NLP corpus from the late 1900s to accommodate for age-specific speech patterns and to realize language function failure detection without prompting the users to read out sentences
Convert prompted test methods into a passive automatic detection mechanism

### Appreciation

A big thanks to the guidance and mentorship from Dr. Vishu Ravi and esteemed Software Engineer Terrel Ibanez!


