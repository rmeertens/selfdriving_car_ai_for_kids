# Teaching kids about self-driving cars
For the success of self-driving cars its important to educate children about them. This is why autonomous intelligent driving (AID) decided to open its doors to children on the October 3 2019 (https://www.wdrmaus.de/tuer_oeffner_tag/2019/index.php5?detail=705854). 

For this day I decided to make a simple educational tool to show children in an interactive way what the current state of the art is in computer vison. It's a simple neural network (yolo v3) which can recognise quite a lot of objects. The idea is to talk with children and ask them questions to get them thinking about machine learning, and what recognition capabilities you need for self-driving cars.

## Necessary materials
For this demo you need the following materials: 
- Laptop with NVIDIA GPU
- Webcam (possibly mounted on a (selfdriving) car)
- A set of objects that can be recognised by YOLO, which are:
    person,   bicycle,   car,   motorcycle,   airplane,
    bus,   train,   truck,   boat,   traffic light,   fire hydrant,   stop_sign,
    parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra,
    giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard,
    sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket,
    bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange,
    broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed,
    dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,
    oven,   toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer,
    toothbrush.
  
 Its nice to put these objects in a big box so children can take them out, show them to the car/webcam, and see if they are recognised. Its also nice to point the car to the road so the car will see cars and pedestrians walking by. 

Its also nice to teach children about what you train on and interesting adversarial samples. For example: the detector can detect "real" mice, but is unable to recognise a cartoon mouse like the one from the German "Die Sendung mit der Maus". 



## Educational materials (English)
Discover how self-driving cars will see the world!
Welcome to our self-driving car. We put a camera on this car and taught it about the world around us by showing it 200.000 images and telling the car what is in the image. It's now your task to discover what the car learned to recognise, and to think about how useful this is for a self-driving car. 
Try to see if the car can recognise the following things:  
    person,   bicycle,   car,   motorcycle,   airplane,
    bus,   train,   truck,   boat,   traffic light,   fire hydrant,   stop_sign,
    parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra,
    giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard,
    sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket,
    bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange,
    broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed,
    dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,
    oven,   toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer,
    toothbrush.

Which of these objects should a self-driving car really recognise? 

Are there things missing in this list which you think are necessary to make a self-driving car?  

We showed the car images of real mice. Try to show the car the cartoon mouse from "Die Sendung mit der Maus". Does the car recognise it? Why/why not? Do you think a car which only uses a camera will recognise you if you put on a tiger suit? 



