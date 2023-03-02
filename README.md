Topic: Effective Usage of Drones in Precision Agriculture
This consists of various files:
1) 'Classification_Rice_Land-CNN' consists of the training and evaluation of the CNN model to classify input image into crop and arable land
2) 'GrowthStageOfRice-CNN' has the python code to classify the rice crop into growth stages : week 1, week 2 and week 3 if the crop is classified as rice crop in above mentioned model
3) 'DataAugmentation-DifferentCrops' is used to augment and generate larger data from existing smaller dataset
4) 'CropsClassification-CNN'  consists of the training and evaluation of the CNN model to classify different crops

Phase 2 Added:
5)'Weed_Model_Tutorial.ipynb' - The Yolo V5I model is used to train on the Weed Dataset with labels, accuracy increased from 30% to 70% by increasing dataset size and preprocessing the weed data. Test Images were given as input to the Yolo model and it returns an output with red boundaries above weed in the image.
6)Results and Metrics - F1 score, Precision and Accuracy have been displayed in graphical format
7)'ndvi.py' - This is for estimating NDVI values with RGB images
8)'FalseColorMap.py' - This is for giving separate color to Vegetation Indice values with a given range, to make the VI applied image look distint and comprehendable
