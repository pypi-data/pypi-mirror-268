import numpy as np
import tensorflow as tf
import keras
from keras import layers, models

# How can I import the functions from preprocess_data module?

class ModelCreator:
    """
    A class to create and compile the DualFinder CNN tailored for image classification tasks.

    Parameters
    ----------
    image_shape : tuple
        The shape of the input images (height, width, channels).
    learning_rate : float
        The initial learning rate for the Adam optimizer.
    num_classes : int
        The number of classes for the output layer of the model.
    display_architecture : bool, optional
        Whether to display the model architecture upon creation (default is True).

    Methods
    -------
    f1_score(y_true, y_pred)
        Calculate the F1 score, a harmonic mean of precision and recall.
    static_f1_score(y_true, y_pred)
        Calculate the F1 score statically (class method), without needing a class instance.
    MCC(y_true, y_pred)
        Calculate the Matthews correlation coefficient, a measure of the quality of binary classifications.
    static_MCC(y_true, y_pred)
        Calculate the Matthews correlation coefficient (static method, to be accessed later without creating a DualFinder instance).
    create_model(dropout, display_architecture=True)
        Construct and compile the neural network model based on the initial parameters and the specified dropout rate.
    """
    def __init__(self, image_shape, learning_rate, num_classes, display_architecture = True):
        self.image_shape = image_shape
        self.learning_rate = learning_rate
        self.num_classes = num_classes
        self.display_architecture = display_architecture
        
    def f1_score(self, y_true, y_pred):
        precision = tf.keras.metrics.Precision(thresholds=0.5)
        recall = tf.keras.metrics.Recall(thresholds=0.5)
        precision.update_state(y_true, y_pred)
        recall.update_state(y_true, y_pred)
        precision_result = precision.result()
        recall_result = recall.result()
        f1 = 2 * ((precision_result * recall_result) / (precision_result + recall_result + tf.keras.backend.epsilon()))
        precision.reset_states()
        recall.reset_states()
        return f1
    @staticmethod
    def static_f1_score(y_true, y_pred):
        precision = tf.keras.metrics.Precision(thresholds=0.5)
        recall = tf.keras.metrics.Recall(thresholds=0.5)
        precision.update_state(y_true, y_pred)
        recall.update_state(y_true, y_pred)
        precision_result = precision.result()
        recall_result = recall.result()
        f1 = 2 * ((precision_result * recall_result) / (precision_result + recall_result + tf.keras.backend.epsilon()))
        precision.reset_states()
        recall.reset_states()
        return f1
    def MCC(self, y_true, y_pred):
        true_positives = tf.keras.metrics.TruePositives()
        true_negatives = tf.keras.metrics.TrueNegatives()
        false_positives = tf.keras.metrics.FalsePositives()
        false_negatives = tf.keras.metrics.FalseNegatives()
        true_positives.update_state(y_true, y_pred)
        true_negatives.update_state(y_true, y_pred)
        false_positives.update_state(y_true, y_pred)
        false_negatives.update_state(y_true, y_pred)
        true_positives_result = true_positives.result()
        true_negatives_result = true_negatives.result()
        false_positives_result = false_positives.result()
        false_negatives_result = false_negatives.result()
        mcc = ((true_positives_result*true_negatives_result) -
               (false_positives_result*false_negatives_result))/np.sqrt((true_positives_result + false_positives_result)*(true_positives_result + false_negatives_result)*(true_negatives_result + false_positives_result)*(true_negatives_result + false_negatives_result))
        return mcc
    @staticmethod
    def static_MCC(y_true, y_pred):
        true_positives = tf.keras.metrics.TruePositives()
        true_negatives = tf.keras.metrics.TrueNegatives()
        false_positives = tf.keras.metrics.FalsePositives()
        false_negatives = tf.keras.metrics.FalseNegatives()
        true_positives.update_state(y_true, y_pred)
        true_negatives.update_state(y_true, y_pred)
        false_positives.update_state(y_true, y_pred)
        false_negatives.update_state(y_true, y_pred)
        true_positives_result = true_positives.result()
        true_negatives_result = true_negatives.result()
        false_positives_result = false_positives.result()
        false_negatives_result = false_negatives.result()
        mcc = ((true_positives_result*true_negatives_result) - (false_positives_result*false_negatives_result))/np.sqrt((true_positives_result + false_positives_result)*(true_positives_result + false_negatives_result)*(true_negatives_result + false_positives_result)*(true_negatives_result + false_negatives_result))
        return mcc
    def create_model(self, dropout, display_architecture = True):
        model = models.Sequential()
        model.add(layers.Input(shape=(60, 60, 1)))
        model.add(layers.Rescaling(1./255))
    
        model.add(layers.Conv2D(96, (12, 12), padding='same', strides=(2, 2), activation=tf.nn.leaky_relu, kernel_regularizer = tf.keras.regularizers.l2(0.01)))
        model.add(layers.Dropout(dropout))
        model.add(layers.BatchNormalization())
    
        model.add(layers.Conv2D(256, (6, 6), padding='same', strides=(1, 1), activation=tf.nn.leaky_relu, kernel_regularizer = tf.keras.regularizers.l2(0.01)))
        model.add(layers.Dropout(dropout))
        model.add(layers.BatchNormalization())
    
        model.add(layers.Conv2D(256, (3,3), padding='same', strides=(1, 1), activation=tf.nn.leaky_relu,  kernel_regularizer = tf.keras.regularizers.l2(0.01)))
        model.add(layers.Dropout(dropout))
        model.add(layers.BatchNormalization())
    
        model.add(layers.MaxPooling2D((2, 2), strides=(2, 2)))
        for _ in range(1):
            model.add(layers.Conv2D(384, kernel_size= 3, strides=(1, 1), activation=tf.nn.leaky_relu, kernel_regularizer = tf.keras.regularizers.l2(0.01)))
            model.add(layers.Dropout(dropout))
        model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation=tf.nn.leaky_relu,  kernel_regularizer = tf.keras.regularizers.l2(0.01)))
        model.add(layers.Dropout(dropout))
        #model.add(layers.Dropout())
        model.add(layers.BatchNormalization())
        model.add(layers.Dense(512, activation = tf.nn.leaky_relu, kernel_regularizer = tf.keras.regularizers.l2(0.01)))
        model.add(layers.Dense(2, activation='softmax'))
        lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=self.learning_rate,
                                                                      decay_steps=10000,decay_rate=0.9)
    
        optimized = tf.keras.optimizers.Adam(learning_rate=lr_schedule)
    
        model.compile(optimizer=optimized, loss=tf.keras.losses.CategoricalCrossentropy(),
                      metrics=[tf.keras.metrics.BinaryAccuracy(name='binary_accuracy'),
                               tf.keras.metrics.FalsePositives(name='false positives'),
                               tf.keras.metrics.FalseNegatives(name='false negatives'),
                               tf.keras.metrics.TruePositives(name='true positives'),
                               tf.keras.metrics.TrueNegatives(name='true negatives'),
                               tf.keras.metrics.Recall(name='recall'),
                               tf.keras.metrics.Precision(name='precision'),
                               tf.keras.metrics.F1Score(name = 'f1_score')], run_eagerly=False)
    
        if display_architecture:
            model.summary()
    
        return model
        #assert image_shape.shape != (image_shape.shape[0], image_shape.shape[0], 1), "Image shape must have three channels"
